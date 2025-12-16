from pydantic import BaseModel
from typing import Optional

class ImprovementFeedback(BaseModel):
    analysis: str
    improved_text: Optional[str] = None