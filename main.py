import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chat_log = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input()
    
    chat_log.append({"role": "user", "content": user_input})
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_log
)
    bot_response = completion.choices[0].message.content
    chat_log.append({"role": "assistant", "content": bot_response})
    print(bot_response)