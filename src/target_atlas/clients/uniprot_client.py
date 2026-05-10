import httpx
from pydantic import BaseModel


UNIPROT_API = "https://rest.uniprot.org/uniprotkb"


class UniProtResult(BaseModel):
    """Resolved UniProt entry for a protein target."""
    uniprot_id: str
    gene_name: str
    protein_name: str
    organism: str
    reviewed: bool      # True = Swiss-Prot (curated), False = TrEMBL (automatic)


def resolve_target(query: str) -> UniProtResult:
    """
    Resolve a UniProt ID or protein name into a canonical UniProtResult.

    Args:
        query: UniProt ID (e.g. 'P00533') or protein name (e.g. 'EGFR')

    Returns:
        UniProtResult with canonical ID, gene name, organism

    Raises:
        ValueError: if no reviewed entry is found for the query
        httpx.HTTPError: if the UniProt API is unreachable
    """
    # If it looks like a UniProt ID fetch it directly
    # UniProt IDs are 6-10 alphanumeric characters
    if _looks_like_uniprot_id(query):
        return _fetch_by_id(query)
    else:
        return _search_by_name(query)


def _looks_like_uniprot_id(query: str) -> bool:
    """Heuristic check — UniProt IDs are 6-10 chars, alphanumeric, no spaces."""
    q = query.strip()
    return len(q) >= 6 and len(q) <= 10 and q.isalnum()


def _fetch_by_id(uniprot_id: str) -> UniProtResult:
    """Fetch a UniProt entry directly by accession ID."""
    url = f"{UNIPROT_API}/{uniprot_id.upper()}"
    
    with httpx.Client(timeout=10.0) as client:
        response = client.get(url, params={"format": "json"})
        response.raise_for_status()
        data = response.json()

    return _parse_uniprot_response(data)


def _search_by_name(name: str) -> UniProtResult:
    """Search UniProt by protein or gene name, return top reviewed hit."""
    with httpx.Client(timeout=10.0) as client:
        response = client.get(
            f"{UNIPROT_API}/search",
            params={
                "query": f"gene:{name} AND reviewed:true AND organism_id:9606",
                "format": "json",
                "size": 1,      # we only want the top hit
            }
        )
        response.raise_for_status()
        data = response.json()

    results = data.get("results", [])
    if not results:
        raise ValueError(
            f"No reviewed UniProt entry found for '{name}'. "
            f"Try using the UniProt ID directly."
        )

    return _parse_uniprot_response(results[0])


def _parse_uniprot_response(data: dict) -> UniProtResult:
    """Extract the fields we need from a raw UniProt API response."""
    uniprot_id = data["primaryAccession"]

    # Gene name — take the first listed
    genes = data.get("genes", [])
    gene_name = (
        genes[0].get("geneName", {}).get("value", "unknown")
        if genes else "unknown"
    )

    # Protein name — recommended name from the description block
    description = data.get("proteinDescription", {})
    protein_name = (
        description
        .get("recommendedName", {})
        .get("fullName", {})
        .get("value", "unknown")
    )

    # Organism
    organism = (
        data.get("organism", {})
        .get("scientificName", "unknown")
    )

    # Reviewed = Swiss-Prot
    reviewed = data.get("entryType", "") == "UniProtKB reviewed (Swiss-Prot)"

    return UniProtResult(
        uniprot_id=uniprot_id,
        gene_name=gene_name,
        protein_name=protein_name,
        organism=organism,
        reviewed=reviewed,
    )