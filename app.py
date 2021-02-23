'''
The following code was influenced by Pratik Nabriya's article written on Towards Datascience about SMA's and EMA's

This article can be found at the following link:

https://towardsdatascience.com/making-a-trade-call-using-simple-moving-average-sma-crossover-strategy-python-implementation-29963326da7a

The purpose of this code is to track a few stocks using a EMA, and send an email when there is a crossover which indicates
a buying or selling point. This project was done as a fun introduntion into developing a trading bot, and SHOULD NOT be used
as financial advice in any way.

'''


from send_email import email
import yfinance as yf
import numpy as np
import time

# A list of stocks you want to track
stocklist = ['ETH-USD', 'BTC-USD', 'AAPL', 'TSLA',
             'AMZN', 'BCH-USD', 'GOOGL', 'LTC-USD', 'XLM-USD']

short_ma = 20
long_ma = 50
period = '3mo'
emodel = email()


while True:

    for stock in stocklist:

        # Download the stock data for each day from yfinance
        stockdata = yf.download(tickers=stock, period=period, interval='60m')
        # We are going to use the close price as the predictor
        # Therefore we drop the rest of the tables
        stockdata = stockdata.drop(
            ['Volume', 'Open', 'High', 'Low', 'Adj Close'], axis=1)

        # Create the shorter exponential moving average column
        stockdata[f'{short_ma}_EMA'] = stockdata['Close'].ewm(
            span=short_ma, adjust=False).mean()
        # Create the longer exponential moving average column
        stockdata[f'{long_ma}_EMA'] = stockdata['Close'].ewm(
            span=long_ma, adjust=False).mean()

        stockdata['Signal'] = 0.0
        stockdata['Signal'] = np.where(
            stockdata[f'{short_ma}_EMA'] > stockdata[f'{long_ma}_EMA'], 1.0, 0.0)

        stockdata['Position'] = stockdata['Signal'].diff()

        # If the last entry indicates a buy or a sell, then send an email
        if(stockdata.iloc[-1]['Position'] == 1):
            subject = f'BUY {stock}'
            message = f"Hi Mitch,\n\nI just thought I would let you know that it may be a good idea to buy some {stock} stock.\n\nThe current price in USD is {round(stockdata.iloc[-1]['Close'],2)}.\n\nKind regards,\n\nMietsBot"
            print(subject)
            emodel.send_email(subject, message)
        elif(stockdata.iloc[-1]['Position'] == -1):
            subject = f'SELL {stock}'
            message = f"Hi Mitch,\n\nI just thought I would let you know that it may be a good idea to sell some {stock} stock.\n\nThe current price in USD is {round(stockdata.iloc[-1]['Close'],2)}.\n\nKind regards,\n\nMietsBot"
            print(subject)
            emodel.send_email(subject, message)
        else:
            # If we are holding then we do not want to send an email
            subject = f'HOLD {stock}'
            print(subject)

    time.sleep(3600)
