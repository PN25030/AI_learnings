import time
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

from openai import OpenAI, InternalServerError

client = OpenAI(api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


def get_weather(location: str):
    url=f"http://wttr.in/{location}fmt=3"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Could not retrieve weather data at this time."  


def main():
    user_query = "weather right now in Sangola?"
    response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[{"role": "user", "content": user_query}]
        )
    print(response.choices[0].message.content)

print(get_weather("New York"))
# weather right now in New York