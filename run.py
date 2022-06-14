import yfinance as yf
import datetime
from datetime import date
import pandas as pd
import numpy as np
import colorama as cm
from termcolor import colored
import os
from tabulate import tabulate

def main_menu():
    """
    Displays the main menu on the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-MAIN MENU-")
    print("---------------")
    print("1. U.S. Sector ETF's")
    print("2. U.S. Sector - Small Cap ETF's")
    print("3. Global Sector ETF's")
    print("4. Find instrument by ticker")
    print("---------------")
    while True:
        try:
            choice = int(input("Enter Choice: \n"))
        except ValueError:
            print("You didn't enter a number !")
            continue

        if choice == 1:
            us_etf()
            break
        elif choice == 2:
            us_small_etf()
            break
        elif choice == 3:
            global_etf()
            break
        elif choice == 4:
            find_by_ticker()
            break
        else:
            print("Invalid choice !!!")

def main():
    """
    Run all program functions
    """
    main_menu()


def us_etf():
    """
    Displays the U.S. Sector ETF's on the terminal
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print("-U.S. Sector ETF's-")

    etf = yf.download(
        'XLB XLC XLY XLP XLE XLF XLV XLI XLK XLU XLRE',
        period='1wk',
        progress=False,
        interval="1d",
        rounding=2
    )

    print(etf['Adj Close'].to_markdown(tablefmt="grid"))
    print("---------------")
    print("0. MAIN MENU")
    print("---------------")

    while True:
        try:
            choice = int(input("Enter Choice: \n"))
        except ValueError:
            print("You didn't enter a number !")
            continue

        if choice == 0:
            main_menu()
            break
        else:
            print("Invalid choice !!!")


def us_small_etf():
    """
    Displays the U.S. Sector - Small Cap ETF's on the terminal
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print("-U.S. Sector - Small Cap ETF's-")
    print("---------------")
    print("0. MAIN MENU")
    print("---------------")
    while True:
        try:
            choice = int(input("Enter Choice: \n"))
        except ValueError:
            print("You didn't enter a number !")
            continue

        if choice == 0:
            main_menu()
            break
        else:
            print("Invalid choice !!!")


def global_etf():
    """
    Displays the Global Sector ETF's on the terminal
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print("-Global Sector ETF's-")
    print("---------------")
    print("0. MAIN MENU")
    print("---------------")
    while True:
        try:
            choice = int(input("Enter Choice: \n"))
        except ValueError:
            print("You didn't enter a number !")
            continue

        if choice == 0:
            main_menu()
            break
        else:
            print("Invalid choice !!!")

cm.init()
today = date.today()

column_names = [
    "ETF",
    "Today",
    "1 Month",
    "YTD",
    "1 Year",
    "3 Years"
]

us_etf_tickers = ['XLB', 'XLC', 'XLY',
                  'XLP', 'XLE', 'XLF',
                  'XLV', 'XLI', 'XLK',
                  'XLU', 'XLRE']

us_small_etf_tickers = ['PSCD', 'PSCC', 'PSCH',
                        'PSCF', 'PSCE', 'PSCI',
                        'PSCM', 'PSCU', 'PSCT']

global_etf_tickers = ['MXI', 'JXI', 'RXI',
                      'KXI', 'IXC', 'IXG',
                      'IXJ', 'EXI', 'IXN', 'IXP']

us_etf_tickers_names = [
    'Basic Materials',
    'Communication Services',
    'Consumer Discretionary',
    'Consumer Staples',
    'Energy',
    'Financial Services',
    'Healthcare',
    'Industrial',
    'Technology',
    'Utilities',
    'Real Estate',
]

us_small_etf_tickers_names = [
    'Consumer Discretionary',
    'Consumer Staples',
    'Healthcare',
    'Financials',
    'Energy',
    'Industrials',
    'Basic Materials',
    'Utilities',
    'Technology'
]

global_etf_tickers_names = [
    'Basic Materials',
    'Utilities',
    'Consumer Discretionary',
    'Consumer Staples',
    'Energy',
    'Financial Services',
    'Healthcare',
    'Industrial',
    'Technology',
    'Telecommunications'
]
def normalize_percent(raw_input):
    return round(raw_input * 100, 2)


def format_percent(raw_input: np.float64):
    if raw_input > 0:
        return colored(f"{raw_input} %", 'green')
    else:
        return colored(f"{raw_input} %", 'red')


def get_quotes(tickers):
    return yf.download(
        tickers,
        period='3y',
        progress=False,
        interval="1d",
        rounding=2
    )['Adj Close']

df = pd.DataFrame(get_quotes(us_etf_tickers))

series_daily = df\
    .pct_change(periods=1) \
    .apply(normalize_percent) \
    .tail(1).iloc[0]
one_month_back = datetime\
    .datetime(today.year, today.month - 1, today.day).date()
index_series_month = df.index.to_series()
interval_filter_month = index_series_month\
    .between(str(one_month_back), str(today))
filtered_df_month = df[interval_filter_month]
lookback_days_one_month = len(filtered_df_month.index.to_series()) - 1
series_one_month = filtered_df_month\
    .pct_change(periods=lookback_days_one_month)\
    .apply(normalize_percent).tail(1).iloc[0]

start_of_year = datetime.datetime(date.today().year, 1, 1).date()
index_series_ytd = df.index.to_series()
interval_filter = index_series_ytd.between(str(start_of_year), str(today))
filtered_df = df[interval_filter]
lookback_days = len(filtered_df.index.to_series()) - 1
series_ytd = filtered_df.pct_change(periods=lookback_days)\
    .apply(normalize_percent).tail(1).iloc[0]

one_year_back = datetime.datetime(today.year - 1, today.month, today.day).date()
index_series_year = df.index.to_series()
nterval_filter_year = index_series_year\
    .between(str(one_year_back), str(today))
filtered_df_year = df[interval_filter_year]
lookback_days_one_year = len(filtered_df_year.index.to_series()) - 1
series_one_year = filtered_df_year.pct_change(periods=lookback_days_one_year)\
    .apply(normalize_percent).tail(1).iloc[0]

three_year_back = datetime.datetime(today.year - 3, today.month, today.day)\
    .date()
index_series_three_year = df.index.to_series()
interval_filter_three_year = index_series_three_year\
    .between(str(three_year_back), str(today))
filtered_df_three_year = df[interval_filter_three_year]
lookback_days_three_year = len(filtered_df_three_year.index.to_series()) - 1
series_three_year = filtered_df_three_year\
    .pct_change(periods=lookback_days_three_year)\
    .apply(normalize_percent).tail(1).iloc[0]


print("\n\nWelcome to Sector ETFs Performance App.\n")
main()