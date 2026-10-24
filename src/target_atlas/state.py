from __future__ import annotations

from typing import Literal, NotRequired, TypedDict

from pydantic import BaseModel

# The evidence models are defined once, next to the client that produces them,
# and re-exported here. state.py used to carry its own copies, which drifted
# (no chembl_target_id, no journal) and were never the objects in the graph.
from target_atlas.clients.alphafold_client import AlphaFoldResult
from target_atlas.clients.chembl_client import BioactivitySummary, Inhibitor
from target_atlas.clients.pdb_client import PDBStructure
from target_atlas.clients.pubmed_client import Publication

__all__ = [
    "AlphaFoldResult", "BindingSite", "BioactivitySummary", "DiseaseAssociation",
    "DruggabilityAssessment", "Inhibitor", "PDBStructure", "Publication",
    "SOURCE_ERROR_KEYS", "TargetAtlasState", "retrieval_failed",
]


# ---------------------------------------------------------------------------
# Pydantic models owned by the state (not produced by any client yet)
# ---------------------------------------------------------------------------

class BindingSite(BaseModel):
    """A known or predicted binding site on the target."""
    name: str
    residues: list[str] = []
    source: str                              # e.g. "PDB ligand", "UniProt annotation"


class DiseaseAssociation(BaseModel):
    """A disease linked to this target in the literature."""
    disease_name: str
    evidence_level: Literal["validated", "hypothesis", "unknown"] = "unknown"
    source: str


class DruggabilityAssessment(BaseModel):
    """The reasoning agent's final structured assessment of target druggability."""
    summary: str                             # 2-3 sentence human-readable conclusion
    druggability_score: Literal["high", "medium", "low", "unknown"]
    structural_confidence: Literal["high", "medium", "low", "none"]
    chemical_confidence: Literal["high", "medium", "low", "none"]
    literature_confidence: Literal["high", "medium", "low", "none"]
    evidence_gaps: list[str] = []            # explicit list of what is unknown
    reasoning_trace: str = ""               # full chain-of-thought from Claude


# ---------------------------------------------------------------------------
# TargetAtlasState — the shared state flowing through the LangGraph graph
# ---------------------------------------------------------------------------

class TargetAtlasState(TypedDict):
    """
    Central state object passed between all agents in the graph.
    No agent calls another directly — all communication is through this object.
    """

    # --- Input ---
    query: str                               # raw user input: UniProt ID or name
    uniprot_id: str                          # resolved canonical UniProt ID
    gene_name: str                           # e.g. "EGFR"
    organism: str                            # e.g. "Homo sapiens"

    # --- Structure agent outputs ---
    pdb_structures: list[PDBStructure]
    pdb_total_count: int                     # all PDB entries, not just the detailed ones
    alphafold_result: AlphaFoldResult | None
    binding_sites: list[BindingSite]

    # --- Literature agent outputs ---
    known_inhibitors: list[Inhibitor]
    bioactivity_summary: BioactivitySummary | None
    disease_associations: list[DiseaseAssociation]
    recent_publications: list[Publication]
    publication_total_count: int             # all PubMed title hits, not just the recent ones

    # --- Reasoning agent outputs ---
    druggability_assessment: DruggabilityAssessment | None

    # --- Metadata ---
    run_id: str
    timestamp: str
    agent_errors: dict[str, str]             # agent_name -> error message if failed
    output_dir: NotRequired[str]             # where report_generator writes; default "results"


# agent_errors key for each data source. A key present means the fetch
# raised — except ChEMBL bioactivity, whose key also records "not found".
SOURCE_ERROR_KEYS = {
    "pdb": "structure_agent_pdb",
    "alphafold": "structure_agent_alphafold",
    "chembl": "literature_agent_chembl",
    "chembl_drugs": "literature_agent_chembl_drugs",
    "pubmed": "literature_agent_pubmed",
}


def retrieval_failed(state: TargetAtlasState, source: str) -> bool:
    """True if the source's fetch failed, as opposed to returning no data."""
    error = state.get("agent_errors", {}).get(SOURCE_ERROR_KEYS[source])
    return bool(error) and "failed" in error
