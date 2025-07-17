from typing import Dict

def flag_missing_parts(state: Dict) -> Dict:
    statuses = state.get("section_statuses", {})
    missing = [k for k, v in statuses.items() if v == "missing"]

    state["missing_sections"] = missing
    return state
