import pandas as pd
from text_emotion import detect_emotion_from_text
from behavior_scanner import analyze_behavior, detect_additional_behaviors
from risk_score_engine import calculate_risk_score

def generate_fake_advice(emotion_result, behavior_result):
    emotion = emotion_result["label"]
    overtrading = behavior_result["overtrading"]
    revenge = behavior_result["revenge_trading"]
    pl = behavior_result["net_pl"]

    # Basic fake advice logic
    if emotion == "fear":
        return "Take a step back and evaluate your risk tolerance before your next trade."
    elif emotion == "greed":
        return "Greed can lead to overconfidence. Stick to your strategy."
    elif revenge:
        return "Avoid revenge trading. Accept losses and wait for better setups."
    elif pl < 0:
        return "Review your recent trades — losses may be pointing to a pattern."
    else:
        return "You're in a good mindset. Keep following your plan!"

def run_smartguard():
    print("\n🧠 Welcome to SmartGuard AI\n" + "="*30)

    # Step 1: Emotion detection
    user_input = input("\nHow are you feeling about the market right now?\n> ")
    emotion_result = detect_emotion_from_text(user_input)
    print(f"✅ Detected Emotion: {emotion_result['label'].upper()} ({emotion_result['confidence']*100}%)")

    # Step 2: Load and analyze trades
    df = pd.read_csv("mock_trades.csv", parse_dates=["timestamp"])
    behavior_result = analyze_behavior(df)
    extra_flags = detect_additional_behaviors(df)
    combined_flags = {**behavior_result, **extra_flags}

    # Step 3: Show behavior flags
    print("\n📊 Behavior Report:")
    for key, value in combined_flags.items():
        if key == "net_pl":
            print(f"• Net P&L: ₹{value}")
        else:
            print(f"• {key.replace('_', ' ').title()}: {'⚠️ Yes' if value else '✅ No'}")

    # Step 4: Risk scoring
    risk_data = calculate_risk_score(combined_flags)
    print(f"\n🔢 Risk Score: {risk_data['risk_score']} / 100")
    print(f"⚠️ Risk Level: {risk_data['risk_level']}")

    # Step 5: Coaching tip
    tip = generate_fake_advice(emotion_result, combined_flags)
    print(f"\n💬 SmartCoach Tip:\n{tip}")

if __name__ == "__main__":
    run_smartguard()
