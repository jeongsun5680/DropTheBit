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
    res_list =[]
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
        
        dict_res ={}
        dict_res['market'] = market
        dict_res['coin_type'] = coin
        dict_res['price'] = price
        res_list.append(dict_res)
        
    list_dict = {i : res_list[i] for i in range(len(res_list))}

    # str_Market_result = json.dumps(list_dict)
    # json_Market_result = json.loads(str_Market_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
    # pandas_Market_result = json_normalize(json_Market_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다
    pandas_Market_result = pd.DataFrame(list_dict)
    return pandas_Market_result

def get_market_all():
    list_market =[]
    for key in url_info.keys():
        list_market.append(get_market(key))
    return list_market

print(get_market_all())