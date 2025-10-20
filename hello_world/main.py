from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

# Now you can access variables like this:
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="o3",
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message.content)