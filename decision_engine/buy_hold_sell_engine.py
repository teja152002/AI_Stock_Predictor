def decide_action(technical_report, fundamental_report):
    """
    Combines technical bias + multibagger fundamental strength
    to produce Buy / Hold / Sell decisions.
    """

    decisions = {}

    # -----------------------------
    # FUNDAMENTAL STRENGTH
    # -----------------------------
    multibagger = fundamental_report.get("multibagger", {})

    fund_score = multibagger.get("Score", 0)
    max_score = multibagger.get("Max Score", 11)

    if fund_score >= 8:
        fund_strength = "Strong"
    elif fund_score >= 6:
        fund_strength = "Neutral"
    else:
        fund_strength = "Weak"

    # -----------------------------
    # TECHNICAL BIAS
    # -----------------------------
    trend = technical_report.get("Trend", "Neutral")
    momentum = technical_report.get("Momentum", "Neutral")

    # -----------------------------
    # DECISION LOGIC
    # -----------------------------
    def rule_engine(timeframe):
        if fund_strength == "Strong" and trend == "Bullish":
            return "BUY"
        if fund_strength == "Neutral" and trend == "Bullish":
            return "HOLD"
        if fund_strength == "Weak":
            return "AVOID"
        return "HOLD"

    decisions["Intraday"] = rule_engine("Intraday")
    decisions["Short Term"] = rule_engine("Short Term")
    decisions["Swing"] = rule_engine("Swing")
    decisions["Long Term"] = rule_engine("Long Term")

    return decisions
