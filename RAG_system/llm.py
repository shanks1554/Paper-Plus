import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_core.runnables import RunnableLambda

from RAG_system.config import LLM_MODEL_NAME

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
assert HF_TOKEN, "HF_TOKEN not found in environment"

_client = InferenceClient(
    model=LLM_MODEL_NAME,
    token=HF_TOKEN
)

def _hf_llm_call(prompt: str, **kwargs) -> str:
    if hasattr(prompt, "to_string"):
        prompt = prompt.to_string()

    response = _client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=0.2
    )

    return response.choices[0].message.content

def get_llm():
    return RunnableLambda(_hf_llm_call)
