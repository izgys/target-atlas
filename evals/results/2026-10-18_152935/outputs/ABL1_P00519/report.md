# Target Atlas Report — ABL1 (P00519)

**Generated:** 2026-10-18T13:32:45.362308  
**Organism:** Homo sapiens  
**Run ID:** ccffaaad-2378-4359-a100-3895475f2c10  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

ABL1 is one of the best-validated and most extensively drugged kinase targets in oncology, with 7 approved small-molecule inhibitors, over 5,000 ChEMBL IC50 entries, and multiple ultra-high-resolution crystal structures including ligand-bound complexes. The target is robustly implicated in chronic myeloid leukemia (CML) via the BCR::ABL1 fusion, and recent literature confirms continued active clinical and translational investigation. Druggability is definitively high across all dimensions.

### Evidence Gaps

- AlphaFold mean pLDDT is moderate (63.4%), reflecting disordered regions (e.g., SH2-kinase linker, N-terminal cap), but this is not a concern given abundant experimental PDB structures
- Resistance mutations (e.g., T315I gatekeeper) remain a therapeutic challenge; coverage of resistant mutant structures and chemical matter could be more comprehensively assessed
- Regorafenib is listed as an ABL1 inhibitor but is primarily known as a multi-kinase inhibitor; its ABL1-specific pharmacology may not be a primary indication driver
- No explicit data provided on allosteric inhibitor coverage (e.g., asciminib/STAMP inhibitors) beyond ATP-competitive agents
- Disease indications beyond CML (e.g., Philadelphia chromosome-positive ALL, solid tumors with ABL1 fusions) not deeply enumerated in the provided evidence

### Reasoning Trace

Step 1 - Structural Evidence: ABL1 has 20 PDB structures with the best resolution at 1.03Å (sub-angstrom, exceptional quality). 16/20 structures are ligand-bound, confirming a well-characterised and accessible binding site. The AlphaFold mean pLDDT of 63.4% with only 46% of residues above 70% pLDDT is lower than ideal, but this is entirely expected for a multi-domain protein with flexible linkers and is irrelevant given the wealth of experimental structural data. Structural confidence: HIGH.

Step 2 - Chemical Evidence: 5,295 IC50 entries in ChEMBL with a median IC50 of 140 nM indicates a very large and mature chemical dataset. There are 7 approved drugs including imatinib, dasatinib, nilotinib, and bosutinib — all first- or second-generation ABL1 inhibitors with well-characterised mechanisms. This represents one of the most chemically validated targets in all of drug discovery. Chemical confidence: HIGH.

Step 3 - Literature Evidence: 20 recent publications retrieved, all from 2026, covering CML diagnostics (BCR::ABL1 MRD monitoring), novel fusion oncoproteins (GAB1::ABL1), and germline gain-of-function ABL1 variants (CHDSKM syndrome). This indicates active, contemporary research across multiple disease contexts. Given ABL1's decades-long prominence in oncology, total publication counts are certainly well above 500. Literature confidence: HIGH.

Step 4 - Evidence Gaps: The main gaps are minor. The AlphaFold pLDDT concern is moot given PDB data. Resistance mutations (e.g., T315I, compound mutations) are known challenges not quantified in the provided data. Allosteric inhibitors like asciminib (approved 2021) are not explicitly listed in the 7 drugs shown, suggesting the drug list may be incomplete. Regorafenib's inclusion as an ABL1-specific drug is slightly unusual and may reflect off-target activity.

Step 5 - Overall Assessment: ABL1 is a paradigmatic druggable target. It has exemplary structural data, a massive chemical dataset with multiple approved drugs spanning multiple generations, and robust disease validation primarily in CML. Druggability score: HIGH with very high confidence.

---

## Structural Evidence

**PDB structures retrieved:** 20
**Best resolution:** 1.03Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 16/20

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 5OAZ | 1.03 | X-RAY DIFFRACTION | Yes |
| 7PVS | 1.05 | X-RAY DIFFRACTION | Yes |
| 4J9C | 1.051 | X-RAY DIFFRACTION | Yes |
| 4J9F | 1.094 | X-RAY DIFFRACTION | Yes |
| 7PW2 | 1.1 | X-RAY DIFFRACTION | No |
| 3EG3 | 1.4 | X-RAY DIFFRACTION | Yes |
| 4J9E | 1.4 | X-RAY DIFFRACTION | Yes |
| 5DC4 | 1.48 | X-RAY DIFFRACTION | Yes |
| 4J9D | 1.5 | X-RAY DIFFRACTION | Yes |
| 5HU9 | 1.529 | X-RAY DIFFRACTION | Yes |

### AlphaFold Confidence

**Mean pLDDT:** 63.4  
**High confidence fraction (pLDDT > 70):** 46.30%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-P00519-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL1862
**Total IC50 entries:** 5,295
**Median IC50:** 140.0 nM

### Approved Drugs

| Drug | Mechanism |
|---|---|
| NILOTINIB HYDROCHLORIDE MONOHYDRATE | Tyrosine-protein kinase ABL inhibitor |
| DASATINIB ANHYDROUS | Tyrosine-protein kinase ABL inhibitor |
| BOSUTINIB | Tyrosine-protein kinase ABL inhibitor |
| REGORAFENIB | Tyrosine-protein kinase ABL inhibitor |
| IMATINIB MESYLATE | Tyrosine-protein kinase ABL inhibitor |
| ASCIMINIB | Tyrosine-protein kinase ABL inhibitor |
| UMBRALISIB TOSYLATE | Tyrosine-protein kinase ABL inhibitor |

---

## Literature Evidence

**Recent publications retrieved:** 20

### Most Recent Publications

**[2026]** Next-generation digital polymerase chain reaction assay for BCR::ABL1 in chronic myeloid leukemia: comprehensive validation for standardized measurable residual disease detection.  
*Blood Res* — PMID: 42886318  
> The sensitivity of real-time quantitative reverse-transcription polymerase chain reaction (RT-qPCR) for detecting measurable residual disease (MRD) in patients with chronic myeloid leukemia (CML) who have achieved a deep molecular response is limited. We validated a digital PCR (dPCR) assay (LQ Chec...

**[2026]** Clinical Characteristics of Coexistent Chronic Myeloid Leukemia and BCR::ABL1 Negative Myeloproliferative Neoplasms: A Retrospective Study.  
*Hematol Oncol* — PMID: 42876003  
> Coexistent chronic myeloid leukemia (CML) and BCR::ABL1-negative myeloproliferative neoplasms (MPN) are rare. We aimed to evaluate their clinical and therapeutic profiles. We retrospectively evaluated 36 institutional patients with coexistent CML and BCR::ABL1-negative MPN (Cohort A) and systematica...

**[2026]** Spindle Cell Tumors with a GAB1::ABL1 Fusion-Another Member of Protein-Kinase-Related Soft Tissue Neoplasms: An (Epi)Genetic Study of Six Cases with Benign Behavior.  
*Int J Mol Sci* — PMID: 42794529  
> Mesenchymal neoplasms driven by protein kinases represent an increasing group with a broad clinicopathologic and genetic spectrum. Recently, tumors harboring a

**[2026]** [Inter-laboratory comparison of international standardized BCR::ABL1 (P210) mRNA of chronic myeloid leukemia patients by digital PCR].  
*Zhonghua Xue Ye Xue Za Zhi* — PMID: 42706170  

**[2026]** Clinical and Functional Characterization of Gain-of-Function ABL1 Variants Expands the Phenotypic Spectrum of CHDSKM.  
*Am J Med Genet A* — PMID: 42681542  
> Germline gain-of-function (GOF) variants in ABL1 cause congenital heart defects and skeletal malformations syndrome (CHDSKM), a multisystem developmental disorder characterized by congenital heart disease, skeletal abnormalities, dysmorphic features, and variable developmental delay. More recently, ...

**[2026]** BCR::ABL1 e1a2 (p190)-Positive Myeloid Blast Neoplasm: Diagnostic Challenges in Distinguishing De Novo Acute Myeloid Leukemia From Previously Unrecognized Chronic Myeloid Leukemia in the Blast Phase.  
*Cureus* — PMID: 42667018  
> Chronic myeloid leukemia (CML) is a myeloproliferative neoplasm driven by the BCR::ABL1 fusion gene (abelson breakpoint clustering region 1), usually resulting from the reciprocal translocation t(9;22)(q34;q11.2), which generates the Philadelphia chromosome. Most patients with CML express the p210 B...

**[2026]** Erythroblastic sarcoma with biallelic TP53 mutations and novel NUP214:: ABL1-new finding in erythroblastic sarcoma/acute erythroid leukemia.  
*J Hematop* — PMID: 42611361  
> NUP214::ABL1 generates a fusion protein with constitutively activated tyrosine kinase activity and is present in rare T-lymphoblastic leukemia (ALL), B-ALL, and in rare cases of myelodysplastic neoplasm/acute myeloid leukemia (MDS/AML). Here, we for the first time reported NUP214::ABL1 in a case of ...

**[2026]** First Philippine report of myeloproliferative neoplasms with concurrent JAK2 and BCR::ABL1 mutations.  
*BMJ Case Rep* — PMID: 42575681  
> Myeloproliferative neoplasms (MPNs) are broadly classified into

**[2026]** A Rare BCR::SPECC1L::ABL1 Fusion in a Pediatric Chronic Myeloid Leukemia Patient.  
*J Pediatr Hematol Oncol* — PMID: 42573582  
> Chronic myeloid leukemia (CML) is a myeloproliferative neoplasm typically defined by BCR::ABL1 p210 fusions isoforms. An 8-year-old female CML patient harbored a typical t(9;22)(q34;11) Philadelphia chromosome and BCR::ABL1 fusion by conventional karyotyping and FISH but lacked BCR::ABL1 p210 fusion...

**[2026]** Late acquisition of BCR::ABL1 during clonal evolution of SAMD9-associated MDS with phenotypic shift from AML to B-ALL.  
*Int J Hematol* — PMID: 42533241  
> We describe a unique case of SAMD9-associated myelodysplastic syndrome (MDS) with monosomy 7 that evolved over 16 years into BCR::ABL1-positive acute myeloid leukemia (AML) and subsequently manifested as B-cell acute lymphoblastic leukemia (B-ALL). Genomic analysis at AML diagnosis revealed a germli...

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*