import os
from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient, Noul

load_dotenv()

api_key = os.getenv("TYPESAFE_API_KEY")
base_url = os.getenv("TYPESAFE_BASE_URL", "https://typesafe.ai")

print(f"Connecting to: {base_url}")

client = TypeSafeClient(api_key=api_key, base_url=base_url)

# A simple 1-question check to verify the proxy connection
test_question = {
    "is_positive": Noul(instructions="Is this review overwhelmingly positive?")
}

try:
    response = client.system_one(
        model="~typesafe/jev-latest",
        state="I absolutely love this phone! The battery lasts for days and the display is gorgeous.",
        questions=test_question
    )
    print("Success! Jev Response:", response.answers["is_positive"].noul)
except Exception as e:
    print("Pipeline connection error:", e)
