def calculate_risk_score(behaviors: dict) -> dict:
    """
    Takes a dictionary of behaviors and returns a score (0–100) and risk level.
    """
    # Define weight of each behavior (adjustable)
    weights = {
        "overtrading": 20,
        "revenge_trading": 25,
        "fomo": 20,
        "holding_too_long": 15,
    }

    score = 0
    for key, weight in weights.items():
        if behaviors.get(key):
            score += weight

    # Normalize if score goes above 100
    score = min(score, 100)

    # Risk category
    if score >= 70:
        risk_level = "HIGH 🔴"
    elif score >= 40:
        risk_level = "MODERATE 🟠"
    else:
        risk_level = "LOW 🟢"

    return {
        "risk_score": score,
        "risk_level": risk_level
    }

# 🔍 Example Test
if __name__ == "__main__":
    test_flags = {
        "overtrading": True,
        "revenge_trading": False,
        "fomo": True,
        "holding_too_long": False
    }

    result = calculate_risk_score(test_flags)
    print(f"\n🧠 Risk Score: {result['risk_score']} / 100")
    print(f"⚠️ Risk Level: {result['risk_level']}")
