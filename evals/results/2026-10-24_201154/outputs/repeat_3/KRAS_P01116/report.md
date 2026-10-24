# Target Atlas Report — KRAS (P01116)

**Generated:** 2026-10-24T18:20:55.546419  
**Organism:** Homo sapiens  
**Run ID:** 7876036b-92d1-4ac4-8e66-0461c8392462  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

KRAS is one of the most extensively studied oncology targets, with exceptional structural coverage (556 PDB entries, best resolution 0.953Å), a large chemical dataset (5,903 IC50 entries), and two FDA-approved covalent inhibitors (sotorasib and adagrasib) targeting the G12C mutation. Druggability is high for the G12C mutant allele, though targeting other KRAS mutations (G12D, G12V, G12S, etc.) remains an active and partially unresolved challenge. Overall, KRAS represents a high-confidence, high-druggability target with strong disease validation across multiple cancers.

### Evidence Gaps

- Approved drugs (sotorasib, adagrasib) are mutation-specific (G12C only); druggability of other KRAS mutants (G12D, G12V, G12S, Q61H, etc.) is less established with no approved drugs
- Median IC50 of ~1020 nM suggests many chemical matter entries are of modest potency, indicating the broader chemical space beyond G12C inhibitors is still maturing
- Resistance mechanisms (e.g., secondary KRAS mutations, bypass signalling via RTKs, MAPK reactivation) are not fully characterised and limit durable clinical benefit
- Wild-type KRAS selectivity window: inhibitors must spare WT KRAS to avoid toxicity; therapeutic index data in normal tissues is incompletely defined
- Pan-KRAS or allele-agnostic inhibitor strategies (e.g., SOS1 inhibitors, KRAS-PPI disruptors) are in early clinical stages with limited efficacy data
- Combination therapy optimal partners and sequencing strategies remain under investigation

### Reasoning Trace

Step 1 — Structural confidence: 556 PDB entries with the best resolution at 0.953Å (sub-angstrom, exceptional quality) and all 20 top structures having ligands bound. AlphaFold pLDDT of 91.5 with 92.6% high-confidence fraction further supports a well-ordered protein. Structural confidence is unambiguously HIGH.

Step 2 — Chemical confidence: 5,903 IC50 entries in ChEMBL far exceeds the >1,000 threshold. Two approved drugs exist (sotorasib, adagrasib). Chemical confidence is HIGH. Caveat: median IC50 ~1020 nM indicates that while the dataset is large, a substantial portion of compounds are of moderate potency, reflecting the historical difficulty of drugging KRAS before covalent G12C strategies succeeded.

Step 3 — Literature confidence: 8,140 PubMed titles containing 'KRAS', with very recent 2026 publications covering mechanistic, clinical, and resistance topics. This is among the most published oncology targets. Disease validation is extremely strong across NSCLC, CRC, and PDAC. Literature confidence is HIGH.

Step 4 — Druggability assessment: KRAS was historically considered 'undruggable' due to the lack of deep hydrophobic pockets and picomolar affinity for GTP/GDP. The discovery of the Switch II pocket (S-IIP) and covalent trapping of G12C changed this paradigm. Two approved drugs validate the target clinically. However, druggability is mutation-context-dependent: G12C (~13% of KRAS mutations in NSCLC, ~3% in CRC) is well-drugged; G12D, G12V, and others are targets of active research but lack approved agents. Overall druggability score is HIGH, acknowledging this mutation-specificity caveat.

Step 5 — Evidence gaps: The main gaps are (a) mutation-specific coverage beyond G12C, (b) resistance mechanisms limiting durability, (c) therapeutic index for WT KRAS sparing, and (d) optimal combination strategies. These are important clinical/translational gaps but do not diminish the fundamental druggability classification given existing approvals and rich structural/chemical data.

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