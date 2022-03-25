from msilib import sequence
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd
import matplotlib.pyplot as plt

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=2TIBEM3EFNEF8ZW3'
r = requests.get(url)
data = r.json()

# print(data)

data = pd.DataFrame(data)

print(data)
plt.show