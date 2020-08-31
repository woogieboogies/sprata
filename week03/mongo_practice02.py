from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
## 월-E의 평점을 가져오기 / 월-E 평점이랑 같은 평점의 영화들 리스트업 / 월-E의 평점 0으로 만들기.
walle = db.project_db.insert_one(wall)
print(walle)

