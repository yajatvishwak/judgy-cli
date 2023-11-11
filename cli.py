import click
import json

from loaders import TextLoader

from dotenv import load_dotenv
from commons.transcribe.transcribe import Transcribe
from commons.pdfparser.pdfparser import PDFParser
from commons.summarise.summarise import SummariseAgent
from commons.videoutils.videoutils import VideoUtils
from commons.writer.writer import write

from rate.presentation.presentation_agent import presentation
from rate.business.business_agent import business
from rate.originality.originality_agent import originality
from rate.code.code_agent import code
import warnings
import os
import time




@click.group()
def cli():
    pass

@click.command(
    name="preprocess",
    help="get all the required data before calling any agent, returns transcription from the video, pdf content and summarization",
)
@click.option(
    "--video_link",
    required=True,
    prompt="location of the presentation video (.mp4 format only)",
    help="location of the presentation video (.mp4 format only)",
)
@click.option(
    "--pdf_link",
    required=True,
    prompt="location of the submission pdf (.pdf format only)",
    help="location of the submission pdf (.pdf format only)",
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
    help="output location of the results (leave blank, if you want to echo output to terminal)",
)
def preprocess(video_link, pdf_link, output_location, title):
    p = PDFParser()
    t = Transcribe()
    s = SummariseAgent()
    v = VideoUtils()
    video_length = v.get_video_length(video_link=video_link)
    transcription = t.get_transcription(video_link=video_link)
    pdf_content = p.get_pdf_content(pdf_link=pdf_link)
    summary = s.summarise(
        f"Video Transcript: {transcription}\n PDF Content: {pdf_content}"
    )

    output = {
        "transcription": transcription,
        "pdf_content": pdf_content,
        "summary": summary,
        "video_length": video_length,
    }
    write(output_location,title,output,"_preprocess.json")
    
@click.command(
    name="judge",
    help="get all the judging parameters",
)
@click.option(
    "--title",
    required=True,
    prompt="name of the project",
    help="name of the project",
)
@click.option(
    "--video_link",
    required=True,
    prompt="location of the presentation video (.mp4 format only)",
    help="location of the presentation video (.mp4 format only)",
)
@click.option(
    "--pdf_link",
    required=True,
    prompt="location of the submission pdf (.pdf format only)",
    help="location of the submission pdf (.pdf format only)",
)
@click.option(
    "--git_link",
    prompt="github link of the project",
    required=True,
    help="github link of the project",
)
@click.option(
    "--output_location",
    prompt="output location of the results",
    help="output location of the results",
)
@click.pass_context
def judge(ctx,output_location, title, git_link,pdf_link,video_link):
    start = time.time()
    loader = TextLoader()
    loader.start()
    output = {}
    ctx.invoke(preprocess,video_link=video_link, pdf_link=pdf_link, output_location=output_location, title=title)
    output["preprocess"] = json.load(open(os.path.join(output_location, title + "_preprocess.json"), "r"))
    summary = output["preprocess"]["summary"]
    video_length = output["preprocess"]["video_length"]
    ctx.invoke(presentation,summary=summary, presentation_length=video_length, output_location=output_location, title=title)
    output["presentation"] = json.load(open(os.path.join(output_location, title + "_presentation_scores.json"), "r"))
    
    ctx.invoke(originality,summary=summary, output_location=output_location, title=title)
    output["originality"] = json.load(open(os.path.join(output_location, title + "_originality_scores.json"), "r"))
    
    ctx.invoke(code,summary=summary, output_location=output_location, title=title, git_link=git_link, git_location=output_location)
    output["code"] = json.load(open(os.path.join(output_location, title + "_code_implementation_scores.json"), "r"))
    
    ctx.invoke(business,summary=summary, output_location=output_location, title=title)
    output["business"] = json.load(open(os.path.join(output_location, title + "_business_scores.json"), "r"))

    loader.stop()
    write(output_location,title,output,"_final_results.json")
    end= time.time()
    print(f"Took {start-end} seconds")
   

cli.add_command(preprocess)
cli.add_command(presentation)
cli.add_command(business)
cli.add_command(originality)
cli.add_command(code)
cli.add_command(judge)

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    load_dotenv()
    cli()
