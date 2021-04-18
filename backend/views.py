#from django.shortcuts import render
#from rest_framework import viewsets
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import arbitrage
from .main import star_coin, star_market
from .main.view_table import standard
from .member import login, mypage, register

# http 메소드로 들어오는 get,post 방식에 따라 응답하는 것을 만들거다
@api_view(['GET'])
def get_all_coin_info(request):
    user_id = request.GET.get('user_id')
    # user_id를 기반으로 DB로부터 STANDARD_MARKET 받아와야 한다
    # STANDARD_MARKET = MongoDbManager().get_standard_market({'user_id':user_id})
    # TARGET_MARKET도 마찬가지다
    # TARGET_MARKET = MongoDbManager().get_target_market({'user_id':user_id})
    STANDARD_MARKET = "upbit"
    TARGET_MARKET = ["binance"]
    coins = arbitrage.get_coins_lst(STANDARD_MARKET)
    data = arbitrage.get_all_coin_info(coins, STANDARD_MARKET, TARGET_MARKET)
    return Response(data)
    #return Response()

def update_standard(request):
    user_id = request.POST['user_id']
    standard_market = request.POST['standard_market']
    standard.update_standard(user_id, standard_market)

def update_star_coin(request):
    user_id = request.POST['user_id']
    star_coin = request.POST['star_coin']
    status = request.POST['status']
    star_coin.update_star_coin(user_id, star_coin, status)

def update_star_market(request):
    user_id = request.POST['user_id']
    star_market = request.POST['star_market']
    status = request.POST['status']
    star_coin.update_star_market(user_id, star_market, status)

def get_login(request):
    user_id = request.GET.get('user_id') # 이거 view에서 넘겨받아야 한다
    user_pw = request.GET.get('user_pw')
    status, data = login.get_login(user_id, user_pw) # 200 성공, 400 비번틀림, 404 회원정보 없음
    if status == 200:
        # return HttpResponse(status=200)
        pass # return HttpResponse(json.dumps(dbUserData), status=200)
    elif status == 400:
        # return HttpResponse(status=400)
        pass # return HttpResponse("비밀번호가 틀렸습니다", status = 400)
    else:
        # return HttpResponse(status=404)
        pass # return HttpResponse("회원정보가 존재하지 않습니다", status = 404)
    # return 뭐할지 정해야 한다

def create_user(request):
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']
    email = request.POST['email']
    name = request.POST['name']
    status, data = register.create_user(user_id, user_pw, email, name)
    if status == 200:
        pass # return HttpResponse(status=200)
    else:
        pass # return HttpResponse(status = 400)

def get_mypage(request):
    user_id = request.GET.get('user_id')
    data = mypage.get_mypage(user_id)
    return HttpResponse(data)
