from langchain_community.tools import DuckDuckGoSearchResults
from state import ResearchState


search_tool = DuckDuckGoSearchResults(
    output_format='list'
)


def search_agent(state: ResearchState):

    all_results = []

    for task in state["plan"]:

        results = search_tool.invoke(task)

        all_results.append(
            {
                'task': task,
                'results': results[:3]
            }
        )

    return {
        'search_results': all_results
    }