from typing import TypedDict, List, Dict 

class ResearchState(TypedDict):
    query: str
    complexity: str
    plan: List[str]
    search_results: List[Dict]
    findings: List[str]
    review_feedback: str
    approved: bool
    final_report: str
    