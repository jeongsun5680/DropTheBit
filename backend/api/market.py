import requests, json
import pyupbit
import pandas as pd , dataframe
from django.shortcuts import render
from django.http import HttpResponse

url_info = {
    "upbit" : {
            "base_url":"https://api.upbit.com", "sub_url":"/v1/candles/minutes/1" , "param_key":"market", "symbol":"market", "price":"trade_price", "data_type":"list"
    },

    "binance" : {
            "base_url":"https://api.binance.com", "sub_url":"/api/v3/ticker/price", "param_key":"symbol", "symbol":"symbol", "price":"price", "data_type":"dict"
    },
}

# API 호출 시 market 별로 다른 coin 명칭 필요
coin_info = {
    # "upbit" : {"BTC":"KRW-BTC", "ETH":"KRW-ETH"},
    # "binance" : {"BTC":"BTCUSDT", "ETH":"ETHUSDT"}
}

#"bithum" : {"base_url":"https://api.bithumb.com", "sub_url":"/public/ticker/BTC", "param_key":"symbol" , "param_value":"BTCUSDT" }}
# ----------------------------------------------------------------------------------


u_res = requests.get("https://api.upbit.com/v1/market/all", params={"isDetails":"false"})
b_res = requests.get("https://api.binance.com/api/v3/exchangeInfo")
u_Market_result = u_res.json()
b_Mareket_result = b_res.json()['symbols']

u_market = "upbit"
coin_info[u_market] = {}
for dict_coin in u_Market_result:
    print(str(dict_coin))
    u_coin = dict_coin[url_info[u_market]["param_key"]] # u_coin = KRW-BTC
    if u_coin[0:3] == "KRW":
        data = u_coin.split('-')
        coin_info[u_market][data[1]] = u_coin

b_market = "binance"
coin_info[b_market] = {}
for dict_coin in b_Mareket_result:
    b_coin = dict_coin[url_info[b_market]["param_key"]]
    if b_coin[-4:] == "USDT":
        data = b_coin[:-4]
        coin_info[b_market][data] = b_coin

#b_res = requests.get("https://api.binance.com/sapi/v1/capital/config/getall", params={})
#b_Market_result = b_res.json()
#print(b_Market_result)

#res = requests.get(url_info['upbit']['base_url'] +url_info['upbit']['sub_url'], params={url_info['upbit']['param_key']:coin_info['upbit']['BTC']})
#print('-----upbit-------')
#print(str(type(res)))
#print(str(type(res.text)))
#
#res = requests.get(url_info['binance']['base_url'] +url_info['binance']['sub_url'], params={url_info['binance']['param_key']:coin_info['binance']['BTC']})
#print('-----binance-------')
#print(res.json())



def get_market(market):
    #res_list =[]
    dict_coin_info ={}
    dict_res = {}
    index = 0
    price = 0.1
    symbol = ""

    for coin in coin_info[market].keys():

        while True:
            try:
                res = requests.get(url_info[market]['base_url'] +url_info[market]['sub_url'], params={url_info[market]['param_key']:coin_info[market][coin]})
                Market_result = res.json()
                #print('-----'+coin+'-----')
                if(url_info[market]['data_type']=="dict"):
                    price = float(Market_result[url_info[market]['price']])
                    # price = float(result['price']) #price str -> float로 형변환
                    # result['price'] = price #바이낸스 가격 저장
                elif(url_info[market]['data_type']=="list"):
                    # 업비트의 price는 binance와 1000:1 관계
                    price = Market_result[0][url_info[market]['price']]

                break

            except Exception as ex:
                pass

        dict_coin_info[coin] = price

    dict_res[market] = dict_coin_info

    # str_Market_result = json.dumps(list_dict)
    # json_Market_result = json.loads(str_Market_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
    # pandas_Market_result = json_normalize(json_Market_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다
    # pandas_Market_result = pd.DataFrame(list_dict)

    # print('-------판다스 하기 전에 dict형식---------')
    # print(dict_res)
    
    # pandas_Market_result = pd.DataFrame(dict_res)
    # print('-------판다스, 문제의 원인 나야나---------')
    # print(pandas_Market_result)
    # # 이 pandas_Market_result의 생김새 때문에 아래 get_market_all에서 key value를 올바르게 쪼갤 수 없는 거임
    return dict_res


def get_market_all():
    dict_market = {}
    for key in url_info.keys():
        market = get_market(key)
        dict_market[key] = market[key]
    return dict_market


#음... 판다스로 값을 불러올 때, dict 형식이 아니기 때문에 key, value로 쪼개서 다시 배치할 수가 없다! 해결해줘!
#test.py로 넘겨줘야 할 형식은 다음과 같다! 왜? 완상이형이 짜준 코드가 그러니까!!!!
# {
#     'upbit':{'BTC':100, 'ETH':200},
#     'binance':{'BTC':300, 'ETH':400}
# }

# 이래야 test.py에서 v[market][coin] 해서 돈을 바로바로 불러올 수 있음