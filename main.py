import os
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chat_log = [{"role": "system", "content": "You are a helpful assistant."}]


class UserInput(BaseModel):
    user_input: str
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def chat(user_input: UserInput):
    chat_log.append({"role": "user", "content": user_input.user_input})
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_log
)
    bot_response = completion.choices[0].message.content
    chat_log.append({"role": "assistant", "content": bot_response})
    
    return bot_response