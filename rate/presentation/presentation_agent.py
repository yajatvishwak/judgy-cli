from langchain.prompts import PromptTemplate
from langchain.output_parsers import OutputFixingParser
from langchain.output_parsers import PydanticOutputParser

from .output_parsers import MetricList
from .prompts import presentation_scoring_prompt, categories_rubric
from llm import LLMModels


import click
from commons.writer import writer


class PresentationAgent:
    def __init__(self, summary, presentation_video_length) -> MetricList:
        self.summary = summary
        self.presentation_video_length = presentation_video_length
        self.llm = LLMModels.get_openai_model()
        self.chat_llm = LLMModels.get_chat_model()

    def score(self):
        parser = PydanticOutputParser(pydantic_object=MetricList)
        prompt = PromptTemplate(
            template=presentation_scoring_prompt,
            input_variables=["ideasummary", "presentation_length"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        output = self.llm(
            prompt.format_prompt(
                ideasummary=self.summary,
                presentation_length=self.presentation_video_length,
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
    name="presentation",
    help="score the presentation of the project",
)
@click.option(
    "--summary",
    prompt="summary of the project (generated by judgy's preprocess command)",
    required=True,
    help="summary of the project (generated by judgy's preprocess command)",
)
@click.option(
    "--presentation_length",
    prompt="presentation length",
    required=True,
    help="presentation length",
)
@click.option(
    "--title",
    required=True,
    prompt="name of the project",
    help="name of the project",
)
@click.option(
    "--output_location",
    prompt="output location of the presentation results",
    help="output location of the  presentation results (leave blank, if you want to echo output to terminal)",
)
def presentation(summary, presentation_length, output_location, title):
    pa = PresentationAgent(
        presentation_video_length=presentation_length, summary=summary
    )
    output = pa.score()
    writer.write(output_location,title,output,"_presentation_scores.json")
    