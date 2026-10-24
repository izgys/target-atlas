"""
Repeated evals: the statistics behind 'mean ± SD' and verdict stability.

Temperature 0 reduces but does not remove variation in an API model's
output, so the harness runs the whole eval N times and reports the spread.
"""
import pytest

import evals.run_eval as run_eval
from tests.helpers import levels, make_pass, result


@pytest.fixture
def three_passes():
    """TREM2's gap honesty and structural verdict vary; EGFR is stable."""
    return [
        make_pass(1, [result("EGFR"), result("TREM2", gap=1.0, verdict=levels("medium", "medium"))]),
        make_pass(2, [result("EGFR"), result("TREM2", gap=0.8, verdict=levels("medium", "high"))]),
        make_pass(3, [result("EGFR"), result("TREM2", gap=0.8, verdict=levels("medium", "medium"))]),
    ]


def test_per_target_mean_and_sample_sd(three_passes):
    summary = run_eval.summarize(three_passes)
    trem2 = summary["targets"][1]["gap_honesty"]

    assert trem2["mean"] == pytest.approx(0.8667, abs=1e-4)
    assert trem2["sd"] == pytest.approx(0.1155, abs=1e-4)   # sample SD (n - 1)
    assert (trem2["min"], trem2["max"], trem2["n"]) == (0.8, 1.0, 3)


def test_overall_spread_is_over_per_repeat_means(three_passes):
    summary = run_eval.summarize(three_passes)
    gap = summary["aggregate"]["gap_honesty"]

    # per-repeat means: 1.0, 0.9, 0.9
    assert gap["mean"] == pytest.approx(0.9333, abs=1e-4)
    assert gap["sd"] == pytest.approx(0.0577, abs=1e-4)


def test_verdict_stability(three_passes):
    egfr, trem2 = run_eval.summarize(three_passes)["targets"]

    assert egfr["levels_stable"] is True and egfr["levels_agree"] == 3
    assert trem2["levels_stable"] is False
    assert trem2["levels_agree"] == 2                         # 2 of 3 repeats share the commonest verdict
    assert trem2["levels"]["structural_confidence"] == {"medium": 2, "high": 1}


def test_single_repeat_has_zero_sd_and_plain_formatting():
    summary = run_eval.summarize([make_pass(1, [result("EGFR", gap=0.67)])])
    stat = summary["targets"][0]["gap_honesty"]

    assert stat["sd"] == 0.0 and stat["n"] == 1
    assert run_eval._fmt_stat(stat) == "0.67"                 # no '± 0.00' for one sample


def test_failed_repeats_are_excluded_and_counted():
    passes = [
        make_pass(1, [result("KRAS", gap=1.0)]),
        make_pass(2, [{"query": "KRAS", "error": "ConnectError: boom"}]),
    ]
    kras = run_eval.summarize(passes)["targets"][0]

    assert (kras["scored"], kras["errors"]) == (1, 1)
    assert kras["gap_honesty"]["n"] == 1                       # an error is not a score of 0


def test_failed_reasoning_has_no_verdict():
    passes = [make_pass(1, [{**result("IL6R"), "levels": None}])]
    il6r = run_eval.summarize(passes)["targets"][0]
    assert il6r["levels_stable"] is None


def test_markdown_shows_mean_sd_and_changed_verdicts(three_passes):
    run = {
        "started": "2026-10-24T20:00:00", "git_commit": "abc1234", "model": "m",
        "cache": "evals/cache", "overrides": [], "repeats": 3,
        "config": {"agents": {"reasoning": {"temperature": 0}}},
        **run_eval.summarize(three_passes), "passes": three_passes,
    }
    md = run_eval.build_markdown(run)

    assert "temperature `0`" in md and "repeats 3" in md
    assert "| TREM2 | 1.00 ± 0.00 | 0.50 ± 0.00 | 1.00 ± 0.00 | 0.87 ± 0.12 | **no** (2/3) |" in md
    assert "- TREM2: structural_confidence medium×2 high×1" in md
    assert "| **Mean** |" in md and "1/2 stable" in md
    assert "**Mean per repeat**" in md


# ---------------------------------------------------------------------------
# main(): repeats run end to end with the pipeline faked
# ---------------------------------------------------------------------------

class FakeAssessment:
    def __init__(self, structural):
        self.druggability_score = "medium"
        self.structural_confidence = structural
        self.chemical_confidence = "none"
        self.literature_confidence = "medium"


def test_main_runs_every_target_once_per_repeat(monkeypatch, tmp_path):
    calls = []
    verdicts = iter(["medium", "high", "medium"])

    def fake_run_target(query, out):
        calls.append((query, out.name))
        return {"druggability_assessment": FakeAssessment(next(verdicts))}, {"data_gaps": {}}

    monkeypatch.setattr(run_eval, "run_target", fake_run_target)
    monkeypatch.setattr(run_eval, "score_identity", lambda t, s: {"score": 1.0})
    monkeypatch.setattr(run_eval, "score_fact_recall", lambda t, s: result("x")["fact_recall"])
    monkeypatch.setattr(run_eval, "score_citation_validity", lambda t, s, st: {"score": 1.0})
    monkeypatch.setattr(run_eval, "score_gap_honesty", lambda t, s: {"score": 0.8})
    monkeypatch.setattr(run_eval, "RESULTS_DIR", tmp_path)

    run_eval.main(["--targets", "TREM2", "--no-cache", "--no-mlflow", "--repeats", "3"])

    # Repeats are the outer loop, each with its own output folder
    assert calls == [("TREM2", "repeat_1"), ("TREM2", "repeat_2"), ("TREM2", "repeat_3")]

    import json
    [results_file] = tmp_path.glob("*/results.json")
    run = json.loads(results_file.read_text())
    assert run["repeats"] == 3 and len(run["passes"]) == 3
    assert run["targets"][0]["levels_stable"] is False
    assert run["config"]["agents"]["reasoning"]["temperature"] == 0   # the new default


def test_repeats_must_be_positive():
    with pytest.raises(SystemExit):
        run_eval.main(["--repeats", "0", "--no-mlflow"])


def test_git_commit_falls_back_to_build_arg_without_git(monkeypatch):
    # Inside the Docker image there is no .git; the commit comes from GIT_COMMIT
    def no_git(*args, **kwargs):
        raise FileNotFoundError("git")
    monkeypatch.setattr(run_eval.subprocess, "run", no_git)
    monkeypatch.setenv("GIT_COMMIT", "abc1234")
    assert run_eval._git_commit() == "abc1234"

    monkeypatch.delenv("GIT_COMMIT")
    assert run_eval._git_commit() == "unknown"
