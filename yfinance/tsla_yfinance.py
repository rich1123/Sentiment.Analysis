import yfinance as yf
import numpy as np
import pandas as pd


# enter ticker for Tesla
tsla = yf.Ticker("TSLA")


# get stock info
tsla.info


# create pandas df
df_pandas = tsla.history(start="2020-04-14", end="2020-05-15")
df_pandas = df_pandas.drop(['Dividends', 'Stock Splits'], axis=1)
df_pandas = df_pandas.reset_index( )


# Create new columns for change in prices
df_pandas['Dollar_Change'] = df_pandas.Close.diff()
df_pandas['Percent_Change'] = df_pandas.Close.pct_change().round(4)


# Fill in na cells with 0
df_pandas = df_pandas.fillna(0)


# Export data into CSV
df_pandas.to_csv('tsla_yfinance.csv')