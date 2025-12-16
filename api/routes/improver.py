from fastapi import APIRouter, HTTPException
from api.schemas.improver import (
    ImprovePaperRequest,
    ImprovePaperResponse
)
from research_paper_improver_system.service.improve import improve_paper

router = APIRouter(prefix="/improver", tags=["Research Paper Improver"])

@router.post("/improve-paper", response_model=ImprovePaperResponse)
def improve_paper_endpoint(request: ImprovePaperRequest):
    try:
        result = improve_paper(
            text=request.text,
            rewrite=request.rewrite
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )