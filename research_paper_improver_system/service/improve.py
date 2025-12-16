from research_paper_improver_system.llm.client import LLMClient
from research_paper_improver_system.llm.prompts import (
    analysis_prompt,
    improvement_prompt
)
from research_paper_improver_system.schemas.feedback import ImprovementFeedback

llm_client = LLMClient()

def improve_paper(text: str, rewrite: bool = False) -> ImprovementFeedback:
    # Step-1: Analysis
    analysis_text = analysis_prompt.invoke(
        {"text": text}
    ).to_string()
    
    analysis_output = llm_client.chat(analysis_text)
    
    # Step-2: Optional Improvement
    improved_text = None
    if rewrite:
        improvement_text = improvement_prompt.invoke(
            {
                "text": text,
                "feedback": analysis_output
            }
        ).to_string()
        
        improved_text = llm_client.chat(improvement_text)
    
    return ImprovementFeedback(
        analysis=analysis_output,
        improved_text=improved_text
    )