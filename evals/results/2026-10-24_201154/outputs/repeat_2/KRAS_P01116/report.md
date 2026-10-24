# Target Atlas Report — KRAS (P01116)

**Generated:** 2026-10-24T18:17:01.315033  
**Organism:** Homo sapiens  
**Run ID:** c13600d3-308e-4980-b1ce-e2930fa5c38d  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

KRAS is one of the most extensively studied oncology targets, with 556 high-resolution PDB structures (best 0.953Å), over 5,900 ChEMBL IC50 entries, and two FDA-approved covalent inhibitors (sotorasib and adagrasib) targeting the G12C mutation. Druggability is high for the G12C mutant allele specifically, though targeting other KRAS mutations (G12D, G12V, G13D, etc.) remains an active and partially unresolved challenge. The overall evidence base is exceptionally strong across structural, chemical, and literature dimensions.

### Evidence Gaps

- Approved drugs (sotorasib, adagrasib) are covalent and mutation-specific (G12C only); druggability of other common KRAS mutations (G12D, G12V, G12R, G13D, Q61H) is less established with no approved drugs yet
- Median IC50 of ~1020 nM across ChEMBL entries suggests many compounds have modest potency, and the chemical space for non-covalent pan-KRAS inhibitors is still maturing
- Resistance mechanisms to G12C inhibitors (e.g., secondary KRAS mutations, bypass signalling via RTKs, MAPK reactivation) are not fully solved and limit clinical durability
- Wild-type KRAS selectivity window: therapeutic index for tumour vs. normal tissue is not fully characterised for newer non-covalent approaches
- Combination strategies needed for most KRAS-driven cancers (e.g., pancreatic) are still under investigation and optimal partners are unknown
- Allosteric vs. active-site inhibitor profiles for non-G12C mutants lack clinical validation

### Reasoning Trace

Step 1 — Structural confidence: 556 PDB entries with the best resolution at 0.953Å (sub-angstrom, exceptional quality), all 20 top structures have ligands bound, and AlphaFold pLDDT of 91.5 with 92.6% high-confidence fraction. This is unambiguously 'high' structural confidence. The protein is well-characterised in multiple conformational states (GDP-bound, GTP-bound, switch I/II open/closed, covalent adducts with G12C inhibitors).

Step 2 — Chemical confidence: 5,903 IC50 entries in ChEMBL is a large dataset. Two approved drugs exist (sotorasib, adagrasib), both covalent G12C-selective inhibitors. Median IC50 of ~1020 nM is moderate, reflecting the historical difficulty of targeting KRAS and the fact that many entries predate the covalent G12C breakthrough. The existence of approved drugs firmly places this in 'high' chemical confidence.

Step 3 — Literature confidence: 8,140 PubMed titles containing KRAS, with very recent 2026 publications spanning mechanistic biology, resistance, and clinical oncology. This is among the most-published oncology targets. Disease validation is extremely strong — KRAS is mutated in ~25% of all human cancers (>90% pancreatic, ~40% colorectal, ~30% lung adenocarcinoma). Literature confidence is unambiguously 'high'.

Step 4 — Druggability nuance: KRAS was historically considered 'undruggable' due to the shallow nucleotide-binding pocket and picomolar affinity for GTP. The covalent G12C strategy (exploiting the unique cysteine) broke this barrier. However, the approved drugs only cover G12C (~13% of KRAS mutations). Other mutations (G12D, G12V, G12R, G13D) are being pursued with non-covalent inhibitors (e.g., MRTX1133 for G12D in trials), but none are approved yet. The overall druggability score is 'high' given the proof-of-concept with approved drugs, but with the caveat that full pan-KRAS druggability is still being established.

Step 5 — Evidence gaps: The main gaps are (a) mutation-specific coverage beyond G12C, (b) resistance mechanisms limiting durability, (c) combination strategies for harder-to-treat KRAS-driven cancers like PDAC, and (d) the therapeutic index for non-covalent approaches.

Conclusion: KRAS scores 'high' across all three confidence dimensions and overall druggability, with important caveats around mutation specificity and resistance that are well-documented in the literature.

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