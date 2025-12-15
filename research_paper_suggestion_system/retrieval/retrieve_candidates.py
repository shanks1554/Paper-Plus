def retrieve_candidate_chunks(query, vector_dbs, k=40):
    all_docs = []
    
    for domain, db in vector_dbs.items():
        docs = db.similarity_search(query, k=k)
        for d in docs:
            d.metadata['domain'] = domain
        all_docs.extend(docs)
    
    return all_docs