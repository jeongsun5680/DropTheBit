from django.http import HttpResponse
import json

# from MyApplication.MongoDbManager import MongoDbManager

def get_mypage(request):
    # request.GET 하면은 QueryDict 형태로 받아진다 {'user_id':'jeongsun'}
    user_id = request.GET.get('user_id')
    # dbUserData = MongoDbManager().get_user_from_db({'user_id':user_id}) # _id, user_id, user_pw, name, email 이렇게 온다고 가정하자
    # del dbUserData['_id']
    # del dbUserData['user_pw']
    # return HttpResponse(json.dumps(dbUserData)) # user_id, name, email 의 딕셔너리가 json으로 변환되어 전달 될 것