market_size_scoring_prompt = '''
Project Summary : {ideasummary}
    Parameters :
    Audience Market Size categories: 
    1. Small Market (Niche):
        Estimated Users/Revenue: Fewer than 10,000 users.
        Description: The app targets a very specific niche audience or solves a unique problem with limited market demand.
    2. Medium Market (Local/Regional):
        Estimated Users/Revenue: 10,000 to 100,000 users.
        Description: The app caters to a specific local or regional market with moderate demand.
    3. Large Market (National):
        Estimated Users/Revenue: 100,000 to 1 million users.
        Description: The app appeals to a broader national audience and has a substantial user base.
    4. Very Large Market (Global):
        Estimated Users/Revenue: 1 million to 100 million users.
        Description: The app has a global reach and serves a wide-ranging user base, potentially spanning multiple countries.
    5. Massive Market (Global Dominance):
        Estimated Users/Revenue: Over 100 million users.
        Description: The app has achieved global dominance and is widely adopted across the world, making it a major player in its industry.
    
    Value to Audience categories: 
    1. Essential:
        Apps in this category are vital for the daily lives or work of their target users.
        Users heavily rely on these apps to perform critical tasks.
        These apps often have no direct substitutes.
    2. Important:
        Apps in this category serve important functions for users.
        Users find them highly valuable and use them regularly.
        Replacing them would be inconvenient, but alternatives exist.
    3. Useful:
        These apps enhance users' experiences or provide valuable features.
        While not essential, users appreciate their convenience and utility.
        Users might use them occasionally.
    4. Nice-to-Have:
        Apps in this category offer additional features or entertainment.
        Users enjoy using them but can easily do without them.
        Replacing them with alternatives is straightforward.
    5. Dispensable:
        Apps in this category are of minimal significance to users.
        They might have been downloaded and forgotten.
        Users rarely or never use them.
    Task: Classify project into one category for each parameter. Also, give the reason for the classifcation.
    Rule: Be extremely critical, pessimistic, and classify without bias. DO NOT OVERLOOK ANY DETAILS. Be very strict and thorough 
    {format_instructions}
'''

business_scoring_prompt = '''
Project Summary : {ideasummary}
    Potential Market Size of Project : {marketsize}
    Potential Value to Audience of Project : {valuetoaudience}
    Business Impact Scoring Rubric :

    Parameter 1: Market Relevance:

    1: Little or no potential for practical or commercial viability. Not addressing a significant problem or market need.
    2: Some potential for business value. Uncertain market feasibility, scalability, or revenue generation. Address a niche market with limited demand.
    3: Shows reasonable business value. Addresses market need with potential to generate revenue. Require further development or validation.
    4: High business value, with clear market potential. Potential to attract a large customer base and generate significant revenue. Strong market feasibility and scalability.
    5: Stands out as having exceptional business value. Potential to disrupt the industry or create a new market. Presents a clear sustainable revenue generation and long-term business success.

    Parameter 2: Market Demand:

    1: Addresses a very limited or non-existent niche market.
    2: Targets a small market segment with uncertain demand.
    3: Addresses a defined market need with potential for growth.
    4: Targets a sizable market with strong demand.
    5: Addresses a significant and urgent market need with high demand potential.

    Parameter 3: Revenue Generation:

    1: Minimal to no potential for revenue generation.
    2: Uncertain revenue potential, limited monetization avenues.
    3: Demonstrates potential for revenue, requiring development.
    4: High potential for revenue generation.
    5: Clear path to significant and sustained revenue.

    Parameter 4: Scalability:

    1: Lacks scalability due to niche market or constraints.
    2: Limited scalability due to market limitations.
    3: Shows potential for moderate scalability.
    4: Demonstrates strong scalability potential.
    5: Highly scalable with potential for rapid expansion.

    Parameter 5: Customer Base:

    1: Attracts a very niche or limited customer base.
    2: Appeals to a small segment of potential customers.
    3: Addresses a defined customer segment with growth potential.
    4: Holds appeal for a broad customer base.
    5: Has potential to reach and captivate a vast and diverse customer audience.

    Parameter 6: Long-Term Viability:

    1: Unlikely to have sustainable long-term success.
    2: Potential for short-term viability, uncertain long-term prospects.
    3: Presents reasonable potential for ongoing success.
    4: Demonstrates strong long-term viability.
    5: Shows exceptional potential for enduring and thriving in the long run.

    Task: Classify project into one category for each parameter and Give an explanation for why it belongs/does not belong to each category?
    Rule: Be extremely critical, pessimistic, and classify without bias. DO NOT OVERLOOK ANY DETAILS. Be very strict and thorough 
    {format_instructions}

'''

categories_rubric = ["Poor", "Limited", "Adequate", "Strong", "Exceptional"]