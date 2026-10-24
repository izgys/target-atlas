"""State schema: the contract every node reads from and writes to."""
import pytest
from pydantic import ValidationError

from target_atlas.state import (
    SOURCE_ERROR_KEYS,
    DruggabilityAssessment,
    TargetAtlasState,
    retrieval_failed,
)


def test_assessment_accepts_valid_levels(assessment_dict):
    assessment = DruggabilityAssessment(**assessment_dict)
    assert assessment.druggability_score == "high"
    assert assessment.evidence_gaps == ["No allosteric pocket data"]


@pytest.mark.parametrize(
    "field, bad_value",
    [
        ("druggability_score", "very high"),   # not in the Literal
        ("structural_confidence", "unknown"),  # 'unknown' is only valid for the overall score
        ("chemical_confidence", "HIGH"),       # case matters
    ],
)
def test_assessment_rejects_values_outside_the_scale(assessment_dict, field, bad_value):
    # Claude's JSON is parsed into this model; an off-scale value must fail
    # here rather than leak into reports and eval scores.
    with pytest.raises(ValidationError):
        DruggabilityAssessment(**{**assessment_dict, field: bad_value})


def test_assessment_requires_summary_and_scores():
    with pytest.raises(ValidationError):
        DruggabilityAssessment(summary="incomplete")


def test_every_source_has_an_error_key_the_state_declares():
    assert set(SOURCE_ERROR_KEYS) == {"pdb", "alphafold", "chembl", "chembl_drugs", "pubmed"}
    assert "agent_errors" in TargetAtlasState.__annotations__


def test_retrieval_failed_is_false_without_errors():
    assert retrieval_failed({"agent_errors": {}}, "pdb") is False
    assert retrieval_failed({}, "pubmed") is False


def test_retrieval_failed_distinguishes_failure_from_not_found():
    # The ChEMBL key records both outcomes. Only a failed fetch means
    # "unknown"; "not found" is real evidence of absence.
    not_found = {"agent_errors": {"literature_agent_chembl": "Target P1 not found in ChEMBL"}}
    failed = {"agent_errors": {"literature_agent_chembl": "ChEMBL fetch failed: 500"}}

    assert retrieval_failed(not_found, "chembl") is False
    assert retrieval_failed(failed, "chembl") is True


def test_state_models_are_the_client_models():
    # Regression: state.py once carried its own drifted copies of these.
    # One definition each, owned by the client that produces it.
    from target_atlas import state
    from target_atlas.clients import alphafold_client, chembl_client, pdb_client, pubmed_client

    assert state.PDBStructure is pdb_client.PDBStructure
    assert state.AlphaFoldResult is alphafold_client.AlphaFoldResult
    assert state.BioactivitySummary is chembl_client.BioactivitySummary
    assert state.Inhibitor is chembl_client.Inhibitor
    assert state.Publication is pubmed_client.Publication
