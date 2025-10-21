from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

# Now you can access variables like this:
api_key = os.getenv("GEMINI_API_KEY")

from openai import OpenAI

client = OpenAI(api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

system_prompt = "you are a coding expert. You should answer only coding related questions. FOr any non coding related questions, you should politely refuse to answer."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "system", "content": system_prompt},
        {"role": "user", "content": "Hello, Tell me a joke."}]
)

print(response.choices[0].message.content)