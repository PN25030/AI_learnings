from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

# Now you can access variables like this:
api_key = os.getenv("GEMINI_API_KEY")

from openai import OpenAI

client = OpenAI(api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# few shot prompt Definition:  Few examples are provided to the model to guide its responses.
system_prompt = """you are a coding expert. You should answer only coding related questions. FOr any non coding related questions, you should politely refuse to answer.
Rules:
1. Strictly answer in json format with two keys: 'question' and 'answer'.

example format:
{
  "question": "your question here",
  "answer": "your answer here"
}

here are some examples:
Q: How to reverse a string in Python?
A: You can reverse a string in Python using slicing:
```python
my_string = "Hello, World!"
reversed_string = my_string[::-1]
print(reversed_string)  # Output: !dlroW ,olleH
```
Q: What is the capital of France?
A: I'm sorry, but I can only answer coding related questions.
Q: How to create a virtual environment in Python?
A: You can create a virtual environment in Python using the `venv` module:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "system", "content": system_prompt},
        {"role": "user", "content": "Hello, write a code to add two numbers."}]
)

print(response.choices[0].message.content)