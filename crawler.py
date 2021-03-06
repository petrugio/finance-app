""" Crawler class imports """
# import datetime
import datetime
from datetime import date
# import yahoo finance to fetch data
import yfinance as yf
# import pandas to process data from yahoo finance
import pandas as pd
# import functions and constants
from constants import column_names
from functions import normalize_percent
from functions import format_percent


class Crawler:
    """
    Contains a set of functions to fetch, process, sort and display data
    """
    def __init__(self, tickers, ticker_names):
        """
        Check and formats the data
        """
        self.tickers = tickers if isinstance(
            tickers, (list, set, tuple)) else tickers.replace(',', ' ').split()
        self.ticker_names = ticker_names

    def fetch_data(self) -> pd.DataFrame:
        """
        Fetch abd sort data
        """
        etf_data = self.__fetch_data_for_tickers()
        return self.__sort_order_df(etf_data)

    def __fetch_data_for_tickers(self):
        """Fetch and calculate date for tickers"""
        today = date.today()
        df = pd.DataFrame(self.__get_quotes())

        frame_one_day = df.pct_change(periods=1) \
            .apply(normalize_percent).tail(1).iloc[0] \
            .apply(format_percent).astype(str) \
            .to_frame(name="Today")

        one_month_back = datetime \
            .datetime(today.year, today.month - 1, today.day).date()
        frame_one_month = self.\
            __calculate_data_for_period(df, one_month_back, today, "1 Month")

        start_of_year = datetime.datetime(date.today().year, 1, 1).date()
        frame_ytd = self.\
            __calculate_data_for_period(df, start_of_year, today, "YTD")

        one_year_back = datetime.\
            datetime(today.year - 1, today.month, today.day).date()
        frame_one_year = self.\
            __calculate_data_for_period(df, one_year_back, today, "1 Year")

        three_year_back = datetime.\
            datetime(today.year - 3, today.month, today.day) \
            .date()
        frame_three_year = self.\
            __calculate_data_for_period(df, three_year_back, today, "3 Years")

        return pd.concat([frame_one_day,
                          frame_one_month,
                          frame_ytd,
                          frame_one_year,
                          frame_three_year],
                         axis=1).transpose()[self.tickers]

    def __sort_order_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Sort and arrange the tickers
        """
        df.loc["Index"] = self.ticker_names

        modified_column_names = column_names.copy()
        modified_column_names.insert(0, "Index")

        df = df.transpose()
        df['ETF'] = df.index
        df = df.reset_index(drop=True)

        final_df = df[modified_column_names]
        final_df.index += 1
        return final_df

    # noinspection PyBroadException
    def __calculate_data_for_period(self,
                                    df: pd.DataFrame,
                                    period_start_date: date,
                                    period_end_date: date,
                                    frame_label: str) -> pd.DataFrame:
        """
        Calculates the data for the period
        """
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

    def __get_quotes(self):
        """
        Fetch ticker data from yahoo finance
        """
        return yf.download(
            self.tickers,
            period='3y',
            progress=False,
            interval="1d",
            rounding=2
        )['Adj Close']
