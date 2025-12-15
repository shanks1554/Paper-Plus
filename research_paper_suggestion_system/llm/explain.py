from huggingface_hub import InferenceClient
from research_paper_suggestion_system.config.settings import HF_TOKEN

client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token=HF_TOKEN
)

def explain_recommendation(query, paper_name, snippets):
    context = "\n".join(snippets[:3])
    
    prompt = f"""
    User is researching: {query}
    
    Paper: {paper_name}
    
    Relevant excerpts:
    {context}
    
    Explain briefly why this paper is useful.
    """
    
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.3
    )
    
    return response.choices[0].message.content