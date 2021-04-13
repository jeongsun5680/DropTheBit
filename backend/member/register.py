import djongo
from django.http import httpResponse
# user_id, user_pw, email, name
    # 아이디
    # 아이디 리턴 값이 있으면 -> 400
    # 아이디 리턴 값이 없으면 -> db에 파라미터 값 저장(200)
    # 비번 , 이메일, 이름 

def create_user(request):
    user_id = request.POST['user_id']
    user_pw = request.POST['user_pw']
    email = request.POST['email']
    name = request.POST['name']
  # dbUserData = MongoDbManager().get_user_from_db({'id':user_id,})
    if dbUserData is None:
        # return httpResponse("중복되는 아이디가 있습니다.",status =400)
        pass
    else:
        # return HttpResponse(json.dumps(dbUserData), status=200)
        pass 
    