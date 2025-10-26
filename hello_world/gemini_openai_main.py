import time
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

from openai import OpenAI, InternalServerError

client = OpenAI(api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

max_retries = 3
retry_delay = 5  # seconds

for attempt in range(max_retries):
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert interviewer for the position of data engineer works on Google CLoud. You know in depth about the role and responsibilities of a data engineer. Help me interview for this role."
                },
                {"role": "user", "content": "Hello, gemini from OpenAI SDK! Please refer me as Piyush"}
            ],
            max_tokens=200,
            temperature=1.0,
        )
        print(response.message['content'])
        break
    except InternalServerError as e:
        print(f"Attempt {attempt + 1}: Model overloaded (503). Retrying in {retry_delay} seconds...")
        time.sleep(retry_delay)
else:
    print("Failed after multiple retries due to model overload (503).")

