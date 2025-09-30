import os
import tweepy
from crewai.tools import tool
from dotenv import load_dotenv

@tool("Post a Tweet to X")
def post_tweet(tweet_text: str) -> str:
    """
    This tool takes a string of text and posts it as a tweet to the connected X account.
    It uses the credentials stored in the .env file to authenticate with the X API.
    It returns a confirmation message upon successful posting.
    """
    load_dotenv()

    client = tweepy.Client(
        consumer_key=os.getenv("API_KEY"),
        consumer_secret=os.getenv("API_KEY_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
    )

    try:
        response = client.create_tweet(text=tweet_text)
        return f"Tweet posted successfully! Tweet ID: {response.data['id']}"
    except Exception as e:
        return f"An error occurred while posting the tweet: {e}"