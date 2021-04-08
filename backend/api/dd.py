import requests, json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from django.shortcuts import render
from django.http import HttpResponse

# def Upbit():
#     url = "https://api.upbit.com/v1/candles/minutes/1"
#     querystring = {"market":"KRW-BTC","count":"1"}
#     res = requests.request("GET", url, params=querystring)
#     Upbit_result = res.json()

#     # 업비트의 price는 binance와 1000:1 관계
#     price = Upbit_result[0]['trade_price']
#     symbol = Upbit_result[0]['market']

# 		#key 값을 비교대상(binance)의 key 값과 동일시 하고 이름과 가격에 대한 json 생성(dict타입)
#     dict_res = {}
#     dict_res['symbol'] = symbol
#     dict_res['price'] = price
#     str_Upbit_result = json.dumps(dict_res)
#     json_Upbit_result = json.loads(str_Upbit_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
#     pandas_Upbit_result = json_normalize(json_Upbit_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다
#     return pandas_Upbit_result


# url = "https://api.bithumb.com/public/ticker/BTC"
# querystring = {"status":"0000"}
# res = requests.request("GET", url, params=querystring)

url = "https://api.bithumb.com"
res = requests.get(url + "/public/ticker/BTC", params={"status":"0000"})
Upbit_result = res.json()
print(Upbit_result['data']['acc_trade_value_24H'])
# print(Upbit_result)

# # 업비트의 price는 binance와 1000:1 관계
# price = Upbit_result[0]['trade_price']
# symbol = Upbit_result[0]['market']

#     #key 값을 비교대상(binance)의 key 값과 동일시 하고 이름과 가격에 대한 json 생성(dict타입)
# dict_res = {}
# dict_res['symbol'] = symbol
# dict_res['price'] = price
# str_Upbit_result = json.dumps(dict_res)
# json_Upbit_result = json.loads(str_Upbit_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
# pandas_Upbit_result = json_normalize(json_Upbit_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다
