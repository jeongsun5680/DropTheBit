def get_login(user_id, user_pw):
    # 아이디, 비번이 모두 있을 때 - 200
    # 아이디만 있을 때 - 400
    # 둘 다 없을 때 - 404

    # user_id, user_pw로 DB에 쿼리실행
    # 리턴 값 있으면 -> status = 200
    # 리턴 값 없으면 -> user_id로 DB 쿼리 실행
                    # 리턴 있으면 -> status = 400
                    # 리턴 없으면 -> status = 404
    return # status 코드 리턴 