"""
MLflow tracking of eval runs, against a throwaway SQLite store per test.

The store is a local file, so these tests stay offline. Results are read
back with MlflowClient, the same API the `mlflow ui` uses.
"""
import json

import pytest

import evals.run_eval as run_eval
import evals.tracking as tracking


def _score(value):
    return {"score": value}


@pytest.fixture
def eval_run():
    """A results.json-shaped dict: two scored targets, one failed target."""
    return {
        "started": "2026-10-24T20:00:00",
        "git_commit": "abc1234-dirty",
        "model": "claude-sonnet-4-6",
        "cache": "evals/cache",
        "overrides": ["agents.reasoning.temperature=0"],
        "config": {"agents": {"reasoning": {"model": "claude-sonnet-4-6", "temperature": 0}},
                   "apis": {"pdb": {"max_structures": 20}}},
        "aggregate": {"identity": 1.0, "fact_recall": 0.5, "citation": 1.0, "gap_honesty": 0.9},
        "targets": [
            {"query": "EGFR", "identity": _score(1.0), "fact_recall": _score(0.36),
             "citation": _score(1.0), "gap_honesty": _score(1.0)},
            {"query": "TREM2", "identity": _score(1.0), "fact_recall": _score(0.6),
             "citation": _score(None), "gap_honesty": _score(0.8)},
            {"query": "KRAS", "error": "ConnectError: boom"},
        ],
    }


@pytest.fixture
def run_dir(tmp_path, eval_run):
    folder = tmp_path / "results" / "2026-10-24_200000"
    (folder / "outputs" / "EGFR_P00533").mkdir(parents=True)
    (folder / "results.json").write_text(json.dumps(eval_run))
    (folder / "results.md").write_text("# results")
    (folder / "outputs" / "EGFR_P00533" / "report.md").write_text("# report")
    return folder


def _client(tracking_dir):
    from mlflow.tracking import MlflowClient
    return MlflowClient(tracking_uri=tracking.tracking_uri(tracking_dir))


def test_flatten_turns_nested_config_into_dotted_params():
    assert tracking.flatten({"a": {"b": {"c": 1}}, "d": None}) == {"a.b.c": "1", "d": "None"}


def test_eval_metrics_are_metric_first_with_means_and_errors(eval_run):
    metrics = tracking.eval_metrics(eval_run)

    assert metrics["gap_honesty/mean"] == 0.9
    assert metrics["gap_honesty/TREM2"] == 0.8
    assert metrics["fact_recall/EGFR"] == 0.36
    assert "citation/TREM2" not in metrics          # None score: not logged as 0
    assert metrics["error/KRAS"] == 1.0
    assert metrics["targets_failed"] == 1.0


def test_log_eval_run_records_params_tags_metrics_and_artifacts(tmp_path, eval_run, run_dir):
    store = tmp_path / "mlruns"
    run_id = tracking.log_eval_run(eval_run, run_dir, tracking_dir=store)

    run = _client(store).get_run(run_id)
    assert run.info.run_name == "2026-10-24_200000"
    assert run.data.params["agents.reasoning.temperature"] == "0"
    assert run.data.params["apis.pdb.max_structures"] == "20"
    assert run.data.params["eval.targets"] == "EGFR,TREM2,KRAS"
    assert run.data.params["eval.overrides"] == "agents.reasoning.temperature=0"
    assert run.data.tags["git_commit"] == "abc1234-dirty"
    assert run.data.tags["dirty"] == "true"
    assert run.data.metrics["gap_honesty/TREM2"] == 0.8

    artifacts = {a.path for a in _client(store).list_artifacts(run_id)}
    assert {"results.json", "results.md", "outputs"} <= artifacts
    # Database and artifacts both stay inside the tracking folder
    assert (store / "mlflow.db").exists() and (store / "artifacts").exists()


def test_explicit_folder_wins_over_a_stale_tracking_uri(tmp_path, monkeypatch):
    # Regression: set_tracking_uri() leaves MLFLOW_TRACKING_URI behind
    monkeypatch.setenv("MLFLOW_TRACKING_URI", "sqlite:///somewhere/else.db")
    assert tracking.tracking_uri(tmp_path).endswith(f"{tmp_path.as_posix()}/mlflow.db")
    assert tracking.tracking_uri() == "sqlite:///somewhere/else.db"   # no folder: the user's choice


def test_two_evals_land_in_one_experiment_for_comparison(tmp_path, eval_run, run_dir):
    store = tmp_path / "mlruns"
    first = tracking.log_eval_run(eval_run, run_dir, tracking_dir=store)
    second = tracking.log_eval_run(eval_run, run_dir, tracking_dir=store)

    client = _client(store)
    experiment = client.get_experiment_by_name(tracking.EXPERIMENT_NAME)
    runs = client.search_runs([experiment.experiment_id])
    assert {r.info.run_id for r in runs} == {first, second}


# ---------------------------------------------------------------------------
# run_eval.main: the pipeline and scorers are faked, the MLflow logging is real
# ---------------------------------------------------------------------------

@pytest.fixture
def fake_eval(monkeypatch, tmp_path):
    summary = {"data_gaps": {}}
    monkeypatch.setattr(run_eval, "run_target", lambda query, out: ({}, summary))
    monkeypatch.setattr(run_eval, "score_identity", lambda t, s: _score(1.0))
    monkeypatch.setattr(run_eval, "score_fact_recall", lambda t, s: {
        "score": 0.5,
        "categories": {c: {"found": 1, "expected": 2} for c in ("pdb_ids", "approved_drugs", "pmids")},
    })
    monkeypatch.setattr(run_eval, "score_citation_validity", lambda t, s, st: _score(1.0))
    monkeypatch.setattr(run_eval, "score_gap_honesty", lambda t, s: _score(0.75))
    monkeypatch.setattr(run_eval, "RESULTS_DIR", tmp_path / "results")
    monkeypatch.setattr(tracking, "TRACKING_DIR", tmp_path / "mlruns")
    return tmp_path


def test_main_logs_the_eval_to_mlflow(fake_eval, capsys):
    run_eval.main(["--targets", "EGFR", "--no-cache"])

    client = _client(fake_eval / "mlruns")
    experiment = client.get_experiment_by_name(tracking.EXPERIMENT_NAME)
    [run] = client.search_runs([experiment.experiment_id])
    assert run.data.metrics["gap_honesty/EGFR"] == 0.75
    assert run.data.params["agents.reasoning.model"]          # the real resolved config
    assert "Logged to MLflow" in capsys.readouterr().out


def test_no_mlflow_flag_skips_tracking(fake_eval):
    run_eval.main(["--targets", "EGFR", "--no-cache", "--no-mlflow"])

    assert not (fake_eval / "mlruns").exists()
    assert list((fake_eval / "results").glob("*/results.json"))


def test_tracking_failure_keeps_the_results(fake_eval, monkeypatch, capsys):
    def broken(*args, **kwargs):
        raise RuntimeError("database is locked")
    monkeypatch.setattr(tracking, "log_eval_run", broken)

    run_eval.main(["--targets", "EGFR", "--no-cache"])

    assert list((fake_eval / "results").glob("*/results.json"))
    assert "MLflow logging failed" in capsys.readouterr().out
