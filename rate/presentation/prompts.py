presentation_scoring_prompt = """
    Project Summary : {ideasummary}
    Presentation Length : {presentation_length}
    Scoring Rubric : 
    Parameter 1 : Problem Clarity:
    1: Problem description is absent or unclear.
    2: Problem is vaguely described and difficult to understand.
    3: Problem is adequately explained but lacks depth.
    4: Problem is well-communicated with clear context.
    5: Problem is articulated exceptionally, highlighting its significance.

    Parameter 2 : Solution Effectiveness:
    1: Solution is not presented or is unclear.
    2: Solution is presented but not effectively communicated.
    3: Solution is explained with basic details.
    4: Solution is well-explained, addressing the problem comprehensively.
    5: Solution is presented coherently and creatively, showing innovation.

    Parameter 3 : Communication Ease:
    1: Presentation is extremely difficult to understand.
    2: Presentation is somewhat difficult to follow.
    3: Presentation is clear but lacks engagement.
    4: Presentation is well-structured and easy to comprehend.
    5: Presentation is engaging, clear, and keeps the audience's attention.

    Parameter 4 : Presentation Length:
    1: Presentation is too short (< 1 minute) or too long (> 10 minutes).
    2: Presentation is very brief (< 3 minutes) and lacks details.
    3: Presentation is of appropriate length (3-5 minutes).
    4: Presentation effectively uses time to cover key points (3-5 minutes).
    5: Presentation uses time efficiently, maximizing impact (3-5 minutes).

    Parameter 5 : Value Proposition:
    1: Value proposition is unclear or missing.
    2: Value proposition is vaguely presented.
    3: Value proposition is stated but lacks depth.
    4: Value proposition is well-defined and highlights benefits.
    5: Value proposition is compelling, showcasing clear benefits.

    Parameter 6 : Market Understanding:
    1: No market analysis is included.
    2: Market analysis is insufficient or unclear.
    3: Basic market analysis is presented.
    4: Comprehensive market analysis is provided.
    5: Detailed market analysis with insights into target audience and competition.

    Parameter 7 : Monetization Strategy:
    1: Revenue strategy is missing.
    2: Revenue strategy is vaguely mentioned.
    3: Basic revenue strategy is outlined.
    4: Clear revenue strategy with potential income streams.
    5: Well-explained and innovative revenue strategy.

    Parameter 8 : Future Plans:
    1: No future goals or plans are discussed.
    2: Future plans are briefly mentioned.
    3: Basic future plans are outlined.
    4: Detailed future goals and plans are presented.
    5: Comprehensive and inspiring future roadmap.

    Parameter 9 : Competitive Analysis:
    1: No mention of strengths or uniqueness.
    2: Minimal insights into project's strengths.
    3: Basic strengths and uniqueness are highlighted.
    4: Clear differentiation from competitors is explained.
    5: Exceptional competitive analysis showcasing project's distinct strengths.
    
    Task: Classify project into one category for each parameter. Give an explanation for why it belongs/does not belong to each category?
    Rule: Be extremely critical, pessimistic, and classify without bias. DO NOT OVERLOOK ANY DETAILS. Be very strict and thorough
    {format_instructions}

"""

categories_rubric = ["Poor", "Limited", "Adequate", "Strong", "Exceptional"]
