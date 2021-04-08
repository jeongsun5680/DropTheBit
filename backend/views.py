from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .arbitrage import *

@api_view(["GET"])
def get_all_coins(request):
    """
    거래소별 코인 가격을 얻어오는 함수 호출
    이 때, 모든 거래소에 대한 가격이 통합되어 반환된다.
    반환된 가격을 dict 형태로 전달한다. Response({'user':'jisu'})
    """
    # call backend function
    dict_total = {
        "id": "BTC",
        "name_kr": "비트코인",
        "name_en": "Bitcoin",
        "standard":
            {
                "market": "upbit",
                "market_KRW": uprice,
                "market_USD": uprice_usd
            },
        "target": [
            {
                "market": "Binance",
                "market_KRW": bprice_krw,
                "market_USD": bprice,
                "diff_KRW": uprice - bprice_krw,
                "diff_USD": uprice_usd - bprice,
                "diff_percent": ((uprice - bprice_krw) / uprice) * 100
            }
        ]
    }
    return Response({'data':dict_total})



