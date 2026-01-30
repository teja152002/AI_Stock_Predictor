def analyze_technical(df):
    """
    Interpret technical indicators into human-readable insights
    """

    latest = df.iloc[-1]

    analysis = {}

    # Trend
    if latest["ema_20"] > latest["ema_50"] > latest["ema_200"]:
        analysis["trend"] = "Strong Bullish"
    elif latest["ema_20"] < latest["ema_50"] < latest["ema_200"]:
        analysis["trend"] = "Strong Bearish"
    else:
        analysis["trend"] = "Sideways / Uncertain"

    # Momentum
    if latest["rsi"] > 70:
        analysis["momentum"] = "Overbought"
    elif latest["rsi"] < 30:
        analysis["momentum"] = "Oversold"
    else:
        analysis["momentum"] = "Healthy"

    # MACD
    if latest["macd"] > latest["macd_signal"]:
        analysis["macd_signal"] = "Bullish"
    else:
        analysis["macd_signal"] = "Bearish"

    # Volatility
    analysis["volatility"] = round(latest["atr"], 2)

    return analysis
