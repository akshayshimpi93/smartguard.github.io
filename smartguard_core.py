from text_emotion import detect_emotion
from behavior_scanner import analyze_behavior
import pandas as pd

# STEP 1: Get Emotion Input
user_input = input("🧠 What are you feeling while trading? ")

# STEP 2: Detect Emotion
emotion = detect_emotion(user_input)

# STEP 3: Load Trading Data
df = pd.read_csv("mock_trades.csv", parse_dates=["timestamp"])

# STEP 4: Analyze Behavior
behavior = analyze_behavior(df)

# STEP 5: Combine Both
trader_profile = {
    "emotion": emotion,
    "behavior": behavior
}

# STEP 6: Print Results
print("\n📊 Trader Risk Profile:")
print(f"Emotion: {emotion['label']} (Confidence: {round(emotion['confidence']*100, 2)}%)")
print(f"Overtrading: {behavior['overtrading']}")
print(f"Revenge Trading: {behavior['revenge_trading']}")
print(f"Net P/L: ₹{behavior['net_pl']}")
