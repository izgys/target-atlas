from __future__ import annotations

from typing import Literal, TypedDict
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Pydantic models — the shape of data each agent produces
# ---------------------------------------------------------------------------

class PDBStructure(BaseModel):
    """A single experimental structure from the Protein Data Bank."""
    pdb_id: str
    resolution: float | None = None          # Angstroms — None for NMR/cryo-EM
    method: str                              # X-ray, cryo-EM, NMR
    has_ligand: bool = False
    chain_count: int = 1


class AlphaFoldResult(BaseModel):
    """AlphaFold predicted structure confidence for a target."""
    uniprot_id: str
    mean_plddt: float = Field(..., ge=0, le=100)   # 0-100, higher = more confident
    high_confidence_fraction: float                 # fraction of residues pLDDT > 70
    model_url: str | None = None


class BindingSite(BaseModel):
    """A known or predicted binding site on the target."""
    name: str
    residues: list[str] = []
    source: str                              # e.g. "PDB ligand", "UniProt annotation"


class Inhibitor(BaseModel):
    """A known small molecule inhibitor from ChEMBL."""
    chembl_id: str
    name: str | None = None
    ic50_nm: float | None = None             # IC50 in nanomolar
    mechanism: str | None = None


class BioactivitySummary(BaseModel):
    """Aggregate statistics over all ChEMBL bioactivity entries for a target."""
    total_entries: int
    median_ic50_nm: float | None = None
    approved_drugs: list[str] = []


class DiseaseAssociation(BaseModel):
    """A disease linked to this target in the literature."""
    disease_name: str
    evidence_level: Literal["validated", "hypothesis", "unknown"] = "unknown"
    source: str


class Publication(BaseModel):
    """A recent publication mentioning this target."""
    pubmed_id: str
    title: str
    year: int


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
    alphafold_result: AlphaFoldResult | None
    binding_sites: list[BindingSite]

    # --- Literature agent outputs ---
    known_inhibitors: list[Inhibitor]
    bioactivity_summary: BioactivitySummary | None
    disease_associations: list[DiseaseAssociation]
    recent_publications: list[Publication]

    # --- Reasoning agent outputs ---
    druggability_assessment: DruggabilityAssessment | None

    # --- Metadata ---
    run_id: str
    timestamp: str
    agent_errors: dict[str, str]             # agent_name -> error message if failed