# Target Atlas Report — JAK2 (O60674)

**Generated:** 2026-10-18T14:27:21.550220  
**Organism:** Homo sapiens  
**Run ID:** d3718d9e-be19-47bb-94e9-3512fe0fd836  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

JAK2 is an exceptionally well-validated drug target with 171 PDB structures (best resolution 1.3Å), over 19,000 ChEMBL IC50 entries, and 12 approved drugs including ruxolitinib, fedratinib, baricitinib, and pacritinib. The target has extensive structural, chemical, and clinical validation across multiple disease indications including myeloproliferative neoplasms and inflammatory conditions. Druggability is unambiguously high by every metric.

### Evidence Gaps

- Selectivity over other JAK family members (JAK1, JAK3, TYK2) remains a challenge for next-generation inhibitors
- Covalent or allosteric inhibitor approaches are less explored relative to ATP-competitive scaffolds
- Structural data for JAK2 in complex with non-kinase domain binding ligands or PROTAC degraders is limited
- Resistance mechanisms (e.g., JAK2 mutations conferring inhibitor resistance) are not fully characterised structurally
- Disease-specific contexts (e.g., solid tumours vs. haematological malignancies) may require distinct targeting strategies not fully addressed by existing literature

### Reasoning Trace

Step 1 — Structural confidence: 171 PDB entries with the best resolution at 1.3Å by X-ray diffraction, and all 20 top-resolved structures contain bound ligands. AlphaFold mean pLDDT of 86.9 with 89.4% of residues above 70 confirms high structural order. This is unambiguously 'high' structural confidence. Step 2 — Chemical confidence: 19,301 IC50 entries in ChEMBL with a median IC50 of 111 nM, and 12 approved drugs targeting JAK2. This far exceeds the threshold for 'high' chemical confidence. The approved drug set spans multiple chemical scaffolds and indications. Step 3 — Literature confidence: 3,689 PubMed papers with JAK2 in the title, with active 2026 publications spanning oncology, inflammation, bone biology, and metabolic disease. This is well above the 500-paper threshold and reflects strong, recent disease validation. Confidence is 'high'. Step 4 — Druggability assessment: All three evidence streams independently point to a highly druggable target. The kinase domain presents a well-defined ATP-binding pocket, extensively exploited by approved therapeutics. No evidence gaps undermine the overall assessment. Key residual uncertainties include selectivity challenges within the JAK family, allosteric targeting potential, and resistance mutation profiles — but these are refinement questions for medicinal chemistry programs, not fundamental druggability concerns. Step 5 — Overall score: 'high' druggability with very high confidence across all dimensions.

---

## Structural Evidence

**PDB entries:** 171 (top 20 by resolution detailed below)
**Best resolution:** 1.3Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 20/20

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 8BXH | 1.3 | X-RAY DIFFRACTION | Yes |
| 7LL4 | 1.31 | X-RAY DIFFRACTION | Yes |
| 3UGC | 1.34 | X-RAY DIFFRACTION | Yes |
| 7REE | 1.38 | X-RAY DIFFRACTION | Yes |
| 8BA3 | 1.4 | X-RAY DIFFRACTION | Yes |
| 8BX9 | 1.4 | X-RAY DIFFRACTION | Yes |
| 7TEU | 1.45 | X-RAY DIFFRACTION | Yes |
| 9TM5 | 1.45 | X-RAY DIFFRACTION | Yes |
| 4IVA | 1.5 | X-RAY DIFFRACTION | Yes |
| 7LL5 | 1.5 | X-RAY DIFFRACTION | Yes |

### AlphaFold Confidence

**Mean pLDDT:** 86.9  
**High confidence fraction (pLDDT > 70):** 89.40%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-O60674-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL2971
**Total IC50 entries:** 19,301
**Median IC50:** 111.1 nM

### Approved Drugs

| Drug | Mechanism |
|---|---|
| RUXOLITINIB PHOSPHATE | Tyrosine-protein kinase JAK2 inhibitor |
| MOMELOTINIB | Tyrosine-protein kinase JAK2 inhibitor |
| BARICITINIB | Tyrosine-protein kinase JAK2 inhibitor |
| FEDRATINIB | Tyrosine-protein kinase JAK2 inhibitor |
| PACRITINIB | Tyrosine-protein kinase JAK2 inhibitor |
| FEDRATINIB HYDROCHLORIDE | Tyrosine-protein kinase JAK2 inhibitor |
| PACRITINIB CITRATE | Tyrosine-protein kinase JAK2 inhibitor |
| FILGOTINIB | Tyrosine-protein kinase JAK2 inhibitor |
| FILGOTINIB MALEATE | Tyrosine-protein kinase JAK2 inhibitor |
| UPADACITINIB HEMIHYDRATE | Tyrosine-protein kinase JAK2 inhibitor |
| DEURUXOLITINIB PHOSPHATE | Tyrosine-protein kinase JAK2 inhibitor |
| MOMELOTINIB DIHYDROCHLORIDE MONOHYDRATE | Tyrosine-protein kinase JAK2 inhibitor |

---

## Literature Evidence

**PubMed title matches:** 3689 (20 most recent retrieved)

### Most Recent Publications

**[2026]** Leptin promotes obesity‑related osteoarthritis progression via CD44/JAK2/STAT3 axis‑mediated chondrocyte apoptosis.  
*Mol Med Rep* — PMID: 42885301  
> Osteoarthritis (OA), especially obesity‑related OA, is a common joint disease in which leptin serves a notable role; however, the specific mechanism by which leptin promotes obesity‑related OA progression remains unclear. In the present study, human cartilage samples confirmed the association betwee...

**[2026]** Polydeoxyribonucleotide Promotes Longitudinal Bone Growth Through the Hepatic JAK2-STAT5/IGF-1 Axis Involving A2A Receptor Signaling.  
*Molecules* — PMID: 42883322  
> Longitudinal bone growth is primarily regulated by the growth hormone (GH)-insulin-like growth factor-1 (IGF-1) axis. However, non-hormonal and orally administered strategies for promoting longitudinal growth remain limited. Here, we investigated the effects and mechanisms of polydeoxyribonucleotide...

**[2026]** LAMB1 accelerates esophageal squamous cell carcinoma by triggering JAK2/STAT3 signaling.  
*Mol Biol Rep* — PMID: 42878970  
> Characterized by a high death rate and negative clinical results, esophageal squamous cell carcinoma (ESCC) is a malignant tumor of the digestive tract. Laminin subunit beta 1 (LAMB1), a principal glycoprotein in the extracellular matrix, contributes to the progression of various malignancies. Howev...

**[2026]** Structure-guided discovery of a dual JAK2/RAGE modulator reveals a computationally driven strategy for targeting convergent oncogenic signaling in renal cell carcinoma.  
*J Comput Aided Mol Des* — PMID: 42878945  
> Renal cell carcinoma (RCC) is driven by convergent inflammatory and proliferative signaling pathways. RAGE-mediated NF-κB activation and JAK2-STAT3 signaling cooperate to amplify cytokine production and oncogenic progression. Targeting these interconnected pathways represents a rational therapeutic ...

**[2026]** Hemin suppresses interferon responses in periodontal cell models through JAK2-STAT1 inhibition.  
*Front Immunol* — PMID: 42876722  
> Hemin, an oxidized heme species released during erythrocyte breakdown, is detectable in gingival crevicular fluid during periodontal inflammation, but its effects on local immune signaling remain unclear. We investigated whether hemin modifies cytokine-induced interferon responses in HSC-2 oral squa...

**[2026]** Relaxin-2 overexpression in hUC-MSCs accelerates tendon-bone integration by activating osteogenic Wnt/β-catenin and angiogenic JAK2/STAT3 cascades.  
*Tissue Cell* — PMID: 42874336  
> Rotator cuff injuries frequently result in poor tendon-bone healing and high retear rates post-surgery, necessitating novel therapeutic strategies. This study investigates whether human umbilical cord mesenchymal stem cells overexpressing Relaxin-2 (hUC-MSCs-Relaxin-2) enhance tendon-bone healing an...

**[2026]** [Tiaoqi electroacupuncture alleviates chronic pain-depression comorbidity via miRNA-124- mediated JAK2/STAT3 signaling pathway].  
*Zhongguo Zhen Jiu* — PMID: 42864290  
> To observe the effects of  Sixty male SD rats were randomly divided into a blank group, a model group, an EA group and an EA+inhibitor group, with 15 rats in each group. Except for the blank group, the CPDC model was established by intraplantar injection of complete Freund's adjuvant in the other gr...

**[2026]** Triptolide enhances oxaliplatin sensitivity by suppressing the JAK2/STAT3 pathway in cancer cells.  
*Bioorg Chem* — PMID: 42854601  
> Liver cancer and lung cancer are major causes of cancer-related deaths worldwide. Oxaliplatin is a first-line chemotherapeutic agent, but its efficacy is often limited by acquired resistance. This study investigated whether triptolide (TPL), a bioactive compound derived from a traditional Chinese me...

**[2026]** Aberrant erythrocyte rigidity in JAK2(V617F) myeloproliferative neoplasms underlies concurrent thrombosis and hemorrhage.  
*Sci Transl Med* — PMID: 42842724  
> Thrombotic events are the leading cause of death in myeloproliferative neoplasms (MPNs) driven by the JAK2 Val

**[2026]** Momelotinib induces hemoglobin improvement and symptom control in PCM1::JAK2-associated myeloid neoplasm.  
*Leuk Res* — PMID: 42837801  

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*