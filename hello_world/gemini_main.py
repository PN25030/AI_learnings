from google import genai 
from dotenv import load_dotenv
import os
load_dotenv()  # Loads variables from .env into environment

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Hello, world!",

)

# print only the textual answer from the response (try common response shapes)
def _get_text(resp):
    try:
        return resp.candidates[0].content[0].text
    except Exception:
        pass
    try:
        return resp.candidates[0].content[0]
    except Exception:
        pass
    try:
        return resp.candidates[0].text
    except Exception:
        pass
    try:
        return resp.text
    except Exception:
        pass
    try:
        return resp.output
    except Exception:
        pass
    return str(resp)

print(_get_text(response))