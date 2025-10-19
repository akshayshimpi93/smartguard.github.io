import pandas as pd

# 📊 Main behavior analysis (your original logic)
def analyze_behavior(df):
    df["hour"] = df["timestamp"].dt.hour
    trades_per_hour = df.groupby("hour").size()

    # Rule 1: Overtrading — more than 3 trades in any hour
    overtrading = any(trades_per_hour > 3)

    # Rule 2: Revenge Trading — big loss followed by BUY
    revenge_trading = False
    for i in range(1, len(df)):
        if df.loc[i - 1, "pl"] < -1000 and df.loc[i, "side"] == "BUY":
            revenge_trading = True

    # Rule 3: Net P&L
    net_pl = df["pl"].sum()

    return {
        "overtrading": overtrading,
        "revenge_trading": revenge_trading,
        "net_pl": net_pl
    }

# ➕ New behaviors (FOMO, Holding too long)
def detect_additional_behaviors(df):
    results = {}

    # FOMO — 3+ BUYs within 10 minutes
    df_buy = df[df["side"] == "BUY"].sort_values(by="timestamp")
    df_buy["time_diff"] = df_buy["timestamp"].diff().dt.total_seconds().fillna(9999)
    results["fomo"] = (df_buy["time_diff"] < 600).sum() >= 2

    # Holding Too Long — no SELL within 30 mins after BUY
    holding_too_long = False
    for i in range(len(df) - 1):
        if df.loc[i, "side"] == "BUY":
            for j in range(i + 1, len(df)):
                if df.loc[j, "side"] == "SELL" and df.loc[j, "symbol"] == df.loc[i, "symbol"]:
                    diff = (df.loc[j, "timestamp"] - df.loc[i, "timestamp"]).total_seconds()
                    if diff > 1800:
                        holding_too_long = True
                    break
    results["holding_too_long"] = holding_too_long

    return results

# 🧪 Testing block
if __name__ == "__main__":
    # Load mock data (make sure file exists in same folder)
    df = pd.read_csv("mock_trades.csv", parse_dates=["timestamp"])

    # Run both scanners
    result_main = analyze_behavior(df)
    result_extra = detect_additional_behaviors(df)

    # Merge results
    final_result = {**result_main, **result_extra}

    # Print results clearly
    print("\n🧠 Behavioral Risk Flags:")
    for key, value in final_result.items():
        if key == "net_pl":
            print(f"{key}: ₹{value}")
        else:
            print(f"{key}: {'⚠️ YES' if value else '✅ NO'}")
