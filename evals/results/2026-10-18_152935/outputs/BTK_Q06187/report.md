# Target Atlas Report — BTK (Q06187)

**Generated:** 2026-10-18T13:33:32.792259  
**Organism:** Homo sapiens  
**Run ID:** da863d7f-3e44-49e2-bcf4-ce11e26ea0d5  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

BTK (Q06187) is an exceptionally well-validated drug target with six approved small-molecule inhibitors, over 21,000 ChEMBL IC50 entries, and multiple ultra-high-resolution co-crystal structures. The target has strong disease validation across B-cell malignancies and immunological conditions, with active ongoing research into next-generation covalent, non-covalent, and PROTAC-based approaches.

### Evidence Gaps

- Resistance mechanisms to approved covalent BTK inhibitors (e.g., C481S mutation) limit utility of existing drugs, and full structural characterisation of all clinically relevant resistance mutants may be incomplete
- Long-term safety and efficacy data for newer non-covalent inhibitors (e.g., pirtobrutinib) in broader patient populations are still emerging
- Selectivity profiles across the full kinome for many chemical series may not be fully characterised, particularly for novel PROTAC degraders
- Biomarker strategies for patient stratification and predicting BTK inhibitor-associated immune modulation remain under investigation

### Reasoning Trace

Step 1 – Structural Evidence: BTK has 20 PDB structures retrieved, all ligand-bound, with the best resolution at 1.08 Å by X-ray diffraction. This represents exceptional structural coverage; atomic-resolution co-crystal structures with diverse ligands provide high confidence in binding site geometry and enable structure-based drug design. AlphaFold pLDDT of 84.4 (86.5% high-confidence fraction) further corroborates structural order, though this is secondary given the wealth of experimental structures. Structural confidence is rated HIGH.

Step 2 – Chemical Evidence: ChEMBL lists 21,674 IC50 entries for CHEMBL5251, with a median IC50 of 12.0 nM — indicating a large, potent, and chemically diverse set of inhibitors. Six approved drugs exist (ibrutinib, acalabrutinib, zanubrutinib, tirabrutinib, pirtobrutinib, and one additional), spanning covalent and non-covalent mechanisms. This is among the best-characterised kinase targets chemically. Chemical confidence is rated HIGH.

Step 3 – Literature Evidence: Twenty recent publications (including 2026 entries) cover clinical pharmacokinetics, real-world outcomes, novel variants in disease, immune modulation biomarkers, and next-generation PROTAC discovery. This reflects a highly active and mature research landscape. Disease validation is strong across CLL, SLL, mantle cell lymphoma, and X-linked agammaglobulinemia. Literature confidence is rated HIGH.

Step 4 – Evidence Gaps: Despite the exceptional evidence base, some gaps remain: (a) resistance mutations (especially C481S) pose therapeutic challenges and structural/chemical coverage of mutant forms may be incomplete; (b) long-term clinical data for non-covalent inhibitors are still accruing; (c) kinome-wide selectivity of emerging degrader modalities (PROTACs) is not yet fully established; (d) predictive biomarkers for immune-related adverse events remain investigational.

Step 5 – Overall Assessment: BTK is one of the most thoroughly validated and drugged kinase targets in oncology and immunology. All three evidence pillars (structural, chemical, literature) score at the highest tier. Druggability is unambiguously HIGH.

---

## Structural Evidence

**PDB structures retrieved:** 20
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

**Recent publications retrieved:** 20

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