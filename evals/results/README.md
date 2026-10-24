# Evaluation runs

Each folder is one run of `target-atlas eval` (or `python -m evals.run_eval`): `results.md` (score table), `results.json` (per-target details: missed facts, failed checks, Claude's verdicts, pipeline errors) and `outputs/` (the report and summary produced for every target). Runs with `--repeats N` keep one `outputs/repeat_<k>/` folder per pass and report mean ± SD.

| Run | Commit | What it shows |
|---|---|---|
| [`2026-10-24_201154`](2026-10-24_201154/results.md) | `3319341` | **Current results**, quoted in the main README: temperature 0, five repeats, mean ± SD. Shows the remaining run-to-run variation (TREM2 druggability `high` ×3 / `medium` ×2). |
| [`2026-10-18_162511`](2026-10-18_162511/results.md) | `e642589` | **Previous results**: default temperature (1.0), a single sample. The examples in `examples/` come from this run. |
| [`2026-10-18_152935`](2026-10-18_152935/results.md) | `27f74f8` + uncommitted changes | **Baseline**, before the reasoning node received total PDB and PubMed counts. Scores are identical; the difference is in what Claude was told (e.g. "20 publications" for EGFR instead of 18,783). Recorded before the harness marked uncommitted code as `-dirty`. |

API responses for these runs are cached locally in `evals/cache/` (not committed), so reruns retrieve identical data; only the Claude call is live.
