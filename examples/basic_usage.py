import os
from dotenv import load_dotenv
from costtracker import track
from google import genai

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=api_key)

response=client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Hello there!"
)


track(response)