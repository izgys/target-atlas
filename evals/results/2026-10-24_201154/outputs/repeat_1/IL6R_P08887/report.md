# Target Atlas Report — IL6R (P08887)

**Generated:** 2026-10-24T18:14:48.902441  
**Organism:** Homo sapiens  
**Run ID:** c38616bf-6fae-4a34-a368-a789304e9a36  

---

## Druggability Assessment

**Overall score:** `high`  
**Structural confidence:** `medium`  
**Chemical confidence:** `medium`  
**Literature confidence:** `high`  

IL6R (P08887) is a well-validated, clinically proven drug target with two approved biologic antagonists (tocilizumab and sarilumab). Structural coverage is solid with 10 PDB entries including 8 ligand-bound structures at near-high resolution (best 2.4Å), and the literature base is substantial and actively growing. The primary evidence gap is the complete absence of small-molecule IC50 data in ChEMBL, reflecting that current approved therapies are monoclonal antibodies targeting the extracellular domain rather than small molecules.

### Evidence Gaps

- No small-molecule IC50 data in ChEMBL (0 entries) — all approved drugs are biologics (mAbs), indicating the small-molecule druggability of IL6R remains largely unexplored
- Best PDB resolution is 2.4Å, just at the threshold for high confidence; no sub-2Å structures available
- AlphaFold mean pLDDT of 77.9 with only 67.5% high-confidence fraction suggests some disordered regions, likely in intracellular or linker domains, which may limit structure-based small-molecule design
- No information on allosteric binding sites or cryptic pockets that could enable small-molecule intervention beyond the cytokine-binding interface
- Oral bioavailability and small-molecule tractability of the IL-6/IL-6R protein-protein interaction interface has not been demonstrated

### Reasoning Trace

Step 1 — Target identity and biological context: IL6R (P08887) encodes the IL-6 receptor alpha subunit, a key component of the IL-6 signalling axis. It is a well-established therapeutic target in autoimmune and inflammatory diseases (rheumatoid arthritis, cytokine release syndrome, etc.).

Step 2 — Structural confidence assessment: There are 10 PDB entries, with the best resolution at 2.4Å by X-ray diffraction. Eight of ten structures are ligand-bound, which is excellent for understanding binding modes. However, 2.4Å is just at the boundary of 'high' structural confidence (threshold <2.5Å), and the AlphaFold pLDDT of 77.9 (mean) with 67.5% high-confidence fraction indicates moderate overall structural confidence — some regions (likely intracellular or flexible loops) are disordered. Overall: medium-to-high structural confidence, assigned 'medium' due to the borderline resolution and partial disorder.

Step 3 — Chemical confidence assessment: ChEMBL reports 0 IC50 entries for this target, which is striking. However, two approved drugs exist: tocilizumab and sarilumab, both monoclonal antibodies. The absence of IC50 data reflects that the approved modalities are biologics, not small molecules. ChEMBL IC50 entries typically capture small-molecule assay data. The existence of approved drugs elevates confidence, but the lack of small-molecule data means chemical tractability for oral drugs is unproven. Assigned 'medium' because approved drugs exist but small-molecule data is absent.

Step 4 — Literature confidence assessment: 226 PubMed papers with IL6R in the title, with very recent publications in 2026 covering diverse angles (viral infection, cytokine release syndrome, cancer, inflammatory diseases, epigenetic regulation). This is an active, well-studied target with strong disease validation across multiple indications. Assigned 'high'.

Step 5 — Druggability score: IL6R is clinically validated at the highest level (approved drugs). The target is biologically and medically important, structurally characterised, and actively researched. The main caveat is that current drugs are biologics, and small-molecule druggability of the extracellular cytokine-binding interface (a protein-protein interaction) is inherently challenging. Nevertheless, the overall druggability score is 'high' because the target is proven to be pharmacologically modifiable and disease-relevant, even if small-molecule approaches remain underdeveloped.

Step 6 — Evidence gaps: The most significant gap is the complete absence of small-molecule bioactivity data, which means any small-molecule drug discovery programme would be starting from scratch in terms of chemical matter. Additionally, the PPI interface targeted by mAbs is notoriously difficult for small molecules. Structural disorder in parts of the protein and lack of sub-2Å crystal structures are secondary gaps.

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