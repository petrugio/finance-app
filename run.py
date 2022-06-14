import os
from tabulate import tabulate
from crawler import Crawler
from constants import us_etf_tickers, us_etf_tickers_names
from constants import us_small_etf_tickers, us_small_etf_tickers_names
from constants import global_etf_tickers, global_etf_tickers_names

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

    us_etfs = Crawler(us_etf_tickers, us_etf_tickers_names).fetch_data()
    print(tabulate(us_etfs, headers='keys', tablefmt='psql'))

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

    us_etfs = Crawler(us_small_etf_tickers, us_small_etf_tickers_names).fetch_data()
    print(tabulate(us_etfs, headers='keys', tablefmt='psql'))

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

    us_etfs = Crawler(global_etf_tickers, global_etf_tickers_names).fetch_data()
    print(tabulate(us_etfs, headers='keys', tablefmt='psql'))

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



print("\n\nWelcome to Sector ETFs Performance App.\n")
main()