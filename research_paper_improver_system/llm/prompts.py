from langchain_core.prompts import PromptTemplate

analysis_prompt = PromptTemplate(
    input_variables=["text"],
    template="""
    You are an expert academic reviewer.

    Analyze the following research text and identify:

    1. Clarity issues
    2. Structural issues
    3. Academic tone issues
    4. Logical gaps or weak arguments

    Text:
    {text}

    Respond in clear bullet points under each category.
    """
)

improvement_prompt = PromptTemplate(
    input_variables=["text", "feedback"],
    template="""
    You are an academic writing assistant.

    Improve the following text based on the feedback below.

    Rules:
    - Preserve the original meaning
    - Maintain formal academic tone
    - Do not introduce new claims or data

    Feedback:
    {feedback}

    Original Text:
    {text}
    """
)