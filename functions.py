""" Functions class imports"""
# import time
import time
# import sys for animation
import sys
# import yahoo finance to fetch data
import yfinance as yf
# import pandas and numpy to process data from yahoo finance
import numpy as np
import pandas as pd
# import termcolor for adding color
from termcolor import colored


def normalize_percent(raw_input):
    """
    Normalizes the percent and displays 2 decimals places only
    """
    return round(raw_input * 100, 2)


def format_percent(raw_input: np.float64):
    """
    Colors the values red/green depending if positive or negative
    """
    if raw_input > 0:
        return colored(f"{raw_input} %", 'green')
    else:
        return colored(f"{raw_input} %", 'red')


def fetch_ticker_info(ticker: str):
    """
    Fetches the ticker information from yahoo finance

    Code inspired from
    https://marqueegroup.ca/resource/how-to-use-python-in-a-finance-environment/
    """
    ticker_data = yf.Ticker(ticker)
    info = ticker_data.info

    if 'shortName' not in info:
        return None

    fields = {'shortName': 'Company', 'bookValue': 'Book Value',
              'currency': 'Curr',
              'fiftyTwoWeekLow': '52W L', 'fiftyTwoWeekHigh': '52W H',
              'regularMarketPrice': 'Price',
              'regularMarketDayHigh': 'High', 'regularMarketDayLow': 'Low',
              'priceToBook': 'P/B', 'trailingPE': 'LTM P/E',
              'volume': 'Volume', 'sector': 'Sector'}
    all_results = {}
    single_result = {}
    for key in fields.keys():
        if key in info:
            single_result[fields[key]] = info[key]
        else:
            single_result[fields[key]] = "N/A"

    all_results["Info"] = single_result
    return pd.DataFrame.from_dict(all_results)
