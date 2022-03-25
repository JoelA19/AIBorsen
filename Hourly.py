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

# data = pd.DataFrame(data)
    
newData = pd.DataFrame(data["Time Series (60min)"])
# print(newData)
# graphData = {}
# for k in newData:
#     graphData[k] = newData[k]["1. open"]

# .loc[:,"1. open"]

newData = newData.loc["1. open"]

# print(newData)

# temp_cols=newData.columns.tolist()
# new_cols=temp_cols[-1:] + temp_cols[:-1]
x=newData

# my_dict2 = {y:x for x,y in x.items()}


print(x.index)
print(x[0].index)

x = x.iloc[::-1]

plt.plot(x.index,x)

plt.show()