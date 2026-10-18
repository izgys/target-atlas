# Target Atlas Report — KRAS (P01116)

**Generated:** 2026-10-18T14:26:17.894894  
**Organism:** Homo sapiens  
**Run ID:** 2db95867-32cb-4a17-bfcf-899b9f08a1e8  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

KRAS is one of the most extensively studied oncology targets with exceptional structural, chemical, and literature evidence. Two approved covalent inhibitors (sotorasib and adagrasib) targeting the G12C mutation validate the target clinically, and the deep chemical matter (>5900 IC50 entries) and 556 PDB structures reflect decades of intensive drug discovery efforts. Druggability is high for G12C-mutant KRAS specifically, with ongoing work expanding coverage to other oncogenic variants.

### Evidence Gaps

- Approved drugs (sotorasib, adagrasib) are selective for the G12C mutation only; druggability of other common mutants (G12D, G12V, G13D) and wild-type KRAS remains less established clinically, though tool compounds exist
- Median IC50 of ~1020 nM across all ChEMBL entries reflects historical difficulty in achieving potent non-covalent inhibition; potency profile for non-G12C inhibitors is generally weaker
- Resistance mechanisms (e.g., secondary mutations, bypass signalling via RTKs, RAS amplification) are well-documented and may limit durable clinical benefit, but are not captured in static druggability metrics
- Allele-specific or pan-RAS inhibitor strategies are still in early clinical/preclinical stages with no approved agents beyond G12C
- Combination strategies needed for most KRAS-driven tumours are not reflected in single-target druggability scores

### Reasoning Trace

Step 1 — Structural confidence: 556 PDB entries, best resolution 0.953 Å (sub-angstrom, exceptional), all 20 top structures are ligand-bound, AlphaFold pLDDT 91.5 with 92.6% high-confidence fraction. This is unambiguously high structural confidence. The shallow nucleotide-binding pocket of KRAS was historically considered 'undruggable', but the discovery of the Switch II pocket (S-IIP) in the G12C mutant enabled covalent inhibitor design, and structural data now comprehensively characterises multiple binding sites.

Step 2 — Chemical confidence: 5903 IC50 entries in ChEMBL, 2 approved drugs (sotorasib, adagrasib). This is clearly high chemical confidence. The median IC50 of ~1020 nM reflects the breadth of the dataset including early, less potent compounds and non-G12C efforts; approved covalent G12C inhibitors show sub-100 nM biochemical potency. The existence of approved drugs clinically validates the target.

Step 3 — Literature confidence: 8140 PubMed titles mentioning KRAS, with active 2026 publications spanning mechanisms of resistance, novel mutant targeting, combination strategies, and biology. KRAS mutations are found in ~25% of all human cancers (pancreatic ~90%, colorectal ~45%, NSCLC ~30%), making it one of the best-validated oncology targets. Literature confidence is unambiguously high.

Step 4 — Druggability nuances: The target was historically considered undruggable due to picomolar affinity for GTP/GDP and lack of obvious druggable pockets. The G12C covalent approach circumvented this. For other mutants, emerging non-covalent inhibitors (e.g., MRTX1133 for G12D) are in clinical trials. Wild-type KRAS inhibition remains challenging due to selectivity concerns. The overall druggability score is high, with the caveat that this is most firmly established for G12C-mutant KRAS.

Step 5 — Evidence gaps: The main gaps are (a) allele-specificity — approved drugs cover only G12C, (b) resistance emergence limits durability, (c) non-covalent pan-KRAS inhibition remains an unmet need, and (d) combination dependency for meaningful clinical benefit. None of these gaps reduce the druggability score from high, but they are important context for drug discovery strategy.

Conclusion: KRAS scores high across all three confidence dimensions and receives a high overall druggability score, with important caveats about mutation-specific applicability.

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