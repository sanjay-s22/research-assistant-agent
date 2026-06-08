from pydantic import BaseModel
from state import ResearchState
from config import llm


class Reviewresult(BaseModel):
    approved : bool 
    feedback : str


def reviewer_agent(state:ResearchState):

    print('Running Reviewer')

    structured_llm = llm.with_structured_output(
        Reviewresult
    )

    result = structured_llm.invoke(
        f'''
        You are a senior research reviewer.

Original Query:
{state["query"]}

Research Findings:
{state["findings"]}

Your job is to determine whether the research is sufficient to answer the user's query.

Check:

1. Are all major aspects covered?
2. Are there unsupported claims?
3. Are there contradictions?
4. Are important topics missing?
5. Is additional research required?

Special Rules:

If the query is a comparison, verify coverage of:

 Features
 Strengths
 Weaknesses
 Learning Curve
 Ecosystem
 Scalability
 State Management
 Production Readiness
 Recommended Use Cases

Reject the research if two or more comparison areas are missing.

If the query is explanatory, verify:

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

What information is missing
What additional research is needed
Specific topics the planner should research

Bad feedback:
"Research incomplete."

Good feedback:
"Missing LangGraph scalability information and CrewAI ecosystem comparison."

        '''
    )

    '''
    print("\nReviewer Feedback:")
    print(result.feedback)
    print(f"Approved: {result.approved}")
    print(f"Iterations: {state.get('research_iterations', 0) + 1}")'''   #debug 


    return {
        'approved' :result.approved,
        'review_feedback': result.feedback,
        'research_iterations': state.get('research_iterations', 0)+1
    }


