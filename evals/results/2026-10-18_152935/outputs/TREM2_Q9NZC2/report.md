# Target Atlas Report — TREM2 (Q9NZC2)

**Generated:** 2026-10-18T13:36:18.185846  
**Organism:** Homo sapiens  
**Run ID:** 208c421f-234d-45e6-8382-7d3a2374223a  

---

## Druggability Assessment

**Overall score:** `medium`  
**Structural confidence:** `high`  
**Chemical confidence:** `none`  
**Literature confidence:** `high`  

TREM2 is a well-validated immunoreceptor target with strong structural characterisation (15 PDB structures, best resolution 1.47Å, 11 ligand-bound) and robust disease association in Alzheimer's disease, neurodegeneration, and cancer immunology. However, chemical tractability is currently low with zero IC50 entries in ChEMBL, though very recent (2026) preclinical and first-in-human data for an oral small-molecule agonist (VG-3927/SAR448851) suggests the target is actively being pursued and may soon acquire meaningful chemical data. Overall druggability is rated medium, reflecting strong structural and biological validation offset by a near-absent public small-molecule dataset.

### Evidence Gaps

- No IC50 or bioactivity entries in ChEMBL for this target despite emerging small-molecule agonist programmes — public chemical data is essentially absent
- No approved drugs; clinical-stage molecules are very early (first-in-human 2026)
- Mechanism of TREM2 agonism via small molecules is not yet well characterised in the public domain — binding sites and SAR are largely proprietary
- AlphaFold pLDDT is moderate (76.8 mean, 61% >70) suggesting some structural regions, potentially the transmembrane/intracellular region, lack high confidence — may limit full-length druggability modelling
- Context-dependency of TREM2 signalling (neurodegeneration vs. cancer, agonism vs. antagonism) means the therapeutic modality is not yet settled — different disease indications may require opposing pharmacologies
- No published clinical efficacy or safety data yet for any TREM2-directed small molecule

### Reasoning Trace

Step 1 — Structural confidence: TREM2 has 15 PDB structures with the best at 1.47Å by X-ray diffraction, and 11 of 15 are ligand-bound. This is a strong structural dataset. The AlphaFold mean pLDDT of 76.8 with 61% of residues above 70 is moderate overall but likely reflects lower confidence in transmembrane/intracellular regions rather than the extracellular Ig-like domain, which is well-resolved by crystallography. Structural confidence is rated HIGH.

Step 2 — Chemical confidence: ChEMBL reports zero IC50 entries for CHEMBL6196124 and no approved drugs. This means there is essentially no public quantitative bioactivity data. However, a 2026 publication describes a first-in-human trial of VG-3927/SAR448851, an oral small-molecule TREM2 agonist, indicating active drug discovery programmes exist but data remain proprietary. Chemical confidence is rated NONE based on available public data, though this likely understates true industry activity.

Step 3 — Literature confidence: 20 recent publications were retrieved with 2026 dates, covering Alzheimer's disease, glioma, tuberculosis, and cancer immunology. The presence of a first-in-human small-molecule agonist paper and a mechanistic review of context-dependent TREM2 signalling signals a mature and active field. TREM2 loss-of-function variants (e.g., R47H) are established Alzheimer's disease risk factors in human genetics, providing strong disease validation. Literature confidence is rated HIGH.

Step 4 — Druggability assessment: TREM2 is a type I transmembrane protein with a well-structured extracellular Ig-like domain that binds diverse lipid ligands and has been successfully crystallised with bound molecules. The ligand-bound crystal structures confirm a tractable binding site. The challenge is that TREM2 is an activating immunoreceptor where agonism (not inhibition) is the desired mechanism for neurodegeneration, which is a harder pharmacological problem than classical enzyme inhibition. The complete absence of public ChEMBL data means no chemical series can be independently evaluated. However, the first-in-human small molecule agonist in 2026 demonstrates proof-of-concept feasibility. Balancing strong structural and disease validation against absent public chemical data and an unconventional agonist mechanism, druggability is scored MEDIUM.

Step 5 — Evidence gaps: Key gaps are the absence of public SAR/IC50 data, uncertainty around which binding site(s) confer agonism, the unsettled therapeutic modality (agonist for neurodegeneration vs. potential antagonist for some cancers), and no clinical efficacy readouts yet.

---

## Structural Evidence

**PDB structures retrieved:** 15
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

**Recent publications retrieved:** 20

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