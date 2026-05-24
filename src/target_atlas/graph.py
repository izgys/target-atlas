from langgraph.graph import StateGraph, END

from target_atlas.state import TargetAtlasState
from target_atlas.agents.input_parser import input_parser
from target_atlas.agents.structure_agent import structure_agent
from target_atlas.agents.literature_agent import literature_agent
from target_atlas.agents.reasoning_agent import reasoning_agent
from target_atlas.agents.report_generator import report_generator


def _should_continue(state: TargetAtlasState) -> str:
    """
    Conditional edge after input_parser.

    If input_parser failed to resolve the target identity,
    the uniprot_id will be empty and there is nothing meaningful
    any downstream agent can do. End the graph early.

    Returns:
        "continue" if uniprot_id is populated
        "end" if input_parser failed
    """
    if not state.get("uniprot_id"):
        return "end"
    return "continue"


def build_graph() -> StateGraph:
    """
    Build and compile the Target Atlas LangGraph graph.

    Node execution order:
        input_parser → structure_agent → literature_agent
        → reasoning_agent → report_generator

    Conditional routing:
        input_parser → end if target resolution fails

    Returns:
        compiled LangGraph application ready to invoke
    """
    # Initialise graph with our shared state schema
    graph = StateGraph(TargetAtlasState)

    # Register all nodes
    graph.add_node("input_parser", input_parser)
    graph.add_node("structure_agent", structure_agent)
    graph.add_node("literature_agent", literature_agent)
    graph.add_node("reasoning_agent", reasoning_agent)
    graph.add_node("report_generator", report_generator)

    # Entry point
    graph.set_entry_point("input_parser")

    # Conditional edge after input_parser
    graph.add_conditional_edges(
        "input_parser",
        _should_continue,
        {
            "continue": "structure_agent",
            "end": END,
        }
    )

    # Linear edges for the rest of the pipeline
    graph.add_edge("structure_agent", "literature_agent")
    graph.add_edge("literature_agent", "reasoning_agent")
    graph.add_edge("reasoning_agent", "report_generator")
    graph.add_edge("report_generator", END)

    return graph.compile()


# Module-level compiled graph — import this to run the pipeline
app = build_graph()