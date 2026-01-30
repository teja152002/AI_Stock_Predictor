import yfinance as yf
import pandas as pd


def fetch_yfinance_fundamentals(symbol):
    if not symbol.endswith(".NS"):
        symbol += ".NS"

    stock = yf.Ticker(symbol)

    income = stock.financials
    balance = stock.balance_sheet
    cashflow = stock.cashflow

    def safe(df, keys):
        if df is None or df.empty:
            return None
        for k in keys:
            if k in df.index:
                val = df.loc[k].iloc[0]
                if pd.notna(val):
                    return val
        return None

    data = {
        "net_income": safe(income, ["Net Income", "Net Income Common Stockholders"]),
        "equity": safe(balance, ["Total Stockholder Equity", "Stockholders Equity"]),
        "assets": safe(balance, ["Total Assets"]),
        "liabilities": safe(balance, ["Total Liab", "Total Liabilities Net Minority Interest"]),
        "operating_cf": safe(cashflow, ["Total Cash From Operating Activities"]),
        "capex": safe(cashflow, ["Capital Expenditures"])
    }

    return data
