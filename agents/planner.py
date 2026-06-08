from typing import List 
from pydantic import BaseModel
from state import ResearchState 
from config import llm

class ResearchPlan(BaseModel):
    tasks : List[str]

def planner_agent(state: ResearchState):
    '''
     print('Running Planner')
     print("\nPrevious Feedback:")
     print(state.get("review_feedback", "No feedback")) ''' #debug

    structured_llm = llm.with_structured_output(ResearchPlan)

    result = structured_llm.invoke(f'''
You are a senior research planner.
         
    Query:
{state['query']}

    Previous Feedback:
{state.get('review_feedback', '')}

If feedback is provided:

1. Identify missing information mentioned in the feedback.
2. Generate research tasks specifically to fill those gaps.
3. Do not repeat completed research areas.
4. Focus only on missing aspects.
5. Prefer generating new tasks instead of repeating previous tasks.
6. Use the original query and feedback together when creating tasks.

If no feedback exists:
Generate a complete initial research plan.

Your job is to create research tasks that will help answer the query completely.

Rules:

1. Every task must contain important keywords from the original query.

2. Never generate generic tasks such as:
    Features
    Advantages
    Limitations
    Performance
    Use Cases

3. Tasks must be self-contained search queries.

Bad Examples:
 Features
 Advantages
 Performance

Good Examples:
 FastAPI features
 Django advantages
 FastAPI vs Django performance

4. If the query is a comparison, create tasks covering:
    Features
    Advantages
    Limitations
    Performance
    Use Cases

5. If the query is a concept or topic, create tasks covering:
    Overview
    Benefits
    Limitations
    Challenges
    Future outlook

6. Return 4 to 6 tasks.

7. Each task should:

 Be search-friendly
 Contain important keywords
 Include terms like:
  research
  statistics
  study
  comparison
  benchmark
  survey
  report

when appropriate.

Avoid vague searches.
Prefer evidence-focused searches.

        '''
        )

    print('\nGenerated Tasks:')
    print(result.tasks)

    return {
        "plan" : result.tasks
    }