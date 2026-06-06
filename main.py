from fastapi import FastAPI
from pydantic import BaseModel
from graph import research_graph

app = FastAPI (title = "Research Assistant Agent")

class ResearchRequest(BaseModel):
    query : str


@app.post("/research")
def research(request: ResearchRequest):

    try:

        result = research_graph.invoke(
            {
                'query': request.query
            }
        )

        return {
            'query': result["query"],
            'complexity': result["complexity"],
            'report': result["final_report"]
        }

    except Exception as e:

        return {
            "error": str(e)
        }