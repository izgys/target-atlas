# Target Atlas Report — ERBB2 (P04626)

**Generated:** 2026-10-18T13:30:23.323888  
**Organism:** Homo sapiens  
**Run ID:** 6dd0013a-a1a8-4c67-a93e-0c57a304ef00  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

ERBB2 (HER2) is one of the most extensively validated and drugged oncology targets in human medicine, with 14 approved therapeutics including monoclonal antibodies, small-molecule kinase inhibitors, and antibody-drug conjugates. Structural data are outstanding (1.25 Å best resolution, 9 ligand-bound structures), chemical space is deeply explored (>5,000 IC50 entries, median ~300 nM), and the literature base is enormous with continuing active clinical research across multiple tumor types. Druggability is unambiguously high across all evidence dimensions.

### Evidence Gaps

- AlphaFold mean pLDDT of 74 with only ~67% high-confidence fraction suggests disordered regions (likely extracellular or linker domains) not fully resolved even in crystal structures — conformational flexibility of certain loops may limit structure-based drug design in those regions
- Resistance mechanisms (e.g., ERBB2 mutations, PI3K pathway bypass, HER3 upregulation) are well-documented but not quantified in the evidence provided here, which limits assessment of next-generation drug design opportunities
- Median IC50 of ~300 nM across the ChEMBL dataset indicates that many compounds have moderate potency — the distribution of truly sub-nanomolar tool compounds vs. weaker scaffolds is not broken down
- Disease indication breadth (bladder, colorectal, liver fibrosis, osteoarthritis in recent titles) suggests expanding biology beyond breast/gastric cancer — full translational validation in non-oncology indications remains incomplete
- No explicit data on selectivity profiles or off-target liabilities across the ERBB family (EGFR, HER3, HER4) are summarised here

### Reasoning Trace

Step 1 — Target identity: ERBB2 (HER2/neu, P04626) is a receptor tyrosine kinase of the ErbB/EGFR family. It is one of the most clinically important oncogenes, amplified/overexpressed in ~15-20% of breast cancers and subsets of gastric, bladder, colorectal, and other tumours.

Step 2 — Structural confidence: 20 PDB structures retrieved, best resolution 1.25 Å by X-ray diffraction — this is exceptionally high resolution. 9/20 structures have ligand bound, enabling structure-based drug design with high precision. AlphaFold pLDDT mean of 74 with 66.8% >70 is moderate, but this is superseded by the wealth of experimental crystal structures; AlphaFold is less relevant here. Structural confidence = HIGH.

Step 3 — Chemical confidence: ChEMBL1824 has 5,265 IC50 entries — well above the >1,000 threshold for high confidence. Median IC50 of 301 nM indicates a broad dataset with a range of potencies. Critically, 14 approved drugs exist spanning diverse modalities (trastuzumab, pertuzumab as mAbs; T-DM1 and trastuzumab deruxtecan as ADCs; lapatinib, afatinib, neratinib, tucatinib as small-molecule TKIs). This is an extremely mature chemical landscape. Chemical confidence = HIGH.

Step 4 — Literature confidence: 20 recent publications in the provided sample, all from 2026, indicating continuing high-volume research activity. The broader ERBB2 literature encompasses thousands of publications. Disease validation is among the strongest of any oncology target — multiple randomised Phase III trials have demonstrated overall survival benefit. Recent titles show expansion into bladder cancer, colorectal cancer, liver fibrosis, and osteoarthritis, indicating broadening biological interest. Literature confidence = HIGH.

Step 5 — Druggability synthesis: ERBB2 has a well-defined ATP-binding kinase domain (small molecule tractable), an extracellular domain with defined epitopes (biologics tractable), and proven clinical utility with 14 approved agents. The target is fully validated across structural, chemical, and clinical dimensions. Druggability score = HIGH.

Step 6 — Evidence gaps: Despite the richness of evidence, the following gaps remain relevant for discovery decisions: (a) resistance biology is critical for next-wave therapeutics but not quantified here; (b) AlphaFold coverage of disordered regions is incomplete — relevant if targeting allosteric or non-kinase-domain sites; (c) selectivity data across the ErbB family is not summarised; (d) newer indications (fibrosis, OA) lack the depth of validation seen in breast cancer; (e) potency distribution details (what fraction of ChEMBL entries are truly high-potency leads) is not provided.

Overall conclusion: ERBB2 is among the highest-confidence druggable targets in the human proteome. All three evidence pillars (structural, chemical, literature) are at the highest possible confidence level.

---

## Structural Evidence

**PDB structures retrieved:** 20
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

**Recent publications retrieved:** 20

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