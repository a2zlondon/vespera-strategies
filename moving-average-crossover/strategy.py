import pandas as pd
import yfinance as yf

def main():
    stock_data = fetch_stock_data("PLTR", "2015-01-01", "2024-01-01")
    print(stock_data.head(5))


def fetch_stock_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

if __name__ == "__main__":
    main()
