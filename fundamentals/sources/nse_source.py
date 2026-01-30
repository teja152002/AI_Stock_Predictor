try:
    from nsetools import Nse
    nse = Nse()
except:
    nse = None


def fetch_nse_snapshot(symbol):
    if nse is None:
        return {}

    try:
        quote = nse.get_quote(symbol)
        return {
            "pe": quote.get("pe"),
            "market_cap": quote.get("marketCap"),
            "sector": quote.get("industry")
        }
    except:
        return {}
