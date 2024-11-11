import os
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from typing import Annotated

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chat_log = [{"role": "system", "content": "You are a helpful assistant."}]

app = FastAPI()

@app.post("/")
async def chat(user_input: Annotated[str, Form()]):
    chat_log.append({"role": "user", "content": user_input})
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_log
)
    bot_response = completion.choices[0].message.content
    chat_log.append({"role": "assistant", "content": bot_response})
    
    return bot_response