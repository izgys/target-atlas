import json
from datetime import datetime
from pathlib import Path

from target_atlas.state import TargetAtlasState, retrieval_failed


def report_generator(state: TargetAtlasState) -> dict:
    """
    Final node in the Target Atlas graph.

    Renders the fully populated state into two output files:
    - report.md  — structured markdown report for human review
    - summary.json — machine-readable summary for downstream pipelines

    Reads from state:
        all fields

    Writes to state:
        nothing — terminal node, side effects only (file output)

    Args:
        state: fully populated TargetAtlasState

    Returns:
        empty dict — no state updates needed from terminal node
    """
    gene_name = state.get("gene_name", "unknown")
    uniprot_id = state.get("uniprot_id", "unknown")

    # Create output directory
    output_dir = Path(state.get("output_dir", "results")) / f"{gene_name}_{uniprot_id}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate both outputs
    report_md = _build_report(state)
    summary = _build_summary(state)

    # Write files
    report_path = output_dir / "report.md"
    summary_path = output_dir / "summary.json"

    report_path.write_text(report_md, encoding="utf-8")
    summary_path.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    return {}


def _build_report(state: TargetAtlasState) -> str:
    """
    Build the full markdown report from state.
    """
    lines = []
    gene_name = state.get("gene_name", "unknown")
    uniprot_id = state.get("uniprot_id", "unknown")
    assessment = state.get("druggability_assessment")
    timestamp = state.get("timestamp", datetime.utcnow().isoformat())

    # Header
    lines.append(f"# Target Atlas Report — {gene_name} ({uniprot_id})")
    lines.append("")
    lines.append(f"**Generated:** {timestamp}  ")
    lines.append(f"**Organism:** {state.get('organism', 'unknown')}  ")
    lines.append(f"**Run ID:** {state.get('run_id', 'unknown')}  ")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Assessment summary
    if assessment:
        lines.append("## Druggability Assessment")
        lines.append("")
        lines.append(f"**Overall score:** `{assessment.druggability_score}`  ")
        lines.append(f"**Structural confidence:** `{assessment.structural_confidence}`  ")
        lines.append(f"**Chemical confidence:** `{assessment.chemical_confidence}`  ")
        lines.append(f"**Literature confidence:** `{assessment.literature_confidence}`  ")
        lines.append("")
        lines.append(f"{assessment.summary}")
        lines.append("")

        if assessment.evidence_gaps:
            lines.append("### Evidence Gaps")
            lines.append("")
            for gap in assessment.evidence_gaps:
                lines.append(f"- {gap}")
            lines.append("")

        if assessment.reasoning_trace:
            lines.append("### Reasoning Trace")
            lines.append("")
            lines.append(assessment.reasoning_trace)
            lines.append("")
    else:
        lines.append("## Druggability Assessment")
        lines.append("")
        lines.append("*Assessment unavailable — reasoning agent failed.*")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Structural evidence
    lines.append("## Structural Evidence")
    lines.append("")
    pdb_structures = state.get("pdb_structures", [])
    if pdb_structures:
        lines.append(
            f"**PDB entries:** {state.get('pdb_total_count', len(pdb_structures))} "
            f"(top {len(pdb_structures)} by resolution detailed below)"
        )
        best = pdb_structures[0]
        lines.append(f"**Best resolution:** {best.resolution}Å ({best.method})")
        ligand_count = sum(1 for s in pdb_structures if s.has_ligand)
        lines.append(f"**Ligand-bound structures:** {ligand_count}/{len(pdb_structures)}")
        lines.append("")
        lines.append("### Top Structures by Resolution")
        lines.append("")
        lines.append("| PDB ID | Resolution (Å) | Method | Ligand |")
        lines.append("|---|---|---|---|")
        for s in pdb_structures[:10]:
            res = f"{s.resolution}" if s.resolution else "N/A"
            ligand = "Yes" if s.has_ligand else "No"
            lines.append(f"| {s.pdb_id} | {res} | {s.method} | {ligand} |")
        lines.append("")
    else:
        lines.append(
            "*Retrieval failed — PDB structures could not be fetched, so absence is not established (see Pipeline Metadata).*"
            if retrieval_failed(state, "pdb") else "*No experimental PDB structures found.*"
        )
        lines.append("")

    af = state.get("alphafold_result")
    if af:
        lines.append("### AlphaFold Confidence")
        lines.append("")
        lines.append(f"**Mean pLDDT:** {af.mean_plddt:.1f}  ")
        lines.append(
            f"**High confidence fraction (pLDDT > 70):** "
            f"{af.high_confidence_fraction:.2%}  "
        )
        if af.model_url:
            lines.append(f"**Model URL:** {af.model_url}  ")
        lines.append("")
    else:
        lines.append(
            "*Retrieval failed — the AlphaFold prediction could not be fetched, so absence is not established (see Pipeline Metadata).*"
            if retrieval_failed(state, "alphafold") else "*AlphaFold prediction not available.*"
        )
        lines.append("")

    lines.append("---")
    lines.append("")

    # Chemical evidence
    lines.append("## Chemical Evidence")
    lines.append("")
    bs = state.get("bioactivity_summary")
    if bs:
        lines.append(f"**ChEMBL target ID:** {bs.chembl_target_id}")
        lines.append(f"**Total IC50 entries:** {bs.total_entries:,}")
        if bs.median_ic50_nm:
            lines.append(f"**Median IC50:** {bs.median_ic50_nm:.1f} nM")
        lines.append("")
    else:
        lines.append(
            "*Retrieval failed — ChEMBL bioactivity data could not be fetched, so absence is not established (see Pipeline Metadata).*"
            if retrieval_failed(state, "chembl")
            else "*Target not found in ChEMBL — no bioactivity data available.*"
        )
        lines.append("")

    inhibitors = state.get("known_inhibitors", [])
    if inhibitors:
        lines.append("### Approved Drugs")
        lines.append("")
        lines.append("| Drug | Mechanism |")
        lines.append("|---|---|")
        for drug in inhibitors:
            name = drug.name or drug.chembl_id
            mechanism = drug.mechanism or "unknown"
            lines.append(f"| {name} | {mechanism} |")
        lines.append("")
    else:
        lines.append(
            "*Retrieval failed — approved drugs could not be fetched, so absence is not established (see Pipeline Metadata).*"
            if retrieval_failed(state, "chembl_drugs") else "*No approved drugs found for this target.*"
        )
        lines.append("")

    lines.append("---")
    lines.append("")

    # Literature evidence
    lines.append("## Literature Evidence")
    lines.append("")
    pubs = state.get("recent_publications", [])
    if pubs:
        lines.append(
            f"**PubMed title matches:** {state.get('publication_total_count', len(pubs))} "
            f"({len(pubs)} most recent retrieved)"
        )
        lines.append("")
        lines.append("### Most Recent Publications")
        lines.append("")
        for pub in pubs[:10]:
            lines.append(f"**[{pub.year}]** {pub.title}  ")
            lines.append(f"*{pub.journal}* — PMID: {pub.pubmed_id}  ")
            if pub.abstract:
                # Truncate abstract to first 300 chars
                abstract_preview = pub.abstract[:300]
                if len(pub.abstract) > 300:
                    abstract_preview += "..."
                lines.append(f"> {abstract_preview}")
            lines.append("")
    else:
        lines.append(
            "*Retrieval failed — publications could not be fetched, so absence is not established (see Pipeline Metadata).*"
            if retrieval_failed(state, "pubmed") else "*No recent publications found.*"
        )
        lines.append("")

    lines.append("---")
    lines.append("")

    # Pipeline metadata
    lines.append("## Pipeline Metadata")
    lines.append("")
    agent_errors = state.get("agent_errors", {})
    if agent_errors:
        lines.append("### Data Gaps and Errors")
        lines.append("")
        for agent, error in agent_errors.items():
            lines.append(f"- **{agent}:** {error}")
        lines.append("")
    else:
        lines.append("*All agents completed successfully — no data gaps.*")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "*Generated by Target Atlas v0.1 — "
        "automated protein target analysis for drug discovery.*"
    )

    return "\n".join(lines)


def _build_summary(state: TargetAtlasState) -> dict:
    """
    Build a machine-readable JSON summary from state.
    Suitable for downstream pipeline consumption.
    """
    assessment = state.get("druggability_assessment")
    bs = state.get("bioactivity_summary")
    af = state.get("alphafold_result")
    pdb_structures = state.get("pdb_structures", [])
    inhibitors = state.get("known_inhibitors", [])
    pubs = state.get("recent_publications", [])

    return {
        "target": {
            "uniprot_id": state.get("uniprot_id"),
            "gene_name": state.get("gene_name"),
            "organism": state.get("organism"),
        },
        "run_metadata": {
            "run_id": state.get("run_id"),
            "timestamp": state.get("timestamp"),
        },
        "assessment": {
            "druggability_score": assessment.druggability_score if assessment else None,
            "structural_confidence": assessment.structural_confidence if assessment else None,
            "chemical_confidence": assessment.chemical_confidence if assessment else None,
            "literature_confidence": assessment.literature_confidence if assessment else None,
            "summary": assessment.summary if assessment else None,
            "evidence_gaps": assessment.evidence_gaps if assessment else [],
        },
        "structural_data": {
            "pdb_structure_count": len(pdb_structures),
            "pdb_total_count": state.get("pdb_total_count", len(pdb_structures)),
            "best_resolution_angstrom": pdb_structures[0].resolution if pdb_structures else None,
            "ligand_bound_count": sum(1 for s in pdb_structures if s.has_ligand),
            "alphafold_mean_plddt": af.mean_plddt if af else None,
            "alphafold_high_confidence_fraction": af.high_confidence_fraction if af else None,
            "pdb_ids": [s.pdb_id for s in pdb_structures],
        },
        "chemical_data": {
            "chembl_target_id": bs.chembl_target_id if bs else None,
            "total_ic50_entries": bs.total_entries if bs else 0,
            "median_ic50_nm": bs.median_ic50_nm if bs else None,
            "approved_drug_count": len(inhibitors),
            "approved_drugs": [d.name or d.chembl_id for d in inhibitors],
        },
        "literature_data": {
            "recent_publication_count": len(pubs),
            "publication_total_count": state.get("publication_total_count", len(pubs)),
            "most_recent_year": pubs[0].year if pubs else None,
            "pmids": [p.pubmed_id for p in pubs],
        },
        "data_gaps": state.get("agent_errors", {}),
    }