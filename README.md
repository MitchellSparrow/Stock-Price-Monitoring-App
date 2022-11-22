# Trading_Bot

## About
This repository is for a **python bot** that can send stock advice via email using the 50 and 20 day **EMA (Exponential Moving Average)** crossover points of a stock. This for me is a personal project that serves as an introduction into trading bot's and deploying code remotely in the cloud. The purpose of this code is to track a few stocks using EMA's, and send an email to the user when there is a crossover of these EMA's. A crossover indicates either a buying or selling point. 

![alt text](https://lh3.googleusercontent.com/yZ-iyhNhp2zs7t4pRKqPSKKdoRSPycxRUoEzLCfipp-FW_yh01JkcbA8RFPUFBC1eq5xqKEYCVBIlJmdD1_zX8t-YllJ-TzTkTfez4eE54teEbVkYaZcQssVL0n5KfkxiML7R1cMqoiTW8QBH3FPB-VLhfEZlG_dkXtmsZyaTqLN20MdRm4ZFqeKd4d4H1xKdCoy5bDHPIhtFhNz1ZLDm09g2aZogi61qv57ly2Pd9Jx5Eo92q6yqt_ebFPbTYmUOpUY-wmJQq1pi7RiFxq_e4j2xj4WkSnImyiZ2VWYJA1iLmgn13qSvO96ceD_dICkSkjUFlHPWhL9Z6Lo63vE7D0CgwLb-7GN34TpY3aG4F8fp8PeuvsFMLN41Oq-I0xeCNoGtzYSti0egs1bosYCLlW_JnTZm3uZFv0eRUpvGVfyz3JRAnwFhRD_YHMyVA5W5E-lwy1s-yOuKvquxToZHOem8VOSML-V56cTfWJqA4pGPuTmc9ki7e82yt68jtyPVwRqkzjMpZdEH22YjXYGQ9QYvVKOGp-ljUdzC3tDn9WsD4tuADQLtBBQO2Kzsu5bCDdOK9_Q-hwgsLZgH71COnx1djx2vn0Ex4dyrZ7brLhSuPue4tSTWS4IfQOu50Ng8jsIbicP8LHiXrDDv2vikPAr-GMC3lkWjc2iYv7Td8mTHGQswruzTcBtdPx1ICFrEK-EgkaQbDorepalvuZJEbrfPsiJlkZsrjpj-qpL1e9qrJEjR7jxC423gO82yB5y6mDg8V-ExEGmqCfH27HEDiXcJtnTaezXNSNkvBb9VvdxYVmxOQD9yYvL2h1b3UeR6VEwtQA6A6j5icoYqRNh89L-Ixo4g27R5GzdRfzFguNotHf3Yysh_ONfH4Vs36DzDlyb43b0Ds49NLU1haaAaHtA5xlImGPbLf-UPLV4wV_PEmhqwA=w1490-h734-no?authuser=0)

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
