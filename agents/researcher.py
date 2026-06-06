from state import ResearchState
from config import llm




def researcher_agent(state: ResearchState):

    findings = []

    for item in state["search_results"]:

        task = item["task"]
        results = item["results"]

        prompt = f"""
        Research Topic:
        {task}

        Search Results:
        {results}

        Instructions:
        - Extract the most important facts.
        - Summarize key insights.
        - Mention advantages, limitations, and notable observations.
        - Use only information supported by the search results.
        - Keep the response under 150 words.
        """

        try:
            response = llm.invoke(prompt)

            findings.append(
                {
                    "task": task,
                    "finding": response.content
                }
            )

        except Exception as e:
            print(f"Error researching {task}: {e}")

            findings.append(
                {
                    "task": task,
                    "finding": "Research failed."
                }
            )

    return {
        "findings": findings
    }

