import json

data = {}

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)