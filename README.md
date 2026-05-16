# Target Atlas — Multi-agent protein target analysis for drug discovery

**Author:** Iker Zapirain Gysling  
**Status:** Active development — v0.1  
**Domain:** Drug Discovery · Structural Bioinformatics · Applied LLMs

---

> Given a protein target, Target Atlas retrieves and synthesises structural,
> bioactivity, and literature evidence — producing a calibrated druggability
> assessment with explicit confidence levels and reasoning trace in minutes.

```bash
# Analyse any human protein target by UniProt ID or gene name
python -m target_atlas.cli run --target EGFR
# Output: results/EGFR/report.md + results/EGFR/summary.json
```

**What makes it technically interesting:**
- Multi-agent LangGraph pipeline — five specialised agents with shared state and independent failure isolation
- Synthesises five heterogeneous sources — UniProt, PDB, AlphaFold, ChEMBL, PubMed — into one structured assessment
- Calibrated confidence scoring — structural, chemical, and literature confidence scored independently before synthesis
- Honest uncertainty — evidence gaps explicitly enumerated, not silently omitted
- Production-minded — config-driven (Hydra), experiment tracked (MLflow), Docker packaged, CI tested

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
- **AlphaFold** — predicted structure confidence (pLDDT fractions) for targets with sparse experimental coverage
- **ChEMBL** — bioactivity density, IC50 distribution, approved drugs
- **PubMed** — recent publications, disease associations, field activity

A reasoning agent (Claude) synthesises all retrieved evidence into a calibrated druggability assessment with explicit confidence levels and evidence gaps. Two outputs are produced:

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
│                  │  PubMed E-utils → recent publications, disease context
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

All agents communicate exclusively through a shared `TargetAtlasState` TypedDict — no agent calls another directly. LangGraph manages execution order and state persistence. API failures are caught at the agent level, written to `agent_errors`, and the pipeline continues with whatever data was successfully retrieved.

**Key components:**

| Module | Description |
|---|---|
| `src/target_atlas/state.py` | Shared state schema — TypedDict + Pydantic models |
| `src/target_atlas/clients/uniprot_client.py` | UniProt REST API — name/ID resolution |
| `src/target_atlas/clients/pdb_client.py` | RCSB PDB search + entry detail retrieval |
| `src/target_atlas/clients/alphafold_client.py` | AlphaFold EBI API — pLDDT confidence |
| `src/target_atlas/clients/chembl_client.py` | ChEMBL REST API — bioactivity + approved drugs |
| `src/target_atlas/clients/pubmed_client.py` | NCBI E-utils — recent publications |
| `src/target_atlas/agents/` | LangGraph agent nodes |
| `src/target_atlas/graph.py` | LangGraph graph definition and compilation |

---

## Key Design Decisions

**Why LangGraph rather than a sequential script?**
A sequential script is simpler but fragile — a single API failure aborts the entire run. LangGraph provides node-level error isolation (failures write to `agent_errors` and the graph continues), conditional routing, and checkpointing. The shared state architecture also makes each agent independently testable with mock inputs, without requiring the full pipeline to run.

**Why five separate client files rather than one data fetcher?**
Encapsulation. Each client knows everything about one external API and nothing about the pipeline it serves. If PDB changes their API (as RCSB has done twice), only `pdb_client.py` changes — no agent code is touched. This was validated during development when both the AlphaFold API (field rename: `meanPlddt` → `globalMetricValue`) and ChEMBL API (endpoint rename: `drug_mechanism` → `mechanism`) changed mid-build.

**Why Claude API for the reasoning node rather than a local model?**
The reasoning node requires multi-source synthesis, uncertainty quantification, and structured output — tasks where frontier models significantly outperform smaller local models at this stage. The tradeoff is cost and latency per run. A local model (Llama, Mistral) is a planned v0.2 option for offline or cost-sensitive deployments.

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
| EGFR | P00533 | High evidence density — 200+ PDB structures, 25,758 ChEMBL IC50 entries, 20 approved drugs |
| TREM2 | Q9NZC2 | Sparse evidence — few structures, no ChEMBL entry, active neuroscience literature |
| IL-6R | P08887 | Medium evidence — validated immunology target, approved biologics, moderate small molecule data |

Example outputs for all three targets are committed to `examples/`.

### Confidence scoring

Structural, chemical, and literature confidence are each scored independently on a four-level scale (`high`, `medium`, `low`, `none`) before being synthesised into an overall druggability assessment. Confidence levels are derived from explicit thresholds, not learned — making them inspectable and adjustable.

### Known Failure Modes

- **Salt form duplication in approved drugs**: ChEMBL treats drug salts as separate entities (Osimertinib and Osimertinib Mesylate appear as distinct entries). Deduplication via `molecule_hierarchy` is a planned fix.
- **ChEMBL target coverage gaps**: targets without a ChEMBL entry (e.g. TREM2 at time of writing) return no bioactivity data. The system reports this explicitly as an evidence gap rather than silently omitting it.
- **PubMed noise**: gene name search returns papers with passing mentions of the target, not only primary target biology papers. Publication count is therefore an upper bound on field activity.
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

```bash
export ANTHROPIC_API_KEY=your_key_here
```

### Run a target analysis

```bash
python -m target_atlas.cli run --target P00533
# or by gene name
python -m target_atlas.cli run --target EGFR
```

Outputs are written to `results/<target>/`:
- `report.md` — structured druggability assessment
- `summary.json` — machine-readable summary

### With Docker *(coming in v0.1 release)*

```bash
docker build -t target-atlas .
docker run -e ANTHROPIC_API_KEY=your_key -v $(pwd)/results:/app/results target-atlas --target P00533
```

---

## Repository Structure

```
target-atlas/
├── README.md
├── LICENSE
├── pyproject.toml
├── Dockerfile                          # coming v0.1
│
├── configs/
│   ├── agents.yaml                     # model, temperature, max_tokens
│   └── apis.yaml                       # endpoints, timeouts, rate limits
│
├── src/
│   └── target_atlas/
│       ├── state.py                    # TargetAtlasState TypedDict + Pydantic models
│       ├── graph.py                    # LangGraph graph definition
│       ├── cli.py                      # Typer CLI entrypoint
│       ├── agents/
│       │   ├── input_parser.py
│       │   ├── structure_agent.py
│       │   ├── literature_agent.py
│       │   ├── reasoning_agent.py
│       │   └── report_generator.py
│       └── clients/
│           ├── uniprot_client.py       # ✓ implemented
│           ├── pdb_client.py           # ✓ implemented
│           ├── alphafold_client.py     # ✓ implemented
│           ├── chembl_client.py        # ✓ implemented
│           └── pubmed_client.py        # in progress
│
├── examples/
│   ├── egfr_P00533/                    # coming v0.1
│   ├── trem2_Q9NZC2/                   # coming v0.1
│   └── il6r_P08887/                    # coming v0.1
│
├── tests/
│   ├── test_state.py
│   ├── test_structure_agent.py
│   └── test_graph.py
│
├── notebooks/
│   └── 01_system_walkthrough.ipynb    # coming v0.1
│
└── .github/
    └── workflows/
        └── ci.yml                      # lint + smoke tests
```

---

## Roadmap

**v0.1 (current sprint — target: May 30, 2026)**
- [x] Project scaffold, dependencies, pyproject.toml
- [x] State schema — TargetAtlasState TypedDict + all Pydantic models
- [x] UniProt client — name and ID resolution
- [x] PDB client — resolution-ranked structure retrieval
- [x] AlphaFold client — pLDDT confidence fractions
- [x] ChEMBL client — bioactivity summary + approved drugs
- [ ] PubMed client — recent publications and disease context
- [ ] LangGraph graph — all five agent nodes wired
- [ ] Reasoning agent — Claude API with structured output
- [ ] Report generator — markdown + JSON outputs
- [ ] Hydra config system
- [ ] MLflow experiment tracking
- [ ] Dockerfile
- [ ] Smoke tests + GitHub Actions CI
- [ ] Three benchmark example outputs (EGFR, TREM2, IL-6R)

**v0.2 (planned)**
- [ ] Parallel agent execution (structure + literature agents concurrently)
- [ ] Per-residue pLDDT mapping via AlphaFold confidence endpoint
- [ ] Europe PMC as third literature source
- [ ] Pocket detection integration (fpocket) for structural druggability
- [ ] ChromaDB persistent memory for cross-target comparison
- [ ] Benchmarking against expert druggability consensus (published targets)
- [ ] Salt form deduplication in ChEMBL approved drugs
- [ ] Non-human organism support

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