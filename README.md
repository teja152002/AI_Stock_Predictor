📊 AI Stock Market Predictor (Indian Markets)

An end-to-end AI-powered stock market analysis system for the Indian equity market, combining:

📈 Technical Analysis

🧠 Fundamental Analysis (API + Manual Multibagger Framework)

🎯 Risk-managed Trade Setups (Entry, Target, Stop-Loss, RR)

🖥️ Clean Web UI (Streamlit)

⚙️ Scalable Backend API (FastAPI)

⚠️ This project is built for research & educational purposes only.
It is not investment advice.

🚀 Live Demo

Frontend (UI)
👉 https://ai-stock-predictor-1-23t2.onrender.com

Backend API
👉 https://ai-stock-predictor-qb2c.onrender.com

👉 Example:

https://ai-stock-predictor-qb2c.onrender.com/analyze?symbol=RELIANCE

🧠 What This Project Does

From a single stock symbol (NSE), the system provides:

✅ Buy / Hold / Sell Decisions

Intraday

Short Term

Swing

Long Term

🎯 Trade Setups

Current Market Price (CMP)

Entry Price

Target

Stop Loss

Risk-Reward (1:2 enforced)

Confidence level

📈 Technical Analysis

EMA (20 / 50 / 200)

RSI

MACD

Trend & Momentum interpretation

🧮 Fundamental Analysis (Dual Engine)

API-based fundamentals (quick snapshot)

Manual Multibagger Engine (11-rule framework)

🏆 Multibagger Framework (Conservative)

A stock is considered a potential multibagger if ≥ 8 out of 11 rules pass, including:

OPM ≥ 20%

ROE & ROCE ≥ 15%

Low Debt (D/E ≤ 0.5)

Positive Operating Cash Flow

Stable Promoter Holding

Sales & Profit CAGR validation

Balance Sheet growth

🏗️ System Architecture
Frontend (Streamlit UI)
        ↓
Backend (FastAPI)
        ↓
Core Analysis Engine
        ↓
Market Data + Indicators + Fundamentals

Separation of Concerns

Frontend → User experience

Backend API → Data orchestration

Core Engine → Business logic

Manual Fundamentals → High-quality human input

Forecasting Engine → Risk-managed trade geometry

📁 Project Structure
AI_Stock_Predictor/
│
├── api/
│   └── app.py                 # FastAPI backend
│
├── core/
│   └── engine.py              # Core analysis logic
│
├── frontend/
│   └── app.py                 # Streamlit UI
│
├── data/
├── technicals/
├── fundamentals/
│   ├── manual_multibagger_input.py
│   ├── multibagger_scorer.py
│   └── fundamental_router.py
│
├── forecasting/
├── decision_engine/
├── strategies/
│
├── main.py                    # CLI entry (optional)
├── requirements.txt
└── README.md
