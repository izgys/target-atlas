"""
Configuration: configs/*.yaml composed with Hydra's compose API.

The point of step 2 is that settings change without code edits, so these
tests check that an override actually reaches the code that uses it.
"""
from pathlib import Path

import pytest
from omegaconf import OmegaConf
from typer.testing import CliRunner

import target_atlas.cli as cli
import target_atlas.clients.pdb_client as pdb
import target_atlas.clients.pubmed_client as pubmed
import target_atlas.config as config
from target_atlas.agents import reasoning_agent as rea
from target_atlas.clients.pdb_client import PDBStructure
from target_atlas.utils.http import http_client


def test_default_config_has_every_section():
    cfg = config.get_config()
    assert set(cfg) == {"agents", "apis"}
    assert set(cfg.apis) == {"retry", "uniprot", "pdb", "alphafold", "chembl", "pubmed"}
    reasoning = cfg.agents.reasoning
    assert isinstance(reasoning.model, str) and reasoning.max_tokens > 0


def test_retrieval_windows_are_integers():
    cfg = config.get_config().apis
    for value in (cfg.pdb.max_structures, cfg.pdb.search_rows,
                  cfg.pubmed.max_results, cfg.chembl.max_activities):
        assert isinstance(value, int) and value > 0


def test_override_changes_a_value_with_its_type():
    cfg = config.load_config(["apis.pdb.max_structures=50", "agents.reasoning.temperature=0"])
    assert cfg.apis.pdb.max_structures == 50
    assert cfg.agents.reasoning.temperature == 0
    assert config.get_config() is cfg          # load_config makes it the active config


def test_a_typo_in_a_key_is_an_error_not_a_new_setting():
    with pytest.raises(Exception, match="temprature"):
        config.load_config(["agents.reasoning.temprature=0"])


def test_config_is_read_only_during_a_run():
    cfg = config.get_config()
    with pytest.raises(Exception):
        cfg.agents.reasoning.model = "something-else"


def test_config_dir_can_be_moved_with_an_env_var(tmp_path, monkeypatch):
    (tmp_path / "config.yaml").write_text("defaults:\n  - _self_\nagents:\n  reasoning:\n    model: x\n")
    monkeypatch.setenv(config.CONFIG_DIR_ENV, str(tmp_path))
    assert config.load_config().agents.reasoning.model == "x"


def test_missing_config_dir_gives_a_clear_error(tmp_path, monkeypatch):
    monkeypatch.setenv(config.CONFIG_DIR_ENV, str(tmp_path / "nowhere"))
    with pytest.raises(FileNotFoundError, match="config.yaml"):
        config.load_config()


def test_config_as_dict_is_plain_data():
    data = config.config_as_dict()
    assert isinstance(data, dict) and not OmegaConf.is_config(data["agents"])


# ---------------------------------------------------------------------------
# Overrides reach the code
# ---------------------------------------------------------------------------

def test_reasoning_request_uses_model_temperature_and_max_tokens(full_state, fake_claude):
    config.load_config([
        "agents.reasoning.model=test-model",
        "agents.reasoning.temperature=0",
        "agents.reasoning.max_tokens=123",
    ])
    rea.reasoning_agent(full_state)

    call = fake_claude.calls[0]
    assert (call["model"], call["temperature"], call["max_tokens"]) == ("test-model", 0, 123)


def test_null_temperature_leaves_the_parameter_out(full_state, fake_claude):
    config.load_config(["agents.reasoning.temperature=null"])
    rea.reasoning_agent(full_state)
    assert "temperature" not in fake_claude.calls[0]


def test_pdb_window_comes_from_config(monkeypatch):
    ids = [f"{i}ABC" for i in range(1, 10)]
    monkeypatch.setattr(pdb, "_search_pdb_ids", lambda uid: (ids, len(ids)))
    monkeypatch.setattr(pdb, "_fetch_structure_details",
                        lambda pid: PDBStructure(pdb_id=pid, resolution=2.0, method="X-RAY"))

    config.load_config(["apis.pdb.max_structures=3"])
    assert len(pdb.fetch_structures("P00533")) == 3


def test_pubmed_window_comes_from_config(monkeypatch):
    calls = []
    monkeypatch.setattr(pubmed, "_esearch", lambda gene, n: calls.append((gene, n)) or ([], 0))

    config.load_config(["apis.pubmed.max_results=7"])
    pubmed.fetch_publications("EGFR")
    pubmed.count_publications("EGFR")

    assert calls == [("EGFR", 7), ("EGFR", 7)]   # same key → the memoised search is reused


def test_retry_settings_come_from_config():
    config.load_config(["apis.retry.retries=1", "apis.retry.backoff=0.5"])
    with http_client(timeout=1.0) as client:
        assert (client._transport.retries, client._transport.backoff) == (1, 0.5)


# ---------------------------------------------------------------------------
# CLI: Typer parses the command line, --set goes to Hydra
# ---------------------------------------------------------------------------

class FakeGraph:
    def __init__(self):
        self.calls = []

    def invoke(self, state):
        self.calls.append(state)
        return {"uniprot_id": "", "agent_errors": {"input_parser": "stopped by test"}}


def test_cli_set_is_applied_before_the_graph_runs(monkeypatch):
    graph = FakeGraph()
    seen = {}

    def load_graph():
        seen["model"] = config.get_config().agents.reasoning.model
        return graph

    monkeypatch.setattr(cli, "_load_graph", load_graph)
    result = CliRunner().invoke(cli.app, ["run", "EGFR", "--set", "agents.reasoning.model=cli-model"])

    assert seen["model"] == "cli-model"
    assert graph.calls[0]["query"] == "EGFR"
    assert result.exit_code == 1                 # the fake graph reports an unresolved target


def test_cli_bad_override_exits_before_any_work(monkeypatch):
    graph = FakeGraph()
    monkeypatch.setattr(cli, "_load_graph", lambda: graph)

    result = CliRunner().invoke(cli.app, ["run", "EGFR", "-s", "agents.reasoning.temprature=0"])

    assert result.exit_code == 1
    assert "Invalid configuration" in result.output
    assert graph.calls == []


def test_repository_configs_are_the_ones_loaded():
    assert config.config_dir() == (Path(__file__).parents[1] / "configs").resolve()
