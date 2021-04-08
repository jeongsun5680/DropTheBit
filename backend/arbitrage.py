from .api import binance, upbit, exchange_rate #upbit, binance, exchange_rate의 값을 호출
import json

bprice = binance.Binance()['price'][0] #bprice = 바이낸스 가격 호출 /type(float)
exrate = exchange_rate.Exchange_Rate() #exrate = 달러 환률 변환 호출 /type(str)
exrate = exrate.replace(',','') # 문자열을 정수로 변경하기 위해 ,를 제거한다.ex)1,127.8 ->1127.8
fexrate = float(exrate) #float로 형변환
bprice_krw = bprice*fexrate #바이낸스 가격을 krw로 변환
uprice = upbit.Upbit()['price'][0] #uprice = 업비트 가격 호출
uprice_usd = uprice/fexrate #uprice_usd = 업비트 가격을 usd로 변환
#1. 바이낸스 환률 변환 값 -> 성공

#요청후
dict_total = {
    "id": "BTC",
    "name_kr": "비트코인",
    "name_en": "Bitcoin",
    "standard" : [
        {
            "symbol" : "upbit",
            "standard_price_krw": uprice,
            "standard_price_usd": uprice_usd
        }
    ],
    "target" : [
        {
            "symbol" : "Binance",
            "compare01_price_krw": bprice_krw,
            "compare01_price_usd": bprice,
            "difference01_price_krw": uprice-bprice_krw,
            "difference01_price_usd": uprice_usd-bprice,
	        "difference01_price_percentage": ((uprice-bprice_krw)/uprice)*100
        }
    ]
}
json_total = json.dumps(dict_total,ensure_ascii=False) #ensure_ascii=False :한글 인코딩
print(json_total)