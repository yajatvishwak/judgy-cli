originality_scoring_prompt = """
    Competitive analysis and project differentiation: 
    {similartools}

    This is project description : {ideasummary}
    Originality Scoring Rubric:

    Parameter 1 : Uniqueness : 

    1: Conventional, similar to existing solutions.
    2: Slightly different from existing solutions.
    3: Noticeably distinct from existing solutions.
    4: Fairly unique, sets itself apart.
    5: Completely novel, unlike anything seen before.

    Parameter 2 : Novelty :

    1: Offers no new concepts or methods.
    2: Introduces minor variations on existing concepts.
    3: Presents some new elements not widely explored.
    4: Introduces novel approaches and techniques.
    5: Presents entirely new and groundbreaking concepts.

    Parameter 3 : Creativity :

    1: Lacks creative thinking or innovation.
    2: Incorporates basic creative elements.
    3: Demonstrates creative combinations of ideas.
    4: Shows high levels of creativity and original thinking.
    5: Highly innovative and unconventional approach.

    Parameter 4 : Problem-Solving :

    1: Ineffective at solving the problem.
    2: Offers limited improvement over existing solutions.
    3: Provides noticeable improvements in addressing the problem.
    4: Effectively addresses the problem with innovative methods.
    5: Solves the problem in unexpected and transformative ways.

    Parameter 5 : Impact :

    1: Minimal impact on the field or industry.
    2: Offers slight improvements with limited industry impact.
    3: Has the potential to cause moderate changes in the industry.
    4: Could lead to significant shifts or improvements.
    5: Has the potential to completely transform the industry.

    Parameter 6 : Differentiation : 

    1: Hard to distinguish from existing solutions.
    2: Offers slight differentiation from competitors.
    3: Clearly stands out with noticeable differentiation.
    4: Highly differentiated from existing solutions.
    5: Completely distinct and unique compared to others.

    Parameter 7 : Applicability :

    1: Limited applicability beyond a specific context.
    2: Can be adapted to a few related contexts.
    3: Demonstrates potential for adaptation across various contexts.
    4: Highly adaptable and applicable in diverse settings.
    5: Can be applied creatively in unexpected and transformative ways.

    Parameter 8 : Industry Transformation

    1: Unlikely to cause any significant changes.
    2: May lead to minor changes in industry practices.
    3: Could result in notable shifts within the industry.
    4: Has the potential to substantially alter the industry landscape.
    5: Could revolutionize the industry and redefine norms.

    Parameter 9 : Out-of-the-Box Thinking

    1: Conforms to conventional wisdom and approaches.
    2: Incorporates minor departures from conventional methods.
    3: Demonstrates some unconventional thinking.
    4: Clearly reflects innovative and non-traditional approaches.
    5: Radically challenges norms and traditional methods.

    Parameter 10 : Unforeseen Outcomes

    1: Highly predictable outcomes, no surprises.
    2: Slight potential for unexpected results.
    3: Some potential for unforeseen developments.
    4: Significant potential for surprising and novel outcomes.
    5: High likelihood of generating groundbreaking and unforeseen results.

    Task: Where does this project belong? Give an explanation for why it belongs/does not belong to each category?
    Rule: Be critical, and judge without bias. DO NOT OVERLOOK ANY DETAILS.
    {format_instructions}

"""


similar_tools_prompt = """
            Project description:  {description}
            Task: Identify specific direct and indirect competitors of the project mentioned above, avoiding generic or broad categories.
            Output Format: 
            {format_instructions}
            """


categories_rubric = ["Poor", "Limited", "Adequate", "Strong", "Exceptional"]
