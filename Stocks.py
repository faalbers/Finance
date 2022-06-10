import pandas as pd
import yfinance as yf

# download daily stock prices for Tesla (TSLA) to a pandas DataFrame
dfa = yf.download("TSLA", start="2022-01-01", end="2022-05-27", interval="1d")
print(dfa.head())

# last 4 days
dfb = yf.download("TSLA", period='4d')
print(dfb.head())

# dividents for AT&T
t = yf.Ticker("T")
print(t.dividends)

dfa.loc[:, 'ma20'] = dfa.Close.rolling(20).mean()
dfa.loc[:, 'ma200'] = dfa.Close.rolling(200).mean()

dfa.plot()
