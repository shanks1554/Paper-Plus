from collections import defaultdict

def aggregate_by_paper(docs):
    papers = defaultdict(list)
    
    for doc in docs:
        source = doc.metadata.get('source', 'unknown')
        papers[source].append(doc)
    
    return papers

def score_papers(papers):
    ranked = []
    
    for paper, docs in papers.items():
        score = len(docs)
        domains = sorted(set(d.metadata['domain'] for d in docs))
        pages = sorted(
            set(d.metadata.get('page') for d in docs if d.metadata.get('page') is not None)
        )
        
        ranked.append({
            "paper": paper,
            "score": score,
            "domains": domains,
            "pages": pages[:5],
        })
    
    return sorted(ranked, key=lambda x: x['score'], reverse=True)