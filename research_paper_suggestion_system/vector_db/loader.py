from langchain_community.vectorstores import FAISS
from research_paper_suggestion_system.embeddings.embedding_model import get_embedding_model
from research_paper_suggestion_system.vector_db.registry import DOMAIN_INDEX_PATHS

def load_vector_dbs(domains):
    embedding_model = get_embedding_model()
    vector_dbs = {}
    
    for domain in domains:
        if domain not in DOMAIN_INDEX_PATHS:
            raise ValueError(f"Unsupported domain: {domain}")
        
        vector_dbs[domain] = FAISS.load_local(
            DOMAIN_INDEX_PATHS[domain],
            embedding_model,
            allow_dangerous_deserialization=True
        )
    
    return vector_dbs