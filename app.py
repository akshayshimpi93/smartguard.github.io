from kiteconnect import KiteConnect
from flask import Flask, request

app = Flask(__name__)

# 🔐 Your credentials
api_key = "g3obpvd2yff5q1bp"
api_secret = "1ndwcyaxjzp52xi276mbt1ff6netu0ykp"

kite = KiteConnect(api_key=api_key)

@app.route("/")
def receive_token():
    request_token = request.args.get("request_token")
    print("🟢 Request Token received:", request_token)

    try:
        # Generate session using request_token
        data = kite.generate_session(request_token, api_secret=api_secret)
        kite.set_access_token(data["access_token"])

        print("✅ Access Token:", data["access_token"])
        return "Login Successful. You can close this window now."

    except Exception as e:
        print("❌ Error:", str(e))
        return "Something went wrong: " + str(e)

if __name__ == "__main__":
    print("🚀 Welcome to TradiLink AI login system")
    print("🔗 Login URL:", kite.login_url())  # Paste this in browser
    app.run(port=8000)
