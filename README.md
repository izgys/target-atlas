# Target Atlas — An LLM workflow for protein target analysis in drug discovery

[![CI](https://github.com/izgys/target-atlas/actions/workflows/ci.yml/badge.svg)](https://github.com/izgys/target-atlas/actions/workflows/ci.yml)

**Author:** Iker Zapirain Gysling  
**Status:** v0.1 released · v0.2 planned (see Roadmap)  
**Domain:** Drug Discovery · Structural Bioinformatics · Applied LLMs

---

**Target Atlas** takes a UniProt ID or gene name and produces an evidence-graded druggability assessment — synthesising structural, bioactivity, and literature evidence from five sources into a structured report with explicit confidence levels and reasoning trace.

```bash
# Analyse any human protein target by gene name or UniProt ID
target-atlas run EGFR

# Output: results/EGFR_P00533/report.md + results/EGFR_P00533/summary.json
```

**What makes it technically interesting:**
- LangGraph workflow — five specialised nodes with shared state and independent failure isolation
- Synthesises five heterogeneous sources — UniProt, PDB, AlphaFold, ChEMBL, PubMed — into one structured assessment
- Separate confidence scoring — structural, chemical, and literature confidence scored independently before synthesis
- Honest uncertainty — evidence gaps explicitly enumerated, not silently omitted
- Measured, not asserted — a deterministic evaluation harness scores every change against API-verified facts for ten targets
- Resilient retrieval — shared HTTP layer with retries and backoff, plus an on-disk cache for reproducible evaluation runs
- Reproducible by construction — Hydra config, MLflow-tracked eval runs reported as mean ± SD over repeats, offline tests in CI, and a Docker image

---

## The Problem

Early target selection is one of the most consequential decisions in drug discovery. Committing to a protein target implies years of work and hundreds of millions of dollars — yet the decision is routinely made by synthesising heterogeneous evidence from structural databases, bioactivity repositories, and the primary literature by hand.

For a well-characterised target like EGFR, this synthesis is tractable. For a novel target, or for a portfolio-level assessment across twenty candidates, it becomes a bottleneck. The tools available either require expert manual curation (databases) or produce black-box scores with no auditable reasoning trail (ML models).

Target Atlas sits in the middle: automated multi-source synthesis with a transparent, inspectable reasoning trace.

---

## What It Does

Target Atlas takes a protein target — a UniProt ID (`P00533`) or a gene name (`EGFR`) — and automatically produces a structured druggability assessment by retrieving and synthesising evidence from five sources:

- **UniProt** — canonical protein identity, gene name, organism, curation status
- **PDB** — experimental structures ranked by resolution, ligand-bound states
- **AlphaFold** — predicted structure confidence (pLDDT fractions), as a cross-check on experimental coverage
- **ChEMBL** — bioactivity counts, median IC50, approved drugs
- **PubMed** — recent publications and literature volume

A reasoning node (Claude) synthesises all retrieved evidence into a druggability assessment with explicit confidence levels and evidence gaps. Two outputs are produced:

- `report.md` — structured markdown report for human review
- `summary.json` — machine-readable summary for downstream pipelines

---

## Architecture

```
User input: "EGFR" or "P00533"
        │
        ▼
┌─────────────────┐
│  input_parser   │  UniProt API → resolves canonical ID, gene name, organism
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ structure_agent │  PDB API → experimental structures ranked by resolution
│                 │  AlphaFold API → per-band pLDDT confidence fractions
└────────┬────────┘
         │
         ▼
┌──────────────────┐
│ literature_agent │  ChEMBL API → bioactivity summary, approved drugs
│                  │  PubMed E-utils → recent publications, literature volume
└────────┬─────────┘
         │
         ▼
┌─────────────────┐
│ reasoning_agent │  Claude API → chain-of-thought druggability assessment
│                 │  structured output → DruggabilityAssessment (Pydantic)
└────────┬────────┘
         │
         ▼
┌──────────────────┐
│ report_generator │  renders state → report.md + summary.json
└──────────────────┘
```

All nodes communicate exclusively through a shared `TargetAtlasState` TypedDict — no node calls another directly. LangGraph manages execution order and the flow of state between nodes. API failures are caught at the node level, written to `agent_errors`, and the pipeline continues with whatever data was successfully retrieved.

**Key components:**

| Module | Description |
|---|---|
| `src/target_atlas/state.py` | Shared state schema — TypedDict + Pydantic models |
| `src/target_atlas/clients/uniprot_client.py` | UniProt REST API — name/ID resolution |
| `src/target_atlas/clients/pdb_client.py` | RCSB PDB search + entry detail retrieval |
| `src/target_atlas/clients/alphafold_client.py` | AlphaFold EBI API — pLDDT confidence |
| `src/target_atlas/clients/chembl_client.py` | ChEMBL REST API — bioactivity + approved drugs |
| `src/target_atlas/clients/pubmed_client.py` | NCBI E-utils — recent publications |
| `src/target_atlas/agents/` | LangGraph nodes (the `*_agent` file names predate the workflow framing) |
| `src/target_atlas/graph.py` | LangGraph graph definition and compilation |

---

## Key Design Decisions

**Why a workflow, not an agent?**
Only one node calls an LLM, and the path through the graph is fixed in code: every target is resolved, then gets the same structural, chemical and literature retrieval, then one synthesis step. Nothing is gained by letting a model decide which database to query next — the evidence a druggability assessment needs is known in advance. A fixed workflow is cheaper, faster, reproducible and evaluable step by step. The LLM is used where judgement is actually needed: weighing heterogeneous evidence and naming what is missing. An agentic design would earn its place for open-ended follow-up questions (e.g. deciding to search for a specific mutation or a related target), which is outside the scope of v0.1.

**Why LangGraph rather than a sequential script?**
A sequential script is simpler but fragile — a single API failure aborts the entire run. LangGraph provides node-level error isolation (failures write to `agent_errors` and the graph continues), conditional routing, and checkpointing. The shared state architecture also makes each node independently testable with mock inputs, without requiring the full pipeline to run.

**Why five separate client files rather than one data fetcher?**
Encapsulation. Each client knows everything about one external API and nothing about the pipeline it serves. If PDB changes their API (as RCSB has done twice), only `pdb_client.py` changes — no node code is touched. This was validated during development when both the AlphaFold API (field rename: `meanPlddt` → `globalMetricValue`) and ChEMBL API (endpoint rename: `drug_mechanism` → `mechanism`) changed mid-build.

**Why Claude API for the reasoning node rather than a local model?**
The reasoning node requires multi-source synthesis, explicit handling of missing evidence, and structured output — tasks where frontier models significantly outperform smaller local models at this stage. The tradeoff is cost and latency per run. A local model (Llama, Mistral) is a planned v0.2 option for offline or cost-sensitive deployments.

**Why AlphaFold unconditionally, not only as a PDB fallback?**
The two sources are complementary, not alternatives. When PDB structures exist, AlphaFold provides a confidence cross-check — high pLDDT corroborating experimental coverage strengthens the structural confidence assessment. The discordant case (experimental structures present, low pLDDT in a specific region) is scientifically informative: it flags disordered regions that crystal structures may have failed to resolve.

**Why pLDDT fractions rather than mean pLDDT alone?**
Mean pLDDT collapses the confidence distribution to a single number. A protein with a well-ordered kinase domain and disordered termini may have the same mean pLDDT as a uniformly mediocre prediction. The four-band fraction breakdown (`fractionPlddtVeryHigh`, `fractionPlddtConfident`, `fractionPlddtLow`, `fractionPlddtVeryLow`) preserves that distribution.

**pLDDT and druggability — an important distinction:**
High pLDDT indicates structural order — a stable 3D fold exists. It is a necessary but not sufficient condition for druggability. Low pLDDT is the stronger signal: it essentially rules out conventional small molecule binding in that region. True druggability assessment requires pocket detection (fpocket, SiteMap) — a planned v0.2 extension.

---

## Evaluation

### Benchmark targets

Three targets were selected to span the evidence density spectrum:

| Target | UniProt | Rationale |
|---|---|---|
| EGFR | P00533 | Dense evidence — 393 PDB entries, 26,600 ChEMBL IC50 entries, 15 approved drugs (20 ChEMBL entries including salt forms) |
| TREM2 | Q9NZC2 | Sparse chemistry — 15 PDB entries, a ChEMBL target with no IC50 data or approved drugs, active neuroscience literature |
| IL-6R | P08887 | Biologics-only — validated immunology target, two approved antibodies (tocilizumab, sarilumab), no small-molecule IC50 data |

Outputs for all three targets, generated by the evaluation harness, are in [`examples/`](examples/).

### Evaluation harness

`evals/run_eval.py` runs the full pipeline on ten targets — dense kinases (EGFR, ERBB2, BRAF, ABL1, BTK, JAK2), a historically "undruggable" target (KRAS), biologics-dominated targets (CD274/PD-L1, IL6R) and a sparse one (TREM2) — and scores each output against API-verified expected facts in `evals/targets.yaml`. Scoring is deterministic; no LLM judges another LLM.

| Metric | What it checks |
|---|---|
| Identity | The gene name resolves to the correct canonical UniProt accession |
| Fact recall | Fraction of expected PDB entries, approved drugs and key PMIDs present in `summary.json` |
| Citation validity | Fraction of PDB IDs and PMIDs in the output (retrieved or written by Claude) that exist and belong to the target |
| Gap honesty | Fraction of consistency checks passed between what was retrieved and what the assessment claims (e.g. no ChEMBL bioactivity → chemical confidence low/none and the gap is listed) |

API responses are cached in `evals/cache/`, so reruns are fast and reproducible; the Claude call is never cached. Each run writes `results.json`, `results.md` and all outputs to `evals/results/<timestamp>/`, tagged with the git commit.

```bash
target-atlas eval                      # all ten targets (run from the repository root)
target-atlas eval -t EGFR -t TREM2     # a subset
target-atlas eval --repeats 5          # five full passes, reported as mean ± SD
```

Every run is also logged to a local MLflow store in `mlruns/` (gitignored): the full resolved config as parameters, the git commit and model as tags, the four metrics per target and as means, and the run folder as artifacts. To browse runs and compare them side by side:

```bash
mlflow ui --backend-store-uri sqlite:///mlruns/mlflow.db   # then open http://127.0.0.1:5000
```

Pass `--no-mlflow` to skip tracking.

**Results** (`claude-sonnet-4-6`, temperature 0, commit `3319341`, five repeats of the full eval; run [`2026-10-24_201154`](evals/results/2026-10-24_201154/results.md)):

| Target | Identity | Fact recall | PDB | Drugs | PMIDs | Citation validity | Gap honesty (mean ± SD) | Verdict stable |
|---|---|---|---|---|---|---|---|---|
| EGFR | 1.00 | 0.36 | 0/5 | 4/4 | 0/2 | 1.00 | 1.00 ± 0.00 | 5/5 |
| ERBB2 | 1.00 | 0.75 | 2/3 | 4/4 | 0/1 | 1.00 | 1.00 ± 0.00 | 5/5 |
| BRAF | 1.00 | 0.38 | 0/3 | 3/3 | 0/2 | 1.00 | 1.00 ± 0.00 | 5/5 |
| KRAS | 1.00 | 0.29 | 0/3 | 2/2 | 0/2 | 1.00 | 1.00 ± 0.00 | 5/5 |
| ABL1 | 1.00 | 0.50 | 0/3 | 4/4 | 0/1 | 1.00 | 1.00 ± 0.00 | 5/5 |
| BTK | 1.00 | 0.62 | 2/3 | 3/3 | 0/2 | 1.00 | 1.00 ± 0.00 | 5/5 |
| JAK2 | 1.00 | 0.43 | 0/3 | 3/3 | 0/1 | 1.00 | 1.00 ± 0.00 | 5/5 |
| CD274 | 1.00 | 0.38 | 0/3 | 3/3 | 0/2 | 1.00 | 1.00 ± 0.00 | 5/5 |
| IL6R | 1.00 | 0.80 | 2/2 | 2/2 | 0/1 | 1.00 | 0.67 ± 0.00 | **4/5** |
| TREM2 | 1.00 | 0.60 | 3/3 | — | 0/2 | 1.00 | 0.88 ± 0.11 | **3/5** |
| **Mean** | **1.00** | **0.51** | | | | **1.00** | **0.95 ± 0.01** | **8/10 stable** |

Identity, fact recall and citation validity depend only on retrieval, which is cached, so they were identical in all five repeats and are shown as single values. Gap honesty depends on Claude's verdicts: per target it is mean ± sample SD over the repeats; in the Mean row the SD is over the five per-repeat means (0.97, 0.95, 0.95, 0.95, 0.97), i.e. how much the headline number moves between full evals. *Verdict stable* counts the repeats that match the most common combination of Claude's four verdicts (druggability and the three confidences).

How to read it:
- **Approved drugs are recovered in full (28/28)**, and identity resolution is correct for all ten targets.
- **Low PDB and PMID recall is a retrieval-strategy limit, not a retrieval failure.** The pipeline details the 20 best-resolved structures and the 20 most recent papers; landmark entries fall outside those windows (EGFR's erlotinib complex 1M17 ranks 191 of 393 by resolution). See Known Failure Modes.
- **Citation validity is currently a plumbing check.** Claude did not write any PDB ID or PMID into its own text in these runs, so every citation came straight from an API. The metric becomes a hallucination check once reports cite IDs in prose.
- **IL6R fails the same check in every repeat:** zero ChEMBL IC50 entries, yet chemical confidence was scored `medium` all five times. That is defensible given two approved antibodies, but it falls outside the rubric, which has no notion of biologics. A systematic error, not noise.
- **TREM2 is the borderline case.** Its overall druggability came out `high` in three repeats and `medium` in two; every `high` run fails the sparse-target honesty check (0.80), every `medium` run passes (1.00). The spread of 0.88 ± 0.11 is that one verdict flipping. The single-sample result previously reported here (1.00) was one of the passing draws.
- **Temperature 0 reduces variation but does not remove it.** It makes the model favour its most likely output, but an API model is still not guaranteed to return identical text for identical input. That is why results are reported over repeats rather than from one run.

### Confidence scoring

Structural, chemical, and literature confidence are each scored independently on a four-level scale (`high`, `medium`, `low`, `none`) before being synthesised into an overall druggability assessment. The thresholds are explicit and live in the reasoning prompt, not learned — making them inspectable and adjustable. Claude applies them and occasionally overrides them; see Rubric overrides below.

### Known Failure Modes

- **Salt form duplication in approved drugs**: ChEMBL treats drug salts as separate entities (Osimertinib and Osimertinib Mesylate appear as distinct entries). Deduplication via `molecule_hierarchy` is a planned fix.
- **ChEMBL coverage gaps**: targets without bioactivity data (TREM2 has a ChEMBL target but no IC50 entries) are reported explicitly as an evidence gap rather than silently omitted.
- **Retrieval windows miss landmark evidence**: only the 20 best-resolved PDB entries and the 20 most recent PubMed papers are retrieved in detail, so well-known drug-bound structures and foundational papers are usually absent (PDB recall 9/31, PMID recall 0/16 in the evaluation). Total counts are passed to the reasoning node, so coverage is not understated.
- **Gene-symbol literature search**: PubMed is searched by official gene symbol in the title, which undercounts targets known by another name (CD274: 105 papers, while the field writes "PD-L1").
- **Rubric overrides**: Claude sometimes overrides the numeric confidence thresholds with prior knowledge, scoring literature confidence `high` for CD274 (105 papers) and IL6R (226) where the rubric says `medium`. That is correct for CD274 given the undercount, but it means confidence is not purely evidence-derived. The same happens when a source fails: in one ADRB2 run where ChEMBL returned a server error, chemical confidence was scored `high` from prior knowledge rather than `none`. Failed retrievals are labelled as failures rather than absences in both the reasoning context and the report, and every API call retries transient errors with backoff, but the scoring rule for failed sources is not yet enforced.
- **Run-to-run variation in the reasoning step**: retrieval is cached and the Claude call runs at temperature 0, yet identical evidence does not always produce identical verdicts — temperature 0 does not make an API model deterministic. Over five repeats of the full eval, 8 of 10 targets gave the same four verdicts every time. TREM2's overall druggability was `high` three times and `medium` twice, failing the sparse-target honesty check whenever it was `high`; IL6R's structural confidence changed once (`medium` ×4, `high` ×1). Borderline targets are where this matters, so reported results are mean ± SD over repeats, never a single sample.
- **No biologics in the chemical rubric**: chemical confidence is defined on small-molecule IC50 counts, so antibody-only targets (IL6R) fall outside it.
- **"Ligand-bound" includes ions and glycans**: any non-polymer entity counts as a ligand, which overstates small-molecule structural evidence.
- **Fragment structures rank as "best"**: PDB entries are ranked by resolution only, with no check of how much of the target they contain. For ADRB2 (outside the eval set), the reported best structure, 1GQ4 at 1.9 Å, is a NHERF PDZ domain bound to a short ADRB2 tail peptide; the best receptor structure is 2RH1 at 2.4 Å. Peptide and fragment complexes can inflate structural confidence and crowd real structures out of the top 20.
- **Median IC50 from a sample**: the IC50 count covers all ChEMBL entries, but the median is computed from the first 2,000 values only (`apis.chembl.max_activities`), and the reasoning context does not say so. For EGFR, Claude reports the median "across all 26,600 entries", which overstates what was measured.
- **IC50-only chemistry**: bioactivity counts and the median use IC50 values only. Kinase data is mostly IC50, but GPCR and nuclear-receptor data is mostly Ki, EC50 or Kd (ADRB2: 1,665 IC50 vs 1,862 Ki entries), so chemical evidence is systematically undercounted for non-enzyme target classes.
- **AlphaFold per-residue mapping**: the current API returns pre-computed confidence fractions, not per-residue scores. Binding-site-specific confidence assessment requires a second API call to the confidence JSON endpoint — planned for v0.2.
- **Human targets only**: UniProt search is currently restricted to `organism_id:9606`. Non-human targets require manual UniProt ID input.

---

## Quickstart

### Requirements

- Python 3.12+
- `uv` (recommended) or `pip`
- Anthropic API key

### Local installation

```bash
git clone https://github.com/izgys/target-atlas
cd target-atlas
uv venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # macOS/Linux
uv sync
```

### Set API key

Create a `.env` file in the project root containing one line (no quotes):

```
ANTHROPIC_API_KEY=sk-ant-...
```

`.env` is gitignored and excluded from the Docker image. `target-atlas` reads it automatically, and the Docker commands below pass it with `--env-file .env`, so the key never has to be typed in a terminal. An `ANTHROPIC_API_KEY` environment variable also works.

### Run a target analysis

```bash
target-atlas run EGFR                  # by gene name
target-atlas run P00533                # or by UniProt ID
target-atlas run TREM2 --out reports   # custom output folder
```

The terminal shows the druggability score, the three confidence levels, an evidence summary and the evidence gaps. Unresolvable targets exit with a clear message and status 1.

Outputs are written to `results/<gene>_<uniprot_id>/`:
- `report.md` — structured druggability assessment
- `summary.json` — machine-readable summary

### Change settings

Model, temperature, timeouts, retries and retrieval windows live in `configs/agents.yaml` and `configs/apis.yaml`. Edit the files, or override any value for one run with `--set` (repeatable):

```bash
target-atlas run EGFR --set agents.reasoning.temperature=0
target-atlas run EGFR --set apis.pdb.max_structures=50 --set apis.pubmed.max_results=50
target-atlas eval --set agents.reasoning.max_tokens=4000
```

A misspelt key is rejected rather than silently ignored. Every eval run saves the resolved config and its overrides in `results.json`.

### Run the tests

```bash
uv run ruff check .
uv run pytest
```

The tests mock every API and Claude, so they run offline and need no API key. CI runs them on every push with networking switched off.

### With Docker

The image is built with uv from `uv.lock`, runs as a non-root user and contains no secrets: `.env` is excluded from the build context, and the API key is passed when the container starts. Run these from the repository root.

**Build**

```bash
docker build -t target-atlas .
```

**Analyse a target.** `--env-file .env` passes the key from your `.env` file to the container when it starts (write it as `ANTHROPIC_API_KEY=sk-ant-...`, without quotes: Docker keeps quotes as part of the value). Reports land in `results/` on your machine.

```bash
docker run --rm --env-file .env -v "$(pwd)/results:/app/results" target-atlas run EGFR   # macOS/Linux
docker run --rm --env-file .env -v "%cd%/results:/app/results" target-atlas run EGFR     # Windows (cmd)
```

If the key is in an environment variable instead, `-e ANTHROPIC_API_KEY` (no value) copies it into the container. Every CLI option works after the image name, e.g. `target-atlas run EGFR --set agents.reasoning.temperature=0`.

**Run the evaluation.** Mount the results folder, the API cache (so retrieval is replayed instead of called live) and an MLflow store for container runs:

```bash
# macOS/Linux
docker run --rm --env-file .env \
  -v "$(pwd)/evals/results:/app/evals/results" \
  -v "$(pwd)/evals/cache:/app/evals/cache" \
  -v "$(pwd)/mlruns-docker:/app/mlruns" \
  target-atlas eval -t EGFR -t TREM2

# Windows (cmd)
docker run --rm --env-file .env -v "%cd%/evals/results:/app/evals/results" -v "%cd%/evals/cache:/app/evals/cache" -v "%cd%/mlruns-docker:/app/mlruns" target-atlas eval -t EGFR -t TREM2
```

Notes:
- **Commit in eval results.** The image has no `.git`, so pass the commit at build time to have it recorded: `docker build --build-arg GIT_COMMIT=$(git rev-parse --short HEAD) -t target-atlas .` (macOS/Linux, PowerShell), or in cmd: `for /f %i in ('git rev-parse --short HEAD') do docker build --build-arg GIT_COMMIT=%i -t target-atlas .`
- **Separate MLflow store.** MLflow saves artifact locations as absolute paths, which differ between the container (`/app/mlruns`) and your machine, so container runs use `mlruns-docker/`. Browse their scores with `mlflow ui --backend-store-uri sqlite:///mlruns-docker/mlflow.db`; the artifact files are in `mlruns-docker/artifacts/`.
- **Linux file ownership.** The container user has UID 1000. If yours differs and the mounted folders are not writable, add `--user "$(id -u):$(id -g)"`.
- MLflow telemetry is switched off in the image (`MLFLOW_DISABLE_TELEMETRY=true`); override with `-e MLFLOW_DISABLE_TELEMETRY=false`.

---

## Repository Structure

```
target-atlas/
├── README.md
├── LICENSE
├── pyproject.toml
├── Dockerfile                          # uv build, non-root, key passed at runtime
├── .dockerignore                       # keeps .env and local state out of the image
│
├── configs/                            # Hydra config, loaded with the compose API
│   ├── config.yaml                     # composes the two files below
│   ├── agents.yaml                     # model, temperature, max_tokens
│   └── apis.yaml                       # endpoints, timeouts, retries, retrieval windows
│
├── src/
│   └── target_atlas/
│       ├── state.py                    # TargetAtlasState + assessment schema
│       ├── graph.py                    # LangGraph graph definition
│       ├── cli.py                      # Typer CLI: run, eval
│       ├── config.py                   # load_config() / get_config()
│       ├── agents/
│       │   ├── input_parser.py
│       │   ├── structure_agent.py
│       │   ├── literature_agent.py
│       │   ├── reasoning_agent.py
│       │   └── report_generator.py
│       ├── utils/
│       │   └── http.py                 # shared HTTP client: retries + eval cache
│       └── clients/
│           ├── uniprot_client.py       # one client per API, no pipeline knowledge
│           ├── pdb_client.py
│           ├── alphafold_client.py
│           ├── chembl_client.py
│           └── pubmed_client.py
│
├── evals/
│   ├── targets.yaml                    # expected facts for 10 targets
│   ├── run_eval.py                     # harness + four metrics
│   ├── tracking.py                     # MLflow logging (local SQLite store in mlruns/)
│   └── results/                        # one folder per run (see its README)
│
├── examples/
│   ├── egfr_P00533/                    # report.md + summary.json
│   ├── trem2_Q9NZC2/
│   └── il6r_P08887/
│
├── tests/                              # offline: APIs and Claude mocked
│   ├── conftest.py                     # network guard, fake evidence, fake Claude
│   ├── test_state.py
│   ├── test_nodes.py
│   ├── test_graph.py
│   ├── test_http.py
│   ├── test_config.py
│   ├── test_tracking.py
│   ├── test_repeats.py
│   └── helpers.py
│
└── .github/
    └── workflows/
        └── ci.yml                      # ruff + tests (network off), Docker build + smoke checks
```

---

## Roadmap

**v0.1 (released)**
- [x] Project scaffold, dependencies, pyproject.toml
- [x] State schema — TargetAtlasState TypedDict + all Pydantic models
- [x] UniProt client — name and ID resolution
- [x] PDB client — resolution-ranked structure retrieval
- [x] AlphaFold client — pLDDT confidence fractions
- [x] ChEMBL client — bioactivity summary + approved drugs
- [x] PubMed client — recent publications and literature volume
- [x] Reasoning node — Claude API with structured output
- [x] Report generator — markdown + JSON outputs
- [x] LangGraph graph — all five nodes wired
- [x] Evaluation harness — 10 targets, four deterministic metrics, cached APIs
- [x] Typer CLI — `target-atlas run` and `target-atlas eval`
- [x] Hydra config system — `configs/`, `--set` overrides
- [x] MLflow experiment tracking for eval runs
- [x] Temperature 0 and repeated eval runs (`--repeats`), results reported as mean ± SD
- [x] Dockerfile — built with uv, tested in CI
- [x] Smoke tests + GitHub Actions CI (offline)
- [x] Three benchmark example outputs (EGFR, TREM2, IL-6R)

**v0.2 (planned)**

*Fixes for the known failure modes*
- [ ] Salt form deduplication in ChEMBL approved drugs
- [ ] Second bioactivity source (e.g. BindingDB or PubChem BioAssay) for targets with no ChEMBL activities
- [ ] Relevance-ranked literature retrieval alongside the most recent papers, so landmark papers are not missed
- [ ] Literature search with UniProt aliases and protein names (PD-L1, β2-adrenergic receptor), not only the gene symbol
- [ ] Prompt rule for failed sources — score the dimension `none` and state any prior-knowledge expectation separately
- [ ] Stable verdicts on borderline targets (TREM2): sharper sparse-target thresholds in the rubric, or a majority vote over several reasoning samples
- [ ] Biologics and modality in the chemical rubric, so antibody-only targets (IL6R) are scored on their evidence
- [ ] Ligand filter — exclude ions, glycans and buffer molecules from "ligand-bound" structure counts
- [ ] Structure coverage filter — rank PDB entries by target-residue coverage (SIFTS) so peptide and fragment complexes no longer count as best structures
- [ ] Median IC50 over all activities, or the sample size stated in the reasoning context
- [ ] pChEMBL-based chemistry — count IC50, Ki, Kd and EC50 activities on one scale, so non-kinase target classes are not undercounted
- [ ] Per-residue pLDDT mapping via AlphaFold confidence endpoint
- [ ] Non-human organism support

*Evaluation and usability*
- [ ] Held-out evaluation set outside the kinase-heavy ten (e.g. ADRB2, ESR1) and UniProt-ID queries
- [ ] Benchmarking against expert druggability consensus (published targets)
- [ ] Walkthrough notebook and visual summaries of the evidence in reports
- [ ] Rename `literature_agent` to `evidence_agent` and drop the `*_agent` file names (the workflow has no agents)

*Extensions*
- [ ] Parallel node execution (structure + literature nodes concurrently)
- [ ] Europe PMC as third literature source
- [ ] Pocket detection integration (fpocket) for structural druggability
- [ ] ChromaDB persistent memory for cross-target comparison
- [ ] Local model option for the reasoning node (offline or cost-sensitive use)

---

## Scientific References

- Jumper J et al. (2021). *Nature.* — AlphaFold2. DOI: 10.1038/s41586-021-03819-2
- Berman HM et al. (2000). *Nucleic Acids Res.* — The Protein Data Bank. DOI: 10.1093/nar/28.1.235
- Gaulton A et al. (2017). *Nucleic Acids Res.* — The ChEMBL database. DOI: 10.1093/nar/gkw1074
- UniProt Consortium (2023). *Nucleic Acids Res.* — UniProt. DOI: 10.1093/nar/gkac1052

---

## Author

**Iker Zapirain Gysling**  
Computational Biochemist, PhD  
Barcelona, Spain  
[LinkedIn](https://linkedin.com/in/zgysling) · [GitHub](https://github.com/izgys)

---

## License

MIT License — see `LICENSE` for details.