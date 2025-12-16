from pydantic import BaseModel

class ImproverSettings(BaseModel):
    model_name: str = "meta-llama/Meta-Llama-3-8B-Instruct"
    max_tokens: int = 800
    temprature: float = 0.3

settings = ImproverSettings()