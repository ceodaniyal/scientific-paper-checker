import re
from typing import Dict

def extract_sections(state: Dict) -> Dict:
    text = state["text"]  # <-- Extract the actual text from the state dict
    sections = {}
    patterns = {
        "abstract": r"(abstract|summary)\s*[:\-]?\s*(.*?)\n\n",
        "methods": r"(methods|methodology)\s*[:\-]?\s*(.*?)\n\n",
        "results": r"(results|findings)\s*[:\-]?\s*(.*?)\n\n",
        "citations": r"(references|bibliography)\s*[:\-]?\s*(.*?)$",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            sections[key] = match.group(2).strip()
        else:
            sections[key] = None

    state["sections"] = sections
    return state
