""" Finance app imports """
# import os to help clear terminal
import os
# import termcolor for adding color
from termcolor import colored
# import tabulate to display data in a table
from tabulate import tabulate
# import functions and constants
from crawler import Crawler
from functions import fetch_ticker_info
from functions import loading_ticker
from constants import us_etf_tickers, us_etf_tickers_names
from constants import us_small_etf_tickers, us_small_etf_tickers_names
from constants import global_etf_tickers, global_etf_tickers_names


def main_menu():
    """
    Displays the main menu on the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print_main_menu()
    while True:
        try:
            choice = int(input("Enter Choice: [1,2,3,4]\n"))
        except ValueError:
            print("---------------")
            print(colored("You didn't enter a number !", 'red'))
            print("---------------")
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
            print("---------------")
            print(colored("Invalid choice !!!", 'red'))
            print("---------------")


def us_etf():
    """
    Displays the U.S. Sector ETF's on the terminal
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print("-U.S. Sector ETF's-")

    us_etfs = Crawler(us_etf_tickers, us_etf_tickers_names).fetch_data()
    print(tabulate(us_etfs, headers='keys', tablefmt='psql'))

    print_submenu()

    while True:
        try:
            choice = int(input("Enter Choice: [0,1,2,3,4]\n"))
        except ValueError:
            print("---------------")
            print(colored("You didn't enter a number !", 'red'))
            print("---------------")
            continue

        if choice == 0:
            main_menu()
            break
        elif choice == 1:
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
            print("---------------")
            print(colored("Invalid choice !!!", 'red'))
            print("---------------")


def us_small_etf():
    """
    Displays the U.S. Sector - Small Cap ETF's on the terminal
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print("-U.S. Sector - Small Cap ETF's-")

    us_etfs = Crawler(us_small_etf_tickers, us_small_etf_tickers_names)\
        .fetch_data()
    print(tabulate(us_etfs, headers='keys', tablefmt='psql'))

    print_submenu()

    while True:
        try:
            choice = int(input("Enter Choice: [0,1,2,3,4]\n"))
        except ValueError:
            print("---------------")
            print(colored("You didn't enter a number !", 'red'))
            print("---------------")
            continue

        if choice == 0:
            main_menu()
            break
        elif choice == 1:
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
            print(colored("Invalid choice !!!", 'red'))


def global_etf():
    """
    Displays the Global Sector ETF's on the terminal
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    print("-Global Sector ETF's-")

    us_etfs = Crawler(global_etf_tickers, global_etf_tickers_names)\
        .fetch_data()
    print(tabulate(us_etfs, headers='keys', tablefmt='psql'))

    print_submenu()

    while True:
        try:
            choice = int(input("Enter Choice: [0,1,2,3,4]\n"))
        except ValueError:
            print("---------------")
            print(colored("You didn't enter a number !", 'red'))
            print("---------------")
            continue

        if choice == 0:
            main_menu()
            break
        elif choice == 1:
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
            print("---------------")
            print(colored("Invalid choice!!!", 'red'))
            print("---------------")



def print_main_menu():
    """
    When called prints menu to terminal
    """
    print("-MAIN MENU-")
    print("---------------")
    print("1. U.S. Sector ETF's")
    print("2. U.S. Sector - Small Cap ETF's")
    print("3. Global Sector ETF's")
    print("4. Find instrument by ticker")
    print("---------------")


def print_submenu():
    """
    When called prints submenu to terminal
    """
    print("Navigation")
    print("---------------")
    print("0. MAIN MENU")
    print("1. U.S. Sector ETF's")
    print("2. U.S. Sector - Small Cap ETF's")
    print("3. Global Sector ETF's")
    print("4. Find instrument by ticker")
    print("---------------")


print("\n\nWelcome to Sector ETFs Performance App.\n")
main()