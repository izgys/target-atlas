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
              plus eval.cache, eval.targets, eval.overrides
    tags      git_commit, dirty, model
    metrics   <metric>/mean and <metric>/<TARGET> for the four eval metrics,
              e.g. gap_honesty/mean, gap_honesty/TREM2. Metric-first names put
              all targets of one metric in the same section of the UI.
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
    """Means and per-target scores as MLflow metric keys; failed targets as <TARGET>/error."""
    metrics = {}
    for metric in METRICS:
        mean = run["aggregate"].get(metric)
        if mean is not None:
            metrics[f"{metric}/mean"] = mean

    for result in run["targets"]:
        query = result["query"]
        if "error" in result:
            metrics[f"error/{query}"] = 1.0
            continue
        for metric in METRICS:
            score = result.get(metric, {}).get("score")
            if score is not None:
                metrics[f"{metric}/{query}"] = score

    metrics["targets_failed"] = float(sum("error" in r for r in run["targets"]))
    return metrics


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
        })
        mlflow.log_metrics(eval_metrics(run))
        mlflow.log_artifacts(str(run_dir))
        return active.info.run_id
