from langchain_community.tools import DuckDuckGoSearchResults
from state import ResearchState


search_tool = DuckDuckGoSearchResults(
    output_format="list",
    max_results=10
)


def search_agent(state: ResearchState):

    # print("Running Search")
    all_results = []

    blocked_domains = [
        "pinterest",
        "quora",
        "facebook",
        "instagram",
        "tiktok"
    ]

    preferred_domains = [
        ".gov",
        ".edu",
        "wikipedia",
        "ibm",
        "microsoft",
        "aws",
        "stanford",
        "mit",
        "harvard"
    ]

    for task in state["plan"]:

        # print(f"\nSearching: {task}")

        try:

            results = search_tool.invoke(task)

            ''' print(f"\nSearch Task: {task}")

            for r in results[:3]:
                  print(r.get("link"))'''  #debug 

            filtered_results = []

            for r in results:
                link = r.get("link", "").lower()
                if any(
                    domain in link
                    for domain in blocked_domains
                ):
                    continue

                filtered_results.append(r)

            # Push trusted sources higher
            filtered_results.sort(
                key=lambda r: any(
                    domain in r.get("link", "").lower()
                    for domain in preferred_domains
                ),
                reverse=True
            )

            all_results.append(
                {
                    "task": task,
                    "results": filtered_results[:7]
                }
            )

            # print(f"Found {len(filtered_results[:7])} results")

        except Exception as e:
            print(f"Search failed for '{task}'")
            print(e)
            all_results.append(
                {
                    "task": task,
                    "results": []
                }
            )

    return {
        "search_results": all_results
    }