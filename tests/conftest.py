"""
Shared fixtures for the offline test suite.

Two guarantees hold for every test:

1. No network. socket.connect is replaced with a function that raises, so a
   test that was meant to be mocked but reaches a real API fails loudly
   instead of passing on a laptop and flaking in CI.
2. No API key. ANTHROPIC_API_KEY is removed, so a missed Claude mock can
   never spend money.

The fake data uses the client models (the objects the graph really carries).
"""
import json
import os
import socket
from types import SimpleNamespace

import pytest

import target_atlas.config as config
from target_atlas.clients.alphafold_client import AlphaFoldResult
from target_atlas.clients.chembl_client import BioactivitySummary, Inhibitor
from target_atlas.clients.pdb_client import PDBStructure
from target_atlas.clients.pubmed_client import Publication
from target_atlas.clients.uniprot_client import UniProtResult


# MLflow 3.x sends usage telemetry from a background thread; tests make no
# network calls of any kind. Set before any test imports mlflow.
os.environ["MLFLOW_DISABLE_TELEMETRY"] = "true"


class NetworkBlockedError(RuntimeError):
    pass


LOOPBACK = {"127.0.0.1", "::1", "localhost"}


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    # Loopback stays allowed: on Windows, socket.socketpair() (used by event
    # loops) connects to 127.0.0.1 internally. Only external hosts are blocked.
    real_connect = socket.socket.connect

    def guarded_connect(sock, address):
        host = address[0] if isinstance(address, tuple) else address
        if host in LOOPBACK:
            return real_connect(sock, address)
        raise NetworkBlockedError(f"Test tried to connect to {address}")

    def guarded_create_connection(address, *args, **kwargs):
        raise NetworkBlockedError(f"Test tried to connect to {address}")

    monkeypatch.setattr(socket.socket, "connect", guarded_connect)
    monkeypatch.setattr(socket, "create_connection", guarded_create_connection)


@pytest.fixture(autouse=True)
def no_api_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)


@pytest.fixture(autouse=True)
def no_tracking_uri():
    # mlflow.set_tracking_uri() writes this variable; clear it before and after
    # each test so one test's MLflow store never becomes the next one's
    os.environ.pop("MLFLOW_TRACKING_URI", None)
    yield
    os.environ.pop("MLFLOW_TRACKING_URI", None)


@pytest.fixture(autouse=True)
def default_config(monkeypatch):
    # The active config is module-level state. Reset it so a test that loads
    # overrides cannot leak them into the next test; get_config() then
    # recomposes the defaults from configs/.
    monkeypatch.setattr(config, "_config", None)


# ---------------------------------------------------------------------------
# Fake evidence — one small, fully populated target
# ---------------------------------------------------------------------------

@pytest.fixture
def uniprot_result():
    return UniProtResult(
        uniprot_id="P00533",
        gene_name="EGFR",
        protein_name="Epidermal growth factor receptor",
        organism="Homo sapiens",
        reviewed=True,
    )


@pytest.fixture
def pdb_structures():
    return [
        PDBStructure(pdb_id="5UG9", resolution=1.1, method="X-RAY DIFFRACTION", has_ligand=True),
        PDBStructure(pdb_id="1M17", resolution=2.6, method="X-RAY DIFFRACTION", has_ligand=True),
    ]


@pytest.fixture
def alphafold_result():
    return AlphaFoldResult(
        uniprot_id="P00533", mean_plddt=75.0, high_confidence_fraction=0.7,
    )


@pytest.fixture
def bioactivity():
    return BioactivitySummary(chembl_target_id="CHEMBL203", total_entries=26600, median_ic50_nm=50.0)


@pytest.fixture
def drugs():
    return [
        Inhibitor(chembl_id="CHEMBL553", name="ERLOTINIB", mechanism="EGFR inhibitor"),
        Inhibitor(chembl_id="CHEMBL939", name="GEFITINIB", mechanism="EGFR inhibitor"),
    ]


@pytest.fixture
def publications():
    return [
        Publication(pubmed_id="40000001", title="EGFR in lung cancer", year=2026,
                    journal="Nature", abstract="An abstract."),
        Publication(pubmed_id="40000002", title="EGFR resistance", year=2025, journal="Cell"),
    ]


@pytest.fixture
def assessment_dict():
    return {
        "summary": "EGFR is a highly druggable kinase.",
        "druggability_score": "high",
        "structural_confidence": "high",
        "chemical_confidence": "high",
        "literature_confidence": "high",
        "evidence_gaps": ["No allosteric pocket data"],
        "reasoning_trace": "Step 1: structures. Step 2: chemistry.",
    }


@pytest.fixture
def full_state(uniprot_result, pdb_structures, alphafold_result, bioactivity, drugs, publications):
    """State as it looks after both retrieval nodes, just before reasoning."""
    return {
        "query": "EGFR",
        "uniprot_id": uniprot_result.uniprot_id,
        "gene_name": uniprot_result.gene_name,
        "organism": uniprot_result.organism,
        "pdb_structures": pdb_structures,
        "pdb_total_count": 393,
        "alphafold_result": alphafold_result,
        "binding_sites": [],
        "known_inhibitors": drugs,
        "bioactivity_summary": bioactivity,
        "disease_associations": [],
        "recent_publications": publications,
        "publication_total_count": 18783,
        "druggability_assessment": None,
        "run_id": "test-run",
        "timestamp": "2026-10-24T00:00:00",
        "agent_errors": {},
    }


# ---------------------------------------------------------------------------
# Fake Claude
# ---------------------------------------------------------------------------

class FakeAnthropic:
    """
    Stands in for anthropic.Anthropic. Records every messages.create call
    and returns a canned text response, shaped like the real SDK's
    (response.content[0].text).
    """

    def __init__(self, text: str):
        self.text = text
        self.calls: list[dict] = []
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(content=[SimpleNamespace(text=self.text)])


@pytest.fixture
def fake_claude(monkeypatch, assessment_dict):
    """
    Patch Claude with a fake that returns a valid assessment.
    Returns a setter so a test can change the response text.
    """
    fake = FakeAnthropic(json.dumps(assessment_dict))
    monkeypatch.setattr(
        "target_atlas.agents.reasoning_agent.anthropic.Anthropic", lambda *a, **k: fake
    )
    return fake
