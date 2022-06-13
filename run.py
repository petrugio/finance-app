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


print("\n\nWelcome to Sector ETFs Performance App.\n")
main()