# Target Atlas Report — IL6R (P08887)

**Generated:** 2026-10-18T13:35:47.747951  
**Organism:** Homo sapiens  
**Run ID:** b084d959-ce9c-44a8-8775-76d1ae239f7e  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `medium`  
**Literature confidence:** `high`  

IL6R (P08887) is a well-validated, clinically proven drug target with two approved biologic therapies (tocilizumab and sarilumab) and multiple high-resolution crystal structures including ligand-bound complexes. The target is highly druggable at the biologic level, though small-molecule chemical data in ChEMBL is absent (IC50 entries = 0), reflecting that current approved therapies are large antibody-based drugs rather than small molecules. Active recent literature confirms ongoing disease relevance across inflammatory and oncological indications.

### Evidence Gaps

- No small-molecule IC50 data in ChEMBL despite 2 approved drugs — approved drugs are biologics (antibodies), not small molecules, limiting small-molecule druggability inference
- Best PDB resolution is 2.4Å (borderline high confidence threshold); no sub-2Å structures reported
- AlphaFold pLDDT mean of 77.9 with only 67.5% high-confidence fraction suggests some structurally disordered or flexible regions not well-captured by experimental structures
- No allosteric or small-molecule binding site characterisation reported, making small-molecule drug discovery more challenging
- Lack of data on co-crystal structures with small-molecule fragments or tool compounds

### Reasoning Trace

Step 1 — Structural Confidence: 10 PDB structures are available, with the best resolution at 2.4Å by X-ray diffraction. This is at the boundary of 'high confidence' (<2.5Å) but qualifies. Critically, 8/10 structures have ligand bound, which strongly supports identification of binding sites and structural basis for inhibition. AlphaFold pLDDT mean of 77.9 is moderate-good, but only 67.5% of residues exceed pLDDT 70, suggesting flexible or intrinsically disordered regions exist. Overall, structural confidence is HIGH given the number of ligand-bound experimental structures.

Step 2 — Chemical Confidence: Despite 2 FDA-approved drugs targeting IL6R, there are 0 ChEMBL IC50 entries. This is not a contradiction — both approved drugs (tocilizumab, sarilumab) are monoclonal antibodies, which are generally not catalogued as IC50 entries in ChEMBL in the same way small molecules are. The presence of approved biologics strongly validates the target clinically, but the absence of small-molecule data means small-molecule druggability remains unproven. Chemical confidence is rated MEDIUM: approved drugs exist (high clinical validation), but no small-molecule chemical matter is documented.

Step 3 — Literature Confidence: 20 recent publications (within recent years, with publications dated 2026) across diverse disease areas including viral infection, cytokine release syndrome, breast cancer, and inflammatory conditions. This indicates active, broad scientific interest and strong disease validation. The titles also suggest mechanistic depth (e.g., m6A methylation regulation, STAT3 signalling, NLRP3 inflammasome). Literature confidence is HIGH.

Step 4 — Overall Druggability: IL6R is a high-confidence target at the biologic/antibody level with proven clinical utility. From a small-molecule perspective, it is less validated. However, the ectodomain-targeting approach validated by antibodies does not preclude small-molecule or peptide-based approaches, and the presence of ligand-bound crystal structures suggests pockets exist. The overall druggability score is HIGH, primarily anchored by approved drugs and strong structural/literature support, while acknowledging the small-molecule gap.

Step 5 — Evidence Gaps: The key gap is the absence of small-molecule chemical biology data. The structural coverage of flexible regions is incomplete. No fragment screening or allosteric site data is mentioned. These gaps are important for anyone pursuing a small-molecule program but do not diminish the target's overall druggability given the biologic precedent.

---

## Structural Evidence

**PDB structures retrieved:** 10
**Best resolution:** 2.4Å (X-RAY DIFFRACTION)
**Ligand-bound structures:** 8/10

### Top Structures by Resolution

| PDB ID | Resolution (Å) | Method | Ligand |
|---|---|---|---|
| 1N26 | 2.4 | X-RAY DIFFRACTION | Yes |
| 5FUC | 2.7 | X-RAY DIFFRACTION | Yes |
| 7DC8 | 2.757 | X-RAY DIFFRACTION | Yes |
| 8QY5 | 3.1 | ELECTRON MICROSCOPY | Yes |
| 8QY6 | 3.16 | ELECTRON MICROSCOPY | Yes |
| 8IOW | 3.2 | ELECTRON MICROSCOPY | Yes |
| 8D82 | 3.22 | ELECTRON MICROSCOPY | Yes |
| 8J6F | 3.3 | ELECTRON MICROSCOPY | Yes |
| 1P9M | 3.65 | X-RAY DIFFRACTION | No |
| 2ARW | N/A | SOLUTION NMR | No |

### AlphaFold Confidence

**Mean pLDDT:** 77.9  
**High confidence fraction (pLDDT > 70):** 67.50%  
**Model URL:** https://alphafold.ebi.ac.uk/files/AF-P08887-F1-model_v6.pdb  

---

## Chemical Evidence

**ChEMBL target ID:** CHEMBL2364155
**Total IC50 entries:** 0

### Approved Drugs

| Drug | Mechanism |
|---|---|
| TOCILIZUMAB | Interleukin-6 receptor alpha subunit inhibitor |
| SARILUMAB | Interleukin-6 receptor alpha subunit antagonist |

---

## Literature Evidence

**Recent publications retrieved:** 20

### Most Recent Publications

**[2026]** From IL-6 production to IL-6R buffering: a unified IL-6-IL-6R framework for immune homeostasis during viral infection.  
*Front Immunol* — PMID: 42840991  
> Interleukin-6 (IL-6) is a pleiotropic cytokine that coordinates innate and adaptive immunity and maintains tissue homeostasis during infection and inflammation. Although transient IL-6 production is essential for host defense, dysregulated or sustained IL-6 activity contributes to immunopathology ac...

**[2026]** Dual Inhibition of TNF-α and IL-6R mitigates cytokine release syndrome via protection of endothelial integrity and reduction of organ damage in mouse models.  
*Front Immunol* — PMID: 42500657  
> Cytokine Release Syndrome (CRS) is a life-threatening complication of T-cell-engaging immunotherapies, causing vascular leakage and multi-organ dysfunction. Standard Interleukin-6 (IL-6) blockade often fails in severe cases by leaving the upstream initiator, Tumor Necrosis Factor-α (TNF-α), unchecke...

**[2026]** Humanized Antibodies Targeting Ectodomains of IL-6R and GP130 Suppress IL-6/STAT3 Signalling and Tumour Growth in Breast Cancer Models.  
*J Cell Mol Med* — PMID: 42316398  
> Interleukin-6 (IL-6) signalling is a key driver of breast cancer progression, activating pro-survival, pro-inflammatory and metastatic programs through its receptors, IL-6R and GP130. Elevated IL-6 levels correlate with poor prognosis in breast cancer patients and persistent IL-6/STAT3 activation pr...

**[2026]** Smad2/3 Regulates IL-6R m6A Methylation through METTL3 to Influence Inflammatory Responses in Hemorrhoidal Disease.  
*J Innate Immun* — PMID: 42166383  
> This study investigates METTL3's function and mechanisms in hemorrhoidal disease-related inflammation. A rat model of hemorrhoidal disease was induced in vivo using croton oil. Human monocytic leukemia cells THP-1 were induced into macrophages using phorbol myristate acetate, and then lipopolysaccha...

**[2026]** Astragaloside IV alleviates chronic low-grade inflammation in polycystic ovary syndrome by acting on IL-6R and inhibiting the NLRP3 inflammasome.  
*Sci Rep* — PMID: 41998069  
> PCOS is a common endocrine and metabolic disorder. Chronic low-grade inflammation plays a significant role in its pathogenesis, although the precise underlying mechanisms remain incompletely understood. AS-IV, the main active constituent of Astragalus membranaceus, exhibits various pharmacological a...

**[2026]** Danthron as a novel IL-6R agonist promotes thrombopoiesis via the SRC/RAS/MAPK pathway.  
*Front Immunol* — PMID: 41972146  
> This study aimed to investigate the effects of danthron on promoting megakaryocyte (MK) differentiation and alleviating thrombocytopenia, as well as to elucidate its underlying mechanisms. Cell proliferation and apoptosis of Meg-01 and K562 cells were evaluated by CCK-8, LDH release, and apoptosis a...

**[2026]** Age-stratified treatment response in rheumatoid arthritis: a systematic review, meta-analysis, and integrated genetic and single-cell evidence implicating IL6R/TYK2 signaling.  
*Clin Rheumatol* — PMID: 41845003  
> Late-onset rheumatoid arthritis (LORA, onset ≥ 60 years, a threshold commonly adopted based on accelerated immunosenescence at this age) represents a growing clinical challenge as population's age, yet therapeutic outcomes in this subgroup remain inadequately characterized. Whether age-related immun...

**[2026]** Immunogenetic Interplay of IL-6 and IL-6R Genes Variants and Circulating IL-6 Levels in ‎Toxoplasma gondii-infected Women with Recurrent Pregnancy Loss.  
*Iran J Immunol* — PMID: 41804796  
> Recurrent pregnancy loss (RPL) is a global health challenge in women. It has been reported that Toxoplasma gondii (T. gondii) infection and interleukin-6 (IL-6) bioavailability contribute to RPL. This study investigated IL-6 and IL-6 receptor (IL-6R) gene polymorphisms and blood IL-6 levels in T. go...

**[2026]** The role of monoclonal antibodies against IL-6 or IL-6R in the treatment of thyroid eye disease.  
*Rev Endocr Metab Disord* — PMID: 41697457  
> Thyroid eye disease (TED) is a chronic inflammatory autoimmune disorder characterized by expansion and fibrosis of orbital tissues, leading to eyelid retraction, proptosis, periorbital edema, restricted ocular motility, corneal ulceration, and (rarely) compressive optic neuropathy. The relationship ...

**[2026]** Place of anti-IL6R in the therapeutic strategy in NMOSD-AQP4+, MOGAD, and NMOSD double-seronegative patients.  
*Mult Scler* — PMID: 41404646  
> Anti-interleukin-6 receptor (anti-IL6R) therapy has demonstrated efficacy in AQP4 + NMOSD, and emerging evidence suggests a similar benefit in patients with MOGAD. This study aimed to evaluate the role of anti-IL6R therapy within the treatment algorithm for both NMOSD and MOGAD. In addition, it inve...

---

## Pipeline Metadata

*All agents completed successfully — no data gaps.*

---

*Generated by Target Atlas v0.1 — automated protein target analysis for drug discovery.*