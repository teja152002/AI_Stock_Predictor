from fundamentals.manual_multibagger_input import manual_fundamentals
from fundamentals.multibagger_scorer import evaluate_multibagger
from fundamentals.multibagger_report import print_multibagger_report

from fundamentals.api_fundamental_engine import run as run_api_fundamentals


def run_fundamentals(symbol):
    api_result = run_api_fundamentals(symbol)

    multibagger_result = evaluate_multibagger(manual_fundamentals)

    return {
        "api": api_result,
        "multibagger": multibagger_result
    }


def print_fundamental_report(symbol):
    result = run_fundamentals(symbol)

    print("\n==============================")
    print(" API FUNDAMENTAL SNAPSHOT ")
    print("==============================")
    for k, v in result["api"].items():
        print(f"{k}: {v}")

    print_multibagger_report(result["multibagger"])
