import requests

base_url = "https://api.binance.com"


def connectivity():
    response = requests.get(base_url + "/api/v3/ping")
    return response


def exchangInfo():
    symbols = []
    cnt = 0
    res = requests.get(base_url + "/api/v3/exchangeInfo")
    for symbol in res.json()['symbols']:
        symbols.append(symbol['symbol'])
        if 'BTC' in symbol['symbol']:
            cnt += 1
    return len(symbols), cnt, symbols


def priceInfo():
    res = requests.get(base_url + "/api/v3/ticker/price", params={'symbol': "ETHBTC"})
    return res.json()


if __name__ == "__main__":
    print(connectivity())
    print(exchangInfo())
    print(priceInfo())
