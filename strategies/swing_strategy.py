import pandas as pd
import numpy as np


def simulate_swing_strategy(
    df,
    initial_capital=100000,
    risk_per_trade=0.01
):
    """
    Low-risk swing trading simulation
    """

    capital = initial_capital
    position = 0
    entry_price = 0
    stop_loss = 0

    trades = []

    for i in range(1, len(df)):
        row = df.iloc[i]
        prev = df.iloc[i - 1]

        price = row["close"]

        # -----------------------------
        # ENTRY CONDITION
        # -----------------------------
        uptrend = (
            row["ema_50"] > row["ema_200"]
            and row["ema_20"] > row["ema_50"]
        )

        pullback = row["close"] < row["ema_20"]

        if position == 0 and uptrend and pullback:
            risk_amount = capital * risk_per_trade
            stop_loss = price - row["atr"]

            qty = risk_amount / (price - stop_loss)

            position = qty
            entry_price = price

            trades.append({
                "Type": "BUY",
                "Price": round(price, 2),
                "Capital": round(capital, 2)
            })

        # -----------------------------
        # EXIT CONDITIONS
        # -----------------------------
        if position > 0:
            # Stop loss
            if price <= stop_loss:
                capital += position * (price - entry_price)
                trades.append({
                    "Type": "STOP LOSS",
                    "Price": round(price, 2),
                    "Capital": round(capital, 2)
                })
                position = 0

            # Trend breakdown
            elif row["ema_50"] < row["ema_200"]:
                capital += position * (price - entry_price)
                trades.append({
                    "Type": "EXIT",
                    "Price": round(price, 2),
                    "Capital": round(capital, 2)
                })
                position = 0

    return capital, trades


def performance_metrics(trades, initial_capital, final_capital):
    wins = 0
    losses = 0

    for t in trades:
        if t["Type"] in ["EXIT"]:
            wins += 1
        elif t["Type"] == "STOP LOSS":
            losses += 1

    total_trades = wins + losses

    return {
        "Initial Capital": initial_capital,
        "Final Capital": round(final_capital, 2),
        "Total Trades": total_trades,
        "Wins": wins,
        "Losses": losses,
        "Win Rate (%)": round((wins / total_trades) * 100, 2) if total_trades else 0
    }


if __name__ == "__main__":
    df = pd.read_csv("data/RELIANCE_data.csv")

    # Import indicators here to avoid dependency issues
    from technicals.technical_indicators import add_technical_indicators

    df = add_technical_indicators(df)
    df.dropna(inplace=True)

    final_capital, trades = simulate_swing_strategy(df)

    metrics = performance_metrics(trades, 100000, final_capital)

    print("\n===== STRATEGY SIMULATION REPORT =====")
    for k, v in metrics.items():
        print(f"{k}: {v}")
