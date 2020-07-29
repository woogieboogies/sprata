from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##
## 월-E의 평점을 가져오기 / 월-E 평점이랑 같은 평점의 영화들 리스트업 / 월-E의 평점 0으로 만들기.
walle = db.movies.find_one({'title': '월-E'})
print(walle)

star = list(db.movies.find({'star': walle['star']}))
print(star)


#for movie in star:
#    db.movies.update_one({'title': movie['title']}, {'$set': {'star': '9.41'}})

