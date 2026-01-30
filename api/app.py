from fastapi import FastAPI
from core.engine import analyze_stock

app = FastAPI(title="AI Stock Market Analyst")


@app.get("/")
def home():
    return {"status": "AI Stock Analyst Running"}


@app.get("/analyze")
def analyze(symbol: str):
    return analyze_stock(symbol.upper())
