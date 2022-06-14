import datetime
from datetime import date
import yfinance as yf
import pandas as pd

from constants import column_names
from functions import normalize_percent
from functions import format_percent


class Crawler:
    def __init__(self, tickers, ticker_names):
        self.tickers = tickers if isinstance(
            tickers, (list, set, tuple)) else tickers.replace(',', ' ').split()
        self.tickerNames = ticker_names

    def fetch_data(self) -> pd.DataFrame:
        etf_data = self.__fetch_data_for_tickers()
        return self.__sort_order_df(etf_data)

    def __fetch_data_for_tickers(self):
        today = date.today()
        df = pd.DataFrame(self.__get_quotes())

        one_day_back = datetime \
            .datetime(today.year, today.month, today.day - 1).date()
        frame_one_day = self.__calculate_data_for_period(df, one_day_back, today, "Today")
        # print(frame_one_day)

        one_month_back = datetime \
            .datetime(today.year, today.month - 1, today.day).date()
        frame_one_month = self.__calculate_data_for_period(df, one_month_back, today, "1 Month")
        # print(frame_one_month)

        start_of_year = datetime.datetime(date.today().year, 1, 1).date()
        frame_ytd = self.__calculate_data_for_period(df, start_of_year, today, "YTD")
        # print(frame_ytd)

        one_year_back = datetime.datetime(today.year - 1, today.month, today.day).date()
        frame_one_year = self.__calculate_data_for_period(df, one_year_back, today, "1 Year")
        # print(frame_one_year)

        three_year_back = datetime.datetime(today.year - 3, today.month, today.day) \
            .date()
        frame_three_year = self.__calculate_data_for_period(df, three_year_back, today, "3 Years")
        # print(frame_three_year)

        return pd.concat([frame_one_day,
                          frame_one_month,
                          frame_ytd,
                          frame_one_year,
                          frame_three_year],
                         axis=1).transpose()[self.tickers]

    def __sort_order_df(self, df: pd.DataFrame) -> pd.DataFrame:
        df.loc["Index"] = self.tickerNames

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
        return yf.download(
            self.tickers,
            period='3y',
            progress=False,
            interval="1d",
            rounding=2
        )['Adj Close']
