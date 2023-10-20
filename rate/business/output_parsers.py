from pydantic import BaseModel, Extra, Field



class MarketSize(BaseModel):
    audienceSize: str = Field(description="classification of 'audience size'")
    sizeReason: str = Field(
        description="reasoning behind your classification of audience size parameter"
    )
    valueToAudience: str = Field(description="classification of 'value to audience' ")
    valueReason: str = Field(
        description="reasoning behind your classification of value to audience parameter"
    )
    class Config:
        extra = Extra.ignore

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