import json

quotes = []
with open('MF_USA_1STAR.json', 'r') as f:
    quotes = quotes + json.load(f)
with open('MF_USA_2STAR.json', 'r') as f:
    quotes = quotes + json.load(f)
with open('MF_USA_3STAR.json', 'r') as f:
    quotes = quotes + json.load(f)
with open('MF_USA_4STAR.json', 'r') as f:
    quotes = quotes + json.load(f)
with open('MF_USA_5STAR.json', 'r') as f:
    quotes = quotes + json.load(f)

quotes = set(quotes)
quotes = list(quotes)
quotes.sort()

with open('MF_USA_ALL.json', 'w') as f:
    json.dump(quotes, f)
