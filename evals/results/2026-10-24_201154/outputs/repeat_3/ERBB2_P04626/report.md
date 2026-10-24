# Target Atlas Report — ERBB2 (P04626)

**Generated:** 2026-10-24T18:20:11.104079  
**Organism:** Homo sapiens  
**Run ID:** 664aa86c-9a2f-404c-bcbc-a28279fef680  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

ERBB2 (HER2) is one of the most extensively validated and successfully drugged oncology targets in human medicine, with 14 approved drugs spanning monoclonal antibodies, antibody-drug conjugates, and small-molecule kinase inhibitors. Structural data is exceptionally rich (63 PDB entries, best resolution 1.25Å, multiple ligand-bound structures), and chemical space is deeply explored (>5,000 IC50 entries, median 301 nM). Literature support is overwhelming with >2,400 publications and active ongoing clinical development across multiple tumor types.

### Evidence Gaps

- AlphaFold mean pLDDT of 74.0 with only 66.8% high-confidence fraction suggests disordered regions (likely extracellular linkers or flexible loops) not fully resolved in crystal structures — allosteric sites in these regions remain structurally uncertain
- Resistance mechanisms (e.g., HER2 mutations, truncated p95-HER2, bypass signaling) are well-documented but not fully addressed by current approved agents, representing an unmet medicinal chemistry challenge
- HER2-low and HER2-ultralow expression thresholds for therapeutic eligibility are still being defined clinically, limiting target stratification clarity
- Structural coverage of the full-length receptor in membrane context (transmembrane and intracellular juxtamembrane domains) is limited — most PDB structures cover isolated kinase or extracellular domains
- Combination synergy landscape with emerging modalities (e.g., bispecifics, PROTACs, CAR-T) is incompletely characterized at the structural/mechanistic level

### Reasoning Trace

Step 1 — Structural confidence: 63 PDB entries with best resolution of 1.25Å is exceptional. 9 of the top 20 structures have ligand bound, confirming well-defined binding pockets amenable to structure-based drug design. AlphaFold pLDDT of 74.0 (mean) with 66.8% high-confidence fraction is moderate, but this is expected for a multi-domain receptor tyrosine kinase with flexible extracellular and linker regions; the crystallographic data more than compensates. Structural confidence = HIGH.

Step 2 — Chemical confidence: ChEMBL ID CHEMBL1824 has 5,265 IC50 entries with a median of 301 nM, indicating a well-explored SAR landscape. Critically, 14 approved drugs exist covering diverse modalities: two naked mAbs (trastuzumab, pertuzumab), an ADC (T-DM1, T-DXd implied in the 9 additional), and multiple small-molecule TKIs (lapatinib, afatinib, neratinib, tucatinib, etc.). This is among the highest chemical validation possible for any target. Chemical confidence = HIGH.

Step 3 — Literature confidence: 2,443 PubMed titles containing ERBB2, with publications as recent as 2026 spanning breast, gastric, bladder, colorectal, and other cancers. The target has decades of mechanistic, translational, and clinical research. Disease association is causal (amplification/overexpression drives oncogenesis), not merely correlative. Literature confidence = HIGH.

Step 4 — Druggability synthesis: All three pillars (structural, chemical, literature) are at the highest confidence tier. The target has proven tractability across multiple drug classes. The only meaningful gaps are: (a) incomplete structural coverage of membrane-embedded and disordered regions, (b) resistance biology that continues to evolve, and (c) emerging indications (HER2-low) where target biology is still being defined. None of these gaps reduce the overall druggability score from HIGH — they represent opportunities for next-generation agents rather than fundamental barriers.

Step 5 — Evidence gaps: Noted above. The primary scientific frontier is overcoming acquired resistance and extending benefit to HER2-low populations, not establishing basic druggability which is already proven.

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