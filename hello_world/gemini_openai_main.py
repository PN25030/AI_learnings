from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

# Now you can access variables like this:
api_key = os.getenv("GEMINI_API_KEY")

from openai import OpenAI

client = OpenAI(api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "system", "content": "You are an expert interviewer for the position of data engineer works on Google CLoud. You know in depth about the role and responsibilities of a data engineer. Help me interview for this role."},
        {"role": "user", "content": "Hello, gemini from OpenAI SDK! Please refer me as Piyush"}]
)
#print(response.schema)

print(response)
# Print token usage if available (total tokens)
# tokens = None
# if hasattr(response, "usage"):
#     tokens = getattr(response.usage, "total_tokens", None)
# elif isinstance(response, dict):
#     usage = response.get("usage")
#     if isinstance(usage, dict):
#         tokens = usage.get("total_tokens")

# print("Total tokens:", tokens if tokens is not None else "not available")

