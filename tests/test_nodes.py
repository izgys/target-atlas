"""
Each graph node in isolation, with its external calls replaced.

Patch where a name is USED, not where it is defined: the nodes do
`from target_atlas.clients.pdb_client import fetch_structures`, which copies
the name into the node's own module. Patching pdb_client.fetch_structures
would leave the node's copy untouched, so every patch below targets
target_atlas.agents.<node>.<function>.
"""
import json

import pytest

import target_atlas.agents.input_parser as ip
import target_atlas.agents.literature_agent as lit
import target_atlas.agents.reasoning_agent as rea
import target_atlas.agents.report_generator as rep
import target_atlas.agents.structure_agent as st
from target_atlas.config import get_config


def _raise(message):
    def fail(*args, **kwargs):
        raise RuntimeError(message)
    return fail


# ---------------------------------------------------------------------------
# input_parser
# ---------------------------------------------------------------------------

def test_input_parser_resolves_identity(monkeypatch, uniprot_result):
    monkeypatch.setattr(ip, "resolve_target", lambda q: uniprot_result)

    out = ip.input_parser({"query": "EGFR"})

    assert out["uniprot_id"] == "P00533"
    assert out["gene_name"] == "EGFR"
    assert out["organism"] == "Homo sapiens"
    assert out["agent_errors"] == {}
    assert out["run_id"] and out["timestamp"]


def test_input_parser_failure_leaves_empty_id_and_records_error(monkeypatch):
    monkeypatch.setattr(ip, "resolve_target", _raise("No reviewed UniProt entry"))

    out = ip.input_parser({"query": "ZZZZNOTAPROTEIN"})

    # An empty uniprot_id is the signal the conditional edge routes on
    assert out["uniprot_id"] == ""
    assert "No reviewed UniProt entry" in out["agent_errors"]["input_parser"]


# ---------------------------------------------------------------------------
# structure_agent
# ---------------------------------------------------------------------------

def test_structure_agent_collects_pdb_and_alphafold(monkeypatch, pdb_structures, alphafold_result):
    monkeypatch.setattr(st, "fetch_structures", lambda uid: pdb_structures)
    monkeypatch.setattr(st, "count_structures", lambda uid: 393)
    monkeypatch.setattr(st, "fetch_alphafold", lambda uid: alphafold_result)

    out = st.structure_agent({"uniprot_id": "P00533", "agent_errors": {}})

    assert out["pdb_structures"] == pdb_structures
    assert out["pdb_total_count"] == 393
    assert out["alphafold_result"] == alphafold_result
    assert out["agent_errors"] == {}


def test_structure_agent_isolates_a_pdb_failure(monkeypatch, alphafold_result):
    monkeypatch.setattr(st, "fetch_structures", _raise("RCSB down"))
    monkeypatch.setattr(st, "count_structures", lambda uid: 0)
    monkeypatch.setattr(st, "fetch_alphafold", lambda uid: alphafold_result)

    out = st.structure_agent({"uniprot_id": "P00533", "agent_errors": {"earlier": "kept"}})

    assert out["pdb_structures"] == []
    assert out["alphafold_result"] == alphafold_result          # the other source still arrives
    assert "PDB fetch failed" in out["agent_errors"]["structure_agent_pdb"]
    assert out["agent_errors"]["earlier"] == "kept"              # earlier errors carried forward


def test_structure_agent_isolates_an_alphafold_failure(monkeypatch, pdb_structures):
    monkeypatch.setattr(st, "fetch_structures", lambda uid: pdb_structures)
    monkeypatch.setattr(st, "count_structures", lambda uid: 393)
    monkeypatch.setattr(st, "fetch_alphafold", _raise("EBI timeout"))

    out = st.structure_agent({"uniprot_id": "P00533", "agent_errors": {}})

    assert out["pdb_structures"] == pdb_structures
    assert out["alphafold_result"] is None
    assert "AlphaFold fetch failed" in out["agent_errors"]["structure_agent_alphafold"]


# ---------------------------------------------------------------------------
# literature_agent
# ---------------------------------------------------------------------------

@pytest.fixture
def lit_ok(monkeypatch, bioactivity, drugs, publications):
    monkeypatch.setattr(lit, "fetch_bioactivity", lambda uid: bioactivity)
    monkeypatch.setattr(lit, "fetch_approved_drugs", lambda uid: drugs)
    monkeypatch.setattr(lit, "fetch_publications", lambda gene: publications)
    monkeypatch.setattr(lit, "count_publications", lambda gene: 18783)


STATE_IN = {"uniprot_id": "P00533", "gene_name": "EGFR", "agent_errors": {}}


def test_literature_agent_collects_all_sources(lit_ok, bioactivity, drugs, publications):
    out = lit.literature_agent(dict(STATE_IN))

    assert out["bioactivity_summary"] == bioactivity
    assert out["known_inhibitors"] == drugs
    assert out["recent_publications"] == publications
    assert out["publication_total_count"] == 18783
    assert out["agent_errors"] == {}


def test_literature_agent_target_not_in_chembl_is_not_a_failure(lit_ok, monkeypatch):
    monkeypatch.setattr(lit, "fetch_bioactivity", lambda uid: None)

    out = lit.literature_agent(dict(STATE_IN))

    message = out["agent_errors"]["literature_agent_chembl"]
    assert "not found" in message and "failed" not in message


def test_literature_agent_bioactivity_failure_keeps_drugs(lit_ok, monkeypatch, drugs):
    # Regression for 18 Oct: a ChEMBL 500 on activities used to drop the drug list
    monkeypatch.setattr(lit, "fetch_bioactivity", _raise("ChEMBL 500"))

    out = lit.literature_agent(dict(STATE_IN))

    assert out["bioactivity_summary"] is None
    assert out["known_inhibitors"] == drugs
    assert "ChEMBL fetch failed" in out["agent_errors"]["literature_agent_chembl"]


def test_literature_agent_isolates_a_pubmed_failure(lit_ok, monkeypatch, bioactivity):
    monkeypatch.setattr(lit, "fetch_publications", _raise("NCBI 429"))

    out = lit.literature_agent(dict(STATE_IN))

    assert out["bioactivity_summary"] == bioactivity
    assert out["recent_publications"] == []
    assert "PubMed fetch failed" in out["agent_errors"]["literature_agent_pubmed"]


# ---------------------------------------------------------------------------
# reasoning_agent
# ---------------------------------------------------------------------------

def test_reasoning_agent_parses_claude_json(full_state, fake_claude):
    out = rea.reasoning_agent(full_state)

    assessment = out["druggability_assessment"]
    assert assessment.druggability_score == "high"
    assert "reasoning_agent" not in out["agent_errors"]

    # Exactly one Claude call, with the configured model
    assert len(fake_claude.calls) == 1
    assert fake_claude.calls[0]["model"] == get_config().agents.reasoning.model


def test_reasoning_agent_tells_claude_the_totals_not_the_window(full_state, fake_claude):
    # Regression for the count bug: Claude was told "20 papers" for EGFR
    rea.reasoning_agent(full_state)
    context = fake_claude.calls[0]["messages"][0]["content"]

    assert "18783" in context
    assert "393" in context


def test_reasoning_agent_accepts_json_inside_markdown_fences(full_state, fake_claude, assessment_dict):
    fake_claude.text = "Here you go:\n```json\n" + json.dumps(assessment_dict) + "\n```"

    out = rea.reasoning_agent(full_state)

    assert out["druggability_assessment"].summary == assessment_dict["summary"]


def test_reasoning_agent_unparseable_reply_records_error(full_state, fake_claude):
    fake_claude.text = "I cannot assess this target."

    out = rea.reasoning_agent(full_state)

    assert out["druggability_assessment"] is None
    assert "Reasoning failed" in out["agent_errors"]["reasoning_agent"]


def test_context_says_failed_retrieval_is_unknown_not_absent(full_state):
    state = {
        **full_state,
        "pdb_structures": [],
        "recent_publications": [],
        "agent_errors": {
            "structure_agent_pdb": "PDB fetch failed: timeout",   # failed → unknown
        },
    }
    context = rea._build_context(state)

    assert "PDB structures: RETRIEVAL FAILED" in context
    assert "Publications: NONE FOUND" in context                 # empty, but no failure recorded


# ---------------------------------------------------------------------------
# report_generator
# ---------------------------------------------------------------------------

def test_report_generator_writes_report_and_summary(tmp_path, full_state, assessment_dict):
    from target_atlas.state import DruggabilityAssessment

    state = {
        **full_state,
        "druggability_assessment": DruggabilityAssessment(**assessment_dict),
        "output_dir": str(tmp_path),
    }

    assert rep.report_generator(state) == {}

    out_dir = tmp_path / "EGFR_P00533"
    report = (out_dir / "report.md").read_text(encoding="utf-8")
    summary = json.loads((out_dir / "summary.json").read_text(encoding="utf-8"))

    assert "# Target Atlas Report — EGFR (P00533)" in report
    assert "ERLOTINIB" in report
    assert summary["assessment"]["druggability_score"] == "high"
    assert summary["structural_data"]["pdb_total_count"] == 393
    # The eval harness scores fact recall from these two lists
    assert summary["structural_data"]["pdb_ids"] == ["5UG9", "1M17"]
    assert summary["literature_data"]["pmids"] == ["40000001", "40000002"]


def test_report_generator_without_assessment_still_reports_evidence(tmp_path, full_state):
    state = {**full_state, "output_dir": str(tmp_path)}   # druggability_assessment is None

    rep.report_generator(state)

    report = (tmp_path / "EGFR_P00533" / "report.md").read_text(encoding="utf-8")
    summary = json.loads((tmp_path / "EGFR_P00533" / "summary.json").read_text(encoding="utf-8"))
    assert "Assessment unavailable" in report
    assert summary["assessment"]["druggability_score"] is None
    assert summary["chemical_data"]["approved_drug_count"] == 2
