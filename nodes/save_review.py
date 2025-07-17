from utils.mongo_utils import save_review_to_mongo
from datetime import datetime
from typing import Dict

def save_review(state: Dict) -> Dict:
    paper_id = state["paper_id"]
    review_data = {
        "filename": state.get("filename", ""),
        "sections": {
            name: {
                "content": state["sections"].get(name),
                "status": state["section_statuses"].get(name)
            }
            for name in state["sections"]
        },
        "suggestions": state.get("suggestions", {}),
        "missing_sections": state.get("missing_sections", []),
        "timestamp": datetime.now()
    }
    save_review_to_mongo(paper_id, review_data)
    print(f"✅ Saved review for paper {paper_id}")
    return state
