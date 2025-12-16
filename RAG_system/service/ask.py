from RAG_system.rag.qa import answer_question

def ask(
    question: str,
    domain: str
):
    """
    Returns:
    {
        'answer': str,
        'source_documents': List[Document]
    }
    """
    result = answer_question(
        question=question,
        domain=domain
    )
    
    return {
        "answer": result["result"],
        "source_documents": result["source_documents"]
    }