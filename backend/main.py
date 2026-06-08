from fastapi import FastAPI
from pydantic import BaseModel
from graph import research_graph
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI (title = "Research Assistant Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",os.getenv('FRONTEND_URL')],
    allow_methods=["*"],
    allow_headers=["*"],
)

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
            'final_report': result["final_report"]
        }

    except Exception as e:

        return {
            "error": str(e)
        }