"""
Command-line interface for Target Atlas.

    target-atlas run EGFR
    target-atlas run P07550 --out reports
    target-atlas run EGFR --set agents.reasoning.temperature=0
    target-atlas eval -t EGFR -t TREM2
    target-atlas eval --repeats 5

Settings live in configs/*.yaml and are loaded with Hydra's compose API
(target_atlas.config). Typer keeps the command line; --set passes Hydra-style
overrides through, so no setting needs a code edit.

The graph is imported inside each command, not at module level: importing
LangGraph takes a few seconds and `target-atlas --help` should be instant.
"""
import sys
import warnings
from contextlib import contextmanager
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table


app = typer.Typer(
    help="Evidence-graded druggability assessment for human protein targets.",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()

SET_HELP = "Config override, repeatable: --set agents.reasoning.temperature=0"

CONFIDENCE_STYLE = {
    "high": "green", "medium": "yellow", "low": "red", "none": "red", "unknown": "red",
}


@app.command()
def run(
    target: str = typer.Argument(..., help="Gene name (EGFR) or UniProt accession (P00533)."),
    out: Path = typer.Option(Path("results"), "--out", "-o", help="Folder for report.md and summary.json."),
    overrides: list[str] = typer.Option(None, "--set", "-s", help=SET_HELP),
) -> None:
    """Analyse one target and write report.md + summary.json."""
    _apply_config(overrides)
    graph = _load_graph()

    with console.status(f"Analysing [bold]{target}[/bold] — UniProt, PDB, AlphaFold, ChEMBL, PubMed, Claude..."):
        state = graph.invoke({"query": target, "output_dir": str(out)})

    errors = state.get("agent_errors", {})

    # input_parser failed: the graph ended before any retrieval
    if not state.get("uniprot_id"):
        console.print(f"[red]Could not resolve '{target}':[/red] {errors.get('input_parser', 'unknown error')}")
        raise typer.Exit(code=1)

    output_dir = out / f"{state['gene_name']}_{state['uniprot_id']}"
    _print_summary(state, output_dir)

    if state.get("druggability_assessment") is None:
        console.print("[red]The reasoning step failed — the report contains retrieved evidence only.[/red]")
        raise typer.Exit(code=2)


@app.command(name="eval")
def run_evaluation(
    targets: list[str] = typer.Option(None, "--targets", "-t", help="Subset of eval targets, e.g. -t EGFR -t TREM2."),
    no_cache: bool = typer.Option(False, "--no-cache", help="Call live APIs instead of the evals/cache replay."),
    overrides: list[str] = typer.Option(None, "--set", "-s", help=SET_HELP),
    no_mlflow: bool = typer.Option(False, "--no-mlflow", help="Do not log the run to MLflow (mlruns/)."),
    repeats: int = typer.Option(
        1, "--repeats", "-r", min=1, help="Run the whole eval N times; report mean ± SD.",
    ),
) -> None:
    """Run the evaluation harness (from the repository root)."""
    # The harness and its answer key live in the repository, not in the package
    if not Path("evals/run_eval.py").exists():
        console.print("[red]evals/run_eval.py not found.[/red] Run this command from the repository root.")
        raise typer.Exit(code=1)

    _apply_config(overrides)   # fail fast with a friendly message on a bad override

    sys.path.insert(0, str(Path.cwd()))
    with _quiet_imports():
        from evals.run_eval import main
        import target_atlas.graph  # noqa: F401 — run_eval imports it lazily; import it quietly here

    argv = []
    if targets:
        argv += ["--targets", *targets]
    if no_cache:
        argv.append("--no-cache")
    if no_mlflow:
        argv.append("--no-mlflow")
    if repeats > 1:
        argv += ["--repeats", str(repeats)]
    for override in overrides or []:
        argv += ["--set", override]
    main(argv)


def _apply_config(overrides: list[str] | None) -> None:
    """Load configs/ with --set overrides, or exit with a readable error."""
    from target_atlas.config import load_config

    try:
        load_config(overrides)
    except Exception as e:   # Hydra raises several types for bad keys and syntax
        # First line only: Hydra's follow-up hint suggests adding the key with '+',
        # which would turn a typo into a new, unused setting
        console.print(f"[red]Invalid configuration:[/red] {str(e).splitlines()[0]}")
        console.print("Check the key names in configs/agents.yaml and configs/apis.yaml.")
        raise typer.Exit(code=1) from None


def _load_graph():
    with _quiet_imports():
        from target_atlas.graph import app as graph
    return graph


@contextmanager
def _quiet_imports():
    """
    Hide warnings printed while importing LangGraph.

    It emits a pending-deprecation notice on import that users cannot act on.
    A filter is not enough — LangChain installs its own warning filter ahead
    of ours — so output is muted for the import only and restored after.
    """
    with warnings.catch_warnings():
        warnings.showwarning = lambda *args, **kwargs: None
        yield


def _print_summary(state: dict, output_dir: Path) -> None:
    assessment = state.get("druggability_assessment")
    bioactivity = state.get("bioactivity_summary")
    pdb_count = state.get("pdb_total_count", len(state.get("pdb_structures", [])))
    papers = state.get("publication_total_count", len(state.get("recent_publications", [])))

    console.print()
    console.print(
        f"[bold]{state['gene_name']}[/bold] ({state['uniprot_id']}) · {state['organism']}"
    )

    table = Table(show_header=False, box=None, padding=(0, 2))
    if assessment:
        for label, value in [
            ("Druggability", assessment.druggability_score),
            ("Structural confidence", assessment.structural_confidence),
            ("Chemical confidence", assessment.chemical_confidence),
            ("Literature confidence", assessment.literature_confidence),
        ]:
            style = CONFIDENCE_STYLE.get(value, "white")
            table.add_row(label, f"[{style}]{value}[/{style}]")
    chemistry = (
        f"{bioactivity.total_entries:,} IC50 entries" if bioactivity else "no ChEMBL bioactivity"
    )
    table.add_row(
        "Evidence",
        f"{pdb_count:,} PDB entries · {chemistry} · "
        f"{len(state.get('known_inhibitors', []))} approved drugs · {papers:,} papers",
    )
    console.print(table)

    if assessment and assessment.evidence_gaps:
        console.print("\n[bold]Evidence gaps[/bold]")
        for gap in assessment.evidence_gaps:
            console.print(f"  • {gap}")

    retrieval_errors = {k: v for k, v in state.get("agent_errors", {}).items() if "failed" in v}
    if retrieval_errors:
        console.print("\n[yellow]Retrieval problems[/yellow]")
        for source, error in retrieval_errors.items():
            console.print(f"  • {source}: {error.splitlines()[0]}")

    console.print(f"\nReport: [cyan]{output_dir / 'report.md'}[/cyan]")
    console.print(f"Summary: [cyan]{output_dir / 'summary.json'}[/cyan]")


if __name__ == "__main__":
    app()
