# Target Atlas Report — EGFR (P00533)

**Generated:** 2026-05-24T20:52:34.927105  
**Organism:** Homo sapiens  
**Run ID:** b606607c-4755-43bc-a938-64ca311beb2e  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `high`  
**Literature confidence:** `high`  

EGFR (P00533) is one of the most extensively drugged targets in oncology, with numerous approved small-molecule inhibitors (e.g., erlotinib, gefitinib, osimertinib) and therapeutic antibodies (e.g., cetuximab, panitumumab) in clinical use. The structural evidence is exceptional, with 20 PDB structures including a 1.07 Å resolution crystal structure and 19 ligand-bound complexes. The ChEMBL 'not found' result is a clear data pipeline error (timeout), not a genuine absence of chemical matter — EGFR has thousands of documented inhibitors in ChEMBL and beyond.

### Evidence Gaps

- ChEMBL data retrieval failed due to a read timeout — this is a pipeline artifact, not a true data gap; EGFR is extensively represented in ChEMBL with >10,000 bioactivity entries
- AlphaFold pLDDT (75.9 mean, 70.7% high-confidence fraction) is moderate, but this is superseded by the wealth of experimental PDB structures
- No approved drugs listed in the pipeline output — again a pipeline/data retrieval artifact, not reflective of the actual clinical landscape

### Reasoning Trace

Step 1 — Structural evidence: 20 PDB structures retrieved, best resolution 1.07 Å by X-ray diffraction. This is an exceptionally high-resolution dataset. 19/20 structures are ligand-bound, directly demonstrating a well-defined, druggable binding pocket (the ATP-binding site of the kinase domain). AlphaFold pLDDT of 75.9 is moderate but irrelevant given the abundance of experimental structures. Structural confidence = HIGH.

Step 2 — Chemical evidence: The pipeline reports 'TARGET NOT IN DATABASE' for ChEMBL and 'NONE' for approved drugs. However, the pipeline also explicitly notes 'ChEMBL fetch failed: The read operation timed out.' This is unambiguously a data retrieval failure, not a true absence of chemical matter. From established knowledge, EGFR (ChEMBL ID: CHEMBL203) has thousands of bioactivity entries and is one of the most chemically characterised kinases in existence. Approved drugs include first-generation TKIs (erlotinib, gefitinib), second-generation (afatinib, dacomitinib), third-generation (osimertinib), and monoclonal antibodies (cetuximab, panitumumab, amivantamab). Chemical confidence = HIGH (overriding the pipeline artifact).

Step 3 — Literature evidence: 20 recent publications retrieved (2026 dates), covering HCC, lung cancer, OSCC, neuro-immune signalling, and clinical trial regimens (amivantamab). Titles reference EGFR-TKIs and EGFR-mutated NSCLC directly, confirming active clinical and translational research. The broader literature base for EGFR numbers in the tens of thousands of publications. Literature confidence = HIGH.

Step 4 — Druggability assessment: EGFR possesses a well-characterised ATP-binding pocket with multiple co-crystal structures of approved drugs. There are allosteric sites (e.g., the C-helix/DFG region targeted by second-generation inhibitors) and extracellular domains targeted by biologics. Resistance mechanisms are well studied (T790M, C797S, exon 20 insertions), and next-generation inhibitors continue to be developed. Druggability score = HIGH.

Step 5 — Caveats: The only genuine uncertainty is that the pipeline data is partially corrupted (ChEMBL timeout, missing approved drug list). This does not affect the assessment because independent domain knowledge firmly establishes EGFR as a premier drugged target. No meaningful evidence gaps exist for this target beyond the pipeline artifact.

---

## Structural Evidence

**PDB structures retrieved:** 20
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

*Target not found in ChEMBL — no bioactivity data available.*

*No approved drugs found for this target.*

---

## Literature Evidence

**Recent publications retrieved:** 20

### Most Recent Publications

**[2026]** PSMC2 promotes hepatocellular carcinoma progression through interaction with EGFR.  
*Clin Exp Med* — PMID: 42177695  
> Growing evidence highlights the critical involvement of the ubiquitin-proteasome system in cancer development. As an essential component of the 26 S proteasome, Proteasome 26 S Subunit ATPase 2 (PSMC2) has been implicated in various malignancies, but its role in hepatocellular carcinoma (HCC) progre...

**[2026]** Machine Learning Models for Predicting Mortality Risk and Survival Time in Lung Cancer Patients Treated with EGFR-TKIs.  
*Stud Health Technol Inform* — PMID: 42174863  
> This study develops machine learning models to predict patient mortality and estimate survival time using electronic health record (EHR) data from three Taipei Medical University-affiliated hospitals (TMU Hospital, Wan-Fang Hospital, and Shuang Ho Hospital). We built and evaluated predictive models ...

**[2026]** HMGA2 Overexpression Is Associated with Poor Prognosis and EGFR Signaling Activation in Oral Squamous Cell Carcinoma.  
*Asian Pac J Cancer Prev* — PMID: 42169592  
> To evaluate the clinical significance of HMGA2 expression and its association with oncogenic signaling pathways in oral squamous cell carcinoma (OSCC). RNA-seq data and clinical information of OSCC patients (n=253) and normal oral tissues (n=27) were obtained from The Cancer Genome Atlas (TCGA). HMG...

**[2026]** The Epidermal Growth Factor Receptor (EGFR) as a means of neuro-immune cross-conversation.  
*J Neuroinflammation* — PMID: 42169107  
> The nervous and the immune system coevolved, and the crosstalk between both is critical for the maintenance of tissue homeostasis and mental health. In recent years, several examples have been revealed that the immune system influences behaviour, emotions, pain and even such fundamental needs as hun...

**[2026]** Development of the Weight-Tiered Q3W Regimen of Amivantamab in Combination With Carboplatin-Pemetrexed in EGFR-Mutated Non-Small Cell Lung Cancer.  
*CPT Pharmacometrics Syst Pharmacol* — PMID: 42166539  
> Amivantamab, a bispecific antibody targeting epidermal growth factor and mesenchymal-epithelial transition receptors, was initially approved under accelerated approval as a monotherapy for second-line treatment of non-small cell lung cancer (NSCLC) with exon 20 insertion mutations. Subsequently, ami...

**[2026]** Exploring the significance of EGFR, MMP-2, MMP-9, HIF-1α, and CAIX as molecular biomarkers in ocular surface squamous neoplasia.  
*Indian J Med Res* — PMID: 42165725  
> Background and objectives Ocular surface squamous neoplasia (OSSN) encompasses a spectrum of tumours, including conjunctival squamous intraepithelial neoplasia (CSIN), carcinoma in situ (CIS), and invasive squamous cell carcinoma (iSCC). The roles of biomarkers such as epidermal growth factor recept...

**[2026]** Erratum: [Corrigendum] EGFR and ERK activation resists flavonoid quercetin-induced anticancer activities in human cervical cancer cells in vitro.  
*Oncol Lett* — PMID: 42164466  
> [This corrects the article DOI: 10.3892/ol.2021.13015.].

**[2026]** New phenylcyclopropane-carbohydrazide furan derivatives with potent anticancer activity and EGFR inhibitory potential.  
*RSC Adv* — PMID: 42164298  
> Fifteen new phenylcyclopropane-carbohydrazide-containing furan derivatives are synthesised and thoroughly characterized using FT-IR,

**[2026]** Activation of the Hippo Pathway by ATN Suppresses Cancer Stem-Like Properties and EGFR-Associated Signaling in Castration-Resistant Prostate Cancer Cells in vitro.  
*Int J Med Sci* — PMID: 42158813  
> Castration-resistant prostate cancer (CRPC) represents a lethal stage of prostate cancer for which effective therapeutic options remain limited. Aberrant activation of the Hippo pathway effector Yes-associated protein (YAP) and its crosstalk with epidermal growth factor receptor (EGFR) signaling hav...

**[2026]** A Durable Response to Low-Dose Afatinib After Progression on Osimertinib in Advanced Epidermal Growth Factor Receptor (EGFR) L861Q-Mutated Lung Adenocarcinoma: A Case Report.  
*Cureus* — PMID: 42158804  
> Although both afatinib and osimertinib have demonstrated clinical activity in treatment-naive non-small cell lung cancer (NSCLC) harboring uncommon epidermal growth factor receptor (EGFR) mutations, the efficacy and safety of afatinib after progression on osimertinib remain unclear. A 68-year-old ma...

---

## Pipeline Metadata

### Data Gaps and Errors

- **literature_agent_chembl:** ChEMBL fetch failed: The read operation timed out

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*