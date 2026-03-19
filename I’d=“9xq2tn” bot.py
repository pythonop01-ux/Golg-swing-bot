python id="w0mj5o"

import random

price = random.randint(1800, 2000)

if price > 1950:
    print("SELL SIGNAL on XAUUSD")
elif price < 1850:
    print("BUY SIGNAL on XAUUSD")
else:
    print("NO TRADE")
