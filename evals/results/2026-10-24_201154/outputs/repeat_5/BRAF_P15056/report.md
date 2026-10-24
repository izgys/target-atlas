# Target Atlas Report — BRAF (P15056)

**Generated:** 2026-10-24T18:28:13.992099  
**Organism:** Homo sapiens  
**Run ID:** 05d40868-3cb2-4ef6-8904-fb017d2e8093  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

BRAF (P15056) is one of the most extensively validated oncology drug targets in human medicine, with 5 approved small-molecule inhibitors, over 11,000 ChEMBL IC50 entries, and 138 PDB structures including many high-resolution ligand-bound complexes. The target is highly druggable with a well-characterised ATP-binding pocket and a wealth of structural, chemical, and clinical evidence supporting continued drug discovery efforts.

### Evidence Gaps

- AlphaFold mean pLDDT of 66.4 (55% high-confidence fraction) suggests disordered regions outside the kinase domain, but this does not impair druggability given the extensive experimental structural data
- Resistance mechanisms (e.g., BRAF V600E paradoxical activation, splice variants, RAS-independent dimerisation) are well-known but next-generation inhibitor strategies targeting these remain an active and partially unresolved area
- Structural coverage of BRAF in non-V600E mutant contexts (e.g., class II/III mutations, fusions) may be less complete than for the canonical V600E form
- Allosteric and dimer-interface inhibitor binding modes are less structurally characterised compared to ATP-competitive binding
- Long-term clinical resistance profiles and combination strategies are still being defined in several tumour types (e.g., colorectal, biliary tract)

### Reasoning Trace

Step 1 — Structural confidence: 138 PDB entries with a best resolution of 1.5 Å (X-ray crystallography) and 18/20 top structures containing bound ligands. This is an exceptionally rich structural dataset. The AlphaFold mean pLDDT of 66.4 (55% high-confidence fraction) is moderate, but this is largely irrelevant given the abundance of experimental structures. The low pLDDT likely reflects disordered N-terminal and regulatory regions outside the kinase domain, which are not the primary drug-binding site. Structural confidence is therefore HIGH.

Step 2 — Chemical confidence: 11,017 IC50 entries in ChEMBL with a median IC50 of 173.5 nM indicates a very large and mature SAR dataset. Five approved drugs (vemurafenib, dabrafenib, sorafenib, regorafenib, encorafenib) confirm clinical translation. Chemical confidence is HIGH.

Step 3 — Literature confidence: 7,320 PubMed titles containing 'BRAF', with active 2026 publications spanning multiple cancer types (colorectal, thyroid, biliary tract, craniopharyngioma, lung). This reflects a highly active field with strong and multi-faceted disease validation. Literature confidence is HIGH.

Step 4 — Druggability assessment: BRAF is a serine/threonine kinase with a well-defined ATP-binding cleft that has been successfully exploited by multiple approved drugs. The V600E mutation (constitutively active) is the primary oncogenic driver in melanoma (~50%), thyroid cancer, colorectal cancer, and others. The combination of deep structural knowledge, extensive medicinal chemistry, and clinical validation makes this a textbook high-druggability target.

Step 5 — Evidence gaps: The main gaps are not in basic druggability but in next-generation challenges: (a) resistance mechanisms including paradoxical MAPK activation, BRAF splice variants, and RAS-independent dimerisation; (b) structural characterisation of class II/III BRAF mutants and fusion proteins; (c) allosteric/dimer-interface inhibitor design; (d) combination strategies to overcome resistance in colorectal and other tumour types. These are active research areas but do not diminish the overall high druggability rating.

Conclusion: BRAF is unambiguously a high-druggability target with all three confidence dimensions rated high.

---

## Structural Evidence

**PDB entries:** 138 (top 20 by resolution detailed below)
**Best resolution:** 1.5Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 18/20

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 8VSO | 1.5 | X-RAY DIFFRACTION | Yes |
| 8JNB | 1.62 | X-RAY DIFFRACTION | Yes |
| 8C7X | 1.65 | X-RAY DIFFRACTION | Yes |
| 8C7Y | 1.65 | X-RAY DIFFRACTION | Yes |
| 9EW6 | 1.65 | X-RAY DIFFRACTION | Yes |
| 8JNA | 1.7 | X-RAY DIFFRACTION | No |
| 9BP8 | 1.73 | X-RAY DIFFRACTION | Yes |
| 5VYK | 1.749 | X-RAY DIFFRACTION | Yes |
| 9BFB | 1.92 | X-RAY DIFFRACTION | Yes |
| 7K0V | 1.93 | X-RAY DIFFRACTION | Yes |

### AlphaFold Confidence

**Mean pLDDT:** 66.4  
**High confidence fraction (pLDDT > 70):** 55.20%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-P15056-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL5145
**Total IC50 entries:** 11,017
**Median IC50:** 173.5 nM

### Approved Drugs

| Drug | Mechanism |
|---|---|
| DABRAFENIB MESYLATE | Serine/threonine-protein kinase B-raf inhibitor |
| REGORAFENIB | Serine/threonine-protein kinase B-raf inhibitor |
| SORAFENIB TOSYLATE | Serine/threonine-protein kinase B-raf inhibitor |
| VEMURAFENIB | Serine/threonine-protein kinase B-raf inhibitor |
| ENCORAFENIB | Serine/threonine-protein kinase B-raf inhibitor |

---

## Literature Evidence

**PubMed title matches:** 7320 (20 most recent retrieved)

### Most Recent Publications

**[2026]** Impact of Phosphatidylinositol 3-Kinase and B-Raf Mutations in Rat Sarcoma Wild-Type Metastatic Colorectal Cancer.  
*J Vis Exp* — PMID: 42891583  
> Activating mutations in phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha (PIK3CA) and B-Raf proto-oncogene (BRAF) are hypothesized to confer primary resistance to anti-epidermal growth factor receptor (anti-EGFR) monoclonal antibodies in metastatic colorectal cancer (mCRC). How...

**[2026]** Cobimetinib + Vemurafenib in Patients With BRAF V600E-Mutant Papillary Thyroid and Biliary Tract Cancers: Results From the TAPUR Study.  
*JCO Precis Oncol* — PMID: 42886887  
> TAPUR is a phase II basket trial evaluating the antitumor activity of commercially available targeted agents in patients with advanced cancer and genomic alterations. Results of two cohorts of patients with advanced thyroid (TC) or biliary tract cancer (BTC) with  Eligible patients had measurable di...

**[2026]** [Patients with papillary craniopharyngioma successfully treated with BRAF and MEK inhibitors].  
*Lakartidningen* — PMID: 42885245  
> Craniopharyngioma is a rare brain epithelial tumor infiltrating the hypothalamus causing visual loss, panhypopituitarism, cognitive deficits and obesity. 94% of papillary craniopharyngiomas harbour a BRAF mutation. Two patients with PCP and BRAF V600E mutation, with different tumor status, were trea...

**[2026]** Correction for Ran et al., Versatile Xenopus tropicalis model with targeted integration of human BRAF(V600E).  
*Proc Natl Acad Sci U S A* — PMID: 42863086  

**[2026]** Multiple Pulmonary Papillary Adenoma With Malignant Potential Accompanied by ERBIN-BRAF Gene Fusion and APC Mutation: A Case Report and Literature Review.  
*Can Respir J* — PMID: 42853102  
> Pulmonary papillary adenoma is currently considered a benign tumor; however, a few cases have been reported in the past with potential for malignancy. Therefore, the histological nature of papillary adenomas remains controversial. This article presents a rare case of a multifocal papillary adenoma w...

**[2026]** A malignancy risk prediction model for Bethesda category III thyroid nodules based on serological indicators, C-TIRADS, and BRAF V600E testing.  
*Front Endocrinol (Lausanne)* — PMID: 42851340  
> To investigate the diagnostic value of a multimodal prediction model integrating thyroglobulin antibody (TgAb), thyroid peroxidase antibody (TPOAb), the Chinese Thyroid Imaging Reporting and Data System (C-TIRADS), and BRAF V600E mutation status, for evaluating the malignancy risk in Bethesda Catego...

**[2026]** Pediatric Spinal Cord Astrocytoma With Granular Cell-Like Morphology and KIAA1549::BRAF Fusion.  
*Neuropathology* — PMID: 42827401  
> We report a pediatric spinal cord tumor with prominent granular cell-like features that posed a significant diagnostic challenge. Intraoperative findings and the initial histopathological evaluation revealed marked granular cell proliferation, leading to a provisional diagnosis of granular cell astr...

**[2026]** Type II RAF Inhibitor Tovorafenib in Recurrent/Refractory Melanoma or Other Solid Tumors With BRAF Fusions or CRAF/RAF1 Fusions or Amplification: Phase II FIRELIGHT-1 Substudy.  
*JCO Precis Oncol* — PMID: 42826365  
> Tovorafenib is an oral, selective, CNS-penetrant, type II inhibitor of BRAF and CRAF.  Patients ≥12 years of age with a recurrent/refractory solid tumor with a  Twenty-three patients were enrolled; eight in the melanoma cohort and 15 in the tumor-agnostic cohort. The median age was 53 years (range, ...

**[2026]** KRAS and BRAF Hotspot Variants Show Lower Prevalence in Bangladeshi Colorectal Cancer Patients.  
*Asian Pac J Cancer Prev* — PMID: 42808388  
> Colorectal cancer (CRC) is the second-leading cause of cancer-related mortality globally, with a rising incidence in Bangladesh. This study aims to identify pathogenic KRAS and BRAF mutations contributing to anti-EGFR resistance in CRC patients. Two sets of primers were used: one was adopted from a ...

**[2026]** Systemic inflammation and prognosis in patients with RAS/BRAF wild-type metastatic colorectal cancer receiving anti-EGFR therapy: A real-world cohort study.  
*Colorectal Dis* — PMID: 42798176  
> Colorectal cancer outcomes are heterogeneous, so greater prognostic discrimination is needed. In this retrospective real-world analysis, we assessed the prognostic effect of markers of systemic inflammation in a cohort of patients with RAS/BRAF wild-type metastatic colorectal cancer (mCRC) who recei...

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*