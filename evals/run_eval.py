"""
Evaluation harness for Target Atlas.

Runs the full graph on every target in evals/targets.yaml and scores each
output with four deterministic metrics:

    identity       — canonical UniProt accession resolved correctly (0 or 1)
    fact_recall    — fraction of expected PDB IDs, approved drugs and PMIDs
                     present in summary.json (also reported per category)
    citation       — fraction of PDB IDs and PMIDs in the output (API-derived
                     lists and IDs written by Claude) that exist and belong
                     to the target
    gap_honesty    — fraction of consistency checks passed between what was
                     retrieved and what the assessment claims

API responses are cached in evals/cache/ (see target_atlas.utils.http), so
reruns are fast and reproducible. The Claude call is never cached — it is
the thing being evaluated.

Usage:
    python -m evals.run_eval
    python -m evals.run_eval --targets EGFR TREM2
    python -m evals.run_eval --no-cache
    python -m evals.run_eval --set agents.reasoning.temperature=0
    python -m evals.run_eval --no-mlflow
    python -m evals.run_eval --repeats 5     # mean ± SD over 5 full passes

The resolved config (configs/ plus any --set overrides) is saved in
results.json, so every run records the settings that produced it. The run is
also logged to MLflow (see evals/tracking.py) for side-by-side comparison.
"""
import argparse
import json
import re
import statistics
import subprocess
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

import yaml

from target_atlas.config import config_as_dict, load_config
from target_atlas.utils.http import enable_cache, http_client


EVALS_DIR = Path(__file__).parent
TARGETS_FILE = EVALS_DIR / "targets.yaml"
CACHE_DIR = EVALS_DIR / "cache"
RESULTS_DIR = EVALS_DIR / "results"

RCSB_GRAPHQL = "https://data.rcsb.org/graphql"
ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

# PDB IDs as Claude might write them: digit + 3 alphanumerics, at least one letter
PDB_ID_PATTERN = re.compile(r"\b[1-9](?=[A-Z0-9]{0,2}[A-Z])[A-Z0-9]{3}\b")
PMID_PATTERN = re.compile(r"PMID[:\s]*(\d{6,9})", re.IGNORECASE)

METRICS = ["identity", "fact_recall", "citation", "gap_honesty"]


# ---------------------------------------------------------------------------
# Running the pipeline
# ---------------------------------------------------------------------------

def run_target(query: str, output_dir: Path) -> tuple[dict, dict]:
    """Run the graph for one query. Returns (final state, summary.json)."""
    # Imported here so enable_cache() is active before any client is used
    from target_atlas.graph import app

    state = app.invoke({"query": query, "output_dir": str(output_dir)})
    summary_path = output_dir / f"{state['gene_name']}_{state['uniprot_id']}" / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    return state, summary


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def score_identity(target: dict, summary: dict) -> dict:
    got = summary["target"]["uniprot_id"]
    return {
        "score": 1.0 if got == target["uniprot_id"] else 0.0,
        "expected": target["uniprot_id"],
        "got": got,
    }


def score_fact_recall(target: dict, summary: dict) -> dict:
    expected = target["expected"]
    retrieved = {
        "pdb_ids": {p.upper() for p in summary["structural_data"].get("pdb_ids", [])},
        "approved_drugs": [d.upper() for d in summary["chemical_data"].get("approved_drugs", [])],
        "pmids": set(summary["literature_data"].get("pmids", [])),
    }

    categories = {}
    for category in ("pdb_ids", "approved_drugs", "pmids"):
        facts = [str(f).upper() for f in expected.get(category, [])]
        if category == "approved_drugs":
            found = [f for f in facts if _drug_present(f, retrieved[category])]
        else:
            found = [f for f in facts if f in retrieved[category]]
        categories[category] = {
            "expected": len(facts),
            "found": len(found),
            "missing": [f for f in facts if f not in found],
        }

    total_expected = sum(c["expected"] for c in categories.values())
    total_found = sum(c["found"] for c in categories.values())
    return {
        "score": total_found / total_expected if total_expected else None,
        "categories": categories,
    }


def _drug_present(parent_name: str, retrieved_names: list[str]) -> bool:
    """A salt form ('IMATINIB MESYLATE') counts as its parent ('IMATINIB')."""
    return any(n == parent_name or n.startswith(parent_name + " ") for n in retrieved_names)


def score_citation_validity(target: dict, summary: dict, state: dict) -> dict:
    llm_text = _assessment_text(state)

    pdb_from_api = [p.upper() for p in summary["structural_data"].get("pdb_ids", [])]
    pdb_from_llm = sorted(set(PDB_ID_PATTERN.findall(llm_text)) - set(pdb_from_api))
    pmids_from_api = summary["literature_data"].get("pmids", [])
    pmids_from_llm = sorted(set(PMID_PATTERN.findall(llm_text)) - set(pmids_from_api))

    pdb_ids = pdb_from_api + pdb_from_llm
    pmids = pmids_from_api + pmids_from_llm

    pdb_valid = _valid_pdb_ids(pdb_ids, target["uniprot_id"])
    pmid_valid = _valid_pmids(pmids, target["aliases"])

    cited = len(pdb_ids) + len(pmids)
    valid = len(pdb_valid) + len(pmid_valid)
    return {
        "score": valid / cited if cited else None,
        "cited": cited,
        "valid": valid,
        "llm_cited_pdb_ids": pdb_from_llm,
        "llm_cited_pmids": pmids_from_llm,
        "invalid_pdb_ids": [p for p in pdb_ids if p not in pdb_valid],
        "invalid_pmids": [p for p in pmids if p not in pmid_valid],
    }


def _assessment_text(state: dict) -> str:
    assessment = state.get("druggability_assessment")
    if assessment is None:
        return ""
    return "\n".join([
        assessment.summary,
        *assessment.evidence_gaps,
        assessment.reasoning_trace,
    ])


def _valid_pdb_ids(pdb_ids: list[str], uniprot_id: str) -> set[str]:
    """PDB IDs that exist and contain a polymer entity mapped to uniprot_id."""
    if not pdb_ids:
        return set()

    query = """
    query($ids: [String!]!) {
      entries(entry_ids: $ids) {
        rcsb_id
        polymer_entities {
          rcsb_polymer_entity_container_identifiers {
            reference_sequence_identifiers { database_accession }
          }
        }
      }
    }"""
    with http_client(timeout=60.0) as client:
        response = client.post(
            RCSB_GRAPHQL,
            json={"query": query, "variables": {"ids": sorted(set(pdb_ids))}},
        )
        response.raise_for_status()
        entries = response.json().get("data", {}).get("entries") or []

    valid = set()
    for entry in entries:
        if entry is None:
            continue
        for entity in entry.get("polymer_entities") or []:
            refs = (
                entity.get("rcsb_polymer_entity_container_identifiers", {})
                .get("reference_sequence_identifiers") or []
            )
            if any(r.get("database_accession") == uniprot_id for r in refs):
                valid.add(entry["rcsb_id"].upper())
    return valid


def _valid_pmids(pmids: list[str], aliases: list[str]) -> set[str]:
    """PMIDs that exist and whose title mentions the target or an alias."""
    if not pmids:
        return set()

    time.sleep(0.4)   # NCBI allows 3 requests/second without an API key
    with http_client(timeout=30.0) as client:
        response = client.get(
            ESUMMARY,
            params={"db": "pubmed", "id": ",".join(sorted(set(pmids))), "retmode": "json"},
        )
        response.raise_for_status()
        results = response.json().get("result", {})

    lowered = [a.lower() for a in aliases]
    valid = set()
    for pmid in pmids:
        title = results.get(pmid, {}).get("title", "").lower()
        if title and any(a in title for a in lowered):
            valid.add(pmid)
    return valid


def score_gap_honesty(target: dict, summary: dict) -> dict:
    """
    Check that the assessment is consistent with what was retrieved.
    Each applicable rule is one check; score is the fraction passed.
    """
    assessment = summary["assessment"]
    gaps = assessment.get("evidence_gaps") or []
    gaps_text = " ".join(gaps).lower()
    chemical = assessment.get("chemical_confidence")
    structural = assessment.get("structural_confidence")
    chem = summary["chemical_data"]

    checks = []

    def check(name: str, passed: bool) -> None:
        checks.append({"check": name, "passed": bool(passed)})

    check("evidence gaps listed", gaps)

    if chem["chembl_target_id"] is None or chem["total_ic50_entries"] == 0:
        check("chemical confidence low/none without ChEMBL bioactivity", chemical in ("low", "none"))
        check("gap mentions missing bioactivity",
              any(k in gaps_text for k in ("chembl", "bioactivity", "ic50")))
    elif chem["total_ic50_entries"] < 100:
        check("chemical confidence not high with <100 IC50 entries", chemical != "high")

    if chem["approved_drug_count"] == 0:
        check("gap mentions absence of approved drugs", "approved" in gaps_text or "drug" in gaps_text)

    publication_total = summary["literature_data"].get("publication_total_count")
    if publication_total is not None and publication_total < 100:
        check("literature confidence not high with <100 publications",
              assessment.get("literature_confidence") != "high")

    if summary["structural_data"]["pdb_structure_count"] == 0:
        check("structural confidence low/none without PDB structures", structural in ("low", "none"))

    for error_key in summary.get("data_gaps", {}):
        source = next((s for s in ("chembl", "pubmed", "pdb", "alphafold") if s in error_key), None)
        if source:
            check(f"gap mentions failed source '{source}'", source in gaps_text)

    if target["profile"] == "sparse":
        check("sparse target not scored high", assessment.get("druggability_score") != "high")

    passed = sum(c["passed"] for c in checks)
    return {"score": passed / len(checks), "checks": checks}


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def _fmt(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.2f}"


def _fmt_stat(stat: dict | None) -> str:
    """'0.92 ± 0.11' over several repeats, '0.92' for a single one."""
    if not stat:
        return "n/a"
    if stat["n"] == 1:
        return _fmt(stat["mean"])
    return f"{stat['mean']:.2f} ± {stat['sd']:.2f}"


def _fmt_levels(counts: dict[str, int]) -> str:
    """{'medium': 4, 'high': 1} -> 'medium×4 high×1'"""
    return " ".join(f"{level}×{n}" for level, n in sorted(counts.items(), key=lambda kv: -kv[1]))


def build_markdown(run: dict) -> str:
    n = run["repeats"]
    temperature = run.get("config", {}).get("agents", {}).get("reasoning", {}).get("temperature")
    lines = [
        f"# Target Atlas eval — {run['started']}",
        "",
        f"Commit `{run['git_commit']}` · model `{run['model']}` · temperature `{temperature}` · "
        f"cache `{run['cache']}` · repeats {n}",
        *([f"Overrides: `{' '.join(run['overrides'])}`"] if run.get("overrides") else []),
        "",
    ]
    if n > 1:
        lines += [
            f"Scores are mean ± sample SD over {n} repeats of the whole eval. "
            "Retrieval is cached, so variation comes from the Claude call.",
            "",
        ]

    lines += [
        "| Target | Identity | Fact recall | Citation validity | Gap honesty | Verdict stable |",
        "|---|---|---|---|---|---|",
    ]
    for t in run["targets"]:
        if t["scored"] == 0:
            lines.append(f"| {t['query']} | error in all {n} repeats | | | | |")
            continue
        stable = {True: "yes", False: "**no**", None: "n/a"}[t["levels_stable"]]
        if n > 1 and t["levels_stable"] is not None:
            stable += f" ({t['levels_agree']}/{t['scored']})"
        errors = f" · error ×{t['errors']}" if t["errors"] else ""
        lines.append(
            f"| {t['query']} | {_fmt_stat(t['identity'])} | {_fmt_stat(t['fact_recall'])} | "
            f"{_fmt_stat(t['citation'])} | {_fmt_stat(t['gap_honesty'])} | {stable}{errors} |"
        )
    agg = run["aggregate"]
    lines.append(
        f"| **Mean** | {_fmt_stat(agg['identity'])} | {_fmt_stat(agg['fact_recall'])} | "
        f"{_fmt_stat(agg['citation'])} | {_fmt_stat(agg['gap_honesty'])} | "
        f"{run['levels_stable_count']}/{len(run['targets'])} stable |"
    )

    # Verdicts that changed between repeats — the evidence for run-to-run variation
    unstable = [t for t in run["targets"] if t["levels_stable"] is False]
    if unstable:
        lines += ["", "**Verdicts that changed between repeats**", ""]
        for t in unstable:
            changed = [
                f"{field} {_fmt_levels(counts)}"
                for field, counts in t["levels"].items() if len(counts) > 1
            ]
            lines.append(f"- {t['query']}: " + "; ".join(changed))

    # Per-category recall comes from retrieval only, which is cached: repeat 1 stands for all
    lines += [
        "",
        "**Fact recall by category** (retrieval only — identical across repeats)",
        "",
        "| Target | PDB | Drugs | PMIDs |",
        "|---|---|---|---|",
    ]
    for result in run["passes"][0]["targets"]:
        if "error" in result:
            continue
        cats = result["fact_recall"]["categories"]
        per_cat = [
            f"{cats[c]['found']}/{cats[c]['expected']}" if cats[c]["expected"] else "—"
            for c in ("pdb_ids", "approved_drugs", "pmids")
        ]
        lines.append(f"| {result['query']} | " + " | ".join(per_cat) + " |")

    if n > 1:
        lines += [
            "",
            "**Mean per repeat**",
            "",
            "| Repeat | Identity | Fact recall | Citation validity | Gap honesty |",
            "|---|---|---|---|---|",
        ]
        for p in run["passes"]:
            a = p["aggregate"]
            lines.append(
                f"| {p['repeat']} | {_fmt(a['identity'])} | {_fmt(a['fact_recall'])} | "
                f"{_fmt(a['citation'])} | {_fmt(a['gap_honesty'])} |"
            )
    return "\n".join(lines) + "\n"


def _git_commit() -> str:
    """Short HEAD hash, -dirty if code, config or the answer key has uncommitted changes."""
    def git(*args: str) -> str:
        return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout.strip()

    try:
        commit = git("rev-parse", "--short", "HEAD")
        dirty = git(
            "status", "--porcelain", "--",
            "src", "configs", "evals/run_eval.py", "evals/targets.yaml",
        )
        return f"{commit}-dirty" if dirty else commit
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


# ---------------------------------------------------------------------------
# Repeats
# ---------------------------------------------------------------------------

LEVEL_FIELDS = ["druggability_score", "structural_confidence", "chemical_confidence", "literature_confidence"]


def _levels(state: dict) -> dict | None:
    """The four verdicts Claude gave, or None if the reasoning step failed."""
    assessment = state.get("druggability_assessment")
    if assessment is None:
        return None
    return {field: getattr(assessment, field) for field in LEVEL_FIELDS}


def run_pass(targets: list[dict], outputs_dir: Path, label: str = "") -> dict:
    """Run and score every target once. Returns {'targets': [...], 'aggregate': {...}}."""
    results = []
    for target in targets:
        query = target["query"]
        print(f"[{query}]{label} running pipeline...", flush=True)
        t0 = time.perf_counter()
        try:
            state, summary = run_target(query, outputs_dir)
            result = {
                "query": query,
                "identity": score_identity(target, summary),
                "fact_recall": score_fact_recall(target, summary),
                "citation": score_citation_validity(target, summary, state),
                "gap_honesty": score_gap_honesty(target, summary),
                "levels": _levels(state),
                "pipeline_errors": summary.get("data_gaps", {}),
            }
        except Exception as e:
            result = {"query": query, "error": f"{type(e).__name__}: {e}"}
        result["seconds"] = round(time.perf_counter() - t0, 1)
        results.append(result)

        scores = "  ".join(
            f"{m}={_fmt(result[m]['score'])}" for m in METRICS if m in result
        ) or result.get("error")
        print(f"[{query}]{label} {result['seconds']}s  {scores}", flush=True)

    aggregate = {}
    for metric in METRICS:
        values = [r[metric]["score"] for r in results if metric in r and r[metric]["score"] is not None]
        aggregate[metric] = statistics.mean(values) if values else None
    return {"targets": results, "aggregate": aggregate}


def _stats(values: list[float]) -> dict | None:
    """Mean, sample SD, min, max and n — None if there are no values."""
    if not values:
        return None
    return {
        "mean": statistics.mean(values),
        "sd": statistics.stdev(values) if len(values) > 1 else 0.0,
        "min": min(values),
        "max": max(values),
        "n": len(values),
    }


def summarize(passes: list[dict]) -> dict:
    """
    Combine repeated passes into per-target and overall statistics.

    Per target: mean/SD/min/max of each metric over the repeats in which it
    was scored, how many repeats failed, and how often Claude's four verdicts
    (druggability + three confidences) came out the same.

    Overall: mean/SD of the per-repeat means, so the spread describes how
    much the headline number moves from one full eval to the next.
    """
    queries = [r["query"] for r in passes[0]["targets"]]
    targets = []
    for query in queries:
        results = [r for p in passes for r in p["targets"] if r["query"] == query]
        scored = [r for r in results if "error" not in r]
        summary = {
            "query": query,
            "scored": len(scored),
            "errors": len(results) - len(scored),
        }
        for metric in METRICS:
            summary[metric] = _stats(
                [r[metric]["score"] for r in scored if r[metric]["score"] is not None]
            )

        verdicts = [r["levels"] for r in scored if r.get("levels")]
        summary["levels"] = {
            field: dict(Counter(v[field] for v in verdicts)) for field in LEVEL_FIELDS
        } if verdicts else {}
        if verdicts:
            combos = Counter(tuple(v[f] for f in LEVEL_FIELDS) for v in verdicts)
            summary["levels_agree"] = combos.most_common(1)[0][1]   # repeats matching the commonest verdict
            summary["levels_stable"] = len(combos) == 1
        else:
            summary["levels_agree"] = 0
            summary["levels_stable"] = None
        targets.append(summary)

    aggregate = {
        metric: _stats([p["aggregate"][metric] for p in passes if p["aggregate"][metric] is not None])
        for metric in METRICS
    }
    return {
        "aggregate": aggregate,
        "targets": targets,
        "levels_stable_count": sum(t["levels_stable"] is True for t in targets),
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run the Target Atlas evaluation harness.")
    parser.add_argument("--targets", nargs="*", help="subset of queries to run, e.g. EGFR TREM2")
    parser.add_argument("--no-cache", action="store_true", help="call live APIs without caching")
    parser.add_argument(
        "--set", action="append", default=[], metavar="KEY=VALUE",
        help="config override, repeatable, e.g. --set agents.reasoning.temperature=0",
    )
    parser.add_argument("--no-mlflow", action="store_true", help="do not log the run to MLflow")
    parser.add_argument(
        "--repeats", type=int, default=1,
        help="run the whole eval N times and report mean and spread (default 1)",
    )
    args = parser.parse_args(argv)
    if args.repeats < 1:
        parser.error("--repeats must be at least 1")

    cfg = load_config(args.set)

    if not args.no_cache:
        enable_cache(CACHE_DIR)

    targets = yaml.safe_load(TARGETS_FILE.read_text(encoding="utf-8"))["targets"]
    if args.targets:
        wanted = {t.upper() for t in args.targets}
        targets = [t for t in targets if t["query"].upper() in wanted]

    started = datetime.now()
    run_dir = RESULTS_DIR / started.strftime("%Y-%m-%d_%H%M%S")

    # Repeats are the outer loop: if a run is interrupted, every finished
    # repeat is complete (all targets), so partial results stay comparable.
    passes = []
    for k in range(1, args.repeats + 1):
        label = f" r{k}/{args.repeats}" if args.repeats > 1 else ""
        result = run_pass(targets, run_dir / "outputs" / f"repeat_{k}", label)
        passes.append({"repeat": k, **result})

    run = {
        "started": started.isoformat(timespec="seconds"),
        "git_commit": _git_commit(),
        "model": cfg.agents.reasoning.model,
        "overrides": args.set,
        "config": config_as_dict(cfg),
        "cache": "off" if args.no_cache else CACHE_DIR.relative_to(EVALS_DIR.parent).as_posix(),
        "repeats": args.repeats,
        **summarize(passes),
        "passes": passes,
    }

    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "results.json").write_text(json.dumps(run, indent=2), encoding="utf-8")
    markdown = build_markdown(run)
    (run_dir / "results.md").write_text(markdown, encoding="utf-8")

    print()
    print(markdown)
    print(f"Saved to {run_dir}")

    # After the files are written: a tracking problem must never cost the results
    if not args.no_mlflow:
        try:
            from evals.tracking import log_eval_run, tracking_uri
            run_id = log_eval_run(run, run_dir)
            print(f"Logged to MLflow: run {run_id} ({tracking_uri()})")
        except Exception as e:
            print(f"Warning: MLflow logging failed, results are still in {run_dir}: {e}")


if __name__ == "__main__":
    main()
