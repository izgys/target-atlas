# Target Atlas Report — TREM2 (Q9NZC2)

**Generated:** 2026-10-24T18:23:06.942869  
**Organism:** Homo sapiens  
**Run ID:** f345ed1c-561b-40a4-87a6-ec3a772330d3  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `low`  
**Literature confidence:** `high`  

TREM2 is a well-validated immunoreceptor target with strong structural evidence (15 PDB entries up to 1.47Å resolution, 11 with bound ligands) and extensive literature support (841 publications, strong Alzheimer's and neuroinflammation disease links). Despite an empty ChEMBL record, a 2026 first-in-human oral small-molecule agonist (VG-3927/SAR448851) confirms chemical tractability, placing TREM2 as an emerging high-druggability target with a maturing small-molecule pipeline.

### Evidence Gaps

- ChEMBL contains zero IC50 entries for TREM2 despite active small-molecule programs — likely a data curation lag rather than true absence of chemical matter
- No approved drugs exist; the most advanced small molecule (VG-3927/SAR448851) is only at first-in-human stage
- Context-dependent biology (agonism beneficial in neurodegeneration but potentially detrimental in some cancers) complicates therapeutic strategy
- AlphaFold pLDDT is only moderate (76.8 mean, 61.3% high-confidence) suggesting some structurally disordered regions, particularly in transmembrane and intracellular domains
- Binding site selectivity and allosteric vs. orthosteric mechanisms for small-molecule agonists are not fully characterised in public data
- Quantitative SAR data (potency, selectivity series) is absent from public databases, limiting chemical confidence assessment

### Reasoning Trace

Step 1 — Structural: 15 PDB structures with best resolution of 1.466Å (X-ray) and 11/15 ligand-bound structures constitutes high structural confidence. The extracellular C-type lectin-like domain of TREM2 is well-crystallised and shows a defined binding pocket accessible to small molecules and antibodies. AlphaFold pLDDT of 76.8 is moderate but secondary to the rich experimental structural data. Structural confidence = HIGH.

Step 2 — Chemical: ChEMBL ID CHEMBL6196124 exists but reports 0 IC50 entries and no approved drugs. This would normally indicate low chemical confidence. However, a 2026 publication explicitly describes 'VG-3927/SAR448851, an oral small-molecule TREM2 agonist' entering first-in-human evaluation for Alzheimer's disease. This is strong real-world evidence of chemical tractability that has not yet propagated into ChEMBL. The discrepancy is attributed to data curation lag for very recent compounds. Chemical confidence = LOW (by ChEMBL metrics alone), but the pipeline evidence upgrades practical tractability assessment.

Step 3 — Literature: 841 PubMed titles exceed the high-confidence threshold of 500. Recent 2026 papers span neurodegeneration, cancer immunology, tuberculosis, and first-in-human clinical translation. Disease validation is strong and multi-indication. Literature confidence = HIGH.

Step 4 — Druggability synthesis: TREM2 has (a) a well-defined extracellular domain with multiple ligand-bound crystal structures, (b) demonstrated small-molecule agonist activity reaching clinical trials, (c) strong disease validation in Alzheimer's disease and neuroinflammation. The main caveats are: no approved drugs, context-dependent biology (agonism vs. antagonism depending on disease context), and absence of public quantitative SAR data. Balancing these factors — particularly the first-in-human small molecule — the overall druggability score is HIGH, acknowledging that clinical validation is still early-stage.

Step 5 — Gaps: The primary gap is the disconnect between real-world chemical programs and public database records. Additional gaps include lack of selectivity data, unclear optimal modality (small molecule agonist vs. antibody vs. bispecific), and the biological complexity of context-dependent TREM2 signalling across disease indications.

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