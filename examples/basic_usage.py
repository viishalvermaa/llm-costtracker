import os
from dotenv import load_dotenv
from costtracker import track
from openai import OpenAI

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client=OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response=client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages=[{
        "role":"user", 
        "content":"Hello there!"
        }]
)

track(response)