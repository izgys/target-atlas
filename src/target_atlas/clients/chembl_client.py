import statistics
from functools import lru_cache

from pydantic import BaseModel

from target_atlas.config import get_config
from target_atlas.utils.http import http_client


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


@lru_cache(maxsize=32)
def _resolve_chembl_target_id(uniprot_id: str) -> str | None:
    """
    Resolve a UniProt accession to a ChEMBL target ID.
    Transient server failures are retried by the shared HTTP client;
    the result is memoised because bioactivity and drug fetches both need it.
    """
    cfg = get_config().apis.chembl
    with http_client(timeout=cfg.timeout) as client:
        response = client.get(
            f"{cfg.base_url}/target",
            params={
                "target_components__accession": uniprot_id,
                # An accession also appears in protein families, complexes
                # and PPI targets — only the single-protein target is ours
                "target_type": "SINGLE PROTEIN",
                "format": "json",
                "limit": 1,
            },
            follow_redirects=True,
        )
        response.raise_for_status()
        targets = response.json().get("targets", [])

    if not targets:
        return None
    return targets[0].get("target_chembl_id")


def _fetch_bioactivity_summary(chembl_target_id: str) -> BioactivitySummary:
    """
    Total IC50 count for the target, plus the median of a sample of values.

    total_entries comes from page_meta (all entries). The median is computed
    from at most apis.chembl.max_activities values — the first pages only.
    """
    cfg = get_config().apis.chembl
    ic50_values = []
    offset = 0
    limit = cfg.activity_page_size
    total = None

    while True:
        # New client per request — avoids session timeout on long loops
        with http_client(timeout=cfg.timeout) as client:
            response = client.get(
                f"{cfg.base_url}/activity",
                params={
                    "target_chembl_id": chembl_target_id,
                    "standard_type": "IC50",
                    "format": "json",
                    "limit": limit,
                    "offset": offset,
                },
                follow_redirects=True,
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
        if offset >= min(total, cfg.max_activities):
            break

    median_ic50 = statistics.median(ic50_values) if ic50_values else None

    return BioactivitySummary(
        chembl_target_id=chembl_target_id,
        total_entries=total or 0,
        median_ic50_nm=median_ic50,
    )

def _fetch_drug_mechanisms(chembl_target_id: str) -> list[Inhibitor]:
    """
    Fetch approved drugs (max_phase=4) for a ChEMBL target.
    Filters at query level — only returns Phase 4 approved drugs.
    Names are fetched separately from the molecule endpoint.
    """
    cfg = get_config().apis.chembl
    with http_client(timeout=cfg.drug_timeout) as client:

        # Step 1 — get approved mechanisms only (max_phase=4 at query level)
        response = client.get(
            f"{cfg.base_url}/mechanism",
            params={
                "target_chembl_id": chembl_target_id,
                "max_phase": 4,
                "format": "json",
                "limit": cfg.max_mechanisms,
            },
            follow_redirects=True,
        )
        response.raise_for_status()
        mechanisms = response.json().get("mechanisms", [])

        if not mechanisms:
            return []

        # Step 2 — collect unique molecule IDs and their mechanisms
        molecule_mechanisms = {}
        for m in mechanisms:
            chembl_id = m.get("molecule_chembl_id")
            if chembl_id and chembl_id not in molecule_mechanisms:
                molecule_mechanisms[chembl_id] = m.get("mechanism_of_action")

        # Step 3 — fetch preferred names from molecule endpoint
        ids_str = ",".join(molecule_mechanisms.keys())
        response = client.get(
            f"{cfg.base_url}/molecule",
            params={
                "molecule_chembl_id__in": ids_str,
                "format": "json",
                "limit": cfg.max_molecules,
            },
            follow_redirects=True,
        )
        response.raise_for_status()
        molecules = response.json().get("molecules", [])

        # Build name lookup
        name_lookup = {
            m["molecule_chembl_id"]: m.get("pref_name") or m["molecule_chembl_id"]
            for m in molecules
        }

    # Step 4 — build Inhibitor list
    drugs = []
    for chembl_id, mechanism in molecule_mechanisms.items():
        drugs.append(Inhibitor(
            chembl_id=chembl_id,
            name=name_lookup.get(chembl_id, chembl_id),
            mechanism=mechanism,
        ))

    return drugs
