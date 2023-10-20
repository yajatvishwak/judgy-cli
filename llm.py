from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI


class LLMModels:
    def __init__(self) -> None:
        pass

    def get_chat_model():
        return ChatOpenAI(
            temperature=0.01,
            model_name="gpt-3.5-turbo",
        )

    def get_openai_model():
        return OpenAI(
            temperature=0.01,
            model_name="gpt-3.5-turbo",
        )
