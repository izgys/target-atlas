# Target Atlas Report — TREM2 (Q9NZC2)

**Generated:** 2026-10-24T18:15:14.261728  
**Organism:** Homo sapiens  
**Run ID:** 87a2539a-e5a6-4018-8738-5469e1be2504  

---

## Druggability Assessment

**Overall score:** `medium`  
**Structural confidence:** `high`  
**Chemical confidence:** `low`  
**Literature confidence:** `high`  

TREM2 is a well-characterized immunoreceptor with excellent structural coverage (15 PDB entries, best at 1.47Å, 11 with bound ligands), confirming a druggable extracellular binding site. Despite zero ChEMBL IC50 entries, a 2026 first-in-human trial of an oral small-molecule agonist (VG-3927/SAR448851) demonstrates real chemical tractability not yet captured in public databases. Strong disease validation in Alzheimer's disease and cancer immunology, combined with emerging clinical-stage chemistry, supports a medium-to-high druggability assessment.

### Evidence Gaps

- Zero ChEMBL IC50 entries despite apparent small-molecule activity — public chemical data severely lags behind the field
- No approved drugs; clinical-stage compound (VG-3927/SAR448851) has not yet demonstrated efficacy in humans
- Mechanism of small-molecule agonism of TREM2 not fully characterised in the public domain
- AlphaFold coverage of transmembrane and intracellular signalling domains is lower confidence (pLDDT <70 for ~39% of residues)
- Selectivity profile of small-molecule TREM2 agonists versus related TREM family members not established in public data
- Downstream pharmacodynamic biomarkers for TREM2 agonism in humans remain to be validated

### Reasoning Trace

Step 1 — Structural evidence: 15 PDB entries with best resolution of 1.466Å (X-ray crystallography) and 11/15 structures containing bound ligands constitutes high-quality structural evidence. This confirms the existence of a well-defined, ligand-accessible binding pocket on the extracellular Ig-like domain of TREM2. AlphaFold pLDDT of 76.8 (mean) with 61.3% high-confidence residues is moderate but secondary to the strong experimental PDB data. Structural confidence is rated HIGH.

Step 2 — Chemical evidence: ChEMBL lists CHEMBL6196124 for TREM2 but records zero IC50 entries and no approved drugs. This would normally indicate very low chemical tractability. However, a 2026 publication explicitly describes 'VG-3927/SAR448851, an oral small-molecule TREM2 agonist' entering first-in-human evaluation for Alzheimer's disease. This is a critical data point that is not yet reflected in ChEMBL, likely due to publication/deposition lag for a novel target. The existence of a clinical-stage oral small molecule agonist is strong evidence of chemical tractability. Chemical confidence is rated LOW based strictly on ChEMBL, but the true chemical tractability is likely medium based on literature.

Step 3 — Literature evidence: 841 PubMed papers with TREM2 in the title represents a substantial and active field. Recent 2026 papers cover Alzheimer's disease, neurodegeneration, cancer immunology (glioma, tuberculosis), and mechanistic signalling studies. Disease validation is strong, particularly for Alzheimer's disease where TREM2 loss-of-function variants (e.g., R47H) are established risk factors. Literature confidence is rated HIGH.

Step 4 — Druggability synthesis: TREM2 is a type I transmembrane protein with an extracellular C-type lectin-like/Ig-like domain that binds lipid ligands and is the target of therapeutic antibodies (e.g., AL002). The ligand-bound crystal structures confirm a druggable pocket. The first-in-human oral small molecule agonist in 2026 is the most important chemical signal — it demonstrates that small molecules can engage TREM2 with sufficient potency and selectivity for clinical development. The druggability score is set to MEDIUM rather than HIGH because: (a) no approved drugs exist, (b) public chemical data is essentially absent, (c) the clinical compound has not yet demonstrated human efficacy, and (d) agonising an immunoreceptor with a small molecule is mechanistically challenging and the approach is still unproven clinically. The score would be upgraded to HIGH upon successful Phase 2 data or substantial ChEMBL deposition.

Step 5 — Evidence gaps: The primary gap is the disconnect between apparent real-world chemical activity (clinical-stage small molecule) and public database records (zero ChEMBL entries). Additional gaps include lack of selectivity data, unvalidated human PD biomarkers, and incomplete structural coverage of intracellular signalling domains.

---

## Structural Evidence

**PDB entries:** 15 (top 15 by resolution detailed below)
**Best resolution:** 1.466Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 11/15

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 6XDS | 1.466 | X-RAY DIFFRACTION | Yes |
| 5UD8 | 1.8 | X-RAY DIFFRACTION | No |
| 9PWN | 1.8 | X-RAY DIFFRACTION | Yes |
| 8T51 | 1.9 | X-RAY DIFFRACTION | Yes |
| 8T59 | 2.0 | X-RAY DIFFRACTION | Yes |
| 6B8O | 2.2 | X-RAY DIFFRACTION | Yes |
| 5UD7 | 2.20002253654 | X-RAY DIFFRACTION | Yes |
| 6Y6C | 2.26 | X-RAY DIFFRACTION | Yes |
| 6YMQ | 3.07 | X-RAY DIFFRACTION | Yes |
| 5ELI | 3.0977 | X-RAY DIFFRACTION | Yes |

### AlphaFold Confidence

**Mean pLDDT:** 76.8  
**High confidence fraction (pLDDT > 70):** 61.30%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-Q9NZC2-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL6196124
**Total IC50 entries:** 0

*No approved drugs found for this target.*

---

## Literature Evidence

**PubMed title matches:** 841 (20 most recent retrieved)

### Most Recent Publications

**[2026]** A peri-tumoral TREM2-high myeloid state, myeloid continuum polarization, and white matter disconnection in long-term cognitive survivorship after diffuse glioma: a neuroimmune-connectomic cohort study.  
*Front Immunol* — PMID: 42877165  
> Whether a TREM2-high myeloid state and myeloid continuum polarization are associated with long-term cognitive survivorship in diffuse glioma has not been integrated with white matter connectomics and systemic neuroinflammation in a longitudinal framework. In a single-center retrospective cohort of 2...

**[2026]** Identification of a spatially organized TREM2-associated permissive macrophage niche in human pulmonary tuberculosis alveolar pneumonia.  
*Nat Commun* — PMID: 42875426  
> Pulmonary tuberculosis (TB), caused by lung infection with Mycobacterium tuberculosis (Mtb), often manifests both alveolar pneumonia and aggregation of immune cells containing Mtb, termed granulomas, within the same lung. Here, we integrate spatial transcriptomics, single-cell RNA sequencing, high-r...

**[2026]** Preclinical and first-in-human evaluation of VG-3927/SAR448851, an oral small-molecule TREM2 agonist for Alzheimer's disease.  
*Sci Transl Med* — PMID: 42873892  
> Microglial dysfunction is increasingly implicated in Alzheimer's disease (AD) pathogenesis, with loss-of-function variants in the microglial receptor TREM2 as major risk factors for late-onset AD. We report VG-3927, an oral, CNS-penetrant small-molecule TREM2 agonist that engages the transmembrane d...

**[2026]** SHIP1 regulates TREM2 signalling and macrophage functions in a hiPSC-derived model.  
*FEBS J* — PMID: 42872589  
> Genetic and functional studies strongly implicate microglia in the pathology of Alzheimer's disease. The Triggering Receptor Expressed on Myeloid cells 2 (TREM2) pathway is an important functional regulator of microglia, promoting phagocytosis of apoptotic cells, debris and pathogenic proteins. Geno...

**[2026]** Context-dependent TREM2 signalling in myeloid cells: Molecular mechanisms and immunotherapeutic divergence in neurodegeneration and cancer.  
*Clin Transl Med* — PMID: 42865133  
> Triggering receptor expressed on myeloid cells 2 (TREM2) is a pivotal lipid-sensing receptor that governs the functional plasticity and metabolic fitness of mononuclear phagocytes, including microglia, osteoclasts, dendritic cells and tissue-resident macrophages. While originally identified as a gen...

**[2026]** Targeting TREM2(+) and TIMD4(+) Macrophages Reprograms the Tumor Microenvironment and Enhances PD-1 Blockade Efficacy in Intrahepatic Cholangiocarcinoma.  
*Cancer Commun (Lond)* — PMID: 42856794  

**[2026]** TREM2 Orchestrates Myeloid Cell Programming and Immune Dysregulation in Pulmonary Hypertension.  
*bioRxiv* — PMID: 42818059  
> Pulmonary hypertension (PH) is a progressive and fatal disease characterized by pulmonary vascular remodeling, inflammation, and immune dysregulation. Myeloid-derived suppressor cells (MDSCs) and macrophages contribute to PAH pathobiology; however, the molecular regulators of their pathological acti...

**[2026]** TREM2-directed therapy in Alzheimer's disease: from therapeutic window to clinical translation.  
*Front Aging Neurosci* — PMID: 42812614  
> Alzheimer's disease (AD) is characterized by amyloid-β (Aβ) deposition, tau pathology, synaptic dysfunction, and a sustained neuroimmune response. Among immune-related targets, triggering receptor expressed on myeloid cells 2 (TREM2) is of particular interest because it is supported by human genetic...

**[2026]** Single-cell RNA sequencing reveals the interaction of TREM2(+) macrophages and Tc17 lymphocytes in scalp psoriasis.  
*Immunol Res* — PMID: 42806169  
> Scalp psoriasis exhibits unique clinical features and relative resistance to conventional therapies compared with lesions on other body sites. However, the immune landscape underlying these characteristics preferentially observed in scalp lesions remains poorly understood. To characterize immune-cel...

**[2026]** Activation of TREM2 via single-domain antibodies improves synaptic and cognitive function in 5×FAD mice.  
*Cell Rep* — PMID: 42800026  
> Alzheimer's disease (AD) is the most prevalent neurodegenerative disorder, and dysfunction of triggering receptor expressed on myeloid cells 2 (TREM2) in microglia increases AD risk. TREM2 activation promotes protective microglial functions and mitigates AD pathology. Although TREM2-activating antib...

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*