import requests, json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from django.shortcuts import render
from django.http import HttpResponse


# def Upbit():
#     url = "https://api.upbit.com"
#     res = requests.get(url +"/v1/candles/minutes/1", params={"market":"KRW-BTC","count":"1"})
#     # querystring = {"market":"KRW-BTC","count":"1"}
#     # res = requests.request("GET", url, params=querystring)
#     Upbit_result = res.json()
#     # 업비트의 price는 binance와 1000:1 관계
#     price = Upbit_result[0]['trade_price']
#     symbol = Upbit_result[0]['market']
#     dict_res = {}
#     dict_res['symbol'] = symbol
#     dict_res['price'] = price
#     str_Upbit_result = json.dumps(dict_res)
#     json_Upbit_result = json.loads(str_Upbit_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
#     pandas_Upbit_result = json_normalize(json_Upbit_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다
#     return pandas_Upbit_result

url = "https://api.upbit.com"
res = requests.get(url +"/v1/candles/minutes/1", params={"market":"KRW-BTC"})
# querystring = {"market":"KRW-BTC","count":"1"}
# res = requests.request("GET", url, params=querystring)
Upbit_result = res.json()
print(type(Upbit_result))
if(str(type(Upbit_result))=="<class 'dict'>"):
    print("dict형식 입니다")
elif(str(type(Upbit_result))=="<class 'list'>"):
    print("list입니다")
    # 업비트의 price는 binance와 1000:1 관계
    price = Upbit_result[0]['trade_price']
    symbol = Upbit_result[0]['market']
    dict_res = {}
    dict_res['symbol'] = symbol
    dict_res['price'] = price
str_Upbit_result = json.dumps(dict_res)
json_Upbit_result = json.loads(str_Upbit_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
pandas_Upbit_result = json_normalize(json_Upbit_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다

#코인 모든 정보 가져오기
# url = "https://api.upbit.com"
# res = requests.get(url +"/v1/market/all", params={"market":"KRW-BTC"})



#210406
#데이터 순서(symbol,price)
#변수명 변경 완료
#데이터 불러오기 완료
#함수로 변환하는 작업 필요
#이전 작업 코드
    #Upbit_result = dict_result.json()
    #strprice = json.dumps(price) #json의 dict타입을 str 타입으로 변환시켜준다.
    #print(strprice)