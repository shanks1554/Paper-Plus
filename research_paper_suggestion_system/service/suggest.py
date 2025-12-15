from research_paper_suggestion_system.vector_db.loader import load_vector_dbs
from research_paper_suggestion_system.retrieval.retrieve_candidates import retrieve_candidate_chunks
from research_paper_suggestion_system.ranking.rank_papers import (
    aggregate_by_paper,
    score_papers
)
from research_paper_suggestion_system.llm.explain import explain_recommendation


def suggest_papers(
    query: str,
    domains: list[str],
    top_n: int = 5,
    explain: bool = True
):
    vector_dbs = load_vector_dbs(domains)

    docs = retrieve_candidate_chunks(query, vector_dbs, k=50)

    paper_chunks = aggregate_by_paper(docs)

    ranked_papers = score_papers(paper_chunks)

    results = []

    for item in ranked_papers[:top_n]:
        entry = item.copy()

        if explain:
            snippets = [
                d.page_content
                for d in paper_chunks[item["paper"]][:5]
            ]

            entry["explanation"] = explain_recommendation(
                query=query,
                paper_name=item["paper"],
                snippets=snippets
            )

        results.append(entry)

    return results
