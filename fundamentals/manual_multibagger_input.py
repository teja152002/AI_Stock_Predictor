# manual_fundamentals = {
#     # Hindustan Copper
#     # Operating Margin (FY23–FY25 avg: 29%, 32%, 36%)
#     "opm_3y": 32.3,

#     # EPS
#     "eps_3y_ago": 3.87,          # FY22 EPS
#     "eps_latest": 5.93,          # TTM EPS

#     # Capital structure
#     "debt_to_equity": 0.05,

#     # Profitability (3Y averages)
#     "roe_3y": 16.0,              # FY23–FY25 avg
#     "roce_3y": 18.0,             # FY23–FY25 avg

#     # Latest profitability
#     "net_profit": 574,           # ₹ Cr (TTM)
#     "interest": 5,               # ₹ Cr (TTM)

#     # Promoter holding
#     "promoter_holding_3y_ago": 66.14,   # Mar 2022
#     "promoter_holding_latest": 66.14,   # Dec 2025

#     # Cash flows
#     "operating_cf_latest": 544,  # ₹ Cr (FY25)

#     # Asset growth
#     "total_assets_3y_ago": 3164, # Mar 2022
#     "total_assets_latest": 3711, # Mar 2025

#     # Growth rates (from Screener)
#     "sales_cagr_10y": 7,
#     "sales_cagr_5y": 20,
#     "sales_cagr_3y": 4,

#     "profit_cagr_10y": 22,
#     "profit_cagr_5y": 23,
#     "profit_cagr_3y": 8
# }


manual_fundamentals = {
    # Operating Margin (NOT applicable for banks)
    "opm_3y": None,

    # EPS
    "eps_3y_ago": 34.31,          # FY22 EPS
    "eps_latest": 48.54,          # TTM EPS

    # Capital structure (banking specific – high leverage is normal)
    "debt_to_equity": 6.20,

    # Profitability (3Y averages from Screener)
    "roe_3y": 16.0,               # FY23–FY25 avg ROE
    "roce_3y": None,              # ROCE not meaningful for banks

    # Latest profitability
    "net_profit": 77430,          # ₹ Cr (TTM)
    "interest": 187257,           # ₹ Cr (TTM interest expense)

    # Promoter holding
    "promoter_holding_3y_ago": 0.00,    # Mar 2022
    "promoter_holding_latest": 0.00,    # Dec 2025

    # Cash flows
    "operating_cf_latest": 127242,      # ₹ Cr (FY25)

    # Asset growth
    "total_assets_3y_ago": 2122934,     # Mar 2022
    "total_assets_latest": 4392110,     # Mar 2025

    # Growth rates (from Screener)
    "sales_cagr_10y": 21,
    "sales_cagr_5y": 22,
    "sales_cagr_3y": 35,

    "profit_cagr_10y": 21,
    "profit_cagr_5y": 21,
    "profit_cagr_3y": 23
}
