from langgraph.graph import StateGraph, END
from agents import researcher
from state import ResearchState
from agents.planner import planner_agent
from agents.search import search_agent
from agents.researcher import researcher_agent
from agents.reviewer import reviewer_agent
from agents.writer import writer_agent

graph = StateGraph(ResearchState)

graph.add_node('planner', planner_agent)
graph.add_node('search', search_agent)
graph.add_node('researcher', researcher_agent)
graph.add_node('reviewer', reviewer_agent)
graph.add_node('writer', writer_agent)

graph.add_edge('planner', 'search')
graph.add_edge('search', 'researcher')
graph.add_edge('researcher', 'reviewer')

def review_router(state: ResearchState):
    if state['approved']:
        return 'writer'
    return 'search'

graph.add_conditional_edges('reviewer', review_router,
{
    'writer' : 'writer',
    'search': 'search'
}
)
graph.add_edge('writer',END)

graph.set_entry_point('planner')

research_graph = graph.compile()
