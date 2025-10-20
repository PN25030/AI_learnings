from google import genai 
from dotenv import load_dotenv
import os
load_dotenv()  # Loads variables from .env into environment

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello, world!",
)

print(response)