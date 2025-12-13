from langchain_community.vectorstores import FAISS
from RAG_system.embeddings import get_embedding_model
from RAG_system.config import DOMAIN_INDEX_PATHS

def load_vector_db(domain: str):
    if domain not in DOMAIN_INDEX_PATHS:
        raise ValueError(f"Unsupported domain: {domain}")

    return FAISS.load_local(
        DOMAIN_INDEX_PATHS[domain],
        get_embedding_model(),
        allow_dangerous_deserialization=True
    )
