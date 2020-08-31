import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

Musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

count = 1
for Music in Musics:
    # count = count + 1

    Number = Music.select_one("td.number").text[0:2].strip()
    Title = Music.select_one("td.info > a.title.ellipsis").text.strip()
Artist = Music.select_one("td.info > a.artist.ellipsis").text
print(Number, Title, Artist)
db.music.insert_one({
    'Number': Music.select_one("td.number").text[0:2].strip(),
    'Title': Music.select_one("td.info > a.title.ellipsis").text.strip(),
    'Artist': Music.select_one("td.info > a.artist.ellipsis").text
})
