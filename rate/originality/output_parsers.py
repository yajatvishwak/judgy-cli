from pydantic import BaseModel, Extra, Field


class Metric(BaseModel):
    label: str = Field(description="name of the judging parameter")
    score: int = Field(description="assigned score of the judging parameter")
    reason: str = Field(
        description="justification of your assigned score for the judging parameter"
    )

    class Config:
        extra = Extra.ignore


class MetricList(BaseModel):
    metrics: list[Metric] = Field(description="List of all the judging parameters")

    class Config:
        extra = Extra.ignore


class SimilarTools(BaseModel):
    toolname: str = Field(description="name of the tool that is related to the project")
    reason: str = Field(
        description="explain how the tool is similar and dissimilar to the project"
    )

    class Config:
        extra = Extra.ignore


class SimilarToolsList(BaseModel):
    listoftools: list[SimilarTools] = Field(description="list of all the similar tools")

    class Config:
        extra = Extra.ignore
