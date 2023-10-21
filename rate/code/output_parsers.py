from pydantic import BaseModel, Extra, Field


class ClaimedFeature(BaseModel):
    featureName: str = Field(description="technical feature question")

    class Config:
        extra = Extra.ignore


class ClaimedFeatureList(BaseModel):
    featureList: list[ClaimedFeature] = Field(
        description="List of all the technical features that are claimed in the project description"
    )

    class Config:
        extra = Extra.ignore


class FeaturesImplementation(BaseModel):
    featureName: str = Field(description="name of the feature")
    implementationStatus: str = Field(
        description="classification of the implementation of this feature"
    )
    explanation: str = Field(
        description="explanation of the features implementation, as is."
    )

    class Config:
        extra = Extra.ignore
