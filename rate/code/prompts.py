code_implementation_prompt = """
    Role: You are a classification bot
    Context:
    You are given a response from another bot about a project which looks at source code of a project and answers questions about the project features.
    The bot is asked the question about the source code : {question}
    The bot replies with : 

    Technical Feature Name: {feature_name}
    Technical Feature Explanation: {feature_description}

    -----
    Task: Classify the technical feature into "Implemented" or "Not Implemented" category.

    Categories:
    "Implemented" - "Technical feature explanation" explains how the feature work briefly
    "Not Implemented" - "Technical feature explanation" does not explain or mentions anything about feature, "I dont know", "I need human assistance" also fall under this category 

    -----
    Output format instructions:
    {format_instructions}
"""

# Task: List the core technical features this project claims to have implemented in code.
claimed_features_prompt = """
    Role: You are a technical hackathon judge
    Project Description : 
    {ideasummary}
    ----
    Given above is the description of a project you are judging.
    Task: List the features from the description that you would expect to be implemented in the project's code base
    Tone: Your responses should be in a question form. For example, "How is XYZ implemented in code?" or "Explain the implementation of XYZ" where XYZ is a technical feature 
    Quantity: List only up to four to five features
    Focus on:
        1. technical functionalities of the project
        2. features that are related to technology only
    Avoid and Ignore:
        1. Buzzwords
        2. Generic non-technical or non-code related claims
    Rule:
        Do not add just the technology name, instead respond with it's functionality mentioned.
    ----
    Output Format instructions:
    {format_instructions}
"""


categories_rubric = ["Poor", "Limited", "Adequate", "Strong", "Exceptional"]
