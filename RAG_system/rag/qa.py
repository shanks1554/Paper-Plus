from RAG_system.rag.chain import create_qa_chain

def answer_question(question: str, domain: str):
    qa_chain = create_qa_chain(domain)
    return qa_chain.invoke({"query": question})
