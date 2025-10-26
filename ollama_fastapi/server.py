from typing import Union
from ollama import Client
from fastapi import FastAPI, Body

app = FastAPI()
client = Client(host="http://localhost:11434")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/contact")
def read_root():
    return {"email": "my@test.com", "phone": "123-456-7890"}

@app.post("/chat")  
def chat(message: str = Body(..., description="The message to send to the model")) -> Union[str, dict]:
    response = client.chat(
        model="gemma2:2b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.message['content']