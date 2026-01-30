"""
CORE ANALYSIS ENGINE
This file contains pure logic (no input(), no print()).
Used by:
- main.py (CLI)
- FastAPI (API)
- Streamlit (Frontend)
"""

from data.data_loader import get_stock_data
from technicals.technical_indicators import add_technical_indicators
from technicals.technical_analysis import analyze_technical

from fundamentals.fundamental_router import run_fundamentals
from forecasting.price_forecaster import generate_forecast
from decision_engine.buy_hold_sell_engine import decide_action


def analyze_stock(symbol: str) -> dict:
    # -----------------------------
    # DATA
    # -----------------------------
    df = get_stock_data(symbol)
    df = add_technical_indicators(df)
    df.dropna(inplace=True)

    # -----------------------------
    # ANALYSIS
    # -----------------------------
    technical_report = analyze_technical(df)
    fundamental_report = run_fundamentals(symbol)
    forecast_report = generate_forecast(df)
    decisions = decide_action(technical_report, fundamental_report)

    # -----------------------------
    # FINAL OUTPUT
    # -----------------------------
    return {
        "symbol": symbol,
        "decisions": decisions,
        "technical": technical_report,
        "fundamentals": fundamental_report,
        "forecast": forecast_report
    }
