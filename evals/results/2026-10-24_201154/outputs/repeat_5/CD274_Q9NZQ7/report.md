# Target Atlas Report — CD274 (Q9NZQ7)

**Generated:** 2026-10-24T18:30:04.572663  
**Organism:** Homo sapiens  
**Run ID:** b939942e-d927-420d-b213-b66cc0e3ae35  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

CD274 (PD-L1) is a highly validated immuno-oncology target with exceptional structural, chemical, and clinical evidence. Five approved antibody drugs exist, over 1,700 ChEMBL IC50 entries are recorded, and 80 PDB structures including sub-angstrom resolution co-crystal structures confirm a well-characterised binding interface. Druggability is high, though the dominant modality remains biologics; small-molecule inhibitors of the PD-1/PD-L1 interaction are an active but more challenging area.

### Evidence Gaps

- Small-molecule druggability of the PD-1/PD-L1 protein-protein interface remains challenging; approved drugs are all monoclonal antibodies, and no small-molecule has yet reached approval
- Median IC50 of ~210 nM in ChEMBL likely reflects a mix of antibody and small-molecule data; potency distribution for small molecules specifically is not disaggregated here
- Resistance mechanisms (e.g., CD274 amplification, alternative checkpoint upregulation) are not fully characterised and may limit therapeutic durability
- Tissue- and tumour-specific expression patterns and their impact on patient selection are still being refined
- Combination therapy optimal partners and sequencing strategies remain an open clinical question

### Reasoning Trace

Step 1 — Structural confidence: 80 PDB entries with the best resolution at 0.99 Å (X-ray diffraction) is exceptional. 13 of the top 20 structures have ligands bound, confirming a tractable binding site has been crystallographically characterised with bound partners. AlphaFold mean pLDDT of 88.2 and 84.4% of residues above pLDDT 70 further support a well-ordered protein. Structural confidence is unambiguously HIGH.

Step 2 — Chemical confidence: ChEMBL lists 1,772 IC50 entries with a median of ~210 nM, and five approved drugs (atezolizumab, durvalumab, avelumab, sugemalimab, cosibelimab) all targeting PD-L1. This exceeds the >1,000 entry and approved drug thresholds for HIGH chemical confidence. Caveat: all approved agents are monoclonal antibodies; small-molecule inhibitors of the PD-1/PD-L1 PPI are in development but none approved, reflecting the inherent difficulty of disrupting a flat, hydrophobic protein-protein interface with small molecules. Nevertheless, chemical confidence overall is HIGH.

Step 3 — Literature confidence: 105 PubMed papers with CD274 in the title is a lower-bound estimate (the gene is more commonly searched as PD-L1), and the broader PD-L1/PD-1 checkpoint literature numbers in the tens of thousands. Recent 2025-2026 publications cover mechanistic biology (ubiquitination, OTUB2, siRNA knockdown), biomarker/prognostic studies, and clinical correlates across multiple tumour types. Disease validation is extremely strong across many solid tumours and haematological malignancies. Literature confidence is HIGH.

Step 4 — Druggability score: All three pillars (structural, chemical, literature) are HIGH. The target is clinically validated with multiple approved drugs. The main nuance is that the approved modality is biologics (mAbs), and small-molecule druggability of the PD-1/PD-L1 interface is harder but actively pursued. Overall druggability score is HIGH.

Step 5 — Evidence gaps: The primary gaps are (a) lack of approved small molecules, meaning the PPI interface may be less tractable for small-molecule drug discovery; (b) the ChEMBL IC50 dataset likely mixes antibody and small-molecule assay formats, making potency interpretation for small molecules alone uncertain; (c) resistance mechanisms and combination strategies are incompletely understood; (d) patient selection biomarkers beyond PD-L1 IHC expression are still evolving.

---

## Structural Evidence

**PDB entries:** 80 (top 20 by resolution detailed below)
**Best resolution:** 0.99Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 13/20

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 5O45 | 0.99 | X-RAY DIFFRACTION | No |
| 8ALX | 1.1 | X-RAY DIFFRACTION | Yes |
| 6NP9 | 1.27 | X-RAY DIFFRACTION | Yes |
| 9I0U | 1.46 | X-RAY DIFFRACTION | Yes |
| 6YCR | 1.54 | X-RAY DIFFRACTION | No |
| 8AOK | 1.6 | X-RAY DIFFRACTION | Yes |
| 13DT | 1.64 | X-RAY DIFFRACTION | Yes |
| 7CZD | 1.64 | X-RAY DIFFRACTION | Yes |
| 5JDS | 1.7 | X-RAY DIFFRACTION | Yes |
| 5N2F | 1.7 | X-RAY DIFFRACTION | Yes |

### AlphaFold Confidence

**Mean pLDDT:** 88.2  
**High confidence fraction (pLDDT > 70):** 84.40%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-Q9NZQ7-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL3580522
**Total IC50 entries:** 1,772
**Median IC50:** 210.5 nM

### Approved Drugs

| Drug | Mechanism |
|---|---|
| ATEZOLIZUMAB | Programmed cell death 1 ligand 1 inhibitor |
| DURVALUMAB | Programmed cell death 1 ligand 1 inhibitor |
| AVELUMAB | Programmed cell death 1 ligand 1 other |
| SUGEMALIMAB | Programmed cell death 1 ligand 1 binding agent |
| COSIBELIMAB | Programmed cell death 1 ligand 1 inhibitor |

---

## Literature Evidence

**PubMed title matches:** 105 (20 most recent retrieved)

### Most Recent Publications

**[2026]** Effect of siRNA-mediated knockdown of the PD-L1 (CD274) gene on DUSP gene family expression and potential clinical implications in gastric cancer.  
*Med Oncol* — PMID: 42848101  
> This study aimed to investigate the molecular interaction between PD-L1 (CD274) and members of the dual-specificity phosphatase (DUSP) gene family (DUSP1, DUSP2, DUSP4, DUSP6, and DUSP10) in gastric adenocarcinoma (GC) using integrated bioinformatic and experimental approaches. Bioinformatic analyse...

**[2026]** The ubiquitination of CD274 at MERCs enhances the anti-tumor immunity of cervical cancer.  
*Autophagy* — PMID: 42494073  
> Mitochondria-ER contact sites (MERCs) are crucial signaling hubs, but their role in anti-tumor immunity is unclear. This study revealed that the mitophagy regulator PRKN ubiquitinated CD274 at MERCs in human cervical cancer cells, a key mechanism for anti-tumor immunity. CD274 expression inversely c...

**[2026]** Bioinformatics mining and clinical validation of CD274 as a prognostic indicator in hepatocellular carcinoma.  
*BMC Cancer* — PMID: 42298533  
> Hepatocellular carcinoma (HCC) is a malignant tumour with high global incidence and mortality, featuring limited therapeutic options and poor prognosis, which necessitates novel prognostic biomarkers. The immune checkpoint molecule CD274 (Programmed Death-Ligand 1, PD-L1) correlates with poor progno...

**[2026]** OTUB2 induces M2 tumor-associated macrophage polarization and increases CD274 expression in gastric cancer cells to aggravate the progression of gastric cancer.  
*Cell Death Dis* — PMID: 41986305  
> Gastric cancer (GC) is often diagnosed at an advanced stage due to the absence of early symptoms and low screening rates, resulting in poor prognosis. The progression of GC is closely related to the immune response within the tumor microenvironment (TME). Tumor-associated macrophages (TAMs), particu...

**[2025]** CD274 Alterations and PD-L1 Expression on Tumor Cells and Tumor-Infiltrating Lymphocytes in Patients With Melanoma: Relationships to Histopathologic Features and Outcomes.  
*Arch Pathol Lab Med* — PMID: 41662873  
> In patients with melanoma, the predictive and prognostic relevance of programmed death ligand 1 (PD-L1) protein expression on tumor cells and tumor-infiltrating lymphocytes (TILs) and of alterations in the gene encoding PD-L1, CD274, are not yet established. To address these gaps in knowledge. We re...

**[2026]** Regorafenib enhances anti-PDCD1/PD-1 therapeutic efficacy in colorectal cancer by promoting SQSTM1/p62-mediated CD274/PD-L1 degradation.  
*Autophagy* — PMID: 41655134  
> Despite the clinical success of PDCD1/PD-1 and CD274/PD-L1 immune checkpoint blockade in multiple cancers, its efficacy in colorectal cancer (CRC) remains limited. Here, we report that the combination of the tyrosine kinase inhibitor regorafenib with PDCD1 blockade enhances anti-tumor immunity in CR...

**[2026]** Integrative transcriptomic and structural modeling reveal CASP1, TLR3, PYCARD, and CD274 as immune-modulatory drivers in breast cancer.  
*Naunyn Schmiedebergs Arch Pharmacol* — PMID: 41549178  
> Breast cancer (BRCA) remains one of the most prevalent malignancies worldwide, characterized by marked molecular heterogeneity and diverse clinical outcomes. Necroptosis and ferroptosis, two regulated forms of programmed cell death (PCD), play pivotal roles in tumor progression and immune regulation...

**[2026]** Fusobacterium nucleatum Enhances Immune Escape in Colorectal Cancer by Inducing H3K18 Lactylation of CD274 (PD-L1) Protein Through Lactate Accumulation.  
*APMIS* — PMID: 41494987  
> Fusobacterium nucleatum (Fn), an intratumoral pathogenic bacterium, is confirmed to be associated with tumor progression in colorectal cancer (CRC). To evaluate CD8

**[2025]** Epigenetic activation of CD274/PD-L1 by the MSL complex expands its role beyond dosage compensation.  
*Front Immunol* — PMID: 41409271  
> The regulation of CD274 (PD-L1), a pivotal immune checkpoint in cancer immunotherapy, remain incompletely understood. The male-specific lethal (MSL) complex, initially identified in  Using TIMER and GEPIA2, we charted pan-cancer expression of MSL subunits and their correlation with immune infiltrati...

**[2025]** Structural insights into the impacts of non-synonymous single nucleotide polymorphisms in CD274 gene on the PD-1/PD-L1 interaction: An in silico approach.  
*Biochem Biophys Res Commun* — PMID: 40983009  
> Programmed cell death ligand 1 (PD-L1) on tumor cells interacts with PD-1 of activated T cells causing immune evasion. Polymorphisms in CD274 gene encoding PD-L1 have been associated with several cancer types. In this study, various bioinformatics tools were employed to identify the most deleterious...

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*