import os
import openai
from dotenv import load_dotenv


load_dotenv('key.env')
key = os.getenv('key')

def chat_gpt(frase):

    os.environ['OPENAI_API_KEY'] = key
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[ { "role": "user", "content": frase } ]
    )
    chatgpt_response = response.choices[0].message.content
    print("Resposta: "+chatgpt_response)

    return chatgpt_response
