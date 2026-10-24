"""
Configuration loading with Hydra's compose API.

Typer owns the command line; Hydra only composes YAML. Each CLI command calls
load_config(overrides) once, before the graph runs, and every module reads
values through get_config(). This avoids @hydra.main, which would take over
sys.argv (clashing with Typer's arguments) and by default changes the working
directory and creates an output folder for every run.

The config lives in configs/ at the repository root. Set TARGET_ATLAS_CONFIG_DIR
to use another folder (for example a mounted volume in Docker).
"""
import os
from pathlib import Path

from hydra import compose, initialize_config_dir
from omegaconf import DictConfig, OmegaConf

CONFIG_DIR_ENV = "TARGET_ATLAS_CONFIG_DIR"

_config: DictConfig | None = None


def config_dir() -> Path:
    """Folder holding config.yaml: $TARGET_ATLAS_CONFIG_DIR, else <repo>/configs."""
    env = os.environ.get(CONFIG_DIR_ENV)
    # src/target_atlas/config.py -> parents[2] is the repository root
    path = Path(env) if env else Path(__file__).resolve().parents[2] / "configs"
    if not (path / "config.yaml").is_file():
        raise FileNotFoundError(
            f"No config.yaml in {path}. Run from a clone of the repository, "
            f"or set {CONFIG_DIR_ENV} to the folder that contains it."
        )
    return path.resolve()


def load_config(overrides: list[str] | None = None) -> DictConfig:
    """
    Compose configs/ with Hydra-style overrides (e.g. "apis.pdb.max_structures=50")
    and make the result the active config.

    Overriding a key that does not exist raises an error instead of silently
    adding it, so a typo cannot be mistaken for a setting.
    """
    global _config
    with initialize_config_dir(version_base="1.3", config_dir=str(config_dir()), job_name="target_atlas"):
        cfg = compose(config_name="config", overrides=list(overrides or []))
    # Read-only: no node can change a setting halfway through a run
    OmegaConf.set_readonly(cfg, True)
    _config = cfg
    return cfg


def get_config() -> DictConfig:
    """The active config; the defaults from configs/ if load_config() was never called."""
    return _config if _config is not None else load_config()


def config_as_dict(cfg: DictConfig | None = None) -> dict:
    """Plain-dict copy of the resolved config, for logging alongside results."""
    return OmegaConf.to_container(cfg or get_config(), resolve=True)
