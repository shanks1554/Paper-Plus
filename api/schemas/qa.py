from pydantic import BaseModel, Field
from typing import List

class AskRequest(BaseModel):
    question: str = Field(..., min_length=10)
    domain: str = Field(..., description="Single domain to query")

class SourceDocument(BaseModel):
    source: str
    content: str

class AskResponse(BaseModel):
    answer: str
    sources: List[SourceDocument]