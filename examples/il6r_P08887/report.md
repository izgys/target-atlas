# Target Atlas Report — IL6R (P08887)

**Generated:** 2026-10-18T13:41:10.880427  
**Organism:** Homo sapiens  
**Run ID:** 1691a46c-c4c0-4eea-a7b8-983575c241f4  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `medium`  
**Chemical confidence:** `medium`  
**Literature confidence:** `high`  

IL6R (P08887) is a well-validated, clinically proven drug target with two approved monoclonal antibody therapeutics (tocilizumab and sarilumab) and multiple high-resolution crystal structures, several with ligands bound. While small-molecule chemical matter is essentially absent from ChEMBL (0 IC50 entries), the target is highly druggable at the biologics level with strong structural and literature support.

### Evidence Gaps

- No small-molecule IC50 data in ChEMBL — the target has been exclusively pursued via large biologics (mAbs), so small-molecule druggability remains undemonstrated
- Best resolution (2.4Å) is at the boundary of 'high' structural confidence; no sub-2.5Å structures confirmed with multiple ligand series
- AlphaFold pLDDT of 77.9 with only 67.5% of residues above 70 suggests moderate disorder in portions of the protein (likely flexible extracellular loops or intracellular regions), which may affect small-molecule pocket definition
- No allosteric or orthosteric small-molecule binding pocket characterisation reported in the literature
- Lack of co-crystal structures with small-molecule ligands limits structure-based drug design for non-biologic modalities

### Reasoning Trace

Step 1 — Structural evidence: IL6R has 10 PDB entries with a best resolution of 2.4Å by X-ray diffraction. Eight of ten structures have a ligand bound, which is a strong indicator of a druggable binding site that has been structurally characterised in complex with binding partners. The 2.4Å resolution sits just at the cusp of 'high' confidence; combined with the modest AlphaFold mean pLDDT of 77.9 and only 67.5% of residues above pLDDT 70, there is meaningful structural uncertainty in disordered regions. I rate structural_confidence as 'medium' rather than 'high' because the best resolution is borderline and the AlphaFold data suggests partial disorder.

Step 2 — Chemical evidence: ChEMBL reports 0 IC50 entries, which at face value would suggest 'none' for chemical confidence. However, two approved drugs exist: tocilizumab (a humanised anti-IL6R mAb) and sarilumab (a human anti-IL6R mAb), both validated therapeutics. The ChEMBL schema for this target appears to capture only small-molecule activity; biologic-based approvals are recorded separately. This means there is strong clinical proof of concept for target engagement and therapeutic benefit, but no small-molecule chemical matter has been reported. I rate chemical_confidence as 'medium' — the target is chemically validated at the biologic level (approved drugs exist), but small-molecule tractability is unproven.

Step 3 — Literature evidence: 226 PubMed papers with IL6R in the title, with active 2026 publications spanning mechanistic biology, disease indications (cytokine release syndrome, breast cancer, PCOS, hemorrhoidal disease, viral infection), and novel targeting strategies (dual inhibition, GP130 co-targeting). This reflects a mature, actively researched target with strong disease validation across multiple indications. I rate literature_confidence as 'high'.

Step 4 — Overall druggability: IL6R is a paradigmatic example of a biologically and clinically validated drug target. The approved mAbs confirm that blocking this receptor has clear therapeutic utility in inflammatory and autoimmune disease. The absence of small-molecule data reflects the biology (large protein-protein interaction surface, extracellular cytokine receptor) rather than a lack of druggability per se — it is harder to drug with small molecules, but the target is unambiguously druggable. The overall druggability score is 'high', specifically for biologic modalities; caution is warranted if small-molecule programmes are being considered.

Step 5 — Evidence gaps: The key gaps are (1) absence of small-molecule chemical matter, (2) no characterised small-molecule binding pocket, (3) moderate structural disorder in parts of the protein, and (4) the best crystal structure resolution is borderline.

---

## Structural Evidence

**PDB entries:** 10 (top 10 by resolution detailed below)
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

**PubMed title matches:** 226 (20 most recent retrieved)

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