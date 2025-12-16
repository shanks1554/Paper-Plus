import os
from huggingface_hub import InferenceClient
from research_paper_improver_system.config.settings import settings
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self):
        token = os.getenv("HF_TOKEN")
        if not token:
            raise RuntimeError("HF_TOKEN not set")
        
        self.client = InferenceClient(
            model=settings.model_name,
            token=token
        )
    
    def chat(self, prompt: str) -> str:
        response = self.client.chat_completion(\
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=settings.max_tokens,
            temperature=settings.temprature
        )
        return response.choices[0].message.content