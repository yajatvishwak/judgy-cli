from llm import LLMModels
from langchain.agents import Tool
from langchain.tools import DuckDuckGoSearchRun
from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain.prompts import PromptTemplate

from langchain.agents import AgentExecutor
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent

from .output_parsers import SimilarToolsList
from .prompts import similar_tools_prompt


class SimilarToolsAgent:
    def __init__(self, summary) -> None:
        self.summary = summary
        search = DuckDuckGoSearchRun()
        self.tools = [
            Tool(
                name="search",
                func=search.run,
                description="Useful for when you need to answer questions about current events. You should ask targeted questions",
            ),
        ]
        self.llm = LLMModels.get_chat_model()

    def get_similar_tools(self):
        system_message = SystemMessage(
            content="You are a seasoned online market researcher skilled at efficiently and effectively identifying competitive products through thorough online searches"
        )
        prompt = OpenAIFunctionsAgent.create_prompt(system_message=system_message)
        search_agent = OpenAIFunctionsAgent(
            llm=self.llm, tools=self.tools, prompt=prompt
        )
        agent_executor = AgentExecutor(
            agent=search_agent, tools=self.tools, verbose=True
        )
        parser = PydanticOutputParser(pydantic_object=SimilarToolsList)
        pp = PromptTemplate(
            template=similar_tools_prompt,
            input_variables=["description"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        gg = agent_executor.run(pp.format_prompt(description=self.summary))
        try:
            similartools = parser.parse(gg)
        except:
            fixing_parser = OutputFixingParser.from_llm(parser=parser, llm=self.llm)
            similartools = fixing_parser.parse(gg)

        return similartools
