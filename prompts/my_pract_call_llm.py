from urllib import response
"""
Module for making API calls to language models.

This module initializes an OpenAI client and sends a content generation request
to the Gemini 2.5 Flash Lite model with a specific prompt instruction.

Note: The API key should be stored securely as an environment variable
rather than hardcoded in the source code.
"""
import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.Client(api_key= os.getenv("OPENAI_API_KEY"))

response = client.models.generate_content(model="gemini-2.5-flash-lite",Content="Hello AI. Dont be descriptive.")
print(response)