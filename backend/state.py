from typing import TypedDict, List, Dict, Annotated
from operator import add

class ResearchState(TypedDict):
    query: str
    complexity: str
    plan: List[str]
    search_results: List[Dict]
    findings: Annotated[List[dict], add]
    review_feedback: str
    approved: bool
    research_iterations : int
    final_report: str
    