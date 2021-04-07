import json

import requests
from bs4 import BeautifulSoup

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


def upbit():
    res = requests.get("https://upbit.com/vi/candle/minutes/1?", params={})
    return res.text


def binance():
    binc_url = 'https://www.binance.com/ko/trade/BTC_USDT?layout=basic'
    res = requests.get(binc_url)
    soup = BeautifulSoup(res.text, 'html.parser')  # 바이낸스 파서하기
    content = soup.find("script", {"id": "__APP_DATA"}).string
    return json.dumps(json.loads(content), indent=4)



if __name__ == "__main__":
    '''
    print(connectivity())
    print(exchangInfo())
    print(priceInfo())
    '''
    print(upbit())
    #print(binance())