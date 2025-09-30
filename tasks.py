from crewai import Task
from agents import socrates, spy , shakespeare , fabrizio
from datetime import datetime

find_topic = Task(
    description=f"""
    Analyze the latest AI trends and developments as of {datetime.now().strftime('%Y-%m-%d')}.
    Your primary goal is to identify a single, highly relevant and engaging topic
    that would captivate a tech-savvy audience on social media.

    Your analysis must focus on the absolute cutting-edge. Consider these sub-fields:
    - Generative AI (advances in models like LLMs, diffusion models, etc.)
    - Agentic AI and Autonomous Systems
    - Novel AI architectures and techniques
    - The release of significant new models or open-source tools.

    CRITICAL: Avoid broad, generic, or outdated topics. For example, do not suggest
    "What is AI?" or "The history of Transformers." The topic must be fresh, specific,
    and compelling for an audience that is already knowledgeable about AI.
    """,
    expected_output="""
    A single, well-defined topic idea in a structured format. The output MUST include:
    1. **Topic:** A concise, attention-grabbing headline.
    2. **Relevance:** A 2-3 sentence explanation of why this topic is critical and timely.
    3. **Key Angles:** A bulleted list of 3-4 specific points, questions, or facts that the Research Agent should investigate to gather compelling details.
    
    Example Output:
    ---
    Topic: The Emergence of Multi-Modal Agentic AI
    Relevance: Recent breakthroughs are allowing AI agents to not only understand text but also interpret images, audio, and video to perform complex tasks. This is a major leap towards more capable and autonomous systems.
    Key Angles:
    - How do models like Gemini 1.5 Pro process and reason across different data types?
    - What are the most impressive real-world use cases demonstrated in the last month?
    - What are the primary technical challenges or limitations of this technology?
    - Which new open-source projects are making this accessible to developers?
    ---
    """,
    agent=socrates
)

research = Task(
    description="""
    Take the topic outline provided by the Social Media Strategist and conduct a
    thorough investigation. Your primary goal is to gather detailed, factual, and
    up-to-date information for each of the "Key Angles" identified.

    Use your search tool to explore recent articles, technical blogs, and reputable
    news sources. You must find specific data, examples, or quotes that support
    the topic's relevance.

    CRITICAL: Do not just list links. Synthesize the information you find into
    concise, easy-to-digest bullet points. Your output is the raw material the
    writer will use, so its clarity and accuracy are paramount.
    """,
    expected_output="""
    A detailed research report formatted as a bulleted list. Each bullet point
    should be a self-contained, verifiable fact or key insight directly related
    to the topic's "Key Angles."

    The report must be comprehensive enough for the writer to draft a tweet
    without needing to do any further research. Include the source URL for any
    critical data points or quotes.

    Example Output:
    ---
    - According to a recent paper on ArXiv, multi-modal agents can achieve a 30% higher success rate on complex instruction-following tasks compared to text-only models (Source: http://arxiv.org/...).
    - Google's new "Project Astra" demo showcased an agent identifying objects through a phone camera and remembering their location in real-time (Source: http://googleblog.com/...).
    - The main challenge remains the high computational cost and latency of processing multiple data streams simultaneously (Source: http://techcrunch.com/...).
    ---
    """,
    agent=spy
)

tweet = Task(
    description="""
    Review the research report provided by the Senior Tech Analyst and craft a
    single, compelling tweet. Your goal is to distill the most interesting insight
    from the report into a format that is engaging and easy to share.

    Your tone must be authoritative yet accessible for a tech-savvy audience.
    Identify the single most impactful fact or idea in the research to use as a "hook."
    Ensure the tweet is concise, accurate, and adheres to the platform's best practices.

    CRITICAL: You MUST include 2-3 relevant and trending hashtags to maximize reach.
    Do not add any commentary or notes; your output must be the final tweet itself.
    """,
    expected_output="""
    A single, complete tweet, ready for publication. The tweet must be under 280
    characters. It should be grammatically correct, engaging, and contain 2-3
    appropriate hashtags.

    Example Output:
    ---
    Mind-blowing stuff happening in agentic AI. 🤯 New multi-modal agents can now see and hear, leading to a 30% jump in task success over text-only models.

    Google's Project Astra is already showing a glimpse of this future, with agents remembering object locations via a phone camera.

    #AI #AgenticAI #Tech
    ---
    """,
    agent=shakespeare
)

publish = Task(
    description="""
    Take the final tweet draft, which will be provided as context from the 
    previous task, and post it to X.com using your specialized tool.
    You MUST NOT alter the tweet's content in any way. Your final answer must
    be the confirmation message from your posting tool.
    """,
    expected_output="""
    A confirmation message indicating the successful posting of the tweet,
    including the Tweet ID.
    """,
    agent=fabrizio,
    context=[tweet]
)