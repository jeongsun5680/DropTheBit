import requests, json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from django.shortcuts import render
from django.http import HttpResponse

def Binance():
    url = "https://api.binance.com"
    res = requests.get(url + "/api/v3/ticker/price", params={'symbol': "BTCUSDT"})
    Bin_result = res.json()
    binance_price = float(Bin_result['price']) #price str -> float로 형변환
    Bin_result['price'] = binance_price #바이낸스 가격 저장
    str_Bin_result = json.dumps(Bin_result) #json의 dict타입을 str 타입으로 변환시켜준다.
    json_Bin_result = json.loads(str_Bin_result) #json의 string 형태의 객체에서 json 형식 내용을 추출할 때 사용한다.
    pandas_Bin_result = json_normalize(json_Bin_result) #json에서 데이터프레임을 쉽게 생성하도록 도움을 준다
    return pandas_Bin_result 
    # 1. 열 추가 방법
    # 1-1. 방법1
    # city = ['32424']
    # pandas_Bin_result['city'] = city
    

# 1-2. 방법2
# df = df.assign(city = ['Lahore'])
#print(df)

#210406
#데이터 순서(symbol,price)
#변수명 변경 완료
#데이터 불러오기 완료