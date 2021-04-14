#from MyApplication.MongoDbManager import MongoDbManager

def update_star_coin(user_id, star_coin, status):
    if status == 1: # 추가
        pass
        # dbUserData = MongoDbManager().add_star_coin({'user_id':user_id, 'star_coin':star_coin})
    else: # 삭제
        pass
        # dbUserData = MongoDbManager().del_star_coin({'user_id':user_id, 'star_coin':star_coin})