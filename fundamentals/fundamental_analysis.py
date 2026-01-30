# import yfinance as yf
# import pandas as pd


# def get_financials(symbol):
#     if not symbol.endswith(".NS"):
#         symbol += ".NS"

#     stock = yf.Ticker(symbol)
#     return stock.financials, stock.balance_sheet, stock.cashflow


# def get_value(df, possible_keys):
#     """
#     Try multiple possible row names safely
#     """
#     if df is None or df.empty:
#         return None

#     for key in possible_keys:
#         if key in df.index:
#             value = df.loc[key].iloc[0]
#             if pd.notna(value):
#                 return value
#     return None


# def calculate_ratios(income, balance, cashflow):
#     ratios = {}

#     net_income = get_value(income, [
#         "Net Income", "Net Income Common Stockholders"
#     ])

#     equity = get_value(balance, [
#         "Total Stockholder Equity", "Stockholders Equity"
#     ])

#     assets = get_value(balance, [
#         "Total Assets"
#     ])

#     liabilities = get_value(balance, [
#         "Total Liab", "Total Liabilities Net Minority Interest"
#     ])

#     operating_cf = get_value(cashflow, [
#         "Total Cash From Operating Activities"
#     ])

#     capex = get_value(cashflow, [
#         "Capital Expenditures"
#     ])

#     # ROE
#     ratios["roe"] = net_income / equity if net_income and equity else None

#     # ROA
#     ratios["roa"] = net_income / assets if net_income and assets else None

#     # Debt to Equity (proxy)
#     ratios["debt_to_equity"] = liabilities / equity if liabilities and equity else None

#     # Free Cash Flow
#     ratios["free_cash_flow"] = (
#         operating_cf - abs(capex)
#         if operating_cf and capex else None
#     )

#     return ratios


# def score_fundamentals(ratios):
#     score = 0
#     risks = []
#     data_missing = []

#     if ratios["roe"] is None:
#         data_missing.append("ROE data missing")
#     elif ratios["roe"] > 0.15:
#         score += 2
#     else:
#         risks.append("Low ROE")

#     if ratios["debt_to_equity"] is None:
#         data_missing.append("Debt data missing")
#     elif ratios["debt_to_equity"] < 1.5:
#         score += 2
#     else:
#         risks.append("High leverage")

#     if ratios["roa"] is None:
#         data_missing.append("ROA data missing")
#     elif ratios["roa"] > 0.07:
#         score += 2
#     else:
#         risks.append("Low asset efficiency")

#     if ratios["free_cash_flow"] is None:
#         data_missing.append("Cash flow data missing")
#     elif ratios["free_cash_flow"] > 0:
#         score += 2
#     else:
#         risks.append("Negative free cash flow")

#     # Adjust score if data missing
#     max_possible = 8
#     adjusted_score = round((score / max_possible) * 10, 1) if max_possible else 0

#     return adjusted_score, risks, data_missing


# def view_from_score(score):
#     if score >= 7:
#         return "Strong Bullish"
#     elif score >= 4:
#         return "Neutral to Bullish"
#     else:
#         return "Inconclusive / Data Limited"


# def run_fundamental_analysis(symbol):
#     income, balance, cashflow = get_financials(symbol)
#     ratios = calculate_ratios(income, balance, cashflow)
#     score, risks, missing = score_fundamentals(ratios)
#     bias = view_from_score(score)

#     return {
#         "Fundamental Score": f"{score} / 10",
#         "Long-Term Bias": bias,
#         "Ratios Used": ratios,
#         "Risks Identified": risks,
#         "Data Limitations": missing
#     }


# if __name__ == "__main__":
#     symbol = input("Enter Indian stock symbol (e.g. TCS, RELIANCE): ").upper()
#     result = run_fundamental_analysis(symbol)

#     print("\n===== FUNDAMENTAL ANALYSIS REPORT =====")
#     for k, v in result.items():
#         print(f"{k}: {v}")
