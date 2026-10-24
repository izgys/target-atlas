# Target Atlas Report — EGFR (P00533)

**Generated:** 2026-10-24T18:11:54.203715  
**Organism:** Homo sapiens  
**Run ID:** d811115e-5503-4a45-a46c-162ff82cd74a  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

EGFR (P00533) is one of the most extensively validated and drugged targets in oncology, with 393 PDB structures (best resolution 1.07Å), 26,600 ChEMBL IC50 entries, and 20 approved drugs including small molecules and biologics. The structural, chemical, and literature evidence collectively place this target in the highest tier of druggability with exceptional confidence across all dimensions.

### Evidence Gaps

- AlphaFold mean pLDDT of 75.9 with only 70.7% high-confidence residues suggests disordered regions (likely extracellular or linker domains) not well-captured by crystallography — functional relevance of these regions for novel modalities is incompletely characterised
- Median IC50 of 2000 nM across 26,600 entries is relatively high, suggesting many compounds in ChEMBL are weak binders or tested in less relevant assay formats — potency landscape for novel scaffolds may be less favourable than compound count implies
- Resistance mechanisms (e.g., T790M, C797S, exon 20 insertions) limit efficacy of existing drugs; coverage of allosteric or covalent binding sites beyond the ATP pocket for next-generation inhibitors is not fully explored
- Some recent literature conflates eGFR (estimated glomerular filtration rate) with EGFR (epidermal growth factor receptor), introducing noise into publication counts and potentially into disease-association analyses
- Tumour-specific isoforms (e.g., EGFRvIII in glioblastoma) and their distinct structural/pharmacological properties are not fully addressed by the aggregate data presented

### Reasoning Trace

Step 1 — Structural confidence: 393 PDB entries with a best resolution of 1.07Å (X-ray diffraction) and 19/20 top structures containing bound ligands constitutes exceptional structural coverage. This is among the best-characterised kinase targets structurally. The AlphaFold pLDDT of 75.9 (70.7% high-confidence) is moderate, but this is expected for a multi-domain receptor with flexible extracellular and juxtamembrane regions; the kinase domain itself is very well resolved crystallographically. Structural confidence = HIGH.

Step 2 — Chemical confidence: 26,600 IC50 entries in ChEMBL is an extraordinarily large dataset. 20 approved drugs spanning multiple generations (first-gen: gefitinib, erlotinib; second-gen: afatinib, lapatinib; third-gen: osimertinib; biologics: cetuximab, panitumumab) confirm deep chemical tractability. The median IC50 of 2000 nM is worth noting — it reflects the breadth of the dataset including many weak or non-optimised compounds, not the potency of clinical candidates (which are typically sub-nanomolar). Chemical confidence = HIGH.

Step 3 — Literature confidence: 18,783 PubMed titles containing 'EGFR' with active 2026 publications confirms this is one of the most studied targets in biomedicine. Disease validation in NSCLC, colorectal cancer, head and neck cancer, glioblastoma, and others is extremely strong. Caveat: some publications use 'eGFR' for estimated glomerular filtration rate (a renal function metric), which inflates the raw count slightly, but even discounting these, the literature base is enormous. Literature confidence = HIGH.

Step 4 — Druggability synthesis: All three pillars (structural, chemical, literature) are at the highest confidence tier. EGFR has a well-defined ATP-binding pocket, allosteric sites, and extracellular epitopes for antibody targeting. Multiple approved drugs validate the target clinically. The primary challenges are not druggability per se but resistance mechanisms and tumour heterogeneity — these are clinical/translational challenges, not target assessment failures. Druggability score = HIGH.

Step 5 — Evidence gaps: The main gaps are (a) incomplete structural coverage of disordered regions, (b) the high median IC50 reflecting assay diversity rather than true potency ceiling, (c) resistance mutations limiting existing drug classes, (d) literature noise from eGFR/EGFR conflation, and (e) tumour-specific isoforms like EGFRvIII requiring separate assessment.

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