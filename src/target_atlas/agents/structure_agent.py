from target_atlas.clients.pdb_client import fetch_structures
from target_atlas.clients.alphafold_client import fetch_alphafold
from target_atlas.state import TargetAtlasState


def structure_agent(state: TargetAtlasState) -> dict:
    """
    Second node in the Target Atlas graph.

    Fetches experimental structures from PDB and predicted structure
    confidence from AlphaFold. Each source is fetched independently —
    failure of one does not prevent the other from running.

    Reads from state:
        uniprot_id

    Writes to state:
        pdb_structures, alphafold_result, agent_errors (partial)

    Failure behaviour:
        Each client failure is caught independently and written to
        agent_errors. The node always returns whatever data was
        successfully retrieved — never aborts on partial failure.

    Args:
        state: TargetAtlasState with uniprot_id populated

    Returns:
        partial state update dict
    """
    uniprot_id = state["uniprot_id"]

    # Carry forward existing errors from previous nodes
    errors = dict(state.get("agent_errors", {}))

    # If input_parser failed we have no uniprot_id to work with
    if not uniprot_id:
        errors["structure_agent"] = "No UniProt ID in state — input_parser may have failed"
        return {
            "pdb_structures": [],
            "alphafold_result": None,
            "agent_errors": errors,
        }

    # --- PDB structures ---
    pdb_structures = []
    try:
        pdb_structures = fetch_structures(uniprot_id)
    except Exception as e:
        errors["structure_agent_pdb"] = f"PDB fetch failed: {str(e)}"

    # --- AlphaFold confidence ---
    alphafold_result = None
    try:
        alphafold_result = fetch_alphafold(uniprot_id)
    except Exception as e:
        errors["structure_agent_alphafold"] = f"AlphaFold fetch failed: {str(e)}"

    return {
        "pdb_structures": pdb_structures,
        "alphafold_result": alphafold_result,
        "agent_errors": errors,
    }