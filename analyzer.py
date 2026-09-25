"""
analyzer.py
Send ONE review to Jev via OpenRouter proxy gateway.
"""

import os
from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient
from questions import QUESTIONS, TOPICS

load_dotenv()

# Read from OpenRouter environment updates dynamically
api_key = os.getenv("TYPESAFE_API_KEY")
base_url = os.getenv("TYPESAFE_BASE_URL", "https://api.typesafe.ai")

client = TypeSafeClient(api_key=api_key, base_url=base_url)

MENTION_THRESHOLD = 0.5

def analyze_review(review_text):
    """Return a dict like {"Quality": 4.2, "Battery Life": 1.8}."""
    response = client.system_one(
        model="~typesafe/jev-latest",  # Adjusted for OpenRouter's model routing
        state=review_text,
        questions=QUESTIONS,
    )
    answers = response.answers

    ratings = {}
    for topic_name, topic_id in TOPICS.items():
        mentioned = answers[topic_id + "_mentioned"].noul

        if mentioned >= MENTION_THRESHOLD:
            level = answers[topic_id + "_rating"].score
            stars = level + 1  
            ratings[topic_name] = round(stars, 1)

    return ratings
