# Target Atlas eval — 2026-10-24T20:11:54

Commit `3319341` · model `claude-sonnet-4-6` · temperature `0` · cache `evals/cache` · repeats 5

Scores are mean ± sample SD over 5 repeats of the whole eval. Retrieval is cached, so variation comes from the Claude call.

| Target | Identity | Fact recall | Citation validity | Gap honesty | Verdict stable |
|---|---|---|---|---|---|
| EGFR | 1.00 ± 0.00 | 0.36 ± 0.00 | 1.00 ± 0.00 | 1.00 ± 0.00 | yes (5/5) |
| ERBB2 | 1.00 ± 0.00 | 0.75 ± 0.00 | 1.00 ± 0.00 | 1.00 ± 0.00 | yes (5/5) |
| BRAF | 1.00 ± 0.00 | 0.38 ± 0.00 | 1.00 ± 0.00 | 1.00 ± 0.00 | yes (5/5) |
| KRAS | 1.00 ± 0.00 | 0.29 ± 0.00 | 1.00 ± 0.00 | 1.00 ± 0.00 | yes (5/5) |
| ABL1 | 1.00 ± 0.00 | 0.50 ± 0.00 | 1.00 ± 0.00 | 1.00 ± 0.00 | yes (5/5) |
| BTK | 1.00 ± 0.00 | 0.62 ± 0.00 | 1.00 ± 0.00 | 1.00 ± 0.00 | yes (5/5) |
| JAK2 | 1.00 ± 0.00 | 0.43 ± 0.00 | 1.00 ± 0.00 | 1.00 ± 0.00 | yes (5/5) |
| CD274 | 1.00 ± 0.00 | 0.38 ± 0.00 | 1.00 ± 0.00 | 1.00 ± 0.00 | yes (5/5) |
| IL6R | 1.00 ± 0.00 | 0.80 ± 0.00 | 1.00 ± 0.00 | 0.67 ± 0.00 | **no** (4/5) |
| TREM2 | 1.00 ± 0.00 | 0.60 ± 0.00 | 1.00 ± 0.00 | 0.88 ± 0.11 | **no** (3/5) |
| **Mean** | 1.00 ± 0.00 | 0.51 ± 0.00 | 1.00 ± 0.00 | 0.95 ± 0.01 | 8/10 stable |

**Verdicts that changed between repeats**

- IL6R: structural_confidence medium×4 high×1
- TREM2: druggability_score high×3 medium×2

**Fact recall by category** (retrieval only — identical across repeats)

| Target | PDB | Drugs | PMIDs |
|---|---|---|---|
| EGFR | 0/5 | 4/4 | 0/2 |
| ERBB2 | 2/3 | 4/4 | 0/1 |
| BRAF | 0/3 | 3/3 | 0/2 |
| KRAS | 0/3 | 2/2 | 0/2 |
| ABL1 | 0/3 | 4/4 | 0/1 |
| BTK | 2/3 | 3/3 | 0/2 |
| JAK2 | 0/3 | 3/3 | 0/1 |
| CD274 | 0/3 | 3/3 | 0/2 |
| IL6R | 2/2 | 2/2 | 0/1 |
| TREM2 | 3/3 | — | 0/2 |

**Mean per repeat**

| Repeat | Identity | Fact recall | Citation validity | Gap honesty |
|---|---|---|---|---|
| 1 | 1.00 | 0.51 | 1.00 | 0.97 |
| 2 | 1.00 | 0.51 | 1.00 | 0.95 |
| 3 | 1.00 | 0.51 | 1.00 | 0.95 |
| 4 | 1.00 | 0.51 | 1.00 | 0.95 |
| 5 | 1.00 | 0.51 | 1.00 | 0.97 |
