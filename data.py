from lib2to3.pgen2 import grammar
from msilib import sequence
from pytz import UTC
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

yf.pdr_override()

# download dataframe
stocks = {"MIPS.st": [], "EQT.st": [], "STOR-B.st": [], "ANOD-B.st": [], "ALIF-B.st": [], "THULE.st": [], "HEXA-B.st": [], "LAGR-B.st": [], "INDT.st": [],
          "EMBRAC-B.st": [], "SBB-B.st": [], "ADDT-B.st": [], "AAK.st": [], "BEIJ-B.st": [], "POOL": [], "LIFCO-B.st": [], "APG": [], "INSTAL.st": [], "XPEL": []}


def main():
    date = getDate()
    getClose(date)
    showRSI()


def getDate():
    date = datetime.now()
    date = str(date).split(" ")[0]
    return date


def getClose(date):
    for stock in stocks:
        movement = []
        data = pdr.get_data_yahoo(
            stock, start="2021-03-24", end=date)
        closes = data.loc[:, "Close"].values.tolist()
        for i in range(len(closes)):
            if i > 0:
                movement.append(closes[i]/closes[i-1])
        rsi = rsiCal(movement)
        stocks[stock] = rsi


def rsiCal(movement):
    i = 0
    avgGain = 0
    avgLoss = 0
    window_size = 14
    window = []
    RSI = []
    avgGainList = []
    avgLossList = []

    for mov in movement:
        window = movement[i - window_size: i]
<<<<<<< Updated upstream
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

if RSI[-1] > 70:
    ## send discord notif
    print("time to sell!")
if RSI[-1] < 30:
    ## send discord notif
    print("Time to buy!")
    print(RSI[-1])

=======
        if i >= window_size:
            for mov in window:
                if mov > 1:
                    avgGain += mov-1
                elif mov <= 1:
                    avgLoss -= mov-1
            avgGain = avgGain / window_size
            avgLoss = avgLoss / window_size
            avgGainList.append(avgGain)
            avgLossList.append(avgLoss)
            rsifunction = 100 - (100 / (1 + (avgGain/avgLoss)))
            RSI.append(rsifunction)
        i += 1
    return RSI


def showRSI():
    i = 0
    fig, axs = plt.subplots(19)
    fig.suptitle('Vertically stacked subplots')
    for stock in stocks:
        axs[i].plot(stocks[stock])
        i += 1
    plt.show()


main()
>>>>>>> Stashed changes


<<<<<<< Updated upstream
print(SMA)
fig, axs = plt.subplots(3)
fig.suptitle('INDU-C')
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
=======
"""
>>>>>>> Stashed changes
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
