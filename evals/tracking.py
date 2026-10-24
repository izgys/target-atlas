"""
MLflow tracking for eval runs.

Each `target-atlas eval` becomes one MLflow run in a local SQLite store:

    mlruns/mlflow.db       runs, params, metrics, tags
    mlruns/artifacts/      results.json, results.md, outputs/ per run

(MLflow 3.x deprecates the plain-folder store, so the database lives inside
mlruns/ instead.) Browse and compare runs with:

    mlflow ui --backend-store-uri sqlite:///mlruns/mlflow.db

What is logged:
    params    the full resolved config, flattened (agents.reasoning.model, ...),
              plus eval.cache, eval.targets, eval.overrides, eval.repeats
    tags      git_commit, dirty, model
    metrics   <metric>/mean and <metric>/<TARGET> for the four eval metrics,
              e.g. gap_honesty/mean, gap_honesty/TREM2 — always the mean over
              repeats (with one repeat, simply the score). With several repeats
              also <metric>/<TARGET>_sd, and the per-repeat values under
              repeat/<metric>/<TARGET>, logged with step = repeat number, which
              the UI draws as a chart. levels_stable/<TARGET> is 1 when Claude's
              four verdicts were identical in every repeat.
              Metric-first names put all targets of one metric in one section.
    artifacts the run folder written by run_eval

One MLflow run per eval (targets as metric keys, not child runs), so comparing
two evals in the UI is a comparison of two runs.

Set MLFLOW_TRACKING_URI to log somewhere else (e.g. a shared server).
"""
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRACKING_DIR = REPO_ROOT / "mlruns"
EXPERIMENT_NAME = "target-atlas-eval"
METRICS = ["identity", "fact_recall", "citation", "gap_honesty"]


def tracking_uri(tracking_dir: Path | None = None) -> str:
    """
    Where runs are logged: an explicit tracking_dir wins, then MLFLOW_TRACKING_URI,
    then the SQLite database in mlruns/.

    The explicit folder must win over the environment variable because
    mlflow.set_tracking_uri() itself writes MLFLOW_TRACKING_URI: reading the
    variable first would make every later call reuse the previous location.
    """
    if tracking_dir is None and os.environ.get("MLFLOW_TRACKING_URI"):
        return os.environ["MLFLOW_TRACKING_URI"]
    db = Path(tracking_dir or TRACKING_DIR) / "mlflow.db"
    return f"sqlite:///{db.resolve().as_posix()}"


def flatten(data: dict, prefix: str = "") -> dict[str, str]:
    """{'apis': {'pdb': {'max_structures': 20}}} -> {'apis.pdb.max_structures': '20'}"""
    flat = {}
    for key, value in data.items():
        name = f"{prefix}{key}"
        if isinstance(value, dict):
            flat.update(flatten(value, prefix=f"{name}."))
        else:
            flat[name] = str(value)
    return flat


def eval_metrics(run: dict) -> dict[str, float]:
    """Summary metrics: means over repeats, SDs when there are several, failures, verdict stability."""
    several = run["repeats"] > 1
    metrics = {}
    for metric in METRICS:
        stat = run["aggregate"].get(metric)
        if stat:
            metrics[f"{metric}/mean"] = stat["mean"]
            if several:
                metrics[f"{metric}/mean_sd"] = stat["sd"]

    for target in run["targets"]:
        query = target["query"]
        if target["errors"]:
            metrics[f"error/{query}"] = float(target["errors"])
        for metric in METRICS:
            stat = target.get(metric)
            if stat:
                metrics[f"{metric}/{query}"] = stat["mean"]
                if several:
                    metrics[f"{metric}/{query}_sd"] = stat["sd"]
        if target["levels_stable"] is not None:
            metrics[f"levels_stable/{query}"] = float(target["levels_stable"])

    metrics["targets_failed"] = float(sum(t["scored"] == 0 for t in run["targets"]))
    metrics["levels_stable/count"] = float(run["levels_stable_count"])
    return metrics


def repeat_metrics(run: dict) -> dict[int, dict[str, float]]:
    """Per-repeat scores keyed by repeat number, for metric history (step = repeat)."""
    by_repeat = {}
    for p in run["passes"]:
        values = {
            f"repeat/{m}/mean": p["aggregate"][m]
            for m in METRICS if p["aggregate"][m] is not None
        }
        for result in p["targets"]:
            for m in METRICS:
                score = result.get(m, {}).get("score")
                if score is not None:
                    values[f"repeat/{m}/{result['query']}"] = score
        by_repeat[p["repeat"]] = values
    return by_repeat


def log_eval_run(run: dict, run_dir: Path, tracking_dir: Path | None = None) -> str:
    """Log one eval run (the dict run_eval saves as results.json). Returns the MLflow run id."""
    import mlflow   # imported here: it takes ~2 s and only eval needs it

    uri = tracking_uri(tracking_dir)
    tracking_dir = Path(tracking_dir or TRACKING_DIR)
    mlflow.set_tracking_uri(uri)

    experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
    if experiment is None and uri.startswith("sqlite:"):
        # Artifacts next to the database, inside mlruns/ (gitignored)
        artifacts = (tracking_dir / "artifacts").resolve()
        experiment_id = mlflow.create_experiment(EXPERIMENT_NAME, artifact_location=artifacts.as_uri())
    elif experiment is None:   # a remote server chooses its own artifact store
        experiment_id = mlflow.create_experiment(EXPERIMENT_NAME)
    else:
        experiment_id = experiment.experiment_id

    commit = run["git_commit"]
    with mlflow.start_run(experiment_id=experiment_id, run_name=run_dir.name) as active:
        mlflow.set_tags({
            "git_commit": commit,
            "dirty": str(commit.endswith("-dirty")).lower(),
            "model": run["model"],
        })
        mlflow.log_params(flatten(run.get("config", {})))
        mlflow.log_params({
            "eval.cache": run["cache"],
            "eval.targets": ",".join(r["query"] for r in run["targets"]),
            "eval.overrides": " ".join(run.get("overrides", [])) or "none",
            "eval.repeats": run["repeats"],
        })
        mlflow.log_metrics(eval_metrics(run))
        if run["repeats"] > 1:
            for step, values in repeat_metrics(run).items():
                mlflow.log_metrics(values, step=step)
        mlflow.log_artifacts(str(run_dir))
        return active.info.run_id
