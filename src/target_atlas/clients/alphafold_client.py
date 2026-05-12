import httpx
from pydantic import BaseModel, Field


ALPHAFOLD_API = "https://alphafold.ebi.ac.uk/api/prediction"


class AlphaFoldResult(BaseModel):
    """AlphaFold predicted structure confidence for a protein target."""
    uniprot_id: str
    mean_plddt: float = Field(..., ge=0, le=100)
    high_confidence_fraction: float = Field(..., ge=0, le=1)
    model_url: str | None = None


def fetch_alphafold(uniprot_id: str) -> AlphaFoldResult | None:
    with httpx.Client(timeout=15.0) as client:
        response = client.get(f"{ALPHAFOLD_API}/{uniprot_id}")

        # 404 — valid ID format but not in AlphaFold DB
        # 400 — invalid ID format entirely
        # Both are expected failure modes, not errors
        if response.status_code in (400, 404):
            return None

        response.raise_for_status()
        data = response.json()

    if not data:
        return None

    canonical = next(
        (e for e in data if e.get("uniprotAccession") == uniprot_id),
        data[0]
    )

    return _parse_alphafold_response(uniprot_id, canonical)


def _parse_alphafold_response(uniprot_id: str, entry: dict) -> AlphaFoldResult:
    """
    Extract confidence metrics from a single AlphaFold API entry.

    Uses globalMetricValue for mean pLDDT. Computes high_confidence_fraction
    as fractionPlddtVeryHigh + fractionPlddtConfident — residues with
    pLDDT > 70, the threshold above which AlphaFold considers the
    backbone reliable for structural interpretation.
    """
    # globalMetricValue replaced meanPlddt in the updated API
    mean_plddt = float(entry.get("globalMetricValue", 0.0))

    # high confidence = pLDDT > 70
    # API now provides pre-computed fractions instead of per-residue array
    very_high = float(entry.get("fractionPlddtVeryHigh", 0.0))  # > 90
    confident = float(entry.get("fractionPlddtConfident", 0.0))  # 70-90
    high_confidence_fraction = very_high + confident

    model_url = entry.get("pdbUrl", None)

    return AlphaFoldResult(
        uniprot_id=uniprot_id,
        mean_plddt=mean_plddt,
        high_confidence_fraction=high_confidence_fraction,
        model_url=model_url,
    )