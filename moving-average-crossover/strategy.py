import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def main():
    stock_data = fetch_stock_data("PLTR", "2015-01-01", "2024-01-01")
    stock_data['SMA_50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['SMA_200'] = stock_data['Close'].rolling(window=200).mean()


	# •	SMA_50 crosses above SMA_200 → Buy (Golden Cross)
	# •	SMA_50 crosses below SMA_200 → Sell (Death Cross)
	# •	Store signals as a new column (e.g. "Signal")
    stock_data['Signal'] = 0

    stock_data.loc[stock_data['SMA_50'] > stock_data['SMA_200'], 'Signal'] = 1
    stock_data.loc[stock_data['SMA_50'] < stock_data['SMA_200'], 'Signal'] = -1



    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Close'], label='Close Price', color='blue', alpha=0.6)
    plt.plot(stock_data['SMA_50'], label='50-Day SMA', color='orange', alpha=0.75)
    plt.plot(stock_data['SMA_200'], label='200-Day SMA', color='pink', alpha=0.75)

    # Identify signals
    stock_data['Crossover'] = stock_data['Signal'].diff()

    # Buy signal: Golden Cross (from -1 to 1)
    buy_signals = stock_data[stock_data['Crossover'] == 2]
    # Sell signal: Death Cross (from 1 to -1)
    sell_signals = stock_data[stock_data['Crossover'] == -2]

    # Plot buy/sell markers
    plt.plot(buy_signals.index, buy_signals['Close'], '^', markersize=10, color='green', label='Buy Signal')
    plt.plot(sell_signals.index, sell_signals['Close'], 'v', markersize=10, color='red', label='Sell Signal')

    # Final touches
    plt.title('PLTR Price with SMA Crossover Signals')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


    print(stock_data.tail(10))


def fetch_stock_data(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

if __name__ == "__main__":
    main()
