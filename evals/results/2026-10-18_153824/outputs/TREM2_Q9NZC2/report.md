# Target Atlas Report — TREM2 (Q9NZC2)

**Generated:** 2026-10-18T13:41:34.049832  
**Organism:** Homo sapiens  
**Run ID:** c7a915a4-3ea5-402e-ba99-520fe883c931  

---

## Druggability Assessment

**Overall score:** `medium`  
**Structural confidence:** `high`  
**Chemical confidence:** `none`  
**Literature confidence:** `high`  

TREM2 is a well-characterised immunoreceptor expressed on microglia and myeloid cells with strong disease validation in Alzheimer's disease, neurodegeneration, and cancer. It has excellent structural coverage (15 PDB entries, best resolution 1.47Å, 11 ligand-bound structures) and a robust and growing literature base (841 publications), but currently lacks ChEMBL IC50 data and approved drugs, with a first-in-human oral small-molecule agonist (VG-3927/SAR448851) only just entering clinical evaluation in 2026. Druggability is assessed as medium-high: the structural tractability is clearly established but chemical maturity remains early-stage.

### Evidence Gaps

- No ChEMBL IC50 entries for this target — chemical activity data is absent from the standard cheminformatics database
- No approved drugs targeting TREM2 exist; the most advanced small molecule (VG-3927/SAR448851) is only at first-in-human stage (2026)
- TREM2 is primarily a receptor/signalling adaptor — canonical small-molecule binding pockets may be limited; most therapeutic approaches have historically focused on antibodies or biologics
- The agonist vs antagonist therapeutic rationale differs by disease context (neurodegeneration vs cancer), creating target-validation complexity
- AlphaFold mean pLDDT of 76.8 with only 61% high-confidence residues suggests the full-length protein (including transmembrane and intracellular regions) has structural uncertainty beyond the well-resolved ectodomain
- Selectivity risk: TREM2 shares structural homology with other TREM family members (e.g., TREM1); selectivity data for small molecules is lacking
- Cellular target engagement and pharmacodynamic biomarkers for small-molecule TREM2 agonism are not yet established in the literature

### Reasoning Trace

Step 1 — Structural confidence: 15 PDB entries with a best resolution of 1.47Å (X-ray crystallography) and 11/15 structures with bound ligands provides an excellent structural foundation. This is clearly high structural confidence. The AlphaFold pLDDT of 76.8 (61% high-confidence residues) is moderate, consistent with a protein that has a well-ordered ectodomain but disordered transmembrane/cytoplasmic regions — this is expected for a type I transmembrane receptor and does not undermine the high PDB-based structural confidence for the ectodomain.

Step 2 — Chemical confidence: The ChEMBL target ID exists but has 0 IC50 entries, and there are no approved drugs. This is formally 'none' by definition. However, the 2026 literature explicitly mentions a first-in-human oral small-molecule agonist (VG-3927/SAR448851), indicating that small-molecule tractability has been demonstrated at a preclinical level — this is simply not yet captured in ChEMBL. I must report chemical confidence as 'none' per schema definitions, but note this is a rapidly evolving situation.

Step 3 — Literature confidence: 841 PubMed papers with TREM2 in the title is well above the 500-paper threshold, recent publications span 2026, and the disease associations (Alzheimer's disease, neurodegeneration, tuberculosis, glioma/cancer) are strongly validated at multiple levels. Literature confidence is high.

Step 4 — Druggability assessment: TREM2 is a C-type lectin-like receptor with an immunoglobulin-like ectodomain. The 11 ligand-bound crystal structures confirm the existence of a druggable binding site. The target is biologically well-validated, especially in neurodegeneration. The key limitation is that the chemical space is nascent — no IC50 data in ChEMBL and no approved drugs — meaning the medicinal chemistry has not yet matured to the point where potency, selectivity, and ADMET profiles are publicly established at scale. The therapeutic modality question is also unresolved: antibody-based agonists (e.g., AL002c) are further advanced clinically than small molecules. Small-molecule agonism of a receptor is inherently more challenging than inhibition. Given strong structural and biological validation but early-stage chemical maturity, 'medium' druggability is the most calibrated assessment — it is more tractable than a truly undrugged target but has not yet reached the confidence level of 'high'.

Step 5 — Evidence gaps: The absence of ChEMBL data is a significant gap for cheminformatics-based druggability assessment. The context-dependent biology (pro-microglial in neurodegeneration vs potentially tumour-promoting in some cancers) adds therapeutic complexity. Selectivity within the TREM family is unstudied publicly for small molecules. The structural data covers primarily the ectodomain; intracellular signalling domain structure is less resolved.

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