# Target Atlas Report — ERBB2 (P04626)

**Generated:** 2026-10-18T14:25:37.219821  
**Organism:** Homo sapiens  
**Run ID:** 09a50cc8-b22b-4887-b422-9907dba737ee  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

ERBB2 (HER2) is one of the most extensively validated oncology drug targets in human medicine, with 14 approved drugs, over 5,000 ChEMBL IC50 entries, 63 PDB structures (best resolution 1.25Å), and nearly 2,500 publications. Both the extracellular domain (targeted by antibodies such as trastuzumab and pertuzumab) and the intracellular kinase domain (targeted by small molecules such as lapatinib and afatinib) are well-characterized binding sites. Druggability confidence is unambiguously high across all dimensions.

### Evidence Gaps

- AlphaFold mean pLDDT of 74.0 (66.8% high-confidence fraction) suggests the full-length model including flexible linker and transmembrane regions is partially disordered — but this is expected for a multi-domain receptor and does not affect druggability of the well-resolved kinase and extracellular domains
- Only 9 of the 20 best-resolved PDB structures have a ligand bound; additional co-crystal structures for newer covalent or allosteric inhibitor chemotypes could further inform structure-based design
- Resistance mechanisms (e.g., ERBB2 mutations, compensatory pathway activation) are known clinical liabilities but are not fully captured in the structural/chemical data presented here
- Activity at the transmembrane domain, which mediates dimerisation, remains structurally undercharacterised and represents an untapped binding site
- Emerging indications (bladder cancer, colorectal cancer, liver fibrosis) are active areas of investigation but clinical validation data in those settings are still accumulating

### Reasoning Trace

Step 1 — Structural confidence: ERBB2 has 63 PDB entries with the best resolution at 1.25Å by X-ray diffraction and 9/20 top structures containing bound ligands. This is exceptional structural coverage. The AlphaFold mean pLDDT of 74.0 and 66.8% high-confidence fraction are moderate overall, but this is expected for a large multi-domain transmembrane receptor where the kinase and extracellular subdomains are individually well-ordered while linker/TM regions are flexible. The crystallographically resolved regions (kinase domain, ECD domains II and IV) are the therapeutically relevant regions and are high confidence. Structural confidence = HIGH.

Step 2 — Chemical confidence: 5,265 IC50 entries in ChEMBL with a median of ~301 nM demonstrates a rich SAR landscape. Fourteen approved drugs spanning multiple modalities (monoclonal antibodies, antibody-drug conjugates, small-molecule TKIs including irreversible/covalent agents) confirm deep chemical tractability. This is among the highest chemical evidence profiles of any cancer target. Chemical confidence = HIGH.

Step 3 — Literature confidence: 2,443 PubMed papers with ERBB2 in the title, with active publication in 2026 across diverse indications (breast, bladder, colorectal, gastric cancers and beyond). Disease association is thoroughly validated at clinical level. Literature confidence = HIGH.

Step 4 — Druggability synthesis: All three pillars (structural, chemical, literature) are at the highest level. ERBB2 is a textbook druggable target with multiple approved drugs addressing distinct binding sites. There are no meaningful evidence gaps that would downgrade the overall druggability score. Druggability score = HIGH.

Step 5 — Evidence gaps: The primary gaps are (a) incomplete structural coverage of the TM domain and potential allosteric sites; (b) resistance mechanisms that reduce clinical efficacy of existing drugs; (c) emerging indications where benefit is still being established. These are research opportunities rather than flags against druggability.

---

## Structural Evidence

**PDB entries:** 63 (top 20 by resolution detailed below)
**Best resolution:** 1.25Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 9/20

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 1MFG | 1.25 | X-RAY DIFFRACTION | No |
| 8VB5 | 1.48 | X-RAY DIFFRACTION | Yes |
| 8JYR | 1.69 | X-RAY DIFFRACTION | Yes |
| 8U8X | 1.69 | X-RAY DIFFRACTION | Yes |
| 8JYQ | 1.75 | X-RAY DIFFRACTION | No |
| 7PCD | 1.77 | X-RAY DIFFRACTION | Yes |
| 5TQS | 1.876 | X-RAY DIFFRACTION | No |
| 1MFL | 1.88 | X-RAY DIFFRACTION | No |
| 4GFU | 2.0 | X-RAY DIFFRACTION | No |
| 6LBX | 2.03 | X-RAY DIFFRACTION | Yes |

### AlphaFold Confidence

**Mean pLDDT:** 74.0  
**High confidence fraction (pLDDT > 70):** 66.80%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-P04626-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL1824
**Total IC50 entries:** 5,265
**Median IC50:** 301.0 nM

### Approved Drugs

| Drug | Mechanism |
|---|---|
| TRASTUZUMAB | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| PERTUZUMAB | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| TRASTUZUMAB EMTANSINE | Receptor protein-tyrosine kinase erbB-2 binding agent |
| LAPATINIB DITOSYLATE | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| AFATINIB DIMALEATE | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| TUCATINIB | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| MASOPROCOL | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| NERATINIB | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| DACOMITINIB | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| MARGETUXIMAB | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| DACOMITINIB ANHYDROUS | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| NERATINIB MALEATE | Receptor protein-tyrosine kinase erbB-2 inhibitor |
| TRASTUZUMAB DERUXTECAN | Receptor protein-tyrosine kinase erbB-2 binding agent |
| ZANIDATAMAB | Receptor protein-tyrosine kinase erbB-2 inhibitor |

---

## Literature Evidence

**PubMed title matches:** 2443 (20 most recent retrieved)

### Most Recent Publications

**[2026]** Integrated Analysis of HER2 Expression and ERBB2 Alterations in Bladder Cancer.  
*Cancer Sci* — PMID: 42732768  
> Human epidermal growth factor receptor 2 (HER2) has emerged as a potential therapeutic target in bladder cancer (BC), particularly with the advent of next-generation antibody-drug conjugates (ADCs) like trastuzumab deruxtecan (T-DXd). However, the complex relationship between HER2 protein expression...

**[2026]** Secoisolariciresinol diglucoside alleviates inflammatory injury in osteoarthritis chondrocytes through ERBB2-associated JAK2/STAT3 signaling: network pharmacology and experimental validation.  
*Front Immunol* — PMID: 42718780  
> Cartilage injury is a hallmark of osteoarthritis (OA). erb-B2 receptor tyrosine kinase 2 (ERBB2) has been reported to be involved in mediating the therapeutic effects of polyphenols in orthopedic diseases. This study aimed to investigate the protective effects and underlying mechanisms of action of ...

**[2026]** S100 Calcium-Binding Protein 16 (S100A16) Promotes Hepatic Stellate Cell Activation Via Erb-B2 Receptor Tyrosine Kinase 2 (ERBB2)-mediated Glycolysis to Facilitate Liver Fibrosis.  
*Cell Biochem Funct* — PMID: 42704362  
> Hepatic stellate cell (HSC) activation is a key mediator in hepatic fibrosis, with glycolysis serving a key regulatory function. S100 calcium-binding protein 16 (S100A16) has been associated with various pathologies; however, its function and underlying mechanisms in liver fibrosis remains elusive. ...

**[2026]** Trastuzumab Deruxtecan in Metastatic Urothelial Carcinoma with NGS-Detected ERBB2 Amplification: A Four-Patient Real-World Case Series.  
*Curr Oncol* — PMID: 42645361  

**[2026]** Clinical significance of WES-defined ERBB2 amplification in resectable colorectal cancer.  
*Int J Clin Oncol* — PMID: 42622787  
> HER2 amplification is demonstrated to influence response to therapy and outcomes in metastatic colorectal cancer (mCRC), but its role in resectable CRC remains unclear. This study investigated the prognostic impact of WES-defined ERBB2 amplification and its association with adjuvant chemotherapy (AC...

**[2026]** Selective and Synergistic Targeting of ErbB2-Positive Cancer Cells with ErbB2 Transmembrane Peptide-Ionic Liquid Nanocarrier Formulation.  
*ACS Appl Mater Interfaces* — PMID: 42616845  
> ErbB2-positive cancers are highly aggressive and remain difficult to treat due to limitations of current therapies, such as poor selectivity, insufficient delivery, and toxicity toward healthy tissues. Herein, we developed a dual-action nanoformulation combining prolinium-based surface-active ionic ...

**[2026]** Genomic landscape and clinical characteristics of ERBB2/HER2-mutated colorectal cancers.  
*Oncologist* — PMID: 42536421  
> Molecular underpinnings and clinical characteristics of ERBB2/HER2-mutated colorectal cancers (CRCs) remain poorly understood. We aimed to comprehensively characterize the genomic landscape and clinical features of ERBB2/HER2-mutated CRC and to compare them with those of ERBB2/HER2-amplified CRC. We...

**[2026]** ERBB2 copy number alterations and protein expression in bladder cancer treated by cystectomy.  
*Hum Pathol* — PMID: 42532350  
> The introduction of antibody-drug-conjugates (ADC) that target HER2 has renewed interest in ERBB2 alterations in bladder cancer. Little is known about the frequency of ERBB2 copy number alterations in primary bladder cancer subtypes and regional nodal metastases, and the effect of amplification on p...

**[2026]** Cemiplimab and Fianlimab With Neoadjuvant Chemotherapy in Early-Stage High-Risk ERBB2-Negative Breast Cancer: The I-SPY2 Randomized Clinical Trial.  
*JAMA Oncol* — PMID: 42530945  
> Although adding immune checkpoint inhibitors to neoadjuvant chemotherapy improves outcomes in high-risk early-stage breast cancer, opportunities remain to further enhance response. Dual checkpoint blockade offers a potential strategy to further enhance efficacy. To evaluate the combination of anti-p...

**[2026]** [Expression characteristics and clinical significance of ERBB2 in bladder urothelial carcinoma based on the TCGA database].  
*Beijing Da Xue Xue Bao Yi Xue Ban* — PMID: 42493450  
> To investigate the expression pattern of Erb-B2 receptor tyrosine kinase 2 ( RNA sequencing expression data and clinical information were obtained from The Cancer Genome Atlas bladder urothelial carcinoma cohort (TCGA-BLCA). Differences in  HPA immunohistochemistry demonstrated stronger

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*