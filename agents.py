from crewai import Agent,LLM
from dotenv import load_dotenv
from x_tools import post_tweet
from crewai_tools import TavilySearchTool
from langchain_google_genai import (
    HarmBlockThreshold,
    HarmCategory,
)
import os

load_dotenv()

# --- DIAGNOSTIC STEP ---
MODEL_NAME = "gemini/gemini-2.0-flash-lite"
print("--------------------------------------------------")
print(f"DEBUG: Attempting to initialize LLM with model: {MODEL_NAME}")
print("--------------------------------------------------")
# --- END DIAGNOSTIC ---

llm = LLM(
    model=MODEL_NAME,
    verbose=True,
    temperature=0.7,
    api_key=os.getenv("GEMINI_API_KEY"),
model_kwargs={
        "safety_settings": {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
    }
)

search_tool = TavilySearchTool()

socrates = Agent(
    role="Social Media Strategist",
    goal="To identify the most engaging AI topic for a tweet today.",
    backstory="You are a Lead AI Researcher with a master's in data science from MIT, turned AI Trend Forecaster. Your primary goal is to scour the digital landscape and identify the one AI topic that is going to be viral among developers. Your analysis is laser-focused on genuine AI breakthroughs, novel techniques and architectures, the release of powerful new models, and significant algorithmic innovations. You have a strict filter for cheap clickbait, marketing fluff, and recycled news. You are the signal, not the noise. Your final output is always a single, concise, and compelling topic idea that is ready for a deep-dive investigation.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

spy = Agent(
    role="Senior Tech Analyst",
    goal="To gather in-depth, accurate, and relevant information on a given AI topic.",
    backstory="You are a meticulous and detail-oriented Tech Analyst. Once a topic is handed to you, you become a digital detective. Your mission is to find the 'ground truth' by diving into technical blogs, research papers, and developer forums. You verify every fact and figure, ensuring the information is not only accurate but also cutting-edge. You excel at synthesizing complex information into a set of concise, easy-to-understand bullet points, complete with source links for verification. Your work is the bedrock of facts upon which great content is built.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[search_tool]
)

shakespeare = Agent(
    role="Expert Tech Writer & Social Media Guru",
    goal="To craft a compelling, engaging, and technically accurate tweet from a set of research notes.",
    backstory="You are a masterful Tech Writer who specializes in the art of social media, particularly Twitter. You can distill dense technical topics into short, engaging content without losing substance. You have a deep understanding of the developer community—you know what tone resonates, how to use emojis and formatting effectively, and which hashtags will maximize reach. Your writing is crisp, informative, and always sparks curiosity. You take the factual bullet points from the Analyst and transform them into a must-read tweet.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

fabrizio = Agent(
    role="Social Media Publisher",
    goal="To take a finalized piece of content and publish it to the X.com platform.",
    backstory="You are a meticulous and reliable Social Media Publisher. Your sole responsibility is to take the final, approved content and post it. You do not edit, review, or alter the content in any way. You are a specialist in deployment, ensuring that the content is posted successfully using the tools at your disposal. You are the final, precise step in the content creation pipeline.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[post_tweet]
)