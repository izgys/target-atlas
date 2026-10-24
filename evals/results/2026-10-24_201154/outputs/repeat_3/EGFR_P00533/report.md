# Target Atlas Report — EGFR (P00533)

**Generated:** 2026-10-24T18:19:47.289341  
**Organism:** Homo sapiens  
**Run ID:** 8e1ec37a-284d-4cf8-88be-a701eef266bf  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

EGFR (P00533) is one of the most extensively validated and drugged targets in oncology, with 393 PDB structures (best resolution 1.07Å), 26,600 ChEMBL IC50 entries, and 20 approved drugs including small-molecule kinase inhibitors and therapeutic antibodies. The structural, chemical, and literature evidence collectively place this target in the highest tier of druggability. Ongoing clinical research continues to explore novel EGFR-targeting strategies across multiple cancer indications.

### Evidence Gaps

- Median IC50 of 2000 nM across all ChEMBL entries suggests a large proportion of compounds in the dataset have modest potency, reflecting the breadth of screening data rather than a lack of potent inhibitors — this is not a true gap but warrants contextual interpretation
- AlphaFold mean pLDDT of 75.9 with only 70.7% high-confidence residues suggests disordered regions (e.g., extracellular domain, flexible loops) that may not be fully captured by crystallographic structures
- Resistance mechanisms (e.g., T790M, C797S, exon 20 insertions) limit the utility of existing approved drugs in certain patient populations; next-generation inhibitors addressing all resistance mutations are still an active area of unmet need
- CNS penetration of current EGFR inhibitors remains limited, relevant for glioblastoma and brain metastases settings as highlighted in recent literature
- Some approved drugs listed may reflect combination formulations or salt forms rather than distinct molecular entities, which could slightly inflate the approved drug count

### Reasoning Trace

Step 1 — Structural confidence: 393 PDB entries with a best resolution of 1.07Å (X-ray crystallography) and 19/20 top structures containing bound ligands. This is exceptional structural coverage. The AlphaFold pLDDT of 75.9 (mean) with 70.7% high-confidence residues is moderate but irrelevant given the wealth of experimental structures. Structural confidence = HIGH.

Step 2 — Chemical confidence: ChEMBL ID CHEMBL203 has 26,600 IC50 entries — far exceeding the >1000 threshold for high confidence. Twenty approved drugs exist spanning multiple mechanistic classes (small-molecule TKIs: erlotinib, gefitinib, afatinib, osimertinib, etc.; monoclonal antibodies: cetuximab, panitumumab). The median IC50 of 2000 nM reflects the heterogeneity of the full dataset (including weak binders and screening hits) rather than a lack of potent compounds — many approved drugs have sub-nanomolar to low-nanomolar potency. Chemical confidence = HIGH.

Step 3 — Literature confidence: 18,783 PubMed papers with EGFR in the title, with active publication in 2026 across multiple disease areas (NSCLC, glioblastoma, colorectal cancer, etc.). This is among the most-published targets in biomedical research. Disease validation is extremely strong. Literature confidence = HIGH.

Step 4 — Druggability synthesis: EGFR possesses a well-defined ATP-binding kinase pocket (small molecule druggable), an extracellular ligand-binding domain (antibody druggable), and allosteric sites that have been exploited. The combination of structural tractability, chemical matter abundance, approved drugs, and deep disease validation makes this a paradigmatic high-druggability target.

Step 5 — Evidence gaps: The main gaps are not about druggability per se but about clinical challenges: acquired resistance mutations, CNS penetration, and specific patient subpopulations (e.g., exon 20 insertion mutations). The moderate AlphaFold pLDDT reflects disordered extracellular regions, but this does not diminish druggability given the extensive PDB coverage. The median IC50 of 2000 nM is a dataset artifact and not a true potency concern.

Conclusion: EGFR is unambiguously a HIGH druggability target with HIGH confidence across all three evidence dimensions.

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