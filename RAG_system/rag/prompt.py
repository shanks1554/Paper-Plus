from langchain_core.prompts import PromptTemplate

CUSTOM_PROMPT_TEMPLATE = """
You are a research assistant answering questions using the source documents provided.

Use the context chunks below to produce a meaningful answer.
If context does not contain exact matching sentences, summarize patterns across the chunks.
If context suggests partial information, infer a supported conclusion.

Rules:
- Do NOT say "I don't know" unless no relevant context exists at all.
- Do NOT invent facts unrelated to the context.
- Cite concepts if present.

Context:
{context}

Question:
{question}

Helpful, detailed answer:
"""

def get_prompt():
    return PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )
