import numpy as np


def reconcile_fundamentals(yf_data):
    """
    AI-style reconciliation:
    - Ignore missing values
    - Normalize ratios
    - Penalize uncertainty
    """

    ratios = {}
    confidence = 1.0

    net_income = yf_data.get("net_income")
    equity = yf_data.get("equity")
    assets = yf_data.get("assets")
    liabilities = yf_data.get("liabilities")
    operating_cf = yf_data.get("operating_cf")
    capex = yf_data.get("capex")

    if net_income and equity:
        ratios["roe"] = net_income / equity
    else:
        ratios["roe"] = None
        confidence -= 0.2

    if net_income and assets:
        ratios["roa"] = net_income / assets
    else:
        ratios["roa"] = None
        confidence -= 0.2

    if equity and liabilities:
        ratios["debt_to_equity"] = liabilities / equity
    else:
        ratios["debt_to_equity"] = None
        confidence -= 0.2

    if operating_cf and capex:
        ratios["free_cash_flow"] = operating_cf - abs(capex)
    else:
        ratios["free_cash_flow"] = None
        confidence -= 0.2

    confidence = max(confidence, 0.2)

    return ratios, round(confidence, 2)
