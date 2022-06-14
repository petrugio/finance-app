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

print("\n\nWelcome to Sector ETFs Performance App.\n")
main()