from langchain_core.prompts import PromptTemplate

CUSTOM_PROMPT_TEMPLATE = """
Use the pieces of information provided in the context to answer the user's question.
If you do not know the answer, say that you do not know.
Do not make up an answer.
Do not use information outside the given context.

Context:
{context}

Question:
{question}

Answer directly. No small talk.
"""

def get_prompt():
    return PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )
