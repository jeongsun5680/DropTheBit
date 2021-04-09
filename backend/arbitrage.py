from api import binance, upbit, exchange_rate, market
import json

# bprice = binance.Binance()['price'][0] #bprice = 바이낸스 가격 호출 /type(float)
# exrate = exchange_rate.Exchange_Rate() #exrate = 달러 환률 변환 호출 /type(str)
# exrate = exrate.replace(',','') # 문자열을 정수로 변경하기 위해 ,를 제거한다.ex)1,127.8 ->1127.8
# fexrate = float(exrate) #float로 형변환
# bprice_krw = bprice*fexrate #바이낸스 가격을 krw로 변환
# uprice = upbit.Upbit()['price'][0] #uprice = 업비트 가격 호출
# uprice_usd = uprice/fexrate #uprice_usd = 업비트 가격 호출

#1. 바이낸스 환률 변환 값 -> 성공

# dict_total = {
#     "id": "BTC",
#     "name_kr": "비트코인",
#     "name_en": "Bitcoin",
#     "standard" : [
#         {
#             "symbol" : "upbit",
#             "standard_price_krw": uprice,
#             "standard_price_usd": uprice_usd
#         }
#     ],
#     "target" : [
#         {
#             "symbol" : "Binance",
#             "compare01_price_krw": bprice_krw,
#             "compare01_price_usd": bprice,
#             "difference01_price_krw": uprice-bprice_krw,
#             "difference01_price_usd": uprice_usd-bprice,
# 	        "difference01_price_percentage": ((uprice-bprice_krw)/uprice)*100
#         }
#     ]
# }

# 1. market.py에서 이더리움을 받아오는 정보를 url_info에 추가
# 2. market.py의 url_info에서 코인을 구분할 수 있는 "coin" 키 값 추가 -> "coin":"bitcoin" 혹은 "coin":"etherium"
# 3. market.py의 get_market에서 리턴하는 값에 url_info의 "coin"을 추가
# 4. arbitarage.py에서 market.py의 get_market으로 받아야 하는 값 -> (코인 종류, 거래소 이름, 가격) -> market.py에서 보내주던 symbol을 바꿀 필요가 있다


coin_list=['BTC', 'ETH']

{
        id: "BTC",
        name_kr: "비트코인",
        name_en: "Bitcoin",
        standard: {
          market: "Upbit",
          market_KRW: 77777777,
          market_USD: 66666.32,
        },
        target: [{
          market: "Binance",
          market_KRW: 66666666,
          market_USD: 5555500,
          diff_KRW: 11111111,
          diff_USD: 1111132,
          diff_percent: 1442,
        }],
      }, 



list_total =[
      {
        id: "BTC",
        name_kr: "비트코인",
        name_en: "Bitcoin",
        standard: {
          market: "Upbit",
          market_KRW: 77777777,
          market_USD: 66666.32,
        },
        target: [{
          market: "Binance",
          market_KRW: 66666666,
          market_USD: 5555500,
          diff_KRW: 11111111,
          diff_USD: 1111132,
          diff_percent: 1442,
        }],
      },
      {
        id: "ETH",
        name_kr: "이더리움",
        name_en: "Etherem",
        standard: {
          market: "Upbit",
          market_KRW: 11111,
          market_USD: 6666623232323.32,
        },
        target: [{
          market: "Binance",
          market_KRW: 62226666666,
          market_USD: 55551233500,
          diff_KRW: 1111111211,
          diff_USD: 1111122323323,
          diff_percent: 14422222222,
        }],
      },
  ]

json_total = json.dumps(dict_total,ensure_ascii=False)
print(json_total)