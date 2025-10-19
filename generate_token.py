from kiteconnect import KiteConnect

# Step 1: Replace with your own API credentials from Zerodha developer portal
api_key = "g3obpvd2yff5q1bp"
api_secret = "1ndwcyaxjzp52xi276mbt1ff6netu0yk"

# Step 2: After you login using the browser URL, paste the request token below
request_token = "4JwBzwEcfgCJNeIzxccCINS2KhuyPsFE"

# Step 3: Initialize KiteConnect
kite = KiteConnect(api_key=api_key)

try:
    # Step 4: Exchange request token for access token
    data = kite.generate_session(request_token=request_token, api_secret=api_secret)
    access_token = data["access_token"]

    # Step 5: Print and save the access token
    print("✅ Access token generated successfully!")
    print("Access Token:", access_token)

    # Save to file
    with open("access_token.txt", "w") as f:
        f.write(access_token)

except Exception as e:
    print("❌ Failed to generate access token.")
    print("Error:", str(e))
