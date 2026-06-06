
from state import ResearchState
from config import llm


'''
response = llm.invoke("how far is the moon from the earth?")

print(response.content)

from agents.router import router_agent

state = {
    "query": "Compare LangGraph, CrewAI and AutoGen for enterprise multi-agent systems"
}

result = router_agent(state)
print(result)

from agents.planner import planner_agent

state = {
    "query": "Compare FastAPI vs Django for AI applications"
}

result = planner_agent(state)

print(result)

from agents.search import search_agent

state = {
    "plan": [
        "FastAPI features",
        "Django features"
    ]
}

result = search_agent(state)

from pprint import pprint

pprint(result)


from agents.researcher import researcher_agent

state = {
    "search_results": [
        {
            "task": "FastAPI features",
            "results": [
                {
                    "title": "FastAPI",
                    "snippet": "FastAPI is a modern Python web framework...",
                    "link": "https://..."
                }
            ]
        }
    ]
}

result = researcher_agent(state)

print(result)'''

from agents.planner import planner_agent 
from agents.search import search_agent
from agents.researcher import researcher_agent
from agents.reviewer import reviewer_agent
from agents.writer import writer_agent
from pprint import pprint


state = {
    'query': "compare FastAPI vs Django for AI applications"
}

state.update (planner_agent(state))

state.update(search_agent(state))

state.update(researcher_agent(state))

state.update(reviewer_agent(state))

if state["approved"]:
    state.update(writer_agent(state))
else:
    print("Research rejected.")
    print(state["review_feedback"])
    exit()

print("\n=== APPROVED ===")
print(state["approved"])

print("\n=== REVIEW FEEDBACK ===")
print(state["review_feedback"])

print("\n=== FINDINGS ===")
pprint(state["findings"])

print("\n=== FINAL REPORT===")
print(state["final_report"])