from state import ResearchState
from config import llm


def writer_agent (state: ResearchState):
    prompt = f'''
    Generate a final research report
    Original Query :
    {state['query']}
    
    Findings :
    {state['findings']}

    Create : 
    Executive Summary
    Key Findings
    Comparison/Analysis 
    Final Conclusion

    Use markdown formatting. 
    '''

    response = llm.invoke(prompt)

    return {
        'final_report' : response.content
    }

