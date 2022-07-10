import json

# https://www.morningstar.com/funds/xnas/RFNFX/quote

funds = []
with open('MF_USA_ALL.json', 'r') as f:
    funds = json.load(f)

for fund in funds:
    