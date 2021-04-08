import requests, json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from django.shortcuts import render
from django.http import HttpResponse

def Upbit():
    url = "https://api.upbit.com/v1/candles/minutes/1"
    querystring = {"market":"KRW-BTC","count":"1"}
    res = requests.request("GET", url, params=querystring)
    Upbit_result = res.json()

    # 업비트의 price는 binance와 1000:1 관계
    price = Upbit_result[0]['trade_price']
    symbol = Upbit_result[0]['market']

		#key 값을 비교대상(binance)의 key 값과 동일시 하고 이름과 가격에 대한 json 생성(dict타입)
    dict_res = {}
    dict_res['symbol'] = symbol
    dict_res['price'] = price
    str_Upbit_result = json.dumps(dict_res)
    json_Upbit_result = json.loads(str_Upbit_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
    pandas_Upbit_result = json_normalize(json_Upbit_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다
    return pandas_Upbit_result


#210406
#데이터 순서(symbol,price)
#변수명 변경 완료
#데이터 불러오기 완료
#함수로 변환하는 작업 필요