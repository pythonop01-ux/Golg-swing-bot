import requests

def get_gold_price():
    url = "https://api.metals.live/v1/spot/gold"
    response = requests.get(url)
    data = response.json()
    return float(data[0]["price"])

price = get_gold_price()

print(f"Current XAUUSD Price: {price}")

# Simple strategy
if price > 1950:
    print("SELL SIGNAL on XAUUSD")
elif price < 1850:
    print("BUY SIGNAL on XAUUSD")
else:
    print("NO TRADE")