from langchain.prompts import PromptTemplate

# -------------------------------------------------------------------------
summarise_prompt = """Write a concise summary of the following in such a way that all points from the text exist in your summary:
    {text}
    Make sure to include use of technology, statistics, claims, facts, market analysis, revenue details. Do not miss out on any points.
    CONCISE SUMMARY:"""

SUMMARISE_PROMPT_TEMPLATE = PromptTemplate.from_template(summarise_prompt)
# -------------------------------------------------------------------------
refine_prompt = (
    "You are a summarizer, Answer in third person."
    "Your job is to produce a final summary of 4-5 sentences\n"
    "We have provided an existing summary up to a certain point: {existing_answer}\n"
    "We have the opportunity to refine the existing summary"
    "(only if needed) with some more context below.\n"
    "Make sure to include use of technology, statistics, claims, facts, market analysis, revenue details mentioned. Do not miss out on any points."
    "------------\n"
    "{text}\n"
    "------------\n"
)

REFINE_PROMPT_TEMPLATE = PromptTemplate.from_template(refine_prompt)
# -------------------------------------------------------------------------
