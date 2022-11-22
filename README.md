# Trading_Bot

## About
This repository is for a **python bot** that can send stock advice via email using the 50 and 20 day **EMA (Exponential Moving Average)** crossover points of a stock. This for me is a personal project that serves as an introduction into trading bot's and deploying code remotely in the cloud. The purpose of this code is to track a few stocks using EMA's, and send an email to the user when there is a crossover of these EMA's. A crossover indicates either a buying or selling point. 

![alt text](https://i.imgur.com/bgFnxIN.png)

Image Source: [Generating Trade Signals using Moving Average(MA) Crossover Strategy — A Python implementation](https://towardsdatascience.com/making-a-trade-call-using-simple-moving-average-sma-crossover-strategy-python-implementation-29963326da7a)

## References

The code was influenced by [Pratik Nabriya's article](https://towardsdatascience.com/making-a-trade-call-using-simple-moving-average-sma-crossover-strategy-python-implementation-29963326da7a): Generating Trade Signals using Moving Average(MA) Crossover Strategy — A Python implementation.


## Disclaimer
This project was done as a fun introduction into developing a trading bot, and **SHOULD NOT** be used
as financial advice in any way.

## Installation
The following code will install the necessary python packages required to run the code:
```
pip install yfinance numpy pandas
```
At the time of writing this I am using **python 3.7.10**, however other versions should work fine, as long as the packages listed above can be installed.
