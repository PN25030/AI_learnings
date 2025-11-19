import os
import google.generativeai as genai
from dotenv import load_dotenv
from weather_tool import get_current_weather

load_dotenv()

class WeatherAgent:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")
        
        genai.configure(api_key=api_key)
        # Use a model that supports function calling
        self.model = genai.GenerativeModel('gemini-2.0-flash', tools=[get_current_weather])
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def chat_with_agent(self, user_input):
        try:
            response = self.chat.send_message(user_input)
            return response.text
        except Exception as e:
            return f"An error occurred: {e}"
