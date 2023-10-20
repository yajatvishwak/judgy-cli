from pydantic import BaseModel, Field, Extra


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
