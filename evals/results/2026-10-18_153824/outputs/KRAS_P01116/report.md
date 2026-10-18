# Target Atlas Report — KRAS (P01116)

**Generated:** 2026-10-18T13:39:28.162536  
**Organism:** Homo sapiens  
**Run ID:** 53ad523a-cc30-4538-9c7b-cd9f66fd8405  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

KRAS is a well-validated, highly druggable oncology target with exceptional structural coverage (556 PDB entries, best resolution 0.953Å), two FDA-approved covalent inhibitors (sotorasib and adagrasib targeting G12C), and over 5,900 ChEMBL IC50 entries. Despite historical reputation as 'undruggable,' the field has clearly demonstrated tractability, though the median IC50 of ~1 µM reflects the ongoing challenge of achieving potent engagement across diverse KRAS mutants beyond G12C. Literature support is among the strongest of any cancer target with >8,000 publications and active 2026 research.

### Evidence Gaps

- Approved drugs (sotorasib, adagrasib) are specific to KRAS G12C mutation; druggability of other clinically relevant mutants (G12D, G12V, G12R, Q61H) remains less established with fewer approved agents
- Median IC50 of ~1020 nM across ChEMBL entries suggests many chemical series lack high potency, indicating the broader chemical space is not yet well optimised
- Resistance mechanisms (e.g., acquired G12C→G13D, bypass signalling via RTKs, SHP2 pathway) limit clinical durability and are not fully resolved
- Pan-KRAS inhibitors and KRAS wild-type selectivity windows are still under active investigation with no approved agents
- KRAS G12D and G12V inhibitor clinical data are still early-stage; no approved drugs for these predominant pancreatic and colorectal mutants
- Allele-specific vs. non-selective inhibitor strategies for combination regimens not yet fully clinically validated

### Reasoning Trace

Step 1 — Structural confidence: 556 PDB entries with 20/20 best-resolved structures having bound ligands and a best resolution of 0.953Å is exceptional. AlphaFold pLDDT of 91.5 with 92.6% high-confidence fraction further supports this. Structural confidence is unambiguously HIGH.

Step 2 — Chemical confidence: 5,903 IC50 entries in ChEMBL far exceeds the 1,000-entry threshold. Two approved drugs exist (sotorasib/AMG 510 and adagrasib/MRTX849), both covalent inhibitors targeting the G12C mutant. The median IC50 of 1,020 nM is notable — this reflects the historical difficulty in achieving potency across all KRAS variants and the inclusion of early-generation or non-covalent scaffolds in the dataset. However, the existence of approved drugs definitively places chemical confidence at HIGH.

Step 3 — Literature confidence: 8,140 PubMed titles containing 'KRAS' is extraordinary. Recent 2026 publications show active mechanistic, translational, and clinical research. Disease association (multiple solid tumours — NSCLC, CRC, PDAC) is extremely well validated. Literature confidence is HIGH.

Step 4 — Druggability score synthesis: All three confidence dimensions are HIGH. The target has approved drugs, outstanding structural data, rich chemical matter, and the broadest disease validation in oncology. Despite nuances around mutant selectivity, resistance, and the challenge of non-G12C variants, the overall druggability is clearly HIGH. There is no ambiguity here — the historical 'undruggable' label has been definitively overturned by clinical approvals.

Step 5 — Evidence gaps: The key gaps are not about basic druggability but about completeness: (a) G12C-specific approved drugs leave other major mutants (G12D, G12V prevalent in pancreatic and colorectal cancers) without approved therapies; (b) acquired resistance is clinically significant; (c) the median IC50 of ~1 µM across ChEMBL suggests many compounds are suboptimal; (d) combination strategies and patient selection biomarkers beyond G12C genotyping are still evolving. These gaps reduce confidence in the breadth of druggability but do not reduce the overall score given existing approvals.

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