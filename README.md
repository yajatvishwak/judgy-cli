# judgy-cli

judgy is a cli tool that rates your hackathon projects using the power of LLMs

## What you'll need

1. Project's Video submission
2. Project's Github code link
3. Project's PDF submission

## Judging criteria

1. Presentation
2. Originality
3. Business Value
4. Application of Technology

## How to use

1. Install all the packages

   `pip install -r requirements.txt`

2. Copy `.env.example` to `.env`, replace your OPENAI Keys in the `.env` file

3. Run Judgy Preprocess on a project

   `python cli.py judge`

4. Results are in form JSON files.

## Limitations

- Takes a while - 2 mins or so
- Costs approx 0.05 - 0.1 dollars per project
- Not always accurate
