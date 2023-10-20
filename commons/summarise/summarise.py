from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

from llm import LLMModels

from .prompts import REFINE_PROMPT_TEMPLATE, SUMMARISE_PROMPT_TEMPLATE


class SummariseAgent:
    def __init__(self) -> None:
        self.llm = LLMModels.get_openai_model()
        pass

    def summarise(self, text):
        doc = Document(page_content=text, metadata={"source": "local"})
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents([doc])

        chain = load_summarize_chain(
            self.llm,
            chain_type="refine",
            verbose=False,
            question_prompt=SUMMARISE_PROMPT_TEMPLATE,
            refine_prompt=REFINE_PROMPT_TEMPLATE,
        )
        summary = chain.run(texts)
        return summary if summary else ""
