from pydantic import BaseModel
from state import ResearchState
from config import llm


class Reviewresult(BaseModel):
    approved : bool 
    feedback : str


def reviewer_agent(state:ResearchState):

    structured_llm = llm.with_structured_output(
        Reviewresult
    )

    result = structured_llm.invoke(
        f'''
        Review these research findings.

        Determine if the research is sufficient
        to generate a final report.

        Findings:
        {state["findings"]}

        Approve only if:
        Findings are detailed
        Findings cover the query
        Findings are useful
        '''
    )


    return {
        'approved' :result.approved,
        'review_feedback': result.feedback
    }


