from pydantic import BaseModel 
from state import ResearchState
from config import llm


class ComplexityResult(BaseModel):
    complexity : str


def router_agent(state : ResearchState):

    #print('Running Router')
    structured_llm = llm.with_structured_output(ComplexityResult)

    result = structured_llm.invoke( f"""
        Classify this query.

        Return:
        quick
        deep

        Query:
        {state["query"]}
        """)
    
    return { 
        "complexity" : result.complexity,
        'research_iterations' : 0
    }
    