from msilib import sequence
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd
import matplotlib.pyplot as plt


yf.pdr_override()  # <== that's all it takes :-)

# download dataframe

data = pdr.get_data_yahoo("INDU-C.st", start="2021-03-24", end="2022-03-24")

closes = data.loc[:, "Close"].values.tolist()

movement = []

i = 1
while i < len(closes):
    movement.append(closes[i]/closes[i-1])
    i += 1

SMA = data.loc[:, "Close"].rolling(20).mean()

avgGain = 0
avgLoss = 0

window_size = 14
window = []
RSI = []
avgGainList = []
avgLossList = []
smoothRSI = []

for i in range(len(movement) - window_size + 1):
    if i >= window_size:
        window = movement[i - window_size: i]
        for mov in window:
            if mov > 1:
                avgGain += mov-1
            elif mov <= 1:
                avgLoss -= mov-1
        avgGain = avgGain / window_size
        avgLoss = avgLoss / window_size
        avgGainList.append(avgGain)
        avgLossList.append(avgLoss)
        RSI.append(100 - (100 / (1 + (avgGain/avgLoss))))


# for i in range(len(RSI) - window_size + 1):
#     window = RSI[i + 1: i + window_size]
#     smoothRSI.append(
#         100 - (100 / (1 + ((avgGainList[i-1]*13+avgGainList[i])/(avgLossList[i-1]*13+avgLossList[i])))))
# avgGain = avgGain/14
# avgLoss = avgGain/14


fig, axs = plt.subplots(3)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(data.loc[:, "Close"], color="r", label="Close")
axs[0].plot(SMA, color="b", label="SMA")
axs[1].plot(movement, label="Average volatility", color="r")
axs[2].plot(RSI, label="RSI 14")
axs[2].plot(smoothRSI, label="Smooth RSI 14", color="r")


# plt.plot(data.loc[:,"Close"])
plt.show()

# ts = pd.Series(data.loc[:,"Close"], index=pd.date_range("1/1/2017", periods=1000))

# ts = ts.cumsum()

# ts.plot()


""""
msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
msft.financials
msft.quarterly_financials

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options

# show news
msft.news

# get option chain for specific expiration
# opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
"""
