from fundamentals.sources.yfinance_source import fetch_yfinance_fundamentals
from fundamentals.sources.nse_source import fetch_nse_snapshot
from fundamentals.reconciler import reconcile_fundamentals


def score_fundamentals(ratios, confidence):
    score = 0

    if ratios["roe"] and ratios["roe"] > 0.15:
        score += 3
    if ratios["roa"] and ratios["roa"] > 0.07:
        score += 2
    if ratios["debt_to_equity"] and ratios["debt_to_equity"] < 1.5:
        score += 2
    if ratios["free_cash_flow"] and ratios["free_cash_flow"] > 0:
        score += 3

    adjusted_score = round(score * confidence, 1)

    if adjusted_score >= 7:
        view = "Strong Bullish"
    elif adjusted_score >= 4:
        view = "Neutral to Bullish"
    else:
        view = "Inconclusive"

    return adjusted_score, view


def run(symbol):
    yf_data = fetch_yfinance_fundamentals(symbol)
    nse_data = fetch_nse_snapshot(symbol)

    ratios, confidence = reconcile_fundamentals(yf_data)
    score, view = score_fundamentals(ratios, confidence)

    return {
        "Fundamental Score": f"{score} / 10",
        "Confidence Level": confidence,
        "Bias": view,
        "Ratios": ratios,
        "NSE Snapshot": nse_data
    }


if __name__ == "__main__":
    symbol = input("Enter Indian stock symbol: ").upper()
    result = run(symbol)

    print("\n===== MULTI-SOURCE FUNDAMENTAL REPORT =====")
    for k, v in result.items():
        print(f"{k}: {v}")
