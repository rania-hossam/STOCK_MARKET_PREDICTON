# Import packages
import os
import sys
import datetime
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
# Set date timestamps for historical data download
start_date = datetime.datetime(2018, 1, 1).date()
end_date = datetime.datetime.now().date()
start_date, end_date
end_date - start_date
ticker = "AKBNK.IS"
akbank = yf.Ticker(ticker)

data_directory = "data"
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

file_path = os.path.join(data_directory, f"{ticker}_historical_data.csv")

# Collect historical data with a daily interval
historical_data = yf.download(ticker, start=start_date, end=end_date, interval="1d")
historical_data.to_csv(file_path)

# Check the shape of the historical dataset
print(historical_data.shape)
