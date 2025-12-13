from langchain_classic.chains import RetrievalQA

from RAG_system.vector_db.load_db import load_vector_db
from RAG_system.rag.prompt import get_prompt
from RAG_system.llm import get_llm
from RAG_system.config import DOMAIN_K

def create_qa_chain(domain: str):
    db = load_vector_db(domain)
    k = DOMAIN_K.get(domain, 10)

    return RetrievalQA.from_chain_type(
        llm=get_llm(),
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": k}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": get_prompt()}
    )
