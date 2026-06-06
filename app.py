from graph import research_graph

result = research_graph.invoke(
    {
        "query": "compare FastAPI vs Django for AI applications"
    }
)

print(result["final_report"])