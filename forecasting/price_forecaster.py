# import numpy as np
# import pandas as pd

# from technicals.technical_indicators import add_technical_indicators


# # -----------------------------
# # Helper functions
# # -----------------------------
# def calculate_returns(df):
#     return np.log(df["close"] / df["close"].shift(1)).dropna()


# # -----------------------------
# # RISK UTILITY
# # -----------------------------
# def rr(entry, target, stop):
#     try:
#         return round(abs(target - entry) / abs(entry - stop), 2)
#     except:
#         return None


# # -----------------------------
# # INTRADAY SETUP
# # -----------------------------
# def intraday_forecast(df):
#     latest = df.iloc[-1]

#     cmp = latest["close"]
#     atr = latest["atr"]

#     bias = "Neutral"
#     if latest["ema_20"] > latest["ema_50"]:
#         bias = "Bullish"
#     elif latest["ema_20"] < latest["ema_50"]:
#         bias = "Bearish"

#     if bias == "Bullish":
#         entry = round(cmp, 2)
#         stop = round(cmp - atr, 2)
#         target = round(cmp + 1.5 * atr, 2)
#     elif bias == "Bearish":
#         entry = round(cmp, 2)
#         stop = round(cmp + atr, 2)
#         target = round(cmp - 1.5 * atr, 2)
#     else:
#         entry = target = stop = None

#     return {
#         "CMP": round(cmp, 2),
#         "Bias": bias,
#         "Entry": entry,
#         "Target": target,
#         "Stop Loss": stop,
#         "Risk Reward": rr(entry, target, stop),
#         "Confidence": "Low–Medium"
#     }


# # -----------------------------
# # SHORT TERM (1–5 DAYS)
# # -----------------------------
# def short_term_forecast(df):
#     latest = df.iloc[-1]
#     cmp = latest["close"]
#     atr = latest["atr"]

#     bias = "Neutral"
#     if latest["rsi"] > 55:
#         bias = "Bullish"
#     elif latest["rsi"] < 45:
#         bias = "Bearish"

#     if bias == "Bullish":
#         entry = round(latest["ema_20"], 2)
#         stop = round(entry - 1.2 * atr, 2)
#         target = round(entry + 2 * atr, 2)
#     elif bias == "Bearish":
#         entry = round(latest["ema_20"], 2)
#         stop = round(entry + 1.2 * atr, 2)
#         target = round(entry - 2 * atr, 2)
#     else:
#         entry = target = stop = None

#     return {
#         "CMP": round(cmp, 2),
#         "Bias": bias,
#         "Entry": entry,
#         "Target": target,
#         "Stop Loss": stop,
#         "Risk Reward": rr(entry, target, stop),
#         "Confidence": "Medium"
#     }


# # -----------------------------
# # SWING (1–4 WEEKS)
# # -----------------------------
# def swing_forecast(df):
#     latest = df.iloc[-1]
#     cmp = latest["close"]
#     atr = latest["atr"]

#     bias = "Neutral"
#     if latest["ema_50"] > latest["ema_200"]:
#         bias = "Bullish"
#     elif latest["ema_50"] < latest["ema_200"]:
#         bias = "Bearish"

#     if bias == "Bullish":
#         entry = round(latest["ema_50"], 2)
#         stop = round(entry - 2 * atr, 2)
#         target = round(entry + 4 * atr, 2)
#     elif bias == "Bearish":
#         entry = round(latest["ema_50"], 2)
#         stop = round(entry + 2 * atr, 2)
#         target = round(entry - 4 * atr, 2)
#     else:
#         entry = target = stop = None

#     return {
#         "CMP": round(cmp, 2),
#         "Bias": bias,
#         "Entry": entry,
#         "Target": target,
#         "Stop Loss": stop,
#         "Risk Reward": rr(entry, target, stop),
#         "Confidence": "Medium–High"
#     }


# # -----------------------------
# # LONG TERM (3–12 MONTHS)
# # -----------------------------
# def long_term_forecast(df):
#     latest = df.iloc[-1]
#     cmp = latest["close"]

#     bias = "Neutral"
#     if latest["ema_50"] > latest["ema_200"]:
#         bias = "Bullish"
#     elif latest["ema_50"] < latest["ema_200"]:
#         bias = "Bearish"

#     if bias == "Bullish":
#         entry = round(cmp, 2)
#         stop = round(latest["ema_200"], 2)
#         target = round(cmp * 1.25, 2)
#     elif bias == "Bearish":
#         entry = round(cmp, 2)
#         stop = round(latest["ema_200"], 2)
#         target = round(cmp * 0.75, 2)
#     else:
#         entry = target = stop = None

#     return {
#         "CMP": round(cmp, 2),
#         "Bias": bias,
#         "Entry": entry,
#         "Target": target,
#         "Stop Loss": stop,
#         "Risk Reward": rr(entry, target, stop),
#         "Confidence": "Medium"
#     }


# # -----------------------------
# # MASTER FORECAST
# # -----------------------------
# def generate_forecast(df):
#     df = add_technical_indicators(df)
#     df.dropna(inplace=True)

#     return {
#         "Intraday": intraday_forecast(df),
#         "Short Term (1–5 Days)": short_term_forecast(df),
#         "Swing (1–4 Weeks)": swing_forecast(df),
#         "Long Term (3–12 Months)": long_term_forecast(df),
#     }


# if __name__ == "__main__":
#     df = pd.read_csv("data/RELIANCE_data.csv")
#     forecast = generate_forecast(df)

#     print("\n===== TRADE SETUP REPORT =====")
#     for horizon, details in forecast.items():
#         print(f"\n{horizon}")
#         for k, v in details.items():
#             print(f"{k}: {v}")























import numpy as np
import pandas as pd

from technicals.technical_indicators import add_technical_indicators


# -----------------------------
# Risk–Reward Utility
# -----------------------------
def risk_reward(entry, target, stop):
    try:
        return round(abs(target - entry) / abs(entry - stop), 2)
    except:
        return None


# -----------------------------
# INTRADAY FORECAST (RR = 1:2)
# -----------------------------
def intraday_forecast(df):
    latest = df.iloc[-1]

    cmp = latest["close"]
    atr = latest["atr"]

    bias = "Neutral"
    if latest["ema_20"] > latest["ema_50"]:
        bias = "Bullish"
    elif latest["ema_20"] < latest["ema_50"]:
        bias = "Bearish"

    if bias == "Bullish":
        entry = round(cmp, 2)
        stop = round(cmp - atr, 2)
        target = round(cmp + 2 * atr, 2)   # ✅ 1:2 RR
    elif bias == "Bearish":
        entry = round(cmp, 2)
        stop = round(cmp + atr, 2)
        target = round(cmp - 2 * atr, 2)   # ✅ 1:2 RR
    else:
        entry = stop = target = None

    return {
        "CMP": round(cmp, 2),
        "Bias": bias,
        "Entry": entry,
        "Target": target,
        "Stop Loss": stop,
        "Risk Reward": risk_reward(entry, target, stop),
        "Confidence": "Low–Medium"
    }


# -----------------------------
# SHORT TERM (1–5 DAYS) (RR ≈ 1:2)
# -----------------------------
def short_term_forecast(df):
    latest = df.iloc[-1]
    cmp = latest["close"]
    atr = latest["atr"]

    bias = "Neutral"
    if latest["rsi"] > 55:
        bias = "Bullish"
    elif latest["rsi"] < 45:
        bias = "Bearish"

    if bias == "Bullish":
        entry = round(latest["ema_20"], 2)
        stop = round(entry - 1.2 * atr, 2)
        target = round(entry + 2.4 * atr, 2)  # ✅ RR ≈ 1:2
    elif bias == "Bearish":
        entry = round(latest["ema_20"], 2)
        stop = round(entry + 1.2 * atr, 2)
        target = round(entry - 2.4 * atr, 2)  # ✅ RR ≈ 1:2
    else:
        entry = stop = target = None

    return {
        "CMP": round(cmp, 2),
        "Bias": bias,
        "Entry": entry,
        "Target": target,
        "Stop Loss": stop,
        "Risk Reward": risk_reward(entry, target, stop),
        "Confidence": "Medium"
    }


# -----------------------------
# SWING (1–4 WEEKS) (RR ≥ 1:2)
# -----------------------------
def swing_forecast(df):
    latest = df.iloc[-1]
    cmp = latest["close"]
    atr = latest["atr"]

    bias = "Neutral"
    if latest["ema_50"] > latest["ema_200"]:
        bias = "Bullish"
    elif latest["ema_50"] < latest["ema_200"]:
        bias = "Bearish"

    if bias == "Bullish":
        entry = round(latest["ema_50"], 2)
        stop = round(entry - 2 * atr, 2)
        target = round(entry + 4 * atr, 2)   # ✅ RR = 1:2
    elif bias == "Bearish":
        entry = round(latest["ema_50"], 2)
        stop = round(entry + 2 * atr, 2)
        target = round(entry - 4 * atr, 2)   # ✅ RR = 1:2
    else:
        entry = stop = target = None

    return {
        "CMP": round(cmp, 2),
        "Bias": bias,
        "Entry": entry,
        "Target": target,
        "Stop Loss": stop,
        "Risk Reward": risk_reward(entry, target, stop),
        "Confidence": "Medium–High"
    }


# -----------------------------
# LONG TERM (3–12 MONTHS)
# -----------------------------
def long_term_forecast(df):
    latest = df.iloc[-1]
    cmp = latest["close"]

    bias = "Neutral"
    if latest["ema_50"] > latest["ema_200"]:
        bias = "Bullish"
    elif latest["ema_50"] < latest["ema_200"]:
        bias = "Bearish"

    if bias == "Bullish":
        entry = round(cmp, 2)
        stop = round(latest["ema_200"], 2)
        target = round(cmp * 1.25, 2)  # already > 1:2 in most cases
    elif bias == "Bearish":
        entry = round(cmp, 2)
        stop = round(latest["ema_200"], 2)
        target = round(cmp * 0.75, 2)
    else:
        entry = stop = target = None

    return {
        "CMP": round(cmp, 2),
        "Bias": bias,
        "Entry": entry,
        "Target": target,
        "Stop Loss": stop,
        "Risk Reward": risk_reward(entry, target, stop),
        "Confidence": "Medium"
    }


# -----------------------------
# MASTER FORECAST
# -----------------------------
def generate_forecast(df):
    df = add_technical_indicators(df)
    df.dropna(inplace=True)

    return {
        "Intraday": intraday_forecast(df),
        "Short Term (1–5 Days)": short_term_forecast(df),
        "Swing (1–4 Weeks)": swing_forecast(df),
        "Long Term (3–12 Months)": long_term_forecast(df),
    }


if __name__ == "__main__":
    df = pd.read_csv("data/RELIANCE_data.csv")
    forecast = generate_forecast(df)

    print("\n===== TRADE SETUP REPORT =====")
    for horizon, details in forecast.items():
        print(f"\n{horizon}")
        for k, v in details.items():
            print(f"{k}: {v}")
