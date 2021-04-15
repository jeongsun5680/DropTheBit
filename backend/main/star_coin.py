#from MyApplication.MongoDbManager import MongoDbManager

def update_star_coin(user_id, star_coin, status):
    if status == 1: # 추가
        pass
        # dbUserData = MongoDbManager().add_star_coin({'user_id':user_id, 'star_coin':star_coin})
    else: # 삭제
        pass
        # dbUserData = MongoDbManager().del_star_coin({'user_id':user_id, 'star_coin':star_coin})

# DB에서 user_id 해당하는 star_coin에 insert
#status -> 메인페이지에서 클릭/비클릭 상태
#status가 클릭 상태일때 DB에서 user_id 해당하는 star_coin에 insert
#status가 비클릭 상태일때 DB에서 user_id 해당하는 star_coin에 delete