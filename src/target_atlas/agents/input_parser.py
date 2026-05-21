import uuid
from datetime import datetime

from target_atlas.clients.uniprot_client import resolve_target
from target_atlas.state import TargetAtlasState


def input_parser(state: TargetAtlasState) -> dict:
    """
    First node in the Target Atlas graph.

    Resolves the raw user query (UniProt ID or gene name) into a
    canonical protein identity using the UniProt REST API.

    Writes to state:
        uniprot_id, gene_name, organism, run_id, timestamp

    Failure behaviour:
        Unlike other agents, input_parser failure is terminal —
        if we cannot resolve the target identity, no downstream
        agent can run meaningfully. Errors are written to
        agent_errors and propagated.

    Args:
        state: TargetAtlasState with query field populated

    Returns:
        partial state update dict
    """
    query = state["query"]

    try:
        result = resolve_target(query)

        return {
            "uniprot_id": result.uniprot_id,
            "gene_name": result.gene_name,
            "organism": result.organism,
            "run_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "agent_errors": {},
        }

    except Exception as e:
        # Input parser failure is terminal but we still
        # write to agent_errors for auditability
        return {
            "uniprot_id": "",
            "gene_name": "",
            "organism": "",
            "run_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "agent_errors": {"input_parser": str(e)},
        }