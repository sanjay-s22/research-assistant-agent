from state import ResearchState
from config import llm


def writer_agent(state: ResearchState):

    #print("Running Writer")
    if "findings" not in state:

        prompt = f'''

Answer the following question clearly and concisely.

Question:
{state["query"]}
'''

        response = llm.invoke(prompt)

        return {
            "final_report": response.content
        }

    sources = []

    for finding in state["findings"]:

        sources.extend(
            finding.get("sources", [])
        )

    sources = list(set(sources))

    sources_text = '\n'.join(
        [
            f'[{i+1}] {source}'
            for i, source in enumerate(sources)
        ]
    )

    prompt = f'''
You are a senior technical research writer.

Original Query:
{state['query']}

Research Findings:
{state['findings']}

Available Sources:
{sources_text}

Instructions:

1. Use ONLY the provided research findings.
2. Do NOT invent facts.
3. Do NOT introduce unsupported claims.
4. Base conclusions only on the provided findings.
5. Mention limitations when information is missing.
6. Maintain a professional and objective tone.
7. Use markdown formatting.

Your goal is to directly answer the user's query.

Before writing, determine the most appropriate report structure based on the query.

Guidelines:

- For comparison queries, clearly compare alternatives, highlight tradeoffs, and provide recommendations.
- For explanatory queries, focus on concepts, benefits, limitations, and key insights.
- For technology evaluations, discuss strengths, weaknesses, performance considerations, and suitable use cases.
- For trend or future-oriented queries, discuss current developments, opportunities, risks, and future outlook.

Generate a report that is tailored to the user's query rather than using a fixed template.

The report should generally include:

# Overview

# Key Findings

# Analysis

# Recommendations

# Conclusion

# Sources

When appropriate, include:

- Comparison tables
- Pros and cons
- Use cases
- Recommendations
- Future outlook

Only include sections that make sense for the query.

Always include all available sources.
'''

    response = llm.invoke(prompt)

    return {
        'final_report' : response.content
    }