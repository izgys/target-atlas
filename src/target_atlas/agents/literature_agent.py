from target_atlas.clients.chembl_client import fetch_bioactivity, fetch_approved_drugs
from target_atlas.clients.pubmed_client import fetch_publications
from target_atlas.state import TargetAtlasState


def literature_agent(state: TargetAtlasState) -> dict:
    """
    Third node in the Target Atlas graph.

    Fetches bioactivity data from ChEMBL and recent publications
    from PubMed. Each source is fetched independently — failure
    of one does not prevent the other from running.

    Reads from state:
        uniprot_id, gene_name

    Writes to state:
        known_inhibitors, bioactivity_summary,
        recent_publications, agent_errors (partial)

    Failure behaviour:
        ChEMBL returning None (target not in database) is not an
        error — it is written as None to state and the reasoning
        agent treats it as an evidence gap. Network failures are
        caught and written to agent_errors.

    Args:
        state: TargetAtlasState with uniprot_id and gene_name populated

    Returns:
        partial state update dict
    """
    uniprot_id = state["uniprot_id"]
    gene_name = state["gene_name"]

    errors = dict(state.get("agent_errors", {}))

    # --- ChEMBL bioactivity ---
    bioactivity_summary = None
    known_inhibitors = []

    try:
        # fetch_bioactivity returns None if target not in ChEMBL
        # This is valid — not an error
        bioactivity_summary = fetch_bioactivity(uniprot_id)

        if bioactivity_summary is None:
            errors["literature_agent_chembl"] = (
                f"Target {uniprot_id} not found in ChEMBL — "
                f"no bioactivity data available"
            )
        else:
            # Only fetch approved drugs if target exists in ChEMBL
            known_inhibitors = fetch_approved_drugs(uniprot_id)

    except Exception as e:
        errors["literature_agent_chembl"] = f"ChEMBL fetch failed: {str(e)}"

    # --- PubMed publications ---
    recent_publications = []

    try:
        recent_publications = fetch_publications(gene_name)
    except Exception as e:
        errors["literature_agent_pubmed"] = f"PubMed fetch failed: {str(e)}"

    return {
        "bioactivity_summary": bioactivity_summary,
        "known_inhibitors": known_inhibitors,
        "recent_publications": recent_publications,
        "agent_errors": errors,
    }