import yfinance as yf
import pandas as pd
from datetime import datetime


def get_stock_data(symbol, start_date="2015-01-01"):
    """
    Fetch historical stock data for Indian stocks using yfinance
    """

    # Indian stocks need .NS
    if not symbol.endswith(".NS"):
        symbol = symbol + ".NS"

    print(f"Fetching data for {symbol}...")

    stock = yf.Ticker(symbol)
    df = stock.history(start=start_date)

    if df.empty:
        raise ValueError("No data found. Check stock symbol.")

    df.reset_index(inplace=True)

    # Clean column names
    df.columns = [col.lower() for col in df.columns]

    print("Data fetched successfully!")
    return df


def save_data(df, symbol):
    """
    Save stock data to CSV for reuse
    """
    filename = f"data/{symbol}_data.csv"
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def load_saved_data(symbol):
    """
    Load previously saved stock data
    """
    filename = f"data/{symbol}_data.csv"
    df = pd.read_csv(filename)
    return df


if __name__ == "__main__":
    symbol = input("Enter Indian stock symbol (e.g. TCS, RELIANCE): ").upper()
    data = get_stock_data(symbol)
    save_data(data, symbol)
