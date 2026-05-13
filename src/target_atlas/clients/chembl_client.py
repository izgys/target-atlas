import httpx
from pydantic import BaseModel
import statistics


CHEMBL_API = "https://www.ebi.ac.uk/chembl/api/data"


class Inhibitor(BaseModel):
    """A known small molecule inhibitor from ChEMBL."""
    chembl_id: str
    name: str | None = None
    ic50_nm: float | None = None
    mechanism: str | None = None


class BioactivitySummary(BaseModel):
    """Aggregate statistics over ChEMBL bioactivity entries for a target."""
    chembl_target_id: str
    total_entries: int
    median_ic50_nm: float | None = None
    approved_drugs: list[str] = []


def fetch_bioactivity(uniprot_id: str) -> BioactivitySummary | None:
    """
    Fetch bioactivity summary for a target from ChEMBL.

    Two-step process: resolve UniProt ID to ChEMBL target ID,
    then fetch bioactivity data for that target.

    Args:
        uniprot_id: canonical UniProt accession e.g. 'P00533'

    Returns:
        BioactivitySummary if target found, None if not in ChEMBL
    """
    chembl_id = _resolve_chembl_target_id(uniprot_id)

    if chembl_id is None:
        return None

    return _fetch_bioactivity_summary(chembl_id)


def fetch_approved_drugs(uniprot_id: str) -> list[Inhibitor]:
    """
    Fetch approved drugs targeting this protein from ChEMBL mechanisms.

    Args:
        uniprot_id: canonical UniProt accession e.g. 'P00533'

    Returns:
        list of Inhibitor objects for approved drugs, empty if none found
    """
    chembl_id = _resolve_chembl_target_id(uniprot_id)
    if chembl_id is None:
        return []

    return _fetch_drug_mechanisms(chembl_id)


def _resolve_chembl_target_id(uniprot_id: str) -> str | None:
    """
    Resolve a UniProt accession to a ChEMBL target ID.

    ChEMBL uses its own internal target identifiers (e.g. CHEMBL203).
    This function bridges the two identifier systems.

    Returns:
        ChEMBL target ID string, or None if not found
    """
    with httpx.Client(timeout=15.0) as client:
        response = client.get(
            f"{CHEMBL_API}/target",
            params={
                "target_components__accession": uniprot_id,
                "format": "json",
                "limit": 1,
            }
        )
        response.raise_for_status()
        data = response.json()

    targets = data.get("targets", [])
    if not targets:
        return None

    return targets[0].get("target_chembl_id")


def _fetch_bioactivity_summary(chembl_target_id: str) -> BioactivitySummary:
    """
    Fetch IC50 bioactivity entries for a ChEMBL target and compute summary stats.

    Paginates through all available IC50 entries — ChEMBL caps results at
    1000 per page. Computes median IC50 across all entries with valid values.

    Args:
        chembl_target_id: ChEMBL internal target ID e.g. 'CHEMBL203'
    """
    ic50_values = []
    offset = 0
    limit = 1000
    total = None

    with httpx.Client(timeout=30.0) as client:
        while True:
            response = client.get(
                f"{CHEMBL_API}/activity",
                params={
                    "target_chembl_id": chembl_target_id,
                    "standard_type": "IC50",
                    "format": "json",
                    "limit": limit,
                    "offset": offset,
                }
            )
            response.raise_for_status()
            data = response.json()

            if total is None:
                total = data.get("page_meta", {}).get("total_count", 0)

            activities = data.get("activities", [])
            if not activities:
                break

            for activity in activities:
                value = activity.get("standard_value")
                units = activity.get("standard_units", "")
                if value is not None and units == "nM":
                    try:
                        ic50_values.append(float(value))
                    except (ValueError, TypeError):
                        pass

            offset += limit
            # Cap at 5000 entries to avoid very long fetch times
            if offset >= min(total, 5000):
                break

    median_ic50 = statistics.median(ic50_values) if ic50_values else None

    return BioactivitySummary(
        chembl_target_id=chembl_target_id,
        total_entries=total or 0,
        median_ic50_nm=median_ic50,
    )


def _fetch_drug_mechanisms(chembl_target_id: str) -> list[Inhibitor]:
    """
    Fetch approved drugs for a ChEMBL target.

    Queries the mechanism endpoint filtering by target — returns drugs
    with a known mechanism of action against this specific target.
    """
    with httpx.Client(timeout=15.0) as client:
        response = client.get(
            f"{CHEMBL_API}/mechanism",
            params={
                "target_chembl_id": chembl_target_id,
                "format": "json",
                "limit": 50,
            },
            follow_redirects=True,
        )
        response.raise_for_status()
        data = response.json()

    mechanisms = data.get("mechanisms", [])
    drugs = []

    for m in mechanisms:
        chembl_id = m.get("molecule_chembl_id", "")
        name = m.get("molecule_name") or chembl_id
        mechanism = m.get("mechanism_of_action")

        if chembl_id:
            drugs.append(Inhibitor(
                chembl_id=chembl_id,
                name=name,
                mechanism=mechanism,
            ))

    return drugs