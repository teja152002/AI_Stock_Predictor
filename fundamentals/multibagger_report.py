def print_multibagger_report(result):
    print("\n==============================")
    print(" MULTIBAGGER FUNDAMENTAL CHECK ")
    print("==============================")

    print(f"Score: {result['Score']} / {result['Max Score']}")
    print(f"Verdict: {result['Verdict']}")

    print("\nRule-wise Evaluation:")
    for r in result["Rules"]:
        status = "PASS" if r["Passed"] else "FAIL"
        print(f"- {r['Rule']}: {status} ({r['Reason']})")
