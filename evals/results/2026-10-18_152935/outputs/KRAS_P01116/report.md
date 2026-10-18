# Target Atlas Report — KRAS (P01116)

**Generated:** 2026-10-18T13:31:55.485285  
**Organism:** Homo sapiens  
**Run ID:** bb9ef804-fa27-4c5b-bbcb-00709b56e090  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

KRAS is a well-validated oncology target with exceptional structural characterization (sub-1Å resolution, 20 ligand-bound PDB structures), a large chemical dataset (>5900 ChEMBL IC50 entries), and two FDA-approved covalent inhibitors (sotorasib and adagrasib) targeting the G12C mutation. Druggability is high for KRAS G12C specifically, though broader targeting of other oncogenic KRAS mutations (G12D, G12V, G13D, etc.) remains an active area of research with fewer approved agents. The target is among the most extensively studied in cancer biology with strong disease validation across multiple tumor types.

### Evidence Gaps

- Approved drugs (sotorasib, adagrasib) are mutation-specific (G12C only); druggability of other common KRAS mutants (G12D, G12V, G13D) is less established with no approved drugs
- Median IC50 of ~1020 nM suggests many chemical matter entries are only moderately potent, indicating the full mutant landscape remains challenging
- Resistance mechanisms (e.g., secondary KRAS mutations, bypass signaling via PINK1/mitophagy as noted in recent literature) are not fully addressed by current approved agents
- No information provided on PK/ADME profiles of the broader chemical series beyond approved drugs
- Wild-type KRAS selectivity windows for non-G12C inhibitors are not characterized in the provided data
- Combination therapy strategies and biomarker-driven patient selection beyond G12C mutation status are incompletely defined

### Reasoning Trace

Step 1 - Structural confidence: KRAS has 20 PDB structures retrieved, all ligand-bound, with a best resolution of 0.953Å — this is an exceptionally high-quality crystallographic dataset. AlphaFold mean pLDDT of 91.5 with 92.6% of residues above 70 further supports a well-ordered protein. Structural confidence is unambiguously HIGH.

Step 2 - Chemical confidence: ChEMBL reports 5903 IC50 entries, which is a large dataset. Two approved drugs exist (sotorasib, adagrasib), both covalent inhibitors of KRAS G12C. The median IC50 of ~1020 nM is moderate, reflecting that while the G12C allele has been successfully drugged, the broader KRAS mutant landscape has historically been difficult. Chemical confidence is HIGH given the volume of data and approved drugs.

Step 3 - Literature confidence: 20 recent publications were retrieved, all from 2026, covering diverse aspects including specific mutation mimicry, resistance mechanisms (PINK1/mitophagy), signaling remodeling by RAS inhibitors, and microbiome interactions. KRAS is one of the most published cancer targets globally, with strong disease validation across NSCLC, pancreatic cancer, colorectal cancer, and others. Literature confidence is HIGH.

Step 4 - Druggability assessment: KRAS was historically considered 'undruggable' due to the lack of obvious deep binding pockets and its high GTP affinity. However, the discovery of the Switch II pocket (S-IIP) enabled covalent targeting of G12C, leading to two approved drugs. The sub-angstrom crystal structures confirm druggable binding sites. The large number of ligand-bound structures further validates multiple chemotypes engaging the protein. Druggability is HIGH, with the caveat that this is most firmly established for the G12C mutant.

Step 5 - Evidence gaps: The main gaps are: (1) mutation-specific druggability — approved agents only cover G12C, which represents ~13% of KRAS mutations in NSCLC and ~1-2% in pancreatic cancer; other mutations (G12D, G12V) are under active investigation but lack approved drugs; (2) resistance mechanisms are emerging as a clinical challenge; (3) the moderate median IC50 suggests the chemical series as a whole is not uniformly potent; (4) combination strategies and patient selection beyond G12C are not fully defined.

Conclusion: KRAS scores HIGH on all confidence dimensions. The druggability score is HIGH, anchored by approved drugs, exceptional structural data, and massive chemical and literature support, with the nuance that broader mutant coverage remains an ongoing scientific challenge.

---

## Structural Evidence

**PDB structures retrieved:** 20
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

**Recent publications retrieved:** 20

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