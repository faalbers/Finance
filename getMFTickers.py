import requests
from bs4 import BeautifulSoup
import json

url = 'https://finance.yahoo.com/screener/unsaved/7152162a-49ee-41cd-84fc-04b0f87dca4a?count=100&offset=0'

headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

count = int(soup.find('div', {'class': 'Fw(b) Fz(36px)'}).text)
print(count)
offset = 0

quotes = []

while True:
    url = 'https://finance.yahoo.com/screener/unsaved/8b2e1519-73f5-44a7-9638-4109f3713796?count=100&offset=%s' % offset
    print(offset)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    qlinks = soup.find_all('a', {'data-test': 'quoteLink'})
    for qlink in qlinks:
        quotes.append(qlink.text)
    if len(qlinks) < 100: break
    offset = offset + 100 

print(len(quotes))
with open('MF_USA_1STAR.json', 'w') as f:
    json.dump(quotes, f)