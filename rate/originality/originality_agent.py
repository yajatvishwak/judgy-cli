from langchain.prompts import PromptTemplate
from langchain.output_parsers import OutputFixingParser
from langchain.output_parsers import PydanticOutputParser

from .output_parsers import MetricList
from .prompts import originality_scoring_prompt, categories_rubric
from llm import LLMModels
from commons.similar_tool_agent.similar_tool_agent import SimilarToolsAgent


class OriginalityAgent:
    def __init__(self, summary) -> MetricList:
        self.summary = summary
        self.llm = LLMModels.get_openai_model()

    def score(self):
        parser = PydanticOutputParser(pydantic_object=MetricList)
        prompt = PromptTemplate(
            template=originality_scoring_prompt,
            input_variables=["ideasummary", "similartools"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        tools = SimilarToolsAgent(self.summary).get_similar_tools()
        similartools = ""
        try:
            for index, tool in enumerate(tools.listoftools):
                similartools += f"""
                {index + 1}.{tool.toolname}
                {tool.reason} \n
                """
        except:
            similartools = "No similar projects found"

        output = self.llm(
            prompt.format_prompt(
                ideasummary=self.summary,
                similartools=similartools,
            ).to_string()
        )
        try:
            metrics = parser.parse(output)
        except:
            fixing_parser = OutputFixingParser.from_llm(
                parser=parser, llm=self.chat_llm
            )
            metrics = fixing_parser.parse(output)

        total_score = 0
        for i in metrics.metrics:
            total_score += i.score

        final_score = total_score / len(metrics.metrics)
        rubric_index = max(0, min(int(final_score) - 1, len(categories_rubric) - 1))
        rubric_value = categories_rubric[rubric_index]
        return {
            "score": final_score,
            "category": rubric_value,
            "metrics": metrics.dict(),
            "tools": tools.dict(),
        }
