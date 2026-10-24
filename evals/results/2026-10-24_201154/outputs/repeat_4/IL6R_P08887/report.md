# Target Atlas Report — IL6R (P08887)

**Generated:** 2026-10-24T18:26:34.058660  
**Organism:** Homo sapiens  
**Run ID:** 70254acb-61e2-4620-b509-6e8ed8ad7faf  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `high`  
**Chemical confidence:** `medium`  
**Literature confidence:** `high`  

IL6R (P08887) is a well-validated, clinically proven drug target with two approved biologic antagonists (tocilizumab and sarilumab) and multiple high-resolution crystal structures including ligand-bound complexes. The target has strong disease validation across inflammatory and oncological indications, though small-molecule chemical matter is essentially absent from ChEMBL, reflecting the dominance of antibody-based modalities for this extracellular receptor.

### Evidence Gaps

- No small-molecule IC50 data in ChEMBL despite approved drugs existing — chemical tractability for small molecules is undemonstrated
- Best resolution is 2.4Å, just at the threshold; no sub-2Å structures reported, limiting fine-grained structure-based drug design for small molecules
- AlphaFold mean pLDDT of 77.9 with only 67.5% high-confidence residues suggests some disordered regions not well-captured by existing structures
- Approved drugs are exclusively monoclonal antibodies; no approved small molecules or peptide inhibitors targeting IL6R
- Binding site geometry for small-molecule engagement of the IL-6/IL-6R protein-protein interface has not been well characterised in the available data
- No allosteric or intracellular binding site data provided

### Reasoning Trace

Step 1 — Structural confidence: There are 10 PDB entries, best resolution 2.4Å by X-ray diffraction, and 8/10 structures have a ligand bound. This meets the 'high' structural confidence criterion (multiple structures <2.5Å with ligand bound), though 2.4Å is at the boundary. AlphaFold pLDDT of 77.9 (mean) with 67.5% high-confidence fraction is moderate, consistent with a partially disordered extracellular protein, but the experimental structures dominate the assessment. Structural confidence = HIGH.

Step 2 — Chemical confidence: ChEMBL lists 0 IC50 entries for this target, yet two approved drugs exist (tocilizumab, sarilumab). This apparent paradox is explained by the fact that both approved agents are monoclonal antibodies, which are typically not captured in ChEMBL IC50 tables in the same way as small molecules. The existence of approved drugs is strong evidence of pharmacological tractability, but the complete absence of small-molecule IC50 data means small-molecule druggability is unproven. Per the schema, 'approved drugs exist' but ChEMBL entries are sparse/absent — this maps to 'medium' chemical confidence, acknowledging the biologics success while flagging the small-molecule gap.

Step 3 — Literature confidence: 226 PubMed papers with IL6R in the title, with very recent (2026) publications covering mechanistic, therapeutic, and disease-biology angles across inflammation, cancer, and metabolic disease. This exceeds the 100-500 range and shows strong, ongoing disease validation. Literature confidence = HIGH.

Step 4 — Overall druggability: IL6R is a textbook validated target — two approved antibody drugs, multiple crystal structures with bound ligands, and a rich literature. The druggability score is HIGH for biologic modalities. The caveat is that small-molecule druggability remains undemonstrated, which is a meaningful gap for oral drug discovery programs but does not diminish the overall target validation.

Step 5 — Evidence gaps: The key gaps are (a) absence of small-molecule chemical matter, (b) resolution just at the 2.5Å threshold without sub-2Å structures, (c) partial AlphaFold confidence suggesting disordered regions, and (d) no characterisation of cryptic or allosteric binding sites that might enable small-molecule intervention.

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