from pydantic import BaseModel, Field

class ImprovePaperRequest(BaseModel):
    text: str = Field(..., min_length=50, description="Research paper text or section")
    rewrite: bool = Field(default=False, description="Whether to generate improved text")

class ImprovePaperResponse(BaseModel):
    analysis: str
    improved_text: str | None = None