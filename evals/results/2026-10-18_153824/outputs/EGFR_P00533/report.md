# Target Atlas Report — EGFR (P00533)

**Generated:** 2026-10-18T13:38:25.055830  
**Organism:** Homo sapiens  
**Run ID:** a628bdc3-57ae-43ea-8333-c92b4be01def  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

EGFR (P00533) is one of the most well-validated and extensively drugged targets in oncology, with 393 PDB structures (best resolution 1.07Å), 26,600 ChEMBL IC50 entries, and 20 approved drugs including small molecules and biologics. The target has outstanding structural, chemical, and literature support, making it a benchmark for high druggability. Ongoing research continues to address resistance mechanisms and novel indications such as glioblastoma.

### Evidence Gaps

- Median IC50 of 2000 nM suggests a large fraction of screened compounds have modest potency, indicating selectivity and potency optimization remain non-trivial for new chemical series
- AlphaFold mean pLDDT of 75.9 with only 70.7% high-confidence residues suggests disordered regions (e.g., extracellular domain, flexible loops) are not fully captured structurally, though kinase domain is well resolved by X-ray
- Resistance mutations (e.g., T790M, C797S, exon 20 insertions) limit the utility of existing drugs and create ongoing druggability challenges for next-generation inhibitors
- CNS penetrance of current approved drugs is limited, which is relevant for indications like glioblastoma highlighted in recent literature
- Tissue-specific and mutation-specific efficacy profiles are not fully captured by aggregate ChEMBL or PDB data

### Reasoning Trace

Step 1 - Structural Confidence: EGFR has 393 PDB entries with the best resolution at 1.07Å (X-ray diffraction), and 19 of the top 20 structures are ligand-bound. This is exceptional structural coverage. The AlphaFold mean pLDDT of 75.9 and 70.7% high-confidence fraction are moderate, but this is largely irrelevant given the wealth of experimental structures. The kinase domain is extremely well characterized crystallographically. Structural confidence = HIGH.

Step 2 - Chemical Confidence: ChEMBL target CHEMBL203 has 26,600 IC50 entries and 20 approved drugs spanning multiple mechanisms (covalent and non-covalent small molecule kinase inhibitors, monoclonal antibodies, antibody-drug conjugates). This is among the most chemically characterized targets in existence. The median IC50 of 2000 nM reflects the breadth of screening data including many weak/non-selective compounds, not the quality of the best compounds. Chemical confidence = HIGH.

Step 3 - Literature Confidence: 18,783 PubMed papers with EGFR in the title is extraordinary. Recent publications (2026) continue to appear across multiple cancer types including glioma, lung cancer, and metabolic disease contexts. Disease validation is extremely strong across multiple tumor types. Literature confidence = HIGH.

Step 4 - Evidence Gaps: Despite the overwhelming evidence, some nuance is warranted. The high median IC50 across ChEMBL entries indicates that novel scaffolds still face potency/selectivity challenges. Resistance is a major clinical problem. Structural coverage of disordered regions (extracellular domain, juxtamembrane region) is less complete, which may matter for allosteric drug design. CNS penetrance is a gap for glioblastoma applications.

Step 5 - Overall Druggability: EGFR is the canonical druggable target. All three evidence pillars (structural, chemical, literature) are at the highest possible level. Druggability score = HIGH.

---

## Structural Evidence

**PDB entries:** 393 (top 20 by resolution detailed below)
**Best resolution:** 1.07Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 19/20

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 8A27 | 1.07 | X-RAY DIFFRACTION | Yes |
| 8A2D | 1.11 | X-RAY DIFFRACTION | Yes |
| 5UG9 | 1.33 | X-RAY DIFFRACTION | Yes |
| 5HG8 | 1.42 | X-RAY DIFFRACTION | Yes |
| 8A2A | 1.43 | X-RAY DIFFRACTION | Yes |
| 5UG8 | 1.46 | X-RAY DIFFRACTION | Yes |
| 3POZ | 1.5 | X-RAY DIFFRACTION | Yes |
| 6TFV | 1.5 | X-RAY DIFFRACTION | Yes |
| 6TG0 | 1.5 | X-RAY DIFFRACTION | Yes |
| 3VRP | 1.52 | X-RAY DIFFRACTION | Yes |

### AlphaFold Confidence

**Mean pLDDT:** 75.9  
**High confidence fraction (pLDDT > 70):** 70.70%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-P00533-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL203
**Total IC50 entries:** 26,600
**Median IC50:** 2000.0 nM

### Approved Drugs

| Drug | Mechanism |
|---|---|
| PANITUMUMAB | Epidermal growth factor receptor erbB1 inhibitor |
| CETUXIMAB | Epidermal growth factor receptor erbB1 inhibitor |
| ERLOTINIB HYDROCHLORIDE | Epidermal growth factor receptor erbB1 inhibitor |
| GEFITINIB | Epidermal growth factor receptor erbB1 inhibitor |
| LAPATINIB DITOSYLATE | Epidermal growth factor receptor erbB1 inhibitor |
| AFATINIB DIMALEATE | Epidermal growth factor receptor erbB1 inhibitor |
| OSIMERTINIB MESYLATE | Epidermal growth factor receptor erbB1 inhibitor |
| NECITUMUMAB | Epidermal growth factor receptor erbB1 inhibitor |
| OLMUTINIB | Epidermal growth factor receptor erbB1 inhibitor |
| BRIGATINIB | Epidermal growth factor receptor erbB1 inhibitor |
| OSIMERTINIB | Epidermal growth factor receptor erbB1 inhibitor |
| NERATINIB | Epidermal growth factor receptor erbB1 inhibitor |
| DACOMITINIB | Epidermal growth factor receptor erbB1 inhibitor |
| DACOMITINIB ANHYDROUS | Epidermal growth factor receptor erbB1 inhibitor |
| NERATINIB MALEATE | Epidermal growth factor receptor erbB1 inhibitor |
| AMIVANTAMAB | Epidermal growth factor receptor erbB1 inhibitor |
| MOBOCERTINIB | Epidermal growth factor receptor erbB1 inhibitor |
| LAZERTINIB | Epidermal growth factor receptor erbB1 inhibitor |
| MOBOCERTINIB SUCCINATE | Epidermal growth factor receptor erbB1 inhibitor |
| LAZERTINIB MESYLATE | Epidermal growth factor receptor erbB1 inhibitor |

---

## Literature Evidence

**PubMed title matches:** 18783 (20 most recent retrieved)

### Most Recent Publications

**[2026]** Urinary Liver-Type Fatty Acid-Binding Protein, Albuminuria, and eGFR Trajectories in Type 2 Diabetes.  
*J Diabetes* — PMID: 42888490  
> Urinary liver-type fatty acid-binding protein (L-FABP) reflects proximal tubular stress and has been proposed as a biomarker of diabetic kidney disease. We examined whether urinary L-FABP provides information on longitudinal kidney function beyond urinary albumin-to-creatinine ratio (UACR). This ret...

**[2026]** EGFR-targeted antibody-toxin conjugate in recurrent glioma: a phase 1 trial.  
*Nat Med* — PMID: 42888247  
> D2C7-ATC is a recombinant antibody-toxin conjugate (ATC) targeting wild-type epidermal growth factor receptor (EGFR) and mutant EGFR variant III (EGFRvIII). We conducted a single-arm, single-site, open-label phase 1 trial evaluating a single infusion of D2C7-ATC via convection-enhanced delivery in t...

**[2026]** Triphenyl Phosphate Exposure Is Associated With BRG1-Related Cellular and Metabolic Readouts and EREG-EGFR/ERK Signalling in Glioma Cells.  
*Int J Med Robot* — PMID: 42886048  
> Triphenyl phosphate (TPP), a ubiquitous organophosphate flame retardant and plasticiser, has emerged as a pervasive environmental contaminant with suspected endocrine-disrupting properties. In this study, we employed an integrated approach combining epigenetic CRISPR-Cas9 knockout screening, spatial...

**[2026]** Case Report WIN-MTB-2024001 - WIN International Molecular Tumor Board: A 55-year-old male with glioblastoma exhibiting amplifications in MDM2 and EGFR.  
*Oncotarget* — PMID: 42885740  
> Copyright: &copy; 2026 El-Deiry et al. This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. The WIN Conso...

**[2026]** [Association of tumor metabolic parameters on amino acid PET/CT with EGFR expression].  
*Zh Vopr Neirokhir Im N N Burdenko* — PMID: 42885126  
> According to the 2021 WHO classification, molecular-genetic profiling of CNS tumors is the standard for diagnosis. Beyond  To analyze the relationship between  The study included 71 adults with gliomas: glioblastoma ( Differences in

**[2026]** Novel 2,4-Pyrimidinediamine Derivative as Potent EGFR Inhibitor for NSCLC Treatment.  
*Molecules* — PMID: 42883206  
> Aberrant activation of EGFR drives the progression of non-small-cell lung cancer (NSCLC). As one of the most prevalent driver genes in NSCLC, EGFR represents a critical therapeutic target for patients with NSCLC. In this study, we synthesized 2,4-pyrimidinediamine derivative ZX-3. Compared to its le...

**[2026]** Design, Synthesis, In Vitro and In Silico Evaluation of Triazole-Benzimidazole Hybrid Derivatives as Potential Inhibitors of EGFR, EGFR-L858R, and EGFR-L858R/T790M.  
*Molecules* — PMID: 42883199  
> Epidermal growth factor receptor (EGFR) has become one of the most important molecular targets for the development of anticancer agents because of its critical role in regulating cell proliferation, differentiation, and survival. In the present study, a novel series of benzimidazole-triazole derivat...

**[2026]** Computational Evaluation of Carbazole-Chalcone Urea and Thiourea Derivatives Against EGFR: Molecular Docking, Pharmacokinetic Profiling, Target Prediction, and Molecular Dynamics Simulation.  
*Molecules* — PMID: 42883140  
> A series of previously synthesized carbazole-based urea and thiourea derivatives (

**[2026]** Loss of NCOA6 protein causes aggressive prostate cancer with EGFR overexpression and dependency.  
*Nat Commun* — PMID: 42875450  
> Loss of tumor suppressors can drive carcinogenesis while simultaneously creating actionable therapeutic vulnerabilities. Epidermal growth factor receptor (EGFR) is frequently overexpressed in prostate cancer (PCa), yet EGFR inhibitors have shown limited clinical benefit, and the basis for this varia...

**[2026]** Gefitinib-based therapy in refractory hepatocellular carcinoma with EGFR overexpression: a spatial profiling-guided case report.  
*Front Immunol* — PMID: 42865658  
> Current systemic treatments for advanced hepatocellular carcinoma (HCC) such as antiangiogenic targeted therapies, immune checkpoint inhibitors (ICIs), and their combinations have shown benefit, but widespread drug resistance severely limits patient outcomes and underscores an urgent need for effect...

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*