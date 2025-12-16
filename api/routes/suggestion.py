from fastapi import APIRouter, HTTPException
from api.schemas.suggestion import (
    SuggestPapersRequest,
    SuggestPapersResponse
)
from research_paper_suggestion_system.service.suggest import suggest_papers

router = APIRouter(
    prefix="/suggestion",
    tags=["Research Paper Suggestion"]
)

@router.post("/suggest-papers", response_model=SuggestPapersResponse)
def suggest_papers_endpoint(request: SuggestPapersRequest):
    try:
        results = suggest_papers(
            query=request.query,
            domains=request.domains,
            top_n=request.top_n,
            explain=request.explain
        )
        return {"results": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
