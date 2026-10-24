# Target Atlas Report — KRAS (P01116)

**Generated:** 2026-10-24T18:13:02.224117  
**Organism:** Homo sapiens  
**Run ID:** 6f211917-2146-446d-b486-455aaef103fe  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

KRAS is one of the most extensively studied oncology targets, with 556 high-resolution PDB structures (best 0.953Å), two FDA-approved covalent inhibitors (sotorasib and adagrasib targeting G12C), and nearly 6,000 ChEMBL IC50 entries. Druggability is high for the G12C mutant specifically, though broader mutant coverage (G12D, G12V, G13D, etc.) and wild-type selectivity remain active challenges. The target is robustly validated across multiple cancer indications.

### Evidence Gaps

- Approved drugs (sotorasib, adagrasib) are covalent and mutation-specific (G12C only); druggability of other common KRAS mutants (G12D, G12V, G12R, G13D) is less established clinically
- Median IC50 of ~1020 nM suggests many ChEMBL compounds have modest potency, indicating chemical optimization challenges beyond G12C
- Resistance mechanisms (e.g., secondary KRAS mutations, bypass signaling via RTKs, SHP2, SOS1) are not fully addressed by current approved agents
- Wild-type KRAS inhibition selectivity window is not well defined for non-covalent approaches
- Efficacy in KRAS-mutant pancreatic cancer remains poor despite target engagement, suggesting tumor microenvironment and combination strategy gaps
- Pan-KRAS or RAS(ON) inhibitor clinical data are still emerging and not yet reflected in approvals

### Reasoning Trace

Step 1 — Structural confidence: 556 PDB entries with the best resolution at 0.953Å (sub-angstrom, exceptional quality), all 20 top structures are ligand-bound, and AlphaFold pLDDT of 91.5 with 92.6% high-confidence fraction. This is unambiguously high structural confidence. The switch I/II pocket and covalent C12 pocket are well-characterized structurally.

Step 2 — Chemical confidence: 5,903 IC50 entries in ChEMBL and 2 approved drugs (sotorasib, adagrasib). This clearly meets the 'high' threshold (>1000 entries + approved drugs). However, the median IC50 of ~1020 nM is relatively modest, reflecting the historical difficulty of drugging RAS and the fact that many entries predate the covalent G12C breakthrough. The approved drugs are covalent, mutation-selective agents, which is an important nuance.

Step 3 — Literature confidence: 8,140 PubMed titles containing KRAS, with very recent 2026 publications across mechanistic, clinical, and translational domains. This far exceeds the 'high' threshold (>500 publications) and reflects decades of strong disease validation across NSCLC, CRC, PDAC, and other cancers.

Step 4 — Druggability score: Combining all three lines of evidence, KRAS scores 'high' overall. The existence of approved drugs is the strongest indicator. However, important caveats exist: (a) current approvals are limited to G12C (~13% of KRAS mutations), leaving the majority of KRAS-mutant patients without direct KRAS-targeted options; (b) resistance is a significant clinical problem; (c) the median IC50 suggests the broader chemical space is not highly potent. Despite these caveats, the target is clearly druggable as demonstrated by clinical success, and the field is actively expanding coverage to other mutants.

Step 5 — Evidence gaps: The main gaps are mutation-specific coverage beyond G12C, resistance mechanisms, combination strategies, and the emerging pan-KRAS/RAS(ON) inhibitor landscape which is not yet clinically validated. Wild-type selectivity is also an underexplored concern for non-covalent approaches.

---

## Structural Evidence

**PDB entries:** 556 (top 20 by resolution detailed below)
**Best resolution:** 0.953Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 20/20

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 9IAY | 0.953 | X-RAY DIFFRACTION | Yes |
| 9IAW | 0.997 | X-RAY DIFFRACTION | Yes |
| 12XE | 1.01 | X-RAY DIFFRACTION | Yes |
| 8ONV | 1.01 | X-RAY DIFFRACTION | Yes |
| 6P0Z | 1.011 | X-RAY DIFFRACTION | Yes |
| 9IB5 | 1.011 | X-RAY DIFFRACTION | Yes |
| 8AZZ | 1.02 | X-RAY DIFFRACTION | Yes |
| 8AZX | 1.04 | X-RAY DIFFRACTION | Yes |
| 8B00 | 1.04 | X-RAY DIFFRACTION | Yes |
| 8TVK | 1.04 | X-RAY DIFFRACTION | Yes |

### AlphaFold Confidence

**Mean pLDDT:** 91.5  
**High confidence fraction (pLDDT > 70):** 92.60%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-P01116-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL2189121
**Total IC50 entries:** 5,903
**Median IC50:** 1020.0 nM

### Approved Drugs

| Drug | Mechanism |
|---|---|
| SOTORASIB | GTPase KRas inhibitor |
| ADAGRASIB | GTPase KRas inhibitor |

---

## Literature Evidence

**PubMed title matches:** 8140 (20 most recent retrieved)

### Most Recent Publications

**[2026]** Difluoromethylornithine modulates mutant K-RAS signaling pathways in pancreatic cancer cells.  
*Amino Acids* — PMID: 42892656  
> Oncogenic mutations in the K-RAS small GTPase occur in more than 90% of human PDACs and cause dysregulation of multiple metabolic pathways, including polyamine metabolism. The goal of this study was to determine whether blocking polyamine synthesis with the irreversible inhibitor α-difluoromethylorn...

**[2026]** PINK1-mediated mitophagy supports lung cancer initiation and limits the efficacy of KRAS-targeted therapy.  
*Sci Adv* — PMID: 42886799  
> Mitophagy, the selective degradation of mitochondria by lysosomes, is a major mitochondrial quality-control pathway, yet its role in lung cancer initiation and therapeutic response remains poorly understood. We investigated PINK1-dependent mitophagy in human lung adenocarcinoma and directly monitore...

**[2026]** KRAS G12S Positive Non-Small Cell Lung Cancer Mimicking KRAS G12C Positivity on the AmoyDx PCR Panel: A Case Report.  
*Thorac Cancer* — PMID: 42885664  
> A false-positive KRAS G12C on a multi-PCR assay using the amplification refractory mutation system can potentially occur in cases harboring certain multi-nucleotide variants other than KRAS G12C. A 62-year-old man with a large left upper lobe tumor was diagnosed with lung adenocarcinoma. A multi-PCR...

**[2026]** Dynamic remodeling of the KRAS interactome by direct RAS inhibitors with distinct mechanism of action reveals convergent responses.  
*Oncogene* — PMID: 42881251  
> KRAS is mutated in 30% of all human cancers. Small molecule inhibitors targeting KRAS with distinct mechanisms-of-action and variable specificities have entered the clinic, but their full effect on the RAS signaling network remains unclear. Here, we described the impact of RAS inhibition on the KRAS...

**[2026]** Mutant KRAS favors a microbe that signals back.  
*Cell Host Microbe* — PMID: 42874557  
> Tumor genetics and the microbiome both shape colorectal cancer, but their reciprocal interplay remains poorly defined. In this issue of Cell Host & Microbe, Jiao et al. show that mutant KRAS favors Bacteroides acidifaciens, which signals back through a SusF-ARHGEF2 axis to reinforce RAS-MAPK signali...

**[2026]** Hitting KRAS G12D without the gut punch: Can immunotherapy make it last?  
*Cancer Cell* — PMID: 42863460  
> In this issue of Cancer Cell, Shi et al. report encouraging early-phase results combining HRS-4642, an allele-specific KRAS G12D inhibitor, with the PD-L1 inhibitor adebrelimab in previously treated metastatic pancreatic cancer. The intravenous combination was safe and well tolerated, notably sparin...

**[2026]** MVB Maturation Responsive to KRAS(G12D)/TP53(R175H) Co-mutations Fuels Extracellular Vesicle-hypersecretion Phenotype to Aggravate Lymphangiogenesis and Lymphatic Metastasis.  
*J Extracell Vesicles* — PMID: 42858298  
> KRAS

**[2026]** Advances in KRAS(G12D)-targeted therapy: from small-molecule inhibitors to PROTACs and molecular glues.  
*Bioorg Chem* — PMID: 42854602  
> KRAS gene mutations represent one of the most common drivers of human cancers, with particularly high prevalence in pancreatic, lung, and colorectal cancers. Among these, the KRAS

**[2026]** Hyper-mutational processes provide a head-start for weak cancer drivers: Explaining atypical KRAS variants.  
*PLoS Comput Biol* — PMID: 42853888  
> Hypermutant cancers frequently contain atypical driver gene variants, which may provide sub-optimal oncogenic advantages. The reason why weak cancer drivers prevail and are not outcompeted by stronger alternatives is unclear. Here, using mathematical modelling, we show that aberrant mutational proce...

**[2026]** Association between KRAS gene mutation and clinicopathological factors in patients with metastatic colorectal cancer.  
*Arq Bras Cir Dig* — PMID: 42848681  
> Colorectal cancer is a global health problem with high incidence and mortality rates, frequently diagnosed at metastatic stages. Mutations in the KRAS gene play a key role in colorectal cancer progression, significantly influencing treatment resistance and prognosis. This study investigated the asso...

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*