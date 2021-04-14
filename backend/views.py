#from django.shortcuts import render
#from rest_framework import viewsets
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
import arbitrage

# http 메소드로 들어오는 get,post 방식에 따라 응답하는 것을 만들거다
#@api_view(['GET'])
def get_all_coin_info(request):
    user_id = request.POST('user_id')
    # user_id를 기반으로 DB로부터 STANDARD_MARKET 받아와야 한다
    # STANDARD_MARKET = MongoDbManager().get_standard_market({'user_id':user_id})
    # TARGET_MARKET도 마찬가지다
    # TARGET_MARKET = MongoDbManager().get_target_market({'user_id':user_id})
    STANDARD_MARKET = "upbit"
    TARGET_MARKET = ["binance"]
    coins = arbitrage.get_coins_lst(STANDARD_MARKET)
    data = arbitrage.get_all_coin_info(coins, STANDARD_MARKET, TARGET_MARKET)
    return data
    #return Response()