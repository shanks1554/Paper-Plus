from pydantic import BaseModel, Field
from typing import List, Optional

class SuggestPapersRequest(BaseModel):
    query: str = Field(..., min_length=10, description="Research Query")
    domains: List[str] = Field(..., description="List of domains to search")
    top_n: int = Field(default=5, ge=1, le=20)
    explain: bool = Field(default=True)

class SuggestPaper(BaseModel):
    paper: str
    score: float
    explain: Optional[str] = None

class SuggestPapersResponse(BaseModel):
    results: List[SuggestPaper]