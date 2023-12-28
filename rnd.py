import os
from scrape import find_all
from openai import OpenAI


with open('links.txt', 'r') as f:
    links = f.read().split("\n")[:-1]

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

words = find_all(links)

with open("instructions.txt", "r") as f:
    instructions = f.read()

def api_call(word):
    response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role":"system", "content":instructions},
                {"role":"user", "content":word},
            ],
            top_p=0.8,
            max_tokens=300
            )

    return response.choices[0].message.content

print(api_call(words[1]))

