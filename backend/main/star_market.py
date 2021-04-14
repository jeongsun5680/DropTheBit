#from MyApplication.MongoDbManager import MongoDbManager

def update_star_market(user_id, star_market, status):
    if status == 1: # 추가
        pass
        # dbUserData = MongoDbManager().add_star_market({'user_id':user_id, 'star_market':star_market})
    else: # 삭제
        pass
        # dbUserData = MongoDbManager().del_star_market({'user_id':user_id, 'star_market':star_market})