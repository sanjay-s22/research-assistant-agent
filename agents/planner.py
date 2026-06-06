from typing import List 
from pydantic import BaseModel
from state import ResearchState 

from config import llm

class ResearchPlan(BaseModel):
    tasks : List[str]

def planner_agent (state:ResearchState):
    structured_llm = llm.with_structured_output(ResearchPlan)

    result = structured_llm.invoke(f"""
        You are a research planner.

         Break the query into 3 to 6 concise research tasks.
    Each task should be:
     Short
     Search-friendly
     Less than 10 words

        Query:
        {state["query"]}
        """
        )
    
    return {
        "plan" : result.tasks
    }