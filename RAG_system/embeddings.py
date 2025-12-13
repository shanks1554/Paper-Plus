from langchain_huggingface import HuggingFaceEmbeddings
from RAG_system.config import EMBEDDING_MODEL_NAME

def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME
    )
