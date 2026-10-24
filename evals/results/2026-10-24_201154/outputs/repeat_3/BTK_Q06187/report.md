# Target Atlas Report — BTK (Q06187)

**Generated:** 2026-10-24T18:21:40.475573  
**Organism:** Homo sapiens  
**Run ID:** b57a642a-bc71-49cc-bbd7-41b78ddcdab5  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

BTK (Q06187) is an exceptionally well-validated drug target with 170 PDB structures (best resolution 1.08Å), over 21,000 ChEMBL IC50 entries, and 6 approved drugs including ibrutinib, acalabrutinib, zanubrutinib, and pirtobrutinib. The target has strong disease validation in B-cell malignancies and primary immunodeficiencies, with active ongoing research including next-generation non-covalent inhibitors and PROTACs. Druggability is unambiguously high across all evidence dimensions.

### Evidence Gaps

- Resistance mechanisms to covalent BTK inhibitors (e.g., C481S mutation) remain an active clinical challenge, though non-covalent inhibitors like pirtobrutinib partially address this
- Selectivity profiling across the full kinome for newer-generation inhibitors may be incomplete in public databases
- PROTAC-based BTK degraders are still in early discovery/clinical stages — their long-term efficacy and safety profiles are not yet established
- Structural data for BTK in complex with resistance mutants (e.g., C481S, T474I) may be underrepresented in public PDB entries
- CNS penetration and blood-brain barrier data are limited for most approved BTK inhibitors, relevant for CNS lymphoma indications

### Reasoning Trace

Step 1 — Structural confidence: BTK has 170 PDB entries with the best resolution at 1.08Å (sub-angstrom, exceptional quality). All 20 of the best-resolved structures have ligands bound, confirming a well-characterised, druggable binding pocket. AlphaFold mean pLDDT of 84.4 with 86.5% of residues above 70 further supports a well-ordered protein. Structural confidence is unambiguously HIGH.

Step 2 — Chemical confidence: ChEMBL reports 21,674 IC50 entries with a median IC50 of 12 nM, indicating a highly potent and extensively explored chemical space. Six approved drugs exist (ibrutinib, acalabrutinib, zanubrutinib, tirabrutinib, pirtobrutinib, and one more), spanning both covalent and non-covalent mechanisms. This is among the most chemically validated kinase targets in oncology. Chemical confidence is HIGH.

Step 3 — Literature confidence: 938 PubMed papers with BTK in the title, with very recent publications in 2026 covering clinical pharmacokinetics, real-world outcomes, novel variants in XLA, biomarker studies, and next-generation PROTACs. The disease association (B-cell malignancies: CLL, MCL, WM; and X-linked agammaglobulinemia) is extremely well established. Literature confidence is HIGH.

Step 4 — Druggability assessment: BTK possesses a well-defined ATP-binding pocket that has been successfully exploited by multiple drug classes (irreversible covalent, reversible covalent, non-covalent, and now targeted protein degraders). The combination of atomic-resolution structures, massive chemical data, and 6 approved drugs leaves no ambiguity. Druggability score is HIGH.

Step 5 — Evidence gaps: The main gaps are not about druggability per se but about next-generation challenges: resistance mutations (C481S) limiting covalent inhibitors, selectivity of newer agents across the kinome, PROTAC maturity, CNS penetration, and structural coverage of clinically relevant resistance mutants. These are refinement questions rather than fundamental druggability uncertainties.

---

## Structural Evidence

**PDB entries:** 170 (top 20 by resolution detailed below)
**Best resolution:** 1.08Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 20/20

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 5P9J | 1.08 | X-RAY DIFFRACTION | Yes |
| 6DI1 | 1.1 | X-RAY DIFFRACTION | Yes |
| 5P9I | 1.11 | X-RAY DIFFRACTION | Yes |
| 6HRP | 1.12 | X-RAY DIFFRACTION | Yes |
| 6E4F | 1.15 | X-RAY DIFFRACTION | Yes |
| 4RFZ | 1.17 | X-RAY DIFFRACTION | Yes |
| 7L5O | 1.21 | X-RAY DIFFRACTION | Yes |
| 5P9L | 1.25 | X-RAY DIFFRACTION | Yes |
| 6DI9 | 1.25 | X-RAY DIFFRACTION | Yes |
| 6J6M | 1.25 | X-RAY DIFFRACTION | Yes |

### AlphaFold Confidence

**Mean pLDDT:** 84.4  
**High confidence fraction (pLDDT > 70):** 86.50%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-Q06187-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL5251
**Total IC50 entries:** 21,674
**Median IC50:** 12.0 nM

### Approved Drugs

| Drug | Mechanism |
|---|---|
| IBRUTINIB | Tyrosine-protein kinase BTK inhibitor |
| TIRABRUTINIB | Tyrosine-protein kinase BTK inhibitor |
| ACALABRUTINIB | Tyrosine-protein kinase BTK inhibitor |
| ZANUBRUTINIB | Tyrosine-protein kinase BTK inhibitor |
| PIRTOBRUTINIB | Tyrosine-protein kinase BTK inhibitor |
| ACALABRUTINIB MALEATE | Tyrosine-protein kinase BTK inhibitor |

---

## Literature Evidence

**PubMed title matches:** 938 (20 most recent retrieved)

### Most Recent Publications

**[2026]** Peripheral CD4(+) T-Cell Reserve as a Potential Biomarker of CD20 × CD3 Bispecific Antibody Outcomes and BTK Inhibitor-Associated Immune Modulation in B-Cell Lymphoma.  
*Hematol Oncol* — PMID: 42858312  
> Bispecific antibodies (BsAbs) targeting CD20 × CD3 have achieved remarkable efficacy in relapsed or refractory (R/R) B-cell lymphoma, yet clinical responses remain heterogeneous and predictive biomarkers are lacking. We retrospectively evaluated associations between peripheral immune profiles and ou...

**[2026]** Beyond Recurrent Infections: Immune Dysregulation Manifestations, Genotype-phenotype Heterogeneity, and Three Novel BTK Variants in X-linked Agammaglobulinemia.  
*Iran J Allergy Asthma Immunol* — PMID: 42825907  
> X-linked agammaglobulinemia (XLA) is an inborn error of immunity caused by BTK gene mutations, characterized by hypogammaglobulinemia and recurrent infections. This study evaluates a long-term pediatric cohort to assess clinical spectrum, therapeutic outcomes, and molecular findings. We retrospectiv...

**[2026]** Population pharmacokinetic analysis of pirtobrutinib, a non-covalent BTK inhibitor, in patients with hematological malignancies from the Phase 1/2 BRUIN study.  
*Cancer Chemother Pharmacol* — PMID: 42786239  
> This study aimed to characterize the pharmacokinetics (PK) of pirtobrutinib, a highly selective and noncovalent Bruton's tyrosine kinase (BTK) inhibitor, in adult patients with hematological malignancies using data from the Phase 1/2 BRUIN study (NCT03740529). Pirtobrutinib was administered as monot...

**[2026]** Timing matters: Impact of covalent BTK inhibitor dose modifications on outcomes in chronic lymphocytic leukemia/small lymphocytic leukemia-A 7-year real-world study.  
*Cancer* — PMID: 42740716  
> Covalent BTK inhibitors (cBTKis) are the cornerstone of chronic lymphocytic leukemia (CLL)/small lymphocytic leukemia (SLL) therapy, yet real-world data on dose modifications and their differential impact on long-term outcomes remain incompletely defined. This study investigated the incidence, timin...

**[2026]** Discovery of Highly Potent and Selective, Orally Bioavailable BTK-Targeting PROTACs Featuring Novel CRBN-Binding Warheads.  
*J Med Chem* — PMID: 42720469  
> Drugs targeting Bruton's tyrosine kinase (BTK) are recognized as key tools in hematological oncology. The clinical efficacy of BTK inhibitors is limited, however, by the emerging resistance driven by BTK mutations and the severe toxicity attributed to off-target kinase inhibition. PROteolysis TArget...

**[2026]** Comparative Efficacy of BTK Inhibitors in Treatment-Naïve and Relapsed/Refractory Mantle Cell Lymphoma: A Systematic Review and Meta-Analysis.  
*J Cell Mol Med* — PMID: 42687221  
> Bruton tyrosine kinase inhibitors (BTKis) have been employed in the treatment of mantle cell lymphoma (MCL). However, direct comparisons of ibrutinib, zanubrutinib, and acalabrutinib across treatment-naïve (TN) and relapsed/refractory (R/R) MCL remain limited. This meta-analysis was intended to eval...

**[2026]** Discovery of novel acridine based inhibitors of Bruton's tyrosine kinase (BTK) via pharmacophore modeling and machine learning-driven virtual screening followed by molecular dynamic studies.  
*J Comput Aided Mol Des* — PMID: 42678624  
> Bruton's Tyrosine Kinase (BTK) has been recently recognized as an important drug design target for treating B-cell malignancies. Unfortunately, drug resistance is making the treatment of B-cell malignancies challenging. In this study, we employed a dual machine learning drug design approach that inv...

**[2026]** Evaluating the outputs of ARAE-based molecular generative model for synthetic accessibility and BTK inhibition.  
*Bioorg Med Chem* — PMID: 42667712  
> The application of artificial intelligence (AI) methodologies in drug discovery represents a rapidly expanding area of interest, providing a valuable means for exploring uncharted chemical spaces to identify novel therapeutic candidates. In this proof-of-concept study, we evaluated hypothetical drug...

**[2026]** Polymeric nanoparticle platforms for ibrutinib delivery: tackling solubility, CYP3A4-mediated metabolism, and resistance to facilitate BTK-targeted therapy in solid tumours.  
*Ther Deliv* — PMID: 42639665  
> Because of its poor aqueous solubility, low oral bioavailability, extensive cytochrome P450 3A4 (CYP3A4)-mediated metabolism, and acquired resistance, ibrutinib, a first-in-class covalent Bruton's tyrosine kinase (BTK) inhibitor, has shown limited efficacy in solid tumors despite revolutionizing the...

**[2026]** Emerging pharmacotherapies for chronic spontaneous urticaria: spotlight on BTK inhibitors.  
*Expert Opin Pharmacother* — PMID: 42615080  
> Chronic spontaneous urticaria (CSU) results from multiple interacting pathogenic mechanisms. Despite available treatments, a proportion of patients remain inadequately controlled, supporting the need for therapeutic options. This review examines the role of Bruton's tyrosine kinase (BTK) in CSU and ...

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*