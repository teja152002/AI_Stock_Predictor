import streamlit as st
import requests

# -----------------------------
# CONFIG
# -----------------------------
API_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(
    page_title="AI Stock Market Analyst",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("📊 AI Personal Stock Market Analyst")
st.caption("Indian Stock Market • Fundamentals • Technicals • Risk-Managed Trade Setups")

st.markdown("---")

# -----------------------------
# USER INPUT
# -----------------------------
col1, col2 = st.columns([3, 1])

with col1:
    symbol = st.text_input(
        "Enter NSE Stock Symbol",
        value="RELIANCE",
        help="Example: RELIANCE, SBIN, TCS"
    )

with col2:
    analyze_btn = st.button("🔍 Analyze Stock")

# -----------------------------
# ANALYSIS
# -----------------------------
if analyze_btn:
    if symbol.strip() == "":
        st.error("Please enter a stock symbol")
    else:
        with st.spinner("Analyzing stock... Please wait"):
            try:
                response = requests.get(API_URL, params={"symbol": symbol.upper()})
                data = response.json()
            except Exception as e:
                st.error("Unable to connect to backend API")
                st.stop()

        st.success(f"Analysis completed for {symbol.upper()}")

        # -----------------------------
        # BUY / HOLD / SELL
        # -----------------------------
        st.markdown("## 🟢 Buy / Hold / Sell Decision")

        decisions = data["decisions"]
        dcols = st.columns(4)

        for col, (k, v) in zip(dcols, decisions.items()):
            if v == "BUY":
                col.success(f"{k}\n\n{v}")
            elif v == "HOLD":
                col.warning(f"{k}\n\n{v}")
            else:
                col.error(f"{k}\n\n{v}")

        # -----------------------------
        # TRADE SETUPS
        # -----------------------------
        st.markdown("## 🎯 Trade Setups (Risk-Defined)")

        for horizon, setup in data["forecast"].items():
            with st.expander(horizon):
                c1, c2, c3, c4, c5, c6 = st.columns(6)

                c1.metric("CMP", setup.get("CMP"))
                c2.metric("Bias", setup.get("Bias"))
                c3.metric("Entry", setup.get("Entry"))
                c4.metric("Target", setup.get("Target"))
                c5.metric("Stop Loss", setup.get("Stop Loss"))
                c6.metric("Risk-Reward", setup.get("Risk Reward"))

                st.caption(f"Confidence: {setup.get('Confidence')}")

        # -----------------------------
        # FUNDAMENTALS
        # -----------------------------
        st.markdown("## 🧠 Fundamental Analysis")

        funda = data["fundamentals"]

        with st.expander("API Fundamental Snapshot"):
            st.json(funda["api"])

        with st.expander("Multibagger Analysis"):
            mb = funda["multibagger"]
            st.metric("Multibagger Score", f"{mb['Score']} / {mb['Max Score']}")
            st.write("Verdict:", mb["Verdict"])

            st.markdown("### Rule-wise Evaluation")
            for rule in mb["Rules"]:
                if rule["Passed"]:
                    st.success(f"{rule['Rule']} — PASS")
                else:
                    st.error(f"{rule['Rule']} — FAIL")

        # -----------------------------
        # TECHNICALS
        # -----------------------------
        st.markdown("## 📈 Technical Analysis Summary")

        with st.expander("View Technical Indicators"):
            st.json(data["technical"])

        # -----------------------------
        # DISCLAIMER
        # -----------------------------
        st.markdown("---")
        st.caption(
            "⚠️ This system provides probabilistic analysis, not investment advice. "
            "All trade setups are risk-defined with capital protection as priority."
        )
