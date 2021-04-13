import requests, json
import pandas as pd , dataframe
import numpy as np
from pandas.io.json import json_normalize
from django.shortcuts import render
from django.http import HttpResponse

url_info = {
    "upbit" : {
            "BTC":{"base_url":"https://api.upbit.com", "sub_url":"/v1/candles/minutes/1" , "param_key":"market", "param_value":"KRW-BTC", "symbol":"market", "price":"trade_price"},
            "ETH":{"base_url":"https://api.upbit.com", "sub_url":"/v1/candles/minutes/1" , "param_key":"market", "param_value":"KRW-ETH", "symbol":"market", "price":"trade_price"},
            
    },

    "binance" : {
            "BTC":{"base_url":"https://api.binance.com", "sub_url":"/api/v3/ticker/price", "param_key":"symbol", "param_value":"BTCUSDT", "symbol":"symbol", "price":"price"},
            "ETH":{"base_url":"https://api.binance.com", "sub_url":"/api/v3/ticker/price", "param_key":"symbol", "param_value":"ETHUSDT", "symbol":"symbol", "price":"price"}      
    },
}
#"bithum" : {"base_url":"https://api.bithumb.com", "sub_url":"/public/ticker/BTC", "param_key":"symbol" , "param_value":"BTCUSDT" }}
# ----------------------------------------------------------------------------------

def get_market(market):
    #res_list =[]
    dict_coin_info ={}
    dict_res = {}
    index = 0
    price = 0.1
    symbol = ""

    for coin in url_info[market].keys():
        res = requests.get(url_info[market][coin]['base_url'] +url_info[market][coin]['sub_url'], params={url_info[market][coin]['param_key']:url_info[market][coin]['param_value']})
    
        Market_result = res.json()

        if(str(type(Market_result))=="<class 'dict'>"):
            price = float(Market_result[url_info[market][coin]['price']])
            # price = float(result['price']) #price str -> float로 형변환
            # result['price'] = price #바이낸스 가격 저장
        elif(str(type(Market_result))=="<class 'list'>"):
            # 업비트의 price는 binance와 1000:1 관계
            price = Market_result[0][url_info[market][coin]['price']]
        
        #dict_coin_info ={}
        #dict_res['market'] = market
        #dict_coin_info['coin_type'] = coin
        #dict_coin_info['price'] = price
        dict_coin_info[coin] = price

    dict_res[market] = dict_coin_info
    pandas_Market_result = pd.DataFrame(dict_res)
    
    print('-------판다스, 문제의 원인 나야나---------')
    print(pandas_Market_result)
    # 이 pandas_Market_result의 생김새 때문에 아래 get_market_all에서 key value를 올바르게 쪼갤 수 없는 거임
    return pandas_Market_result

def get_market_all():
    dict_market = {}
    for key in url_info.keys():
        market = get_market(key)
        dict_market[key] = market[key]
        print('-----dict_market을 구할거임--------')
        print(dict_market)
        # key를 가지고 get_market(key)
        # 결과 값을 다시 key, value로 쪼개
        # 새로운 dict에 key, value를 연속적으로 넣어

    return dict_market

print(get_market_all())


# str_Market_result = json.dumps(list_dict)
# json_Market_result = json.loads(str_Market_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
# pandas_Market_result = json_normalize(json_Market_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다
# pandas_Market_result = pd.DataFrame(list_dict)

#음... 판다스로 값을 불러올 때, dict 형식이 아니기 때문에 key, value로 쪼개서 다시 배치할 수가 없다! 해결해줘!
#test.py로 넘겨줘야 할 형식은 다음과 같다! 왜? 완상이형이 짜준 코드가 그러니까!!!!
# {
#     'upbit':{'BTC':100, 'ETH':200},
#     'binance':{'BTC':300, 'ETH':400}
# }

# 이래야 test.py에서 v[market][coin] 해서 돈을 바로바로 불러올 수 있음