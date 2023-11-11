from langchain.prompts import PromptTemplate
from langchain.output_parsers import OutputFixingParser
from langchain.output_parsers import PydanticOutputParser

from .output_parsers import MarketSize, MetricList
from .prompts import market_size_scoring_prompt, business_scoring_prompt,categories_rubric
from llm import LLMModels

import click
from commons.writer.writer import write
class BusinessAgent:
    def __init__(self, summary) -> MetricList:
        self.summary = summary
        self.llm = LLMModels.get_openai_model()
        self.chat_llm = LLMModels.get_chat_model()

    def get_market_data(self):
        parser = PydanticOutputParser(pydantic_object=MarketSize)
        prompt = PromptTemplate(
            template=market_size_scoring_prompt,
            input_variables=["ideasummary"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        output = self.llm(
            prompt.format_prompt(
                ideasummary=self.summary,
            ).to_string()
        )
        try:
            market = parser.parse(output)
        except:
            fixing_parser = OutputFixingParser.from_llm(
                parser=parser, llm=self.chat_llm
            )
            market = fixing_parser.parse(output)
        return market
        
        

    def score(self):
        parser = PydanticOutputParser(pydantic_object=MetricList)
        prompt = PromptTemplate(
            template=business_scoring_prompt,
            input_variables=["ideasummary", "marketsize" , "valuetoaudience"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        market = self.get_market_data()
        output = self.llm(
            prompt.format_prompt(
                ideasummary=self.summary,
                marketsize=market.audienceSize,
                valuetoaudience=market.valueToAudience
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
        }



@click.command(
    name="business",
    help="score the business of the project",
)
@click.option(
    "--summary",
    prompt="summary of the project (generated by judgy's preprocess command)",
    required=True,
    help="summary of the project (generated by judgy's preprocess command)",
)
@click.option(
    "--title",
    required=True,
    prompt="name of the project",
    help="name of the project",
)
@click.option(
    "--output_location",
    prompt="output location of the results",
    help="output location of the  results (leave blank, if you want to echo output to terminal)",
)
def business(summary, output_location, title):
    pa = BusinessAgent(summary=summary)
    output = pa.score()
    write(output_location,title,output,"_business_scores.json")
        