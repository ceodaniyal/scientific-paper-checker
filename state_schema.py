from typing import TypedDict, Dict, Optional, List

class PaperState(TypedDict):
    paper_id: str
    filename: Optional[str]               # Name of uploaded file
    text: str                             # Raw extracted text from PDF or LaTeX
    sections: Dict[str, Optional[str]]    # Extracted sections (abstract, methods, etc.)
    section_statuses: Dict[str, str]      # Status per section: good / unclear / missing
    suggestions: Optional[Dict[str, str]] # LLM-generated suggestions for improvement
    missing_sections: Optional[List[str]] # List of missing section names
    route: Optional[str]                  # Routing decision: good / unclear / missing
