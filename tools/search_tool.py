from langchain_community.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults(output_format="list")

results = search.invoke("LangGraph tutorial")

for result in results[:3]:
    print(result)
    print("-" * 50)