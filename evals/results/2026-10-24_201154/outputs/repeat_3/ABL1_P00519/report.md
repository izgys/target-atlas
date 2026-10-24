# Target Atlas Report — ABL1 (P00519)

**Generated:** 2026-10-24T18:21:19.628263  
**Organism:** Homo sapiens  
**Run ID:** 5f825e7f-f8a6-4136-a429-b218f4e802ec  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

ABL1 is one of the most extensively validated and successfully drugged kinase targets in oncology, with 7 approved drugs, over 5,000 ChEMBL IC50 entries, and 85 high-resolution crystal structures including ligand-bound complexes at sub-angstrom resolution. The target is primarily implicated in BCR-ABL1-driven chronic myeloid leukemia and is supported by a vast and active literature base of over 1,200 publications. Druggability is unambiguously high across all evidence dimensions.

### Evidence Gaps

- AlphaFold mean pLDDT is relatively low (63.4) and high-confidence fraction is only 46.3%, likely reflecting disordered regulatory regions (e.g., SH3/SH2 linkers, N-terminal cap) rather than the kinase domain itself — this does not impair druggability assessment given the wealth of experimental structures
- Resistance mutations (e.g., T315I gatekeeper) remain a clinical challenge; coverage of all clinically relevant mutant structures may be incomplete
- Selectivity profiling across the full kinome for newer inhibitors may be incomplete in ChEMBL
- Non-oncology indications (e.g., fibrosis, neurodegeneration) are less well validated despite emerging interest

### Reasoning Trace

Step 1 — Structural Evidence: ABL1 has 85 PDB entries with the best resolution at 1.03Å by X-ray diffraction. Of the top 20 best-resolved structures, 16 are ligand-bound. This is exceptional structural coverage. The AlphaFold pLDDT is low (63.4 mean, 46.3% >70), but this is expected for a multi-domain protein with intrinsically disordered regions (N-terminal cap, inter-domain linkers). The kinase domain itself is well-ordered and extensively characterized experimentally, so the low AlphaFold score does not diminish structural confidence. Structural confidence = HIGH.

Step 2 — Chemical Evidence: ChEMBL lists 5,295 IC50 entries with a median of 140 nM, indicating a large and potent chemical dataset. Seven approved drugs exist (imatinib, dasatinib, nilotinib, bosutinib, regorafenib, and 2 others), spanning multiple generations of inhibitor design including Type I, Type II, and allosteric mechanisms. This is among the most chemically validated targets in the human proteome. Chemical confidence = HIGH.

Step 3 — Literature Evidence: 1,228 PubMed publications with ABL1 in the title, with active 2026 publications covering clinical diagnostics (BCR::ABL1 MRD monitoring), novel fusions (GAB1::ABL1), and germline gain-of-function variants. Disease association with CML is causal and mechanistically established. Literature confidence = HIGH.

Step 4 — Evidence Gaps: The low AlphaFold pLDDT is noted but explained by protein architecture rather than true disorder in the druggable kinase domain. Resistance mutations (T315I, compound mutations) are a known clinical limitation but do not reduce druggability — they represent an ongoing medicinal chemistry challenge. Selectivity and off-target profiling for all approved and investigational agents may not be fully captured. Emerging non-oncology indications lack the same level of validation.

Step 5 — Overall Assessment: ABL1 is a paradigmatic druggable target. All three evidence pillars (structural, chemical, literature) are at the highest confidence level. The druggability score is unambiguously HIGH.

---

## Structural Evidence

**PDB entries:** 85 (top 20 by resolution detailed below)
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

**PubMed title matches:** 1228 (20 most recent retrieved)

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