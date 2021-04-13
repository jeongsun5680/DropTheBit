"""
이 파일은 api 값 전달을 함수화하여 거래소 변수만 변경하면 쉽게 보낼 수 있는 파일입니다.

할 일
1. 전역 변수에 USD_PER_KRW가 환율인데 이것을 환율 사이트에서 받아오기(기존 코드 활용)
2. 코인별 한글 이름 받아오는 방법 찾아 함수 작성하기(DB에서 불러오기(지수와 이야기))
3. 코인별 영어 이름 받아오는 방법 찾아 함수 작성하기(DB에서 불러오기(지수와 이야기))
4. 마켓별 코인 달러 가격 구하기
   - 판다스에 저장된 데이터 불러오기
5. 마켓별 코인 원화 가격 구하기
   - 판다스에 저장된 데이터 불러오기
"""
from api import market, exchange_rate
import json 

# Global Variable
# exchange rate
# TODO 01: 환율 받아오기(1200원 부분 바꾸기)
#USD_PER_KRW = 1200
STANDARD_MARKET = "upbit"
TARGET_MARKET = ["binance"]


# params : 코인목록, 업비트, 거래소 목록
def get_all_coin_info(coins, std_market, tar_market):
    all_coin_info = []
    for coin in coins:
        all_coin_info.append(get_one_coin_info(coin, std_market, tar_market))

    return all_coin_info


def get_one_coin_info(coin, std_market, tar_market):
    market_info = market.get_market_all()
    std_price_KRW = get_price_KRW(coin, std_market, market_info)
    std_price_USD = get_price_USD(coin, std_market, market_info)

    one_coin_info = {
        "id": coin,
        "name_kr": get_name_kr(coin),
        "name_en": get_name_en(coin),
        "standard": {
            "market": std_market,
            "market_KRW": std_price_KRW,
            "market_USD": std_price_USD,
        },
        "target": get_target_lst(coin, tar_market, std_price_KRW, std_price_USD, market_info)
    }

    return one_coin_info


# TODO 02: 코인별 kr 이름 받아오기
def get_name_kr(coin):
    name_kr = ''
    # DB에서 coin에 대한 한글 이름 받아오기
    return name_kr


# TODO 03: 코인별 en 이름 받아오기
def get_name_en(coin):
    name_en = ''
    # DB에서 coin에 대한 영어 이름 받아오기
    return name_en


# TODO 04: 마켓별 코인 달러 가격 구하기
def get_price_USD(coin, market_name, market_info):
    exrate = exchange_rate.Exchange_Rate() #exrate = 달러 환률 변환 호출 /type(str)
    exrate = exrate.replace(',','') # 문자열을 정수로 변경하기 위해 ,를 제거한다.ex)1,127.8 ->1127.8
    fexrate = float(exrate) #float로 형변환
    # bianance는 if문 처리 필요
    if market_name == "binance":
        market_price_usd = market_info[market_name][coin]
    else:
        market_price_usd = market_info[market_name][coin]/fexrate
    
    return market_price_usd


# TODO 05: 마켓별 코인 원화 가격 구하기
def get_price_KRW(coin, market_name, market_info):
    exrate = exchange_rate.Exchange_Rate() #exrate = 달러 환률 변환 호출 /type(str)
    exrate = exrate.replace(',','') # 문자열을 정수로 변경하기 위해 ,를 제거한다.ex)1,127.8 ->1127.8
    fexrate = float(exrate) #float로 형변환
    # binance는 if문 처리 필요
    if market_name == "binance":
        market_price_krw = market_info[market_name][coin]*fexrate
    else:
        market_price_krw = market_info[market_name][coin]
    return market_price_krw


# TODO 06: 타겟 리스트들의 KRW값, USD값, 차이값(KRW, USD), 퍼센트 구해서 타겟 리스트로 반환
def get_target_lst(coin, tar_market, std_price_KRW, std_price_USD, market_info):
    # 타겟 마켓이 아무것도 없으면(None 이면)
    if tar_market is None:
        return []

    # 여기 논리를 짜주세요.
    target_lst = []

    for target in tar_market:
        dict_target_info = {}
        target_price_KRW = get_price_KRW(coin, target, market_info)
        target_price_USD = get_price_USD(coin, target, market_info)

        dict_target_info["symbol"] = target
        dict_target_info["compare01_price_krw"] = target_price_KRW
        dict_target_info["compare01_price_usd"] = target_price_USD
        dict_target_info["difference01_price_krw"] = std_price_KRW - target_price_KRW
        dict_target_info["difference01_price_usd"] = std_price_USD - target_price_USD
        dict_target_info["difference01_price_percentage"] = ((std_price_KRW-target_price_KRW)/std_price_KRW)*100
        target_lst.append(dict_target_info)

    return target_lst


# TODO 07: 코인 목록 구하기
def get_coins_lst(std_market):
    coins_lst = ['BTC', 'ETH']

    return coins_lst


# Main
# Testing
coins_lst = get_coins_lst(STANDARD_MARKET)

print(get_all_coin_info(coins_lst, STANDARD_MARKET, TARGET_MARKET))