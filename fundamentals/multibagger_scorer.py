def safe_ge(a, b):
    return a is not None and b is not None and a >= b


def safe_le(a, b):
    return a is not None and b is not None and a <= b


def growth_check(data, prefix):
    return (
        (data.get(f"{prefix}_10y") is not None and data[f"{prefix}_10y"] >= 10)
        or (data.get(f"{prefix}_5y") is not None and data[f"{prefix}_5y"] >= 10)
        or (data.get(f"{prefix}_3y") is not None and data[f"{prefix}_3y"] >= 10)
    )


def evaluate_multibagger(data):
    rules = []
    score = 0

    def add_rule(name, passed, reason):
        nonlocal score
        rules.append({
            "Rule": name,
            "Passed": passed,
            "Reason": reason
        })
        if passed:
            score += 1

    # 1. OPM
    add_rule(
        "OPM ≥ 20%",
        safe_ge(data.get("opm_3y"), 20),
        f"OPM = {data.get('opm_3y')}%"
    )

    # 2. EPS Trend
    add_rule(
        "EPS Stable / Increasing",
        safe_ge(data.get("eps_latest"), data.get("eps_3y_ago")),
        f"EPS: {data.get('eps_3y_ago')} → {data.get('eps_latest')}"
    )

    # 3. Debt to Equity
    add_rule(
        "Debt / Equity ≤ 0.5",
        safe_le(data.get("debt_to_equity"), 0.5),
        f"D/E = {data.get('debt_to_equity')}"
    )

    # 4. ROE
    add_rule(
        "ROE ≥ 15%",
        safe_ge(data.get("roe_3y"), 15),
        f"ROE = {data.get('roe_3y')}%"
    )

    # 5. ROCE
    add_rule(
        "ROCE ≥ 15%",
        safe_ge(data.get("roce_3y"), 15),
        f"ROCE = {data.get('roce_3y')}%"
    )

    # 6. Interest Coverage
    add_rule(
        "Net Profit ≥ 2× Interest",
        data.get("net_profit") is not None
        and data.get("interest") is not None
        and data["net_profit"] >= 2 * data["interest"],
        f"Profit = {data.get('net_profit')}, Interest = {data.get('interest')}"
    )

    # 7. Promoter Holding
    add_rule(
        "Promoter Holding Stable",
        data.get("promoter_holding_latest") is not None
        and data.get("promoter_holding_3y_ago") is not None
        and (data["promoter_holding_latest"] - data["promoter_holding_3y_ago"]) >= -1,
        f"{data.get('promoter_holding_3y_ago')}% → {data.get('promoter_holding_latest')}%"
    )

    # 8. Operating Cash Flow
    add_rule(
        "Operating Cash Flow Positive",
        data.get("operating_cf_latest") is not None
        and data["operating_cf_latest"] > 0,
        f"OCF = {data.get('operating_cf_latest')}"
    )

    # 9. Balance Sheet Growth
    add_rule(
        "Assets Increasing",
        data.get("total_assets_latest") is not None
        and data.get("total_assets_3y_ago") is not None
        and data["total_assets_latest"] > data["total_assets_3y_ago"],
        f"{data.get('total_assets_3y_ago')} → {data.get('total_assets_latest')}"
    )

    # 10. Sales Growth
    add_rule(
        "Sales CAGR ≥ 10%",
        growth_check(data, "sales_cagr"),
        "Using best available (10Y / 5Y / 3Y)"
    )

    # 11. Profit Growth
    add_rule(
        "Profit CAGR ≥ 10%",
        growth_check(data, "profit_cagr"),
        "Using best available (10Y / 5Y / 3Y)"
    )

    verdict = (
        "Strong Multibagger Candidate" if score >= 9 else
        "Potential Multibagger" if score >= 8 else
        "Not a Multibagger"
    )

    return {
        "Score": score,
        "Max Score": 11,
        "Verdict": verdict,
        "Rules": rules
    }
