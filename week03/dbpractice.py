from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에서 데이터 모두 보기

# MongoDB에서 특정 조건의 데이터 모두 보기
# 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.delete_one({'name': '론'})

user = db.users.find_one({'name': '론'})
print(user)
