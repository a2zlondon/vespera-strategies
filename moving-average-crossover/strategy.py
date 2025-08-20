import pandas as pd
import yfinance as yf

def main():
    stock_data = fetch_stock_data("PLTR", "2015-01-01", "2024-01-01")
    stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()
    print(stock_data.tail(10))


def fetch_stock_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

if __name__ == "__main__":
    main()
