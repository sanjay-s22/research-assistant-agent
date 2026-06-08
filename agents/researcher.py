from state import ResearchState
from config import llm


def researcher_agent(state: ResearchState):

    #print('Running Researcher')
    findings = []

    for item in state["search_results"]:

        task = item["task"]
        results = item["results"]

        formatted_results = "\n\n".join(
            [
                f'''
    Title: {r.get('title', 'N/A')}
    Snippet: {r.get('snippet', 'N/A')}
    Source: {r.get('link', 'N/A')}
    '''
                for r in results
            ]
        )

        prompt = f'''
You are a senior research analyst.

Original User Query:
{state["query"]}

Research Task:
{task}

Search Results:
{formatted_results}

Instructions:

1. Use ONLY information present in the search results.
2. Do NOT invent facts.
3. Do NOT make unsupported claims.
4. Clearly distinguish facts from conclusions.
5. If information is missing, explicitly state:
   "Insufficient information found."
6. Consider how this research task contributes to answering the ORIGINAL USER QUERY.
7. If the original query is a comparison, identify any direct comparisons found in the search results.

Return:

# Key Facts

# Advantages

# Limitations

# Unknowns

# Notable Observations

# Relevance To Original Query
'''

        try:

            response = llm.invoke(prompt)

            findings.append(
                {
                    'task': task,
                    'finding': response.content,
                    'sources': [
                        r.get("link")
                        for r in results
                    ]
                }
            )

        except Exception as e:

            print(f'Error researching {task}: {e}')

            findings.append(
                {
                    'task': task,
                    'finding': 'Research failed.',
                    'sources': []
                }
            )

    return {
        'findings': findings
    }

