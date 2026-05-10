import httpx
from pydantic import BaseModel


RCSB_SEARCH_API = "https://search.rcsb.org/rcsbsearch/v2/query"
RCSB_DATA_API = "https://data.rcsb.org/rest/v1/core/entry"


class PDBStructure(BaseModel):
    """A single experimental structure from the Protein Data Bank."""
    pdb_id: str
    resolution: float | None = None     # Angstroms — None if NMR (no single resolution)
    method: str                         # X-RAY DIFFRACTION, ELECTRON MICROSCOPY, NMR
    has_ligand: bool = False            # True if small molecule bound in structure
    chain_count: int = 1                # number of protein chains in the assembly


def fetch_structures(uniprot_id: str, max_structures: int = 20) -> list[PDBStructure]:
    """
    Fetch experimental PDB structures for a given UniProt ID.

    Queries RCSB PDB search API for all structures associated with the
    UniProt accession, then fetches resolution and method details for
    the top results ranked by resolution (best first).

    Args:
        uniprot_id: canonical UniProt accession e.g. 'P00533'
        max_structures: maximum number of structures to return

    Returns:
        list of PDBStructure sorted by resolution ascending (best first)
        empty list if no structures found or API unavailable
    """
    pdb_ids = _search_pdb_ids(uniprot_id)

    if not pdb_ids:
        return []

    # Fetch details for each structure — cap at max_structures
    structures = []
    for pdb_id in pdb_ids[:max_structures]:
        structure = _fetch_structure_details(pdb_id)
        if structure is not None:
            structures.append(structure)

    # Sort by resolution ascending — best structures first
    # NMR structures have None resolution — push them to the end
    structures.sort(
        key=lambda s: s.resolution if s.resolution is not None else 999.0
    )

    return structures


def _search_pdb_ids(uniprot_id: str) -> list[str]:
    """
    Search RCSB for all PDB IDs associated with a UniProt accession.

    Uses the RCSB full-text search API with a structured query targeting
    the UniProt cross-reference field specifically.

    Returns:
        list of PDB IDs as strings, empty list if none found
    """
    # RCSB uses a JSON query language for structured searches
    # We search the polymer entity uniprot accession field specifically
    query = {
        "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "attribute": "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession",
                "operator": "exact_match",
                "value": uniprot_id,
            }
        },
        "return_type": "entry",
        "request_options": {
            "paginate": {
                "start": 0,
                "rows": 200      # fetch up to 200 IDs, we'll filter later
            },
            "sort": [
                {
                    "sort_by": "rcsb_entry_info.resolution_combined",
                    "direction": "asc"
                }
            ]
        }
    }

    with httpx.Client(timeout=15.0) as client:
        response = client.post(RCSB_SEARCH_API, json=query)

        # 204 means no results found — not an error
        if response.status_code == 204:
            return []

        response.raise_for_status()
        data = response.json()

    results = data.get("result_set", [])
    return [r["identifier"] for r in results]


def _fetch_structure_details(pdb_id: str) -> PDBStructure | None:
    """
    Fetch resolution, method, and ligand presence for a single PDB entry.

    Args:
        pdb_id: 4-character PDB accession e.g. '1IVO'

    Returns:
        PDBStructure if fetch succeeds, None if entry is unavailable
    """
    url = f"{RCSB_DATA_API}/{pdb_id.upper()}"

    with httpx.Client(timeout=10.0) as client:
        response = client.get(url)

        # Some PDB IDs in search results may be obsolete or redirected
        if response.status_code == 404:
            return None

        response.raise_for_status()
        data = response.json()

    return _parse_structure(pdb_id, data)


def _parse_structure(pdb_id: str, data: dict) -> PDBStructure:
    """
    Extract resolution, method, ligand presence and chain count
    from a raw RCSB entry response.
    """
    # Experimental method — X-RAY DIFFRACTION, ELECTRON MICROSCOPY, NMR etc.
    exptl = data.get("exptl", [{}])
    method = exptl[0].get("method", "UNKNOWN") if exptl else "UNKNOWN"

    # Resolution — only meaningful for X-ray and cryo-EM
    # NMR structures don't have a single resolution value
    resolution = None
    entry_info = data.get("rcsb_entry_info", {})
    resolution_list = entry_info.get("resolution_combined", [])
    if resolution_list:
        resolution = float(resolution_list[0])

    # Ligand presence — non-polymer entities include small molecules,
    # ions, and cofactors. Count > 0 means something is bound.
    # We treat ions (like Mg2+) as ligands too — they matter for catalysis
    nonpolymer_count = entry_info.get(
        "deposited_nonpolymer_entity_instance_count", 0
    )
    has_ligand = nonpolymer_count > 0

    # Chain count — number of polymer chains (protein + nucleic acid)
    # Relevant for understanding the biological assembly
    chain_count = entry_info.get(
        "deposited_polymer_entity_instance_count", 1
    )

    return PDBStructure(
        pdb_id=pdb_id.upper(),
        resolution=resolution,
        method=method,
        has_ligand=has_ligand,
        chain_count=chain_count,
    )