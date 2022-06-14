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

    etf_data = fetch_data_for_tickers(us_etf_tickers)
    major_etfs = sort_order_df(etf_data, us_etf_tickers_names)
    print(tabulate(major_etfs, headers='keys', tablefmt='psql'))

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


def calculate_data_for_period(df: pd.DataFrame,
                              period_start_date: date,
                              period_end_date: date,
                              frame_label: str) -> pd.DataFrame:
    try:
        index_series = df.index.to_series()
        interval_filter = index_series \
            .between(str(period_start_date), str(period_end_date))
        filtered_df = df[interval_filter]
        lookback_days = len(filtered_df.index.to_series()) - 1
        return filtered_df \
            .pct_change(periods=lookback_days) \
            .apply(normalize_percent).tail(1).iloc[0] \
            .apply(format_percent).astype(str) \
            .to_frame(name=frame_label)
    except Exception:
        print("Something bad happened while processing data!")


def fetch_data_for_tickers(tickers):
    tickers = tickers if isinstance(
        tickers, (list, set, tuple)) else tickers.replace(',', ' ').split()

    today = date.today()
    df = pd.DataFrame(get_quotes(tickers))

    one_day_back = datetime \
        .datetime(today.year, today.month, today.day - 1).date()
    frame_one_day = calculate_data_for_period(df, one_day_back, today, "Today")

    one_month_back = datetime \
        .datetime(today.year, today.month - 1, today.day).date()
    frame_one_month = calculate_data_for_period(df, one_month_back, today, "1 Month")

    start_of_year = datetime.datetime(date.today().year, 1, 1).date()
    frame_ytd = calculate_data_for_period(df, start_of_year, today, "YTD")

    one_year_back = datetime.datetime(today.year - 1, today.month, today.day).date()
    frame_one_year = calculate_data_for_period(df, one_year_back, today, "1 Year")

    three_year_back = datetime.datetime(today.year - 3, today.month, today.day) \
        .date()
    frame_three_year = calculate_data_for_period(df, three_year_back, today, "3 Years")

    return pd.concat([frame_one_day,
                      frame_one_month,
                      frame_ytd,
                      frame_one_year,
                      frame_three_year],
                     axis=1).transpose()[us_etf_tickers]


def sort_order_df(df: pd.DataFrame, indexes: list) -> pd.DataFrame:
    df.loc["Index"] = indexes

    modified_column_names = column_names
    modified_column_names.insert(0, "Index")

    df = df.transpose()
    df['ETF'] = df.index
    df = df.reset_index(drop=True)

    final_df = df[modified_column_names]
    final_df.index += 1
    return final_df


print("\n\nWelcome to Sector ETFs Performance App.\n")
main()