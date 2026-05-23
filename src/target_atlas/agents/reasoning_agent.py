import json
import anthropic

from target_atlas.state import TargetAtlasState, DruggabilityAssessment
from dotenv import load_dotenv
load_dotenv()

# Model to use for reasoning — claude-sonnet is the right balance
# of capability and cost for this synthesis task
MODEL = "claude-sonnet-4-6"


def reasoning_agent(state: TargetAtlasState) -> dict:
    """
    Fourth node in the Target Atlas graph.

    Synthesises structural, bioactivity, and literature evidence
    into a calibrated druggability assessment using Claude.

    Reads from state:
        uniprot_id, gene_name, organism,
        pdb_structures, alphafold_result,
        known_inhibitors, bioactivity_summary,
        recent_publications, agent_errors

    Writes to state:
        druggability_assessment, agent_errors (partial)

    Failure behaviour:
        If Claude returns malformed JSON, attempts to extract
        partial assessment. If extraction fails entirely, writes
        error to agent_errors and returns None assessment.

    Args:
        state: TargetAtlasState with all data fields populated

    Returns:
        partial state update dict
    """
    errors = dict(state.get("agent_errors", {}))

    # Build structured context from state
    context = _build_context(state)

    try:
        client = anthropic.Anthropic()
        response = client.messages.create(
            model=MODEL,
            max_tokens=2000,
            system=_system_prompt(),
            messages=[
                {"role": "user", "content": context}
            ]
        )

        raw_text = response.content[0].text
        assessment = _parse_assessment(raw_text)

        return {
            "druggability_assessment": assessment,
            "agent_errors": errors,
        }

    except Exception as e:
        errors["reasoning_agent"] = f"Reasoning failed: {str(e)}"
        return {
            "druggability_assessment": None,
            "agent_errors": errors,
        }


def _system_prompt() -> str:
    """
    System prompt for the reasoning agent.

    Instructs Claude to reason step by step, acknowledge uncertainty
    explicitly, and return a structured JSON assessment.
    """
    return """You are a drug discovery scientist specialising in target assessment.
You will be given evidence about a protein target from multiple sources.
Your task is to synthesise this evidence into a calibrated druggability assessment.

CRITICAL RULES:
1. Reason step by step before producing your assessment
2. Explicitly enumerate what is unknown or missing — do not ignore evidence gaps
3. Never overstate confidence — if data is sparse, say so
4. Distinguish between structural order (pLDDT) and druggability — they are not the same
5. Return ONLY valid JSON matching the schema below — no preamble, no markdown fences

OUTPUT SCHEMA:
{
    "summary": "2-3 sentence plain language assessment",
    "druggability_score": "high|medium|low|unknown",
    "structural_confidence": "high|medium|low|none",
    "chemical_confidence": "high|medium|low|none",
    "literature_confidence": "high|medium|low|none",
    "evidence_gaps": ["gap 1", "gap 2", ...],
    "reasoning_trace": "your full step-by-step reasoning here"
}

CONFIDENCE DEFINITIONS:
structural_confidence:
    high   = multiple high-resolution PDB structures (<2.5Å) with ligand bound
    medium = few structures OR only AlphaFold with high pLDDT (>70%)
    low    = only AlphaFold with low pLDDT OR very low resolution structures
    none   = no structural data available

chemical_confidence:
    high   = >1000 ChEMBL IC50 entries AND approved drugs exist
    medium = ChEMBL entries exist but sparse (<1000) OR no approved drugs
    low    = very few ChEMBL entries (<100)
    none   = no ChEMBL entry for this target

literature_confidence:
    high   = >500 publications, recent activity, strong disease validation
    medium = 100-500 publications OR disease link is hypothesis-level
    low    = <100 publications OR no clear disease association
    none   = no publications found
"""


def _build_context(state: TargetAtlasState) -> str:
    """
    Build a structured text context from state for the reasoning agent.

    Formats all available evidence clearly, explicitly flagging
    missing data sources so Claude can enumerate evidence gaps.
    """
    lines = []

    # Target identity
    lines.append(f"TARGET: {state['gene_name']} ({state['uniprot_id']})")
    lines.append(f"ORGANISM: {state['organism']}")
    lines.append("")

    # Structural evidence
    lines.append("=== STRUCTURAL EVIDENCE ===")
    pdb_structures = state.get("pdb_structures", [])
    if pdb_structures:
        lines.append(f"PDB structures: {len(pdb_structures)} retrieved")
        best = pdb_structures[0]
        lines.append(f"Best resolution: {best.resolution}Å ({best.method})")
        ligand_count = sum(1 for s in pdb_structures if s.has_ligand)
        lines.append(f"Structures with ligand bound: {ligand_count}/{len(pdb_structures)}")
    else:
        lines.append("PDB structures: NONE AVAILABLE")

    af = state.get("alphafold_result")
    if af:
        lines.append(f"AlphaFold mean pLDDT: {af.mean_plddt:.1f}")
        lines.append(f"High confidence fraction (pLDDT>70): {af.high_confidence_fraction:.2%}")
    else:
        lines.append("AlphaFold: NOT AVAILABLE")
    lines.append("")

    # Chemical evidence
    lines.append("=== CHEMICAL EVIDENCE ===")
    bs = state.get("bioactivity_summary")
    if bs:
        lines.append(f"ChEMBL target ID: {bs.chembl_target_id}")
        lines.append(f"Total IC50 entries: {bs.total_entries}")
        if bs.median_ic50_nm:
            lines.append(f"Median IC50: {bs.median_ic50_nm:.1f} nM")
    else:
        lines.append("ChEMBL: TARGET NOT IN DATABASE")

    inhibitors = state.get("known_inhibitors", [])
    if inhibitors:
        lines.append(f"Approved drugs: {len(inhibitors)}")
        for drug in inhibitors[:5]:
            lines.append(f"  - {drug.name} ({drug.mechanism})")
        if len(inhibitors) > 5:
            lines.append(f"  ... and {len(inhibitors) - 5} more")
    else:
        lines.append("Approved drugs: NONE")
    lines.append("")

    # Literature evidence
    lines.append("=== LITERATURE EVIDENCE ===")
    pubs = state.get("recent_publications", [])
    if pubs:
        lines.append(f"Recent publications: {len(pubs)}")
        lines.append("Most recent titles:")
        for pub in pubs[:5]:
            lines.append(f"  [{pub.year}] {pub.title}")
    else:
        lines.append("Publications: NONE FOUND")
    lines.append("")

    # Known failures from previous agents
    agent_errors = state.get("agent_errors", {})
    if agent_errors:
        lines.append("=== DATA GAPS (from pipeline) ===")
        for agent, error in agent_errors.items():
            lines.append(f"  {agent}: {error}")
        lines.append("")

    lines.append("Produce your druggability assessment now.")
    return "\n".join(lines)


def _parse_assessment(raw_text: str) -> DruggabilityAssessment:
    """
    Parse Claude's raw text response into a DruggabilityAssessment.

    Claude is instructed to return only JSON but may occasionally
    include surrounding text. Attempts clean JSON parse first,
    then falls back to extracting JSON block from text.

    Raises:
        ValueError: if no valid JSON matching the schema can be extracted
    """
    # Attempt 1 — clean JSON parse
    try:
        data = json.loads(raw_text.strip())
        return DruggabilityAssessment(**data)
    except (json.JSONDecodeError, Exception):
        pass

    # Attempt 2 — extract JSON block from text
    # Claude sometimes wraps JSON in markdown fences despite instructions
    try:
        start = raw_text.index("{")
        end = raw_text.rindex("}") + 1
        json_str = raw_text[start:end]
        data = json.loads(json_str)
        return DruggabilityAssessment(**data)
    except (ValueError, json.JSONDecodeError, Exception) as e:
        raise ValueError(
            f"Could not parse DruggabilityAssessment from Claude response: {e}\n"
            f"Raw response: {raw_text[:500]}"
        )