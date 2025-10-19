import webbrowser
from kiteconnect import KiteConnect
import pandas as pd
import os
from dotenv import load_dotenv

# ✅ Load API credentials from .env file
load_dotenv()  # Loads variables from .env into environment

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# 🛠️ Debug print to confirm values are loaded
print("✅ API_KEY loaded:", API_KEY)
print("✅ API_SECRET loaded:", API_SECRET)

# 🔁 Check if keys are actually loaded
if not API_KEY or not API_SECRET:
    print("❌ ERROR: API_KEY or API_SECRET is missing. Check your .env file.")
    exit()

# 🌐 Initialize KiteConnect
kite = KiteConnect(api_key=API_KEY)

# 🔗 Step 1: Generate Zerodha login URL
def generate_login_url():
    login_url = kite.login_url()
    print("🔗 Login using this URL:")
    print(login_url)
    webbrowser.open(login_url)

# 🔐 Step 2: Generate access token
def get_access_token(request_token):
    try:
        data = kite.generate_session(request_token, api_secret=API_SECRET)
        kite.set_access_token(data["access_token"])

        # Save token
        with open("access_token.txt", "w") as f:
            f.write(data["access_token"])

        print("✅ Access token set successfully!")
        return data["access_token"]
    except Exception as e:
        print("❌ Error generating access token:", e)
        return None

# 📦 Step 3: Fetch user orders
def fetch_orders():
    try:
        orders = kite.orders()
        df = pd.DataFrame(orders)
        return df
    except Exception as e:
        print("❌ Failed to fetch orders:", e)
        return pd.DataFrame()

# 🧠 Step 4: Analyze trading behavior
def analyze_behavior(df):
    if df.empty:
        print("⚠️ No orders to analyze.")
        return

    print("\n🧠 Analyzing Trading Behavior...")

    buy_count = len(df[df['transaction_type'] == 'BUY'])
    sell_count = len(df[df['transaction_type'] == 'SELL'])
    total = len(df)

    df['order_time'] = pd.to_datetime(df['order_timestamp'], errors='coerce')
    df = df.dropna(subset=['order_time'])

    daily_trades = df.groupby(df['order_time'].dt.date).size()

    print(f"📊 Total Trades: {total}")
    print(f"🟢 BUY Orders: {buy_count}")
    print(f"🔴 SELL Orders: {sell_count}")
    print(f"📆 Avg Trades Per Day: {daily_trades.mean():.2f}")

    if daily_trades.mean() > 10:
        print("⚠️ High-frequency trading detected.")
    if sell_count > buy_count * 1.5:
        print("⚠️ You are selling too often.")
    if buy_count == 0:
        print("📌 No BUY orders. Passive behavior?")
    if sell_count == 0:
        print("📌 No SELL orders. Holding too long?")

# 🚀 Main execution
if __name__ == "__main__":
    generate_login_url()
    request_token = input("📥 Paste the request_token from the URL here: ").strip()
    access_token = get_access_token(request_token)

    if access_token:
        df = fetch_orders()
        print("\n📄 Sample Order Data:")
        print(df.head())
        analyze_behavior(df)
