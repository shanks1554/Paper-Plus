from fastapi import APIRouter, HTTPException
from api.schemas.qa import AskRequest, AskResponse, SourceDocument
from RAG_system.service.ask import ask

router = APIRouter(prefix="/qa", tags=["RAG Question Answering"])

@router.post("/ask", response_model=AskResponse)
def ask_question_endpoint(request: AskRequest):
    try:
        result = ask(
            question=request.question,
            domain=request.domain
        )
        
        sources = [
            SourceDocument(
                source=doc.metadata.get("source", "unknown"),
                content=doc.page_content
            )
            for doc in result["source_documents"]
        ]
        
        return AskResponse(
            answer=result["answer"],
            sources=sources
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )