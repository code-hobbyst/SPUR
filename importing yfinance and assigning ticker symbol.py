#import important libraries
import yfinance as yf
import pandas as pd
import time

ticker_symbol = "GOOGL"
data = yf.Ticker(ticker_symbol)
real_time_data = data.history(period="1d", interval="1m")
closing_prices = real_time_data['Close'].values

print("Closing Prices:", closing_prices)
print(real_time_data)
