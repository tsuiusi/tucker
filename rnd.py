import os
from scrape import find_all

with open('links.txt', 'r') as f:
    links = f.read().split("\n")[:-1]
print(links)
words = find_all(links)
print(words)

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


