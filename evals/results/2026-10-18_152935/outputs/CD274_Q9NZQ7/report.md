# Target Atlas Report — CD274 (Q9NZQ7)

**Generated:** 2026-10-18T13:34:57.931739  
**Organism:** Homo sapiens  
**Run ID:** 77205724-8b90-4695-b262-376ce92d3176  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

CD274 (PD-L1) is a highly druggable immune checkpoint target with exceptional structural, chemical, and clinical validation. Five approved antibody drugs exist, over 1700 IC50 entries are recorded in ChEMBL with a median of ~210 nM, and 20 high-resolution PDB structures (best 0.99 Å) including 13 ligand-bound complexes confirm a well-characterised binding interface. Active research continues across multiple cancer types, solidifying its status as a premier immuno-oncology target.

### Evidence Gaps

- Small-molecule inhibitors remain challenging due to the flat protein-protein interaction surface; most approved agents are monoclonal antibodies, leaving oral small-molecule druggability only partially established
- Resistance mechanisms to existing PD-L1 blockade are not fully elucidated, limiting next-generation drug design
- Biomarker strategies for patient stratification (e.g., which tumour types and PD-L1 expression thresholds predict response) remain an active and unresolved area
- Intracellular and non-canonical signalling roles of CD274 are not comprehensively characterised and may reveal additional druggable modalities
- Data on combination partner optimisation and sequencing with other checkpoint inhibitors is still evolving

### Reasoning Trace

Step 1 – Structural confidence: 20 PDB structures are available, with the best resolution at 0.99 Å (X-ray crystallography). 13 of 20 structures are ligand-bound, directly informing drug design. AlphaFold mean pLDDT of 88.2 with 84.4% of residues above 70 further supports a well-ordered protein. Structural confidence is unambiguously HIGH.

Step 2 – Chemical confidence: ChEMBL records 1,772 IC50 entries against CHEMBL3580522, well above the 1,000-entry threshold. Median IC50 of 210.5 nM indicates a reasonable potency landscape. Critically, 5 approved drugs exist (atezolizumab, durvalumab, avelumab, sugemalimab, cosibelimab), all targeting PD-L1. Chemical confidence is HIGH. Caveat: most chemical matter is biologic (antibody-based); small-molecule PD-L1 inhibitors exist in the literature but none are yet approved, reflecting the difficulty of disrupting the flat PD-1/PD-L1 interface with small molecules.

Step 3 – Literature confidence: 20 recent publications retrieved spanning 2025-2026, covering diverse cancer types (gastric, cervical, hepatocellular, melanoma) and mechanistic angles (ubiquitination, siRNA knockdown, macrophage polarisation, prognostic biomarker roles). The breadth and recency of publications, combined with decades of foundational immuno-oncology literature, place this well above the 500-publication threshold. Literature confidence is HIGH.

Step 4 – Overall druggability: CD274/PD-L1 is one of the most clinically validated immuno-oncology targets in existence. The combination of atomic-resolution structures with bound ligands, abundant and potent chemical matter, five approved drugs, and a continuous stream of disease-validation publications converges on a HIGH druggability score.

Step 5 – Evidence gaps: The primary gap is that all approved drugs are monoclonals; small-molecule druggability of the flat PD-1/PD-L1 interface is harder to achieve (though macrocyclic and BMS-series small molecules exist as clinical candidates). Resistance mechanisms, patient selection biomarkers, and potential non-canonical intracellular functions represent additional open questions but do not diminish the overall druggability assessment.

---

## Structural Evidence

**PDB structures retrieved:** 20
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

**Recent publications retrieved:** 20

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