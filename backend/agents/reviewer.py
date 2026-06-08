from pydantic import BaseModel
from state import ResearchState
from config import llm


class Reviewresult(BaseModel):
    approved: bool
    feedback: str


def reviewer_agent(state: ResearchState):

    print('Running Reviewer')

    structured_llm = llm.with_structured_output(Reviewresult)

    result = structured_llm.invoke(
        f'''
        You are a senior research reviewer.

Original Query:
{state["query"]}

Research Findings:
{state["findings"]}

Your job is to determine whether the research is sufficient to answer the user's query.

Approve the research unless there are MAJOR gaps. Minor missing details, depth improvements, or could-be-better coverage are NOT reasons to reject.

Only reject if:
1. A core aspect of the query is completely absent from the findings
2. There are direct contradictions that make the findings unreliable
3. The query genuinely cannot be answered with what was found

If the query is a comparison, reject only if TWO OR MORE of these are completely missing:
 Features
 Strengths
 Weaknesses
 Learning Curve
 Ecosystem
 Scalability
 State Management
 Production Readiness
 Recommended Use Cases

If the query is explanatory, reject only if TWO OR MORE of these are completely missing:
 Overview
 Benefits
 Limitations
 Challenges
 Future Outlook

Return:

approved: true/false

feedback:

If approved:
Explain briefly why.

If rejected:
Clearly state:
 What information is completely missing
 What additional research is needed
 Specific topics the planner should research

Bad feedback:
"Research incomplete."

Good feedback:
"Missing LangGraph scalability information and CrewAI ecosystem comparison."
        '''
    )

    return {
        'approved': result.approved,
        'review_feedback': result.feedback,
        'research_iterations': state.get('research_iterations', 0) + 1
    }

