from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()  # Loads variables from .env into environment

# Now you can access variables like this:
api_key = os.getenv("GEMINI_API_KEY")
client = OpenAI(api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

SYSTEM_PROMPT = """You are a expert AI Assistant resolving user queries using chain of thought. 
You work on START, PLAN and OUTPUT steps
You need to work on PLAN what needs to be done. The PLAN can have multiple steps.
Once you have the PLAN ready, you will work on OUTPUT step to give final answer.

RUlES: Strictly follow the below json output format:
- only run one step at a time.
- sequence of steps are START -> PLAN (can be multiple) -> OUTPUT(which will be displayed to user)
- Output should be in json format with three keys: 'START'where user gives input, 'PLAN' which can be multiple times and finally 'OUTPUT' which gives final answer.

OUTPUT FORMAT:
{
  "START": "user input here",
  "PLAN": [
      "step 1",
      "step 2",
      "...",
      "step n"
  ],
  "OUTPUT": "final answer here"
}
Example:
Q: How to reverse a string in Python?
A: 
{
  "START": "How to reverse a string in Python?",
  "PLAN": {"Step": "PLAN", "content":"seems like user wants help in specific programming language" },
          {"Step": "PLAN", "content":"find the best way to solve the problem using python" },
          {"Step": "PLAN", "content":"retun then best solution as output" },
  
  "OUTPUT": "You can reverse a string Output: !dlroW ,olleH""
}
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[{"role": "system", "content": SYSTEM_PROMPT},
              {"role": "user", "content": "Hello, write a code to add two numbers 100 and 300."},
              {"role": "json", "content": json.dumps({},
              {"role":"assistant", "content": "Sure! Let's start the process."}
              ]
)

print(response.choices[0].message.content)