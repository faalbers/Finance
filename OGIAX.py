import yfinance as yf

ticker = yf.Ticker('OGIAX')
tInfo = ticker.info

for key, data in tInfo.items():
    print('%s:' % key)
    print(data)
    print('-----------------------')
    
