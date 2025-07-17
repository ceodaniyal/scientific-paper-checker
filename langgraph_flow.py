from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from nodes.extract_sections import extract_sections
from nodes.check_quality import check_section_quality
from nodes.flag_missing import flag_missing_parts
from nodes.suggest_improvements import suggest_improvements
from nodes.save_review import save_review
from state_schema import PaperState


graph = StateGraph(PaperState)

graph.add_node("extract_sections", extract_sections)
graph.add_node("check_quality", check_section_quality)
graph.add_node("flag_missing", flag_missing_parts)
graph.add_node("suggest_improvements", suggest_improvements)
graph.add_node("save_review", save_review)

# Entry point
graph.set_entry_point("extract_sections")

# Sequential edge
graph.add_edge("extract_sections", "check_quality")

# Conditional edge, using lambda to extract 'route' from state
graph.add_conditional_edges(
    "check_quality",
    lambda state: state["route"],   # <-- This is your routing key extractor
    {
        "missing": "flag_missing",
        "unclear": "suggest_improvements",
        "good": "save_review",
    }
)

# Other connections
graph.add_edge("flag_missing", "save_review")
graph.add_edge("suggest_improvements", "save_review")

# End
graph.set_finish_point("save_review")

scientific_graph = graph.compile()
