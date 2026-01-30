import pandas as pd

# -----------------------------
# IMPORT MODULES
# -----------------------------
from data.data_loader import get_stock_data
from technicals.technical_indicators import add_technical_indicators
from technicals.technical_analysis import analyze_technical

from fundamentals.fundamental_router import (
    run_fundamentals,
    print_fundamental_report
)

from forecasting.price_forecaster import generate_forecast
from decision_engine.buy_hold_sell_engine import decide_action
from strategies.swing_strategy import simulate_swing_strategy, performance_metrics


# -----------------------------
# MAIN ORCHESTRATOR
# -----------------------------
def run_ai_market_analyst():
    print("\n==============================")
    print(" AI PERSONAL MARKET ANALYST ")
    print(" (Indian Stock Market)")
    print("==============================\n")

    symbol = input("Enter Indian stock symbol (e.g. RELIANCE, TCS): ").upper()

    # -----------------------------
    # DATA + TECHNICALS
    # -----------------------------
    print("\n[1/6] Fetching market data...")
    df = get_stock_data(symbol)

    print("[2/6] Computing technical indicators...")
    df = add_technical_indicators(df)
    df.dropna(inplace=True)

    print("[3/6] Running technical analysis...")
    technical_report = analyze_technical(df)

    # -----------------------------
    # FUNDAMENTALS (API + MULTIBAGGER)
    # -----------------------------
    print("[4/6] Running fundamental analysis (API + Multibagger)...")
    fundamental_report = run_fundamentals(symbol)

    # -----------------------------
    # FORECASTING
    # -----------------------------
    print("[5/6] Generating trade setups (Entry / Target / SL)...")
    forecast_report = generate_forecast(df)

    # -----------------------------
    # STRATEGY SIMULATION
    # -----------------------------
    print("[6/6] Simulating low-risk strategy...")
    final_capital, trades = simulate_swing_strategy(df)
    strategy_metrics = performance_metrics(trades, 100000, final_capital)

    # -----------------------------
    # BUY / HOLD / SELL
    # -----------------------------
    print("\n==============================")
    print(" BUY / HOLD / SELL DECISIONS ")
    print("==============================")
    decisions = decide_action(technical_report, fundamental_report)
    for k, v in decisions.items():
        print(f"{k}: {v}")

    # -----------------------------
    # TRADE SETUPS
    # -----------------------------
    print("\n==============================")
    print(" TRADE SETUPS (CMP / ENTRY / TARGET / SL)")
    print("==============================")

    for horizon, data in forecast_report.items():
        print(f"\n{horizon}")
        print(f"CMP: {data.get('CMP')}")
        print(f"Bias: {data.get('Bias')}")
        print(f"Entry: {data.get('Entry')}")
        print(f"Target: {data.get('Target')}")
        print(f"Stop Loss: {data.get('Stop Loss')}")
        print(f"Risk Reward: {data.get('Risk Reward')}")
        print(f"Confidence: {data.get('Confidence')}")

    # -----------------------------
    # TECHNICAL SUMMARY
    # -----------------------------
    print("\n==============================")
    print(" TECHNICAL ANALYSIS SUMMARY ")
    print("==============================")
    for k, v in technical_report.items():
        print(f"{k}: {v}")

    # -----------------------------
    # FUNDAMENTAL SUMMARY (PROPER PRINTER)
    # -----------------------------
    print_fundamental_report(symbol)

    # -----------------------------
    # STRATEGY PERFORMANCE
    # -----------------------------
    print("\n==============================")
    print(" STRATEGY SIMULATION SUMMARY ")
    print("==============================")
    for k, v in strategy_metrics.items():
        print(f"{k}: {v}")

    # -----------------------------
    # DISCLAIMER
    # -----------------------------
    print("\n==============================")
    print(" FINAL PROFESSIONAL NOTE ")
    print("==============================")
    print(
        "This system provides probabilistic analysis, not investment advice.\n"
        "All setups are risk-defined with capital protection as priority.\n"
        "Use this as a research assistant, not an automated trading system."
    )


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    run_ai_market_analyst()
