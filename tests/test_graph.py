"""The compiled LangGraph app end to end, with every API and Claude mocked."""
import json
from unittest.mock import Mock

import pytest

import target_atlas.agents.input_parser as ip
import target_atlas.agents.literature_agent as lit
import target_atlas.agents.structure_agent as st
from target_atlas.graph import _should_continue, app


@pytest.fixture
def mocked_sources(monkeypatch, uniprot_result, pdb_structures, alphafold_result,
                   bioactivity, drugs, publications):
    """Replace every external call with a Mock, so tests can also assert on calls."""
    mocks = {
        (ip, "resolve_target"): Mock(return_value=uniprot_result),
        (st, "fetch_structures"): Mock(return_value=pdb_structures),
        (st, "count_structures"): Mock(return_value=393),
        (st, "fetch_alphafold"): Mock(return_value=alphafold_result),
        (lit, "fetch_bioactivity"): Mock(return_value=bioactivity),
        (lit, "fetch_approved_drugs"): Mock(return_value=drugs),
        (lit, "fetch_publications"): Mock(return_value=publications),
        (lit, "count_publications"): Mock(return_value=18783),
    }
    for (module, name), mock in mocks.items():
        monkeypatch.setattr(module, name, mock)
    return {name: mock for (_, name), mock in mocks.items()}


def test_full_run_produces_assessment_and_files(tmp_path, mocked_sources, fake_claude):
    state = app.invoke({"query": "EGFR", "output_dir": str(tmp_path)})

    assert state["uniprot_id"] == "P00533"
    assert state["druggability_assessment"].druggability_score == "high"
    assert state["agent_errors"] == {}
    assert len(fake_claude.calls) == 1

    out_dir = tmp_path / "EGFR_P00533"
    summary = json.loads((out_dir / "summary.json").read_text(encoding="utf-8"))
    assert (out_dir / "report.md").exists()
    assert summary["target"]["gene_name"] == "EGFR"
    assert summary["chemical_data"]["approved_drugs"] == ["ERLOTINIB", "GEFITINIB"]


def test_partial_failure_still_reaches_the_report(tmp_path, mocked_sources, fake_claude):
    mocked_sources["fetch_alphafold"].side_effect = RuntimeError("EBI down")

    state = app.invoke({"query": "EGFR", "output_dir": str(tmp_path)})

    assert "structure_agent_alphafold" in state["agent_errors"]
    assert state["druggability_assessment"] is not None
    assert (tmp_path / "EGFR_P00533" / "report.md").exists()


def test_invalid_target_exits_before_retrieval_and_claude(tmp_path, mocked_sources, fake_claude):
    mocked_sources["resolve_target"].side_effect = ValueError("No reviewed UniProt entry")

    state = app.invoke({"query": "ZZZZNOTAPROTEIN", "output_dir": str(tmp_path)})

    assert state["uniprot_id"] == ""
    assert "No reviewed UniProt entry" in state["agent_errors"]["input_parser"]

    # Nothing downstream ran: no API calls, no Claude call (no cost), no files
    for name, mock in mocked_sources.items():
        if name != "resolve_target":
            mock.assert_not_called()
    assert fake_claude.calls == []
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("uniprot_id, expected", [("P00533", "continue"), ("", "end")])
def test_should_continue_routes_on_uniprot_id(uniprot_id, expected):
    assert _should_continue({"uniprot_id": uniprot_id}) == expected
