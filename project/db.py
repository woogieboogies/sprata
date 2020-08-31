from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.


all_items = db.project.insert_many([
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신혜성약국",
    "Address": "서울특별시 강남구 논현로 409 1층 일부호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "아이조은약국",
    "Address": "서울특별시 강남구 삼성로 620 블래스톤리조트 2층 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "영진약국",
    "Address": "서울특별시 강남구 학동로 421 1층 일부호 (청담동, 원영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "서울온누리약국",
    "Address": "서울특별시 강남구 역삼로77길 23 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "강남소화약국",
    "Address": "서울특별시 강남구 봉은사로114길 42 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "포인트약국",
    "Address": "서울특별시 강남구 도산대로 118 1층 일부호 (논현동, 논현빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ2MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "해림온누리약국",
    "Address": "서울특별시 강남구 테헤란로 152 지하2층 (역삼동, 강남파이낸스센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ4MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "다온약국",
    "Address": "서울특별시 강남구 테헤란로 328 401호 (역삼동, 동우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQyIyQ1IyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "독수리약국",
    "Address": "서울특별시 강남구 일원로 95 106호 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "강남세계로약국",
    "Address": "서울특별시 강남구 논현로 52 남현빌딩 1층 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQwMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "청담본약국",
    "Address": "서울특별시 강남구 학동로97길 20 1층 일부호 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ2MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "블루밍약국",
    "Address": "서울특별시 강남구 강남대로 492 지하1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "압구정온누리약국",
    "Address": "서울특별시 강남구 압구정로 164 아세아빌딩 105호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "좋은아침약국",
    "Address": "서울특별시 강남구 논현로85길 7 5층 (역삼동, 은혜빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "더블유약국",
    "Address": "서울특별시 강남구 강남대로 468 1층 (역삼동, 충림빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ2MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "선릉타워약국",
    "Address": "서울특별시 강남구 테헤란로 326 역삼 아이타워 지하1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 강남구 압구정로 224 208호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "대광약국",
    "Address": "서울특별시 강남구 개포로109길 9 101호 (개포동, 대치임대A상가 )"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "트리스약국",
    "Address": "서울특별시 강남구 언주로147길 6 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "아너힐즈약국",
    "Address": "서울특별시 강남구 삼성로 11 상가 지상1층 113호 (개포동, 디에이치 아너힐즈)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "비타약국",
    "Address": "서울특별시 강남구 논현로 561 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "강남리더스약국",
    "Address": "서울특별시 강남구 헌릉로 569 1층 105호 (세곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "대청약국",
    "Address": "서울특별시 강남구 개포로 623 대청타워 106호 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "삼성해든약국",
    "Address": "서울특별시 강남구 삼성로 520 1층 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신분당약국",
    "Address": "서울특별시 강남구 강남대로 396 23호 (역삼동, 신분당선 강남역내)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "삼성하나약국",
    "Address": "서울특별시 강남구 테헤란로 509 1층 일부호 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "펜타약국",
    "Address": "서울특별시 강남구 테헤란로64길 9 지하1층 101호 (대치동, 선릉역대우아이빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 강남구 논현로 835 JK빌딩 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "베어약국",
    "Address": "서울특별시 강남구 봉은사로114길 12 지하 1층 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "압구정영약국",
    "Address": "서울특별시 강남구 압구정로28길 25 엑시 1층 1호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "케이팜약국",
    "Address": "서울특별시 강남구 도곡로 405 107호 (대치동, 삼환아르누보2)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQyIyQzIyQwMCQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "한티약국",
    "Address": "서울특별시 강남구 선릉로 225 지하1층 133호 (도곡동, 도곡렉슬상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "이룸약국",
    "Address": "서울특별시 강남구 논현로 838 원방프라자 1층 일부호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "청담더약국",
    "Address": "서울특별시 강남구 선릉로 834 모던빌딩 1층 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "해바라기약국",
    "Address": "서울특별시 강남구 강남대로 320 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "세곡리엔약국",
    "Address": "서울특별시 강남구 헌릉로570길 34 1층 108호 (세곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "준약국",
    "Address": "서울특별시 강남구 학동로 121 지하1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQwMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "에이타워약국",
    "Address": "서울특별시 강남구 테헤란로 105 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "영원약국",
    "Address": "서울특별시 강남구 봉은사로 108 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQyIyQzIyQwMCQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "메디피아약국",
    "Address": "서울특별시 강남구 강남대로 242 1층 (도곡동, 크리스탈빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQwMyQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 강남구 남부순환로 2927 대치 클래시아 1층 105호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ4MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "인터팜이화약국",
    "Address": "서울특별시 강남구 도산대로38길 11 102-4호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "명옥약국",
    "Address": "서울특별시 강남구 압구정로 212 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ2MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "제이약국",
    "Address": "서울특별시 강남구 테헤란로 101 B101호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQwMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "강남맑은약국",
    "Address": "서울특별시 강남구 강남대로 292 3층 (도곡동, 뱅뱅빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ2MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "역삼다인약국",
    "Address": "서울특별시 강남구 논현로 521-3 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQ4MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "노벨약국",
    "Address": "서울특별시 강남구 선릉로131길 8 13호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ2MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "건강한세상행복한약국",
    "Address": "서울특별시 강남구 강남대로 488 1층 (논현동, 대남빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ2MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "양성심약국",
    "Address": "서울특별시 강남구 논현로175길 60 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQ3IyQwMCQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "압구정예주약국",
    "Address": "서울특별시 강남구 압구정로29길 65 442빌딩 지하1층 (압구정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "스타약국",
    "Address": "서울특별시 강남구 남부순환로 2615 2층 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "정다운이화약국",
    "Address": "서울특별시 강남구 역삼로 306 4층 407호 (역삼동, 개나리래미안상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQyIyQ3IyQwMCQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "압구정스타약국",
    "Address": "서울특별시 강남구 압구정로20길 15 102호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "소망온누리약국",
    "Address": "서울특별시 강남구 학동로 338 S102호 (논현동, 강남파라곤)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "청담약국",
    "Address": "서울특별시 강남구 학동로 503 한성빌딩 1층 106호 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQxMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "강남프라자약국",
    "Address": "서울특별시 강남구 학동로 323 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "수서메디칼약국",
    "Address": "서울특별시 강남구 밤고개로1길 10 210호 (수서동, 수서현대벤쳐빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQwMyQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "도심공항약국",
    "Address": "서울특별시 강남구 테헤란로87길 22 2층 D-1호 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "굿케어약국",
    "Address": "서울특별시 강남구 선릉로 719 1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "여기애가까운약국",
    "Address": "서울특별시 강남구 압구정로28길 31 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQwMyQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "샘터약국",
    "Address": "서울특별시 강남구 일원로 120 101호 (일원동, 샘터마을 현대아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQwMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "오늘약국",
    "Address": "서울특별시 강남구 도곡로 449 2층 201 일부호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQwMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "이층엔약국",
    "Address": "서울특별시 강남구 자곡로 201 210호 (자곡동, 강남더샵라르고오피스텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "씨티약국",
    "Address": "서울특별시 강남구 강남대로 416 1층 (역삼동, 창림빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQxIyQwMCQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "장약국",
    "Address": "서울특별시 강남구 학동로 224 B109호 (논현동, 삼환아르누보)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ2MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "메트로약국",
    "Address": "서울특별시 강남구 언주로30길 13 B동 102호 (도곡동, 대림아크로빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "싱싱약국",
    "Address": "서울특별시 강남구 선릉로 567 1층 일부호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "청담밝은약국",
    "Address": "서울특별시 강남구 선릉로 612 한일빌딩 1층 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "허지웅약국",
    "Address": "서울특별시 강남구 테헤란로 532 1층 105호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "루비약국",
    "Address": "서울특별시 강남구 논현로 823 101호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신현대약국",
    "Address": "서울특별시 강남구 압구정로 151 상가2동 9호 (압구정동, 현대아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "압구정웰약국",
    "Address": "서울특별시 강남구 압구정로28길 49 유림아트홀 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "이레약국",
    "Address": "서울특별시 강남구 선릉로 314 201-2호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ5MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "참좋은약국",
    "Address": "서울특별시 강남구 테헤란로87길 17 103호 (삼성동, 마젤란21상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ4OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "국송약국",
    "Address": "서울특별시 강남구 광평로51길 49 108호 (수서동, 주공A1단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQwMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "종원약국",
    "Address": "서울특별시 강남구 강남대로118길 38 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "화일약국",
    "Address": "서울특별시 강남구 선릉로 328 1층 6,7호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQxMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "건강한온누리약국",
    "Address": "서울특별시 강남구 압구정로34길 11 압구정스퀘어 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ4MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "청담메디웰약국",
    "Address": "서울특별시 강남구 삼성로 772 105호 (청담동, 로데오프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ2MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "강남미약국",
    "Address": "서울특별시 강남구 강남대로 376 1층 1호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "성균관약국",
    "Address": "서울특별시 강남구 일원로 49 1층 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ5OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "삼우약국",
    "Address": "서울특별시 강남구 개포로82길 11 101호 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "강남조은약국",
    "Address": "서울특별시 강남구 남부순환로 2633 102호 (도곡동, 호림빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "압구정소망약국",
    "Address": "서울특별시 강남구 언주로173길 19 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "행운약국",
    "Address": "서울특별시 강남구 논현로 836 삼신빌딩 1층 102호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "역삼우주약국",
    "Address": "서울특별시 강남구 언주로85길 32 역삼역센트럴푸르지오 B106호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "정일약국",
    "Address": "서울특별시 강남구 도곡로 458 102호 (대치동, 정일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ5MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "이대학약국",
    "Address": "서울특별시 강남구 일원로 95 105,202호 (일원동, 신영프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ2MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "삼성수약국",
    "Address": "서울특별시 강남구 삼성로96길 11 1층 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "동의온누리약국",
    "Address": "서울특별시 강남구 논현로 330 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "희영온누리약국",
    "Address": "서울특별시 강남구 봉은사로 471 204-1호 (삼성동, 힐스테이트2단지상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "석탑이레약국",
    "Address": "서울특별시 강남구 개포로 615 401호 (개포동, 석탑프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQwMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "다솜약국",
    "Address": "서울특별시 강남구 도곡로 205 1층 (역삼동, 원경빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "아이약국",
    "Address": "서울특별시 강남구 삼성로 712 지하1층 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "비원약국",
    "Address": "서울특별시 강남구 논현로 824 1층 일부호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "베스트약국",
    "Address": "서울특별시 강남구 도곡로 423 1층 일부호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ2MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "개포플러스약국",
    "Address": "서울특별시 강남구 선릉로 30 개포빌딩 1층 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "킴다나약국",
    "Address": "서울특별시 강남구 선릉로 511 1층 일부호 (역삼동, 화신빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "테헤란한서약국",
    "Address": "서울특별시 강남구 테헤란로 206 1층 1호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ2MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "사랑플러스약국",
    "Address": "서울특별시 강남구 선릉로 225 313호 (도곡동, 도곡렉슬상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ2MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "메디칼미래약국",
    "Address": "서울특별시 강남구 삼성로 38 306호 (개포동, 개포빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ4OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "동양약국",
    "Address": "서울특별시 강남구 자곡로 180 109-2호 (자곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "아름약국",
    "Address": "서울특별시 강남구 강남대로 364 미왕빌딩 2층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "일원역약국",
    "Address": "서울특별시 강남구 일원로 121 지하층 (일원동, 일원역)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "매봉약국",
    "Address": "서울특별시 강남구 남부순환로 2725 1층 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "세곡온누리약국",
    "Address": "서울특별시 강남구 헌릉로569길 27 2층 (세곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ5OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "생생온누리약국",
    "Address": "서울특별시 강남구 논현로 842 압구정빌딩 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "건강온누리약국",
    "Address": "서울특별시 강남구 삼성로 212 B동 1층 195호 (대치동, 은마아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "도곡메디칼약국",
    "Address": "서울특별시 강남구 도곡로 242 (도곡동, 도곡삼호상가 지하1층 103호 1층 201호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "한양약국",
    "Address": "서울특별시 강남구 언주로157길 6 (신사동, 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQwMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "삼주약국",
    "Address": "서울특별시 강남구 테헤란로 124 B-101호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "타조약국",
    "Address": "서울특별시 강남구 삼성로 707 1층 (청담동, 청담빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "역삼약국",
    "Address": "서울특별시 강남구 역삼로 128 101호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ5OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "신사약국",
    "Address": "서울특별시 강남구 도산대로 109 1층 101호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ2MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "팜메이트수정약국",
    "Address": "서울특별시 강남구 선릉로 338 103호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQwMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "대치이화약국",
    "Address": "서울특별시 강남구 역삼로 536 3층 (대치동, 동성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ2MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "태양약국",
    "Address": "서울특별시 강남구 압구정로 150 110호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "고은약국",
    "Address": "서울특별시 강남구 봉은사로 105 2층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ2MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 강남구 테헤란로 222 도원빌딩 지하1층 일부 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "학동약국",
    "Address": "서울특별시 강남구 학동로 203 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "위드팜바른약국",
    "Address": "서울특별시 강남구 일원로 115 1층 109호 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "압구정엘약국",
    "Address": "서울특별시 강남구 압구정로28길 13 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQzIyQwMCQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "신사웰약국",
    "Address": "서울특별시 강남구 강남대로 596 극동빌딩 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQwMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "민트약국",
    "Address": "서울특별시 강남구 강남대로 590 미혜빌딩 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQxMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "신논현약국",
    "Address": "서울특별시 강남구 봉은사로 109 싼타홍메디컬타워 지하1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "우리대치약국",
    "Address": "서울특별시 강남구 남부순환로 2936 윈플러스상가 1층 102호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "이즈약국",
    "Address": "서울특별시 강남구 논현로164길 14 (신사동, 금강빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "천사약국",
    "Address": "서울특별시 강남구 일원로 95 108호 (일원동, 신영프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQwMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "역삼태평양약국",
    "Address": "서울특별시 강남구 논현로 564 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "옵티마미소약국",
    "Address": "서울특별시 강남구 논현로 570 1층 일부호 (역삼동, 여송빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ2MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "사랑의약국",
    "Address": "서울특별시 강남구 밤고개로1길 10 2층 219호 (수서동, 수서현대벤쳐빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQwMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "로데오약국",
    "Address": "서울특별시 강남구 선릉로 823 1층 (신사동, 한양타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ3OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "누리약국",
    "Address": "서울특별시 강남구 테헤란로 310 3층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ3MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "강남웰약국",
    "Address": "서울특별시 강남구 강남대로 432 점프밀라노 지하1층 101호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQwMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "강남새천년온누리약국",
    "Address": "서울특별시 강남구 도곡로 523 1층 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 강남구 선릉로69길 19 104호 (역삼동, 역삼래미안상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "팜스약국",
    "Address": "서울특별시 강남구 논현로 509 1층 1호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "은혜온누리약국",
    "Address": "서울특별시 강남구 남부순환로 2912 117호, 118호 (대치동, 우성아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQwMyQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "두리약국",
    "Address": "서울특별시 강남구 일원로 35 1층 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQ1IyQwMCQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "강남우리온누리약국",
    "Address": "서울특별시 강남구 테헤란로 403 101호 (삼성동, 리치타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ2MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "유정약국",
    "Address": "서울특별시 강남구 삼성로 225 106호 (대치동, 아주빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "라온약국",
    "Address": "서울특별시 강남구 강남대로 318 1층 (역삼동, TOWER837)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "바이올렛약국",
    "Address": "서울특별시 강남구 강남대로 334 6층 (역삼동, SM타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "수진약국",
    "Address": "서울특별시 강남구 삼성로 150 119호 (대치동, 한보미도종합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "팜엑스약국",
    "Address": "서울특별시 강남구 봉은사로 524 H112호 (삼성동, 코엑스몰)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "다현약국",
    "Address": "서울특별시 강남구 언주로167길 46 1층 2호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "행복온누리약국",
    "Address": "서울특별시 강남구 개포로 231 1층 일부호 (개포동, 반석빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQwMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "왕성약국",
    "Address": "서울특별시 강남구 학동로 106 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ5MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "우창약국",
    "Address": "서울특별시 강남구 논현로113길 13 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "유한약국",
    "Address": "서울특별시 강남구 강남대로122길 47 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "광성약국",
    "Address": "서울특별시 강남구 강남대로 520 (논현동, 영동빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ3OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "신삼성약국",
    "Address": "서울특별시 강남구 봉은사로 465 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ4OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "메디칼청실약국",
    "Address": "서울특별시 강남구 남부순환로 2917 112호, 113호 (대치동, 청실상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "코코약국",
    "Address": "서울특별시 강남구 논현로28길 48 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ2MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "유진약국",
    "Address": "서울특별시 강남구 언주로 323 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "강남정성약국",
    "Address": "서울특별시 강남구 언주로 639 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "라라약국",
    "Address": "서울특별시 강남구 테헤란로 125 지하1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "밝은마음약국",
    "Address": "서울특별시 강남구 논현로 841 제이비 미소빌딩 110호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "에스약국",
    "Address": "서울특별시 강남구 도산대로 111 S-TOWER 지하1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "엠플러스약국",
    "Address": "서울특별시 강남구 강남대로 378 준빌딩 지하1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "약사랑약국",
    "Address": "서울특별시 강남구 테헤란로 339 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "타워약국",
    "Address": "서울특별시 강남구 도산대로 107 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQxMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜보문약국",
    "Address": "서울특별시 강남구 삼성로 38 1층 113호 (개포동, 개포빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "우리온누리약국",
    "Address": "서울특별시 강남구 남부순환로397길 57 1층 1호 (대치동, 대치메디칼센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQxMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "서이약국",
    "Address": "서울특별시 강남구 언주로30길 39 지하1층 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQxMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 강남구 일원로 95 지하1층 103호 (일원동, 신영프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "성지프라자약국",
    "Address": "서울특별시 강남구 논현로 507 지하1층 5호 (역삼동, 성지하이츠3차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "퍼스트약국",
    "Address": "서울특별시 강남구 삼성로 155 304-1호 (대치동, 대치퍼스트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ4MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "인선약국",
    "Address": "서울특별시 강남구 선릉로 755 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ2MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "해오름약국",
    "Address": "서울특별시 강남구 봉은사로73길 5 1층 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ2MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "싱싱온누리약국",
    "Address": "서울특별시 강남구 강남대로 620 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "청담온누리약국",
    "Address": "서울특별시 강남구 학동로 521 1층 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "연세팜약국",
    "Address": "서울특별시 강남구 학동로4길 24 101호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "도곡명약국",
    "Address": "서울특별시 강남구 도곡로28길 8 상가동 102,103호 (도곡동, 도곡1차 I PARK)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "논현수약국",
    "Address": "서울특별시 강남구 선릉로 705 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "수서홍약국",
    "Address": "서울특별시 강남구 광평로 295 사이룩스오피스텔 서관동 1층 101호 (수서동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "리본약국",
    "Address": "서울특별시 강남구 도산대로16길 6 1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQwMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 강남구 테헤란로87길 13 1층 (삼성동, 서영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQwMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "동현당약국",
    "Address": "서울특별시 강남구 언주로146길 18 (논현동, 동현아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "논현약국",
    "Address": "서울특별시 강남구 선릉로129길 22 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "압구정약국",
    "Address": "서울특별시 강남구 선릉로 845 1층 4호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ5IyQwMCQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "곰돌이약국",
    "Address": "서울특별시 강남구 언주로 309 지하1층 (역삼동, 기성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ5MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "논현사랑약국",
    "Address": "서울특별시 강남구 학동로 313 1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQ1IyQwMCQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "강남백세약국",
    "Address": "서울특별시 강남구 도곡로 448 1층 일부호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "기쁨주는약국",
    "Address": "서울특별시 강남구 광평로 281 2층 일부호 (수서동, 수서빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQxMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "화인약국",
    "Address": "서울특별시 강남구 강남대로 372 5층 일부호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQxMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "렉슬약국",
    "Address": "서울특별시 강남구 선릉로 225 B103호 (도곡동, 도곡렉슬상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ4OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "은약국",
    "Address": "서울특별시 강남구 삼성로 549 (삼성동, 정화빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "도움약국",
    "Address": "서울특별시 강남구 압구정로29길 68 103호 (압구정동, 현대아파트주구센타)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "동호약국",
    "Address": "서울특별시 강남구 테헤란로114길 16 1층 1호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "더블유수약국",
    "Address": "서울특별시 강남구 압구정로 316 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQwMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "온누리새재원약국",
    "Address": "서울특별시 강남구 강남대로44길 28 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "선한약국",
    "Address": "서울특별시 강남구 논현로 605 1층 (논현동, 승진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "희병약국",
    "Address": "서울특별시 강남구 봉은사로43길 8 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "강남제일약국",
    "Address": "서울특별시 강남구 테헤란로 139 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 강남구 개포로 615 2층 (개포동, 석탑프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "에스엠피약국",
    "Address": "서울특별시 강남구 광평로19길 15 110호 (일원동, 목련상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQxIyQwMCQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "은마수약국",
    "Address": "서울특별시 강남구 삼성로 212 174호 (대치동, 은마상가에이블럭)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQxMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "메디팜무지개약국",
    "Address": "서울특별시 강남구 논현로159길 10 1층 일부호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "옵티마대영약국",
    "Address": "서울특별시 강남구 삼성로 642 106호, 107호 (삼성동, 삼성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "자곡온누리약국",
    "Address": "서울특별시 강남구 자곡로 114 109호 (자곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "청담제일약국",
    "Address": "서울특별시 강남구 영동대로 722 (청담동, 풍양빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQxMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "선능약국",
    "Address": "서울특별시 강남구 봉은사로54길 9 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ5MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "르씨엘약국",
    "Address": "서울특별시 강남구 학동로 215 101호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "강남역스타약국",
    "Address": "서울특별시 강남구 테헤란로4길 6 지하1층 b106호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQxMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "정성온누리약국",
    "Address": "서울특별시 강남구 도곡로 120 1층 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "솔약국",
    "Address": "서울특별시 강남구 개포로 615 101호 (개포동, 석탑프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "라이프약국",
    "Address": "서울특별시 강남구 삼성로149길 32 102호 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "타임약국",
    "Address": "서울특별시 강남구 선릉로 431 에스케이허브오피스텔 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQwMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "정원약국",
    "Address": "서울특별시 강남구 영동대로 722 풍양빌딩 1층 103호 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "청담별빛약국",
    "Address": "서울특별시 강남구 학동로 443 정한빌딩 1층 103호 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "목화약국",
    "Address": "서울특별시 강남구 양재대로55길 11 1층 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ4MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "대치필리아약국",
    "Address": "서울특별시 강남구 도곡로63길 12 104호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "캠브리지5층약국",
    "Address": "서울특별시 강남구 테헤란로 110 5층 일부호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "튼튼중앙약국",
    "Address": "서울특별시 강남구 개포로 615 석탑프라자 305-1호 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQwMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "수서옵티마약국",
    "Address": "서울특별시 강남구 광평로51길 8 1층 108호 (수서동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQxMyQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "메디칼정성약국",
    "Address": "서울특별시 강남구 밤고개로21길 8 1층 107호 (율현동, 세곡프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQxMyQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "청담명약국",
    "Address": "서울특별시 강남구 학동로 501 4층 일부호 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "압구정제이약국",
    "Address": "서울특별시 강남구 논현로171길 15 105호 (신사동, 카로시티1)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ5MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "호산나약국",
    "Address": "서울특별시 강남구 언주로 871 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ3MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "성일약국",
    "Address": "서울특별시 강남구 압구정로 160 제성빌딩 3층 301호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ2MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "명문약국",
    "Address": "서울특별시 강남구 양재대로55길 6 101호 (일원동, 수서1단지아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "건영약국",
    "Address": "서울특별시 강남구 선릉로 806 지하1층 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ5OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "샘약국",
    "Address": "서울특별시 강남구 테헤란로 322 102호 (역삼동, 한신인터밸리24)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "오렌지약국",
    "Address": "서울특별시 강남구 도산대로 124 1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "상록약국",
    "Address": "서울특별시 강남구 언주로 508 (역삼동, 상록회관내)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "이도건강약국",
    "Address": "서울특별시 강남구 테헤란로87길 29 1층 (삼성동, 엠타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQwMyQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "국기원약국",
    "Address": "서울특별시 강남구 테헤란로 119 2층 (역삼동, 대호빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ3OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "개포메디칼약국",
    "Address": "서울특별시 강남구 개포로 303 지하1층 16호 (개포동, 현대1차아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "다정온누리약국",
    "Address": "서울특별시 강남구 논현로 511 3층 (역삼동, YandC빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "압구정화이트약국",
    "Address": "서울특별시 강남구 압구정로30길 23 102호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "압구정퀸약국",
    "Address": "서울특별시 강남구 논현로 853 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "123약국",
    "Address": "서울특별시 강남구 언주로30길 10 410호 일부호 (도곡동, 현대비전21)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQzIyQwMCQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "수온누리약국",
    "Address": "서울특별시 강남구 테헤란로 216 신웅타워 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ4OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "샬롬온누리약국",
    "Address": "서울특별시 강남구 테헤란로28길 5 1층 일부호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "예주약국",
    "Address": "서울특별시 강남구 논현로115길 72 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "압구정미약국",
    "Address": "서울특별시 강남구 논현로175길 25 1층 (신사동, 다보빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ2MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "행복한미래약국",
    "Address": "서울특별시 강남구 언주로 707 2층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "삼성제일약국",
    "Address": "서울특별시 강남구 양재대로55길 7 1층 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "유니팜서울약국",
    "Address": "서울특별시 강남구 테헤란로 109 1층 (역삼동, 강남제일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "오월애약국",
    "Address": "서울특별시 강남구 강남대로 616 (신사동, 신사미타워 102호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "신논현비비약국",
    "Address": "서울특별시 강남구 강남대로 476 urbanhive 지하2층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 강남구 논현로 839 3층 일부호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 강남구 논현로 88 3층 (개포동, 노엘빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQwMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "사랑온누리약국",
    "Address": "서울특별시 강남구 삼성로92길 27 지하1층 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQyIyQxIyQwMCQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "압구정길약국",
    "Address": "서울특별시 강남구 압구정로 130 종화빌딩 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "신사온누리약국",
    "Address": "서울특별시 강남구 강남대로 600 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "동인프라자온누리약국",
    "Address": "서울특별시 강남구 밤고개로1길 10 117-2호 (수서동, 수서현대벤쳐빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQxMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "플러스약국",
    "Address": "서울특별시 강남구 테헤란로 111 1층 일부호 (역삼동, 대건빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQxMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "갤러리아온누리약국",
    "Address": "서울특별시 강남구 선릉로 843 107호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ3OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "부활약국",
    "Address": "서울특별시 강남구 영동대로112길 15 103호 (삼성동, 풍림아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ2MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "메디칼희민약국",
    "Address": "서울특별시 강남구 영동대로86길 10 1층 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ3MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "민생약국",
    "Address": "서울특별시 강남구 언주로125길 6 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "새휘정약국",
    "Address": "서울특별시 강남구 학동로101길 26 102호 (청담동, 삼익상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQxMyQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "영지약국",
    "Address": "서울특별시 강남구 도산대로92길 6 1층 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "새생명약국",
    "Address": "서울특별시 강남구 도산대로 522 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "호원약국",
    "Address": "서울특별시 강남구 언주로108길 15 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ5IyQwMCQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "채움약국",
    "Address": "서울특별시 강남구 압구정로34길 11 103호 (신사동, 압구정스퀘어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQyIyQ3IyQwMCQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "해맑은약국",
    "Address": "서울특별시 강남구 남부순환로363길 13 1층 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ5OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 강남구 압구정로29길 72-1 A동 109호 (압구정동, 신사시장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "현온누리약국",
    "Address": "서울특별시 강남구 강남대로 560 지하1층 2호 (논현동, 삼익전자빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQwMyQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "압구정원약국",
    "Address": "서울특별시 강남구 압구정로18길 6 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 강남구 도산대로 157 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "파낙스약국",
    "Address": "서울특별시 강남구 논현로 629 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ4MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "이삼성약국",
    "Address": "서울특별시 강남구 일원로 53 1층 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "주민약국",
    "Address": "서울특별시 강남구 일원로 33 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "센느약국",
    "Address": "서울특별시 강남구 강남대로 516 101호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQyIyQ3IyQwMCQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "혜린약국",
    "Address": "서울특별시 강남구 논현로 809 1호 (신사동, 강석빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "나리약국",
    "Address": "서울특별시 강남구 도곡로 442 105호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 강남구 남부순환로 2615 1층 103호 (도곡동, 극동스타클래스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "웰스약국",
    "Address": "서울특별시 강남구 봉은사로1길 4 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "메디팜압구정약국",
    "Address": "서울특별시 강남구 논현로160길 13 1층 101호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "수서약국",
    "Address": "서울특별시 강남구 광평로56길 11 109호 (수서동, 도시개발(아)6단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ2MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 강남구 일원로 95 (일원동, 101~103호, 지하1층(1호,2호일부,3호일부))"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQxMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "역삼라이프약국",
    "Address": "서울특별시 강남구 테헤란로25길 59 지하1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQyIyQ3IyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 강남구 압구정로 152 108호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "청담와이약국",
    "Address": "서울특별시 강남구 압구정로 461 B104호 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQyIyQ3IyQwMCQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 강남구 논현로 717 지하1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "삼성건강약국",
    "Address": "서울특별시 강남구 선릉로 670 1층 일부호 (삼성동, 해운빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 강남구 일원로 95 신영프라자 111호 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "박약국",
    "Address": "서울특별시 강남구 남부순환로 2933 대치상가 1층 101호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "강남봄약국",
    "Address": "서울특별시 강남구 테헤란로4길 46 지하1층 140호 (역삼동, 쌍용플래티넘밸류)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ2MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "가나안약국",
    "Address": "서울특별시 강남구 도산대로 113 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ5MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "솔잎약국",
    "Address": "서울특별시 강남구 개포로 615 308-1호 (개포동, 석탑프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "삼성약국",
    "Address": "서울특별시 강남구 광평로19길 10 101호 (수서동, 까치마을아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQwMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "달구약국",
    "Address": "서울특별시 강남구 양재대로55길 6 113호 (일원동, 수서1단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "강남온누리약국",
    "Address": "서울특별시 강남구 선릉로 406 102호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ2MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "가로수길약국",
    "Address": "서울특별시 강남구 압구정로 108 1층 7호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ2MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "진선약국",
    "Address": "서울특별시 강남구 선릉로 424 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ5MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "지영온누리약국",
    "Address": "서울특별시 강남구 영동대로 221 (대치동, 서림상가 101호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQwMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "온누리구인당약국",
    "Address": "서울특별시 강남구 삼성로 150 110호 (대치동, 한보미도종합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ5OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "양월약국",
    "Address": "서울특별시 강남구 개포로82길 13-11 105호 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "선릉수정약국",
    "Address": "서울특별시 강남구 선릉로 510 1층 (삼성동, 오성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "뉴욕약국",
    "Address": "서울특별시 강남구 테헤란로 107 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ1IyQwMCQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "프리모약국",
    "Address": "서울특별시 강남구 강남대로 240 314호일부호 (도곡동, 양재SK허브프리모상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ2MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "논현필리아약국",
    "Address": "서울특별시 강남구 선릉로 641 1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "갤러리약국",
    "Address": "서울특별시 강남구 학동로20길 55 106호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "청담케이팜약국",
    "Address": "서울특별시 강남구 도산대로 333 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "소나무약국",
    "Address": "서울특별시 강남구 개포로 220 1층 (개포동, 풍전빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "청아약국",
    "Address": "서울특별시 강남구 논현로 705 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ4OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "영양과건강약국",
    "Address": "서울특별시 강남구 강남대로 532 202호 (논현동, 은훈빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ4OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "파랑새약국",
    "Address": "서울특별시 강남구 일원로 47 1층 (일원동, 대청빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQyIyQ1IyQwMCQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "서울세연약국",
    "Address": "서울특별시 강남구 도곡로 213 지하1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ5MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "강남허브약국",
    "Address": "서울특별시 강남구 학동로 342 109호 (논현동, SK허브빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ4MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "온누리우인약국",
    "Address": "서울특별시 강남구 일원로 39 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ2MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "삼성정문약국",
    "Address": "서울특별시 강남구 일원로 95 109호 (일원동, 신영프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQxMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "웰그린약국",
    "Address": "서울특별시 강남구 선릉로 311 1층 103호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ4OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "용모준수 한약국",
    "Address": "서울특별시 강남구 도곡로 423 104호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "역삼생생약국",
    "Address": "서울특별시 강남구 역삼로17길 64 1층 3호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "코코온누리약국",
    "Address": "서울특별시 강남구 강남대로 406 202호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "테헤란건강약국",
    "Address": "서울특별시 강남구 선릉로86길 17 102호 (대치동, 선릉 MT 빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "삼성강남약국",
    "Address": "서울특별시 강남구 일원로 95 107호 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "연우약국",
    "Address": "서울특별시 강남구 도곡로 242 104,105,202호 (도곡동, 삼호아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ1IyQwMCQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "논현동약국",
    "Address": "서울특별시 강남구 논현로132길 5 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "연약국",
    "Address": "서울특별시 강남구 영동대로 416 케이티앤지 타워 지하1층 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "가온약국",
    "Address": "서울특별시 강남구 학동로 413 청담빌딩 2층 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQxIyQwMCQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "미진약국",
    "Address": "서울특별시 강남구 강남대로 390 B1-5호 (역삼동, 미진프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "강남굿모닝약국",
    "Address": "서울특별시 강남구 남부순환로 2615 208호 (도곡동, 극동스타클래스상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQxMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "트리플약국",
    "Address": "서울특별시 강남구 도산대로 108 1층 일부호 (논현동, 렉스타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQwMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 강남구 언주로 601 파크랜드빌딩 지하1층 4,5호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "대치참약국",
    "Address": "서울특별시 강남구 남부순환로 2927 대치 클래시아 204호,205호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "신사수약국",
    "Address": "서울특별시 강남구 압구정로28길 28 1층 일부호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "수서역약국",
    "Address": "서울특별시 강남구 광평로 270 수서역 339-111호 (수서동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "와이약국",
    "Address": "서울특별시 강남구 강남대로 408 YBM강남센터 1층 104호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "에메랄드약국",
    "Address": "서울특별시 강남구 도산대로 122 에메랄드타워 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQ3MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "압구정프라자온누리약국",
    "Address": "서울특별시 강남구 논현로 857 1층 (신사동, 계룡빌딩 )"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "금강약국",
    "Address": "서울특별시 강남구 압구정로 151 1-7호 (압구정동, 현대아파트9차상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "하늘온누리약국",
    "Address": "서울특별시 강남구 영동대로 602 5층 일부호 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "압구정드림약국",
    "Address": "서울특별시 강남구 압구정로54길 5 103호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "정온누리약국",
    "Address": "서울특별시 강남구 도곡로 409 104호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "세진약국",
    "Address": "서울특별시 강남구 압구정로36길 12 1층 103호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQyIyQxIyQwMCQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "메디팜정연약국",
    "Address": "서울특별시 강남구 강남대로 256 103호 (도곡동, 대우양재디오빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ5MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "동성약국",
    "Address": "서울특별시 강남구 삼성로 212 180호 (대치동, 은마상가에이블럭)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ2MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "일원시장약국",
    "Address": "서울특별시 강남구 양재대로55길 19 (일원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "신한약국",
    "Address": "서울특별시 강남구 도곡로 515 2층 일부호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ2MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "동보옵티마약국",
    "Address": "서울특별시 강남구 도곡로14길 16 1층 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "하이약국",
    "Address": "서울특별시 강남구 언주로 859 1층 (신사동, 쉬즈.애비뉴빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ4MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "온누리기쁜약국",
    "Address": "서울특별시 강남구 봉은사로30길 17 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "미네랄약국",
    "Address": "서울특별시 강남구 학동로 342 308-1호 (논현동, SK허브빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ5MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "스카이약국",
    "Address": "서울특별시 강남구 선릉로63길 9 2층 일부호 (역삼동, 백림빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "신사굿약국",
    "Address": "서울특별시 강남구 도산대로 120 청호빌딩 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "모건약국",
    "Address": "서울특별시 강남구 테헤란로 120 상경빌딩 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "경희자연한약국",
    "Address": "서울특별시 강남구 논현로95길 29-13 2층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "여리약국",
    "Address": "서울특별시 강남구 역삼로7길 3 1층 103호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "만약국",
    "Address": "서울특별시 강남구 도산대로53길 13 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ5OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "감마약국",
    "Address": "서울특별시 강남구 압구정로 336 101호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ3MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 강남구 선릉로 815 1층 5호 (신사동, 신한양빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "논현연세약국",
    "Address": "서울특별시 강남구 강남대로122길 50 1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ2MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "다래약국",
    "Address": "서울특별시 강남구 논현로 508 지하1층 (역삼동, GS강남타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQxMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "7층애약국",
    "Address": "서울특별시 강남구 테헤란로78길 8 7층 일부호 (대치동, 현빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQxMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "골드로즈약국",
    "Address": "서울특별시 강남구 선릉로86길 31 318호 일부호 (대치동, 선릉역롯데골드로즈2)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ2MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "녹십자옵티마약국",
    "Address": "서울특별시 강남구 논현로10길 24 1층 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ5OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "행복한온누리약국",
    "Address": "서울특별시 강남구 도곡로 184 107호 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "참좋은선약국",
    "Address": "서울특별시 강남구 논현로 507 지하1층 7호 (역삼동, 성지하이츠3차빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ4OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "제일그랜드약국",
    "Address": "서울특별시 강남구 강남대로 478 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "세명약국",
    "Address": "서울특별시 강남구 학동로 411 4층 403호 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "역삼오늘약국",
    "Address": "서울특별시 강남구 테헤란로26길 10 성보빌딩 2층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQxIyQwMCQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "청아토한약국",
    "Address": "서울특별시 강남구 선릉로72길 10-16 1층 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "대치약국",
    "Address": "서울특별시 강남구 역삼로 417 1층 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQyIyQ3IyQwMCQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "경희서울한약국",
    "Address": "서울특별시 강남구 논현로159길 23 101호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ5OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "자인한약국",
    "Address": "서울특별시 강남구 선릉로 313 1층 마호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "미플러스약국",
    "Address": "서울특별시 강남구 강남대로 598 보림빌딩 지하층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQxMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "자연애약국",
    "Address": "서울특별시 강남구 봉은사로 474 105호 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQxMyQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "국풍당약국",
    "Address": "서울특별시 강남구 선릉로 654 1층 (삼성동, 예인빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "유니팜약국",
    "Address": "서울특별시 강남구 도산대로 415 1층 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQwMyQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "웰팜약국",
    "Address": "서울특별시 강남구 학동로 342 407-2호 (논현동, SK허브블루)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "아로마약국",
    "Address": "서울특별시 강남구 역삼로 243 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQwMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "아름다운우리약국",
    "Address": "서울특별시 강남구 논현로 327 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQwMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "이즈타워약국",
    "Address": "서울특별시 강남구 테헤란로 101 지하1층 103호 (역삼동, 이즈타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 강남구 논현로 841 1층 111호 (신사동, 제이비미소빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "제이비미소약국",
    "Address": "서울특별시 강남구 논현로 841 1층 107호 (신사동, 제이비미소빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "양재미소약국",
    "Address": "서울특별시 강남구 강남대로 238 1층 101호 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "보리수약국",
    "Address": "서울특별시 강남구 학동로87길 9 (청담동, 진흥(아)상가 101호 일부)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "개나리봄약국",
    "Address": "서울특별시 강남구 역삼로 310 한솔필리아 2층 26호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "팜팜약국",
    "Address": "서울특별시 강남구 압구정로 144 선덕빌딩 1층 104호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "늘봄약국",
    "Address": "서울특별시 강남구 논현로159길 17 101호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "해성약국",
    "Address": "서울특별시 강남구 테헤란로 504 지하층 (대치동, 해성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "온누리타워약국",
    "Address": "서울특별시 강남구 테헤란로 534 지하1층 (대치동, 글라스타워빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "장생당약국",
    "Address": "서울특별시 강남구 테헤란로84길 17 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ2MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "소은약국",
    "Address": "서울특별시 강남구 도산대로50길 9 1층 (논현동, 청석빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "약손메디칼약국",
    "Address": "서울특별시 강남구 선릉로 227 1층 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "별하약국",
    "Address": "서울특별시 강남구 봉은사로 117 이건빌딩 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "일번지약국",
    "Address": "서울특별시 강남구 강남대로84길 23 1층 106호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ2MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "서울메디약국",
    "Address": "서울특별시 강남구 역삼로 406 104호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "우주약국",
    "Address": "서울특별시 강남구 선릉로 402 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "기쁨약국",
    "Address": "서울특별시 강남구 개포로 228 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 강남구 테헤란로 514 5층 (대치동, 삼흥제2빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "수라인 한약국",
    "Address": "서울특별시 강남구 영동대로114길 56 101-2호 (삼성동, 래미안 삼성1차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 강남구 선릉로 513 1층 (역삼동, 아펙스타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ5MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "성모약국",
    "Address": "서울특별시 강남구 개포로 516 101호 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQxMyQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "강남보선약국",
    "Address": "서울특별시 강남구 도곡로 516 107호 (대치동, 삼성상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ2MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 강남구 광평로 196 202호 (수서동, 제이스프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "선릉코코약국",
    "Address": "서울특별시 강남구 테헤란로 333 지하1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "노바약국",
    "Address": "서울특별시 강남구 강남대로118길 51 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQyIyQxIyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "동명온누리약국",
    "Address": "서울특별시 강남구 선릉로64길 5 (대치동, 라이온스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ2MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 강남구 밤고개로34길 4 12호 (세곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "드림케어약국",
    "Address": "서울특별시 강남구 압구정로 162 1층 107호 (신사동, 베네하임시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 강남구 역삼로 247 102호 (역삼동, 홍진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "코끼리약국",
    "Address": "서울특별시 강남구 도산대로 110 지하101호 (논현동, KBL센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "더조은약국",
    "Address": "서울특별시 강남구 자곡로3길 21 상가1동 B202호 (자곡동, LH강남힐스테이트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQyIyQxIyQwMCQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "메타팜약국",
    "Address": "서울특별시 강남구 남부순환로 2941 101호 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "세종약국",
    "Address": "서울특별시 강남구 밤고개로1길 22 (수서동, 주영빌딩 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQwMyQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "성심약국",
    "Address": "서울특별시 강남구 개포로 223 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQyIyQ5IyQwMCQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "윈플러스약국",
    "Address": "서울특별시 강남구 남부순환로 2936 108호 (대치동, 윈플러스상가 )"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "한솔인유로온누리약국",
    "Address": "서울특별시 강남구 역삼로 310 2층 25호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "양재소화약국",
    "Address": "서울특별시 강남구 남부순환로363길 17 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "대치예스약국",
    "Address": "서울특별시 강남구 도곡로 408 410호 (대치동, 디마크 빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQxMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "늘푸른온누리약국",
    "Address": "서울특별시 강남구 압구정로 306 101호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ4MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "햇빛약국",
    "Address": "서울특별시 강남구 자곡로 120 107호 (자곡동, 세곡드림프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQxMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "테헤란약국",
    "Address": "서울특별시 강남구 테헤란로 337 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "도곡우리약국",
    "Address": "서울특별시 강남구 선릉로 225 214호 (도곡동, 도곡렉슬아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "수서역정민아약국",
    "Address": "서울특별시 강남구 광평로56길 8-13 1층 101호 (수서동, 수서타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "삼성일신약국",
    "Address": "서울특별시 강남구 테헤란로 421 (삼성동, 1층 일부)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ4OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "강남미소약국",
    "Address": "서울특별시 강남구 논현로86길 22 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "솔빛동양약국",
    "Address": "서울특별시 강남구 언주로30길 10 현대비전21 110호 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "미성약국",
    "Address": "서울특별시 강남구 압구정로 113-22 101호 (압구정동, 미성상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "맑은하늘약국",
    "Address": "서울특별시 강남구 개포로 265 개포동 메디시스빌딩 1층 101호 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "강남퍼스트약국",
    "Address": "서울특별시 강남구 도산대로 104 1층 (논현동, 1st Avenue)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQwMyQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "순수약국",
    "Address": "서울특별시 강남구 강남대로 622 1층 (신사동, 영동빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "명심약국",
    "Address": "서울특별시 강남구 개포로 207 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQxMyQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "개포종로온누리약국",
    "Address": "서울특별시 강남구 선릉로 42 1층 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQxMyQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "강남메디칼약국",
    "Address": "서울특별시 강남구 삼성로 233 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "나무약국",
    "Address": "서울특별시 강남구 선릉로 404 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "올리브온누리약국",
    "Address": "서울특별시 강남구 테헤란로20길 11 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "마리약국",
    "Address": "서울특별시 강남구 논현로 819 1층 (신사동, 명광빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ2MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "세코아약국",
    "Address": "서울특별시 강남구 논현로 503 703-1호 (역삼동, 송촌빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQxMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "메디칼하늘약국",
    "Address": "서울특별시 강남구 남부순환로 2609 1층 (도곡동, 하늘빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ2MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "센트럴약국",
    "Address": "서울특별시 강남구 봉은사로 211 1층 (논현동, 그림바우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQyIyQ3IyQwMCQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "행복한수약국",
    "Address": "서울특별시 강남구 강남대로 446 2층 일부호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ2MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "은마(銀馬)오행한약국",
    "Address": "서울특별시 강남구 삼성로 212 상가동 A블럭 177호 (대치동, 은마아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "스템약국",
    "Address": "서울특별시 강남구 도산대로 507 1층 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQwMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "청담수약국",
    "Address": "서울특별시 강남구 학동로 423 102호 (청담동, 청우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "청담이화약국",
    "Address": "서울특별시 강남구 선릉로130길 20 209호 (삼성동, 래미안삼성2차아파트상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "도곡타워약국",
    "Address": "서울특별시 강남구 언주로30길 21 B1층 101-24A호 (도곡동, 아카데미스위트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "뽀빠이약국",
    "Address": "서울특별시 강남구 논현로 868 1층 101호 (신사동, 구정빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "영동약국",
    "Address": "서울특별시 강남구 강남대로 526 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "선정릉약국",
    "Address": "서울특별시 강남구 봉은사로 327 궁도빌딩 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQxIyQwMCQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "소호약국",
    "Address": "서울특별시 강남구 논현로 848 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "샛별약국",
    "Address": "서울특별시 강남구 남부순환로359길 4 1층 (도곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "논현천사약국",
    "Address": "서울특별시 강남구 논현로 604 태성빌딩 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "조은온누리약국",
    "Address": "서울특별시 강남구 개포로 615 석탑프라자 3층 304호 (개포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "상지온누리약국",
    "Address": "서울특별시 강남구 선릉로93길 8 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQyIyQ3IyQwMCQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "밝은온누리약국",
    "Address": "서울특별시 강남구 압구정로28길 48 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "에이엔씨약국",
    "Address": "서울특별시 강남구 도산대로 204 1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQ4MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "프라임엠약국",
    "Address": "서울특별시 강남구 삼성로 352 1층 (대치동, 창진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "생명샘약국",
    "Address": "서울특별시 강남구 학동로 433 1층 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "삼성도담약국",
    "Address": "서울특별시 강남구 봉은사로 469 1층 (삼성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "대치메디칼약국",
    "Address": "서울특별시 강남구 남부순환로 2935 1층 (대치동, 대치 프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ4MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "거평원온누리약국",
    "Address": "서울특별시 강남구 봉은사로 129 지하1층 (논현동, 거평타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQyIyQ3IyQwMCQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "창현약국",
    "Address": "서울특별시 강남구 선릉로 815 (신사동, 신한양빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQxMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "정약국",
    "Address": "서울특별시 강남구 봉은사로 331 지하1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "중외약국",
    "Address": "서울특별시 강남구 학동로4길 35 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "역삼이화약국",
    "Address": "서울특별시 강남구 논현로 340 1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "굿윌압구정약국",
    "Address": "서울특별시 강남구 압구정로30길 12 1층 101호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "온정약국",
    "Address": "서울특별시 강남구 논현로 648 1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQxMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 강남구 밤고개로1길 10 2층 220-2호 (수서동, 수서현대벤쳐빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "레이첼약국",
    "Address": "서울특별시 강남구 강남대로 470 808타워 5층 502호 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "큰길약국",
    "Address": "서울특별시 강남구 강남대로 370 지하1층 (역삼동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQwMyQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "종로약국",
    "Address": "서울특별시 강남구 도곡로 419 1층 (대치동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQwMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "올리브약국",
    "Address": "서울특별시 강남구 선릉로 669 상경빌딩 지하1층 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "푸른온누리약국",
    "Address": "서울특별시 강남구 도산대로 511 1층 102호 (청담동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQxMyQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "학동봄약국",
    "Address": "서울특별시 강남구 논현로131길 23 홍재빌딩 1층 일부호 (논현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "에스온누리약국",
    "Address": "서울특별시 강남구 압구정로 152 1층 116호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "쌍용약국",
    "Address": "서울특별시 강동구 천중로 216 101호 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "시민당약국",
    "Address": "서울특별시 강동구 양재대로 1479 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ5OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "성덕약국",
    "Address": "서울특별시 강동구 구천면로 372 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "경희수약국",
    "Address": "서울특별시 강동구 동남로 881 103호 (명일동, 서희스타힐스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ4OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "우리선약국",
    "Address": "서울특별시 강동구 동남로49길 21-15 1,지1층 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "건강플러스약국",
    "Address": "서울특별시 강동구 아리수로93길 27 108호 (강일동, 강일타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQwMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "솔솔온누리약국",
    "Address": "서울특별시 강동구 양재대로 1365 심포니타워 111호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "스마일약국",
    "Address": "서울특별시 강동구 고덕로 391 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "나음온누리약국",
    "Address": "서울특별시 강동구 올림픽로 620 예투빌딩 1층 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ4MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "가까운단골약국",
    "Address": "서울특별시 강동구 동남로 891 현대델리안오피스텔 102호 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "현온누리약국",
    "Address": "서울특별시 강동구 올림픽로91길 30 상가동 1층 115호 (암사동, 힐스테이트암사)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "강동엠약국",
    "Address": "서울특별시 강동구 천호대로 1195 지앤지타워 1층 101호 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디컬바른약국",
    "Address": "서울특별시 강동구 양재대로121길 7 거송빌딩 103,104호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "강남참약국",
    "Address": "서울특별시 강동구 구천면로 662 1층 (상일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "센트럴약국",
    "Address": "서울특별시 강동구 고덕로80길 123 고덕센트럴아이파크아파트(상가A동) 2층 206호 (상일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "라라약국",
    "Address": "서울특별시 강동구 성내로 69 케이씨엘빌딩 2관 1층 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ3MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "아르테약국",
    "Address": "서울특별시 강동구 고덕로 390 고덕아르테온아파트(상가1동) 2층 210호 (상일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "강동더본약국",
    "Address": "서울특별시 강동구 양재대로 1465 마루홈타운 107호 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "동남온누리약국",
    "Address": "서울특별시 강동구 성내로 4 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "엄약국",
    "Address": "서울특별시 강동구 성내로14길 45 105호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 강동구 진황도로61길 48 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "강동웰빙약국",
    "Address": "서울특별시 강동구 천호대로 1124 1층 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQwMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "암사현대약국",
    "Address": "서울특별시 강동구 올림픽로 777 102호 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "달약국",
    "Address": "서울특별시 강동구 천호대로 1171 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQyIyQ3IyQwMCQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "중앙온누리약국",
    "Address": "서울특별시 강동구 아리수로 427 1층 (강일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "강동한우리약국",
    "Address": "서울특별시 강동구 올림픽로 778 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQxMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "호원엠약국",
    "Address": "서울특별시 강동구 성내로 66 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQyIyQzIyQwMCQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "강동보건약국",
    "Address": "서울특별시 강동구 성내로 40 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "강동경희한약국",
    "Address": "서울특별시 강동구 풍성로 200 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "선약국",
    "Address": "서울특별시 강동구 고덕로 385 고덕그라시움아파트(상가4동) 102호 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQwMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "21세기메디칼약국",
    "Address": "서울특별시 강동구 천호대로 1199 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "새희망약국",
    "Address": "서울특별시 강동구 동남로 877 (명일동, 한화오벨리스크스위트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ3OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "명일약국",
    "Address": "서울특별시 강동구 양재대로 1626 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ2MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "백세약국",
    "Address": "서울특별시 강동구 구천면로 328 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "맑은샘약국",
    "Address": "서울특별시 강동구 천중로 237 1층 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "길동보룡약국",
    "Address": "서울특별시 강동구 양재대로 1478 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ5MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "양지약국",
    "Address": "서울특별시 강동구 진황도로61길 56 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ2MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "태린약국",
    "Address": "서울특별시 강동구 고덕로 133 5층 513호 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQwMyQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "영일약국",
    "Address": "서울특별시 강동구 풍성로37길 39-21 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQyIyQxIyQwMCQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "고려약국",
    "Address": "서울특별시 강동구 천호대로 1125 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ2MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "승호약국",
    "Address": "서울특별시 강동구 올림픽로 779 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQzIyQwMCQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "튼튼온누리약국",
    "Address": "서울특별시 강동구 올림픽로 732 1층 2호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ2MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "코코약국",
    "Address": "서울특별시 강동구 아리수로93길 27 3층 (강일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "우주약국",
    "Address": "서울특별시 강동구 양재대로 1571 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ4OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "옵티마기쁨약국",
    "Address": "서울특별시 강동구 올림픽로 787 태성프라자 1층 102호 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQxIyQwMCQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "봄날약국",
    "Address": "서울특별시 강동구 고덕로 380 고덕아르테온아파트(상가2동) 2층 206호 (상일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQxMyQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "강동소망약국",
    "Address": "서울특별시 강동구 천호대로 1111 1층 (길동, 정우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신경희약국",
    "Address": "서울특별시 강동구 동남로71길 24 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "현대제이드약국",
    "Address": "서울특별시 강동구 강동대로 155 1층 102호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQyIyQ1IyQwMCQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 강동구 천호대로 1116 1층 102-1호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ3MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "강동해오름약국",
    "Address": "서울특별시 강동구 양재대로 1589 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQyIyQ1IyQwMCQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "고은온누리약국",
    "Address": "서울특별시 강동구 천호대로 1153 1층 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQwMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "그린팜약국",
    "Address": "서울특별시 강동구 올림픽로 665 1층 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "천사약국",
    "Address": "서울특별시 강동구 구천면로 297 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ5OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "한미약국",
    "Address": "서울특별시 강동구 양재대로 1629 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQwMyQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "온누리모세종약국",
    "Address": "서울특별시 강동구 고덕로83길 18 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ4OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "온누리부부약국",
    "Address": "서울특별시 강동구 진황도로 189 104호 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "박선영약국",
    "Address": "서울특별시 강동구 고덕로 254 이화빌딩 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "다정약국",
    "Address": "서울특별시 강동구 양재대로 1377 2층 204호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "경희일번약국",
    "Address": "서울특별시 강동구 동남로 889 101호 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "명일로약국",
    "Address": "서울특별시 강동구 명일로 270 1층 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "아이파크약국",
    "Address": "서울특별시 강동구 동남로79길 26 상가동 101호 (고덕동, 고덕아이파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "중앙대영약국",
    "Address": "서울특별시 강동구 동남로 635 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "새힘약국",
    "Address": "서울특별시 강동구 올림픽로 806 까사팔공육 1층 101호 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQxMyQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 강동구 올림픽로 774 1층 3호 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "더바른약국",
    "Address": "서울특별시 강동구 구천면로 241 1층 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ5IyQwMCQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "서울온누리약국",
    "Address": "서울특별시 강동구 천중로43길 34 신운빌딩 101호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "강동프라자약국",
    "Address": "서울특별시 강동구 올림픽로 624 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "메디팜미래로약국",
    "Address": "서울특별시 강동구 천호대로 1467 (상일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "위드팜천사약국",
    "Address": "서울특별시 강동구 천호대로 1107 101호 (길동, SK허브)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "명성그린약국",
    "Address": "서울특별시 강동구 구천면로 424 115호 (명일동, 명일메카타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQyIyQzIyQwMCQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "월드팜약국",
    "Address": "서울특별시 강동구 진황도로 159 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQxMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "은행약국",
    "Address": "서울특별시 강동구 고덕로83길 14 2층 201호 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "강동우리약국",
    "Address": "서울특별시 강동구 천호대로173길 12 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "길약국",
    "Address": "서울특별시 강동구 천호대로177길 10 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQyIyQ1IyQwMCQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "동아약국",
    "Address": "서울특별시 강동구 천호대로 997 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 강동구 구천면로 304 3층 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "강동미래약국",
    "Address": "서울특별시 강동구 올림픽로 782 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ2MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "강일약국",
    "Address": "서울특별시 강동구 아리수로97길 19 상가동 201호 (강일동, 강일리버파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQwMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "온누리성심약국",
    "Address": "서울특별시 강동구 성안로 147 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ4OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 강동구 구천면로 222 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 강동구 구천면로 250 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "다온약국",
    "Address": "서울특별시 강동구 천호옛길 98 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "둔촌온누리약국",
    "Address": "서울특별시 강동구 양재대로 1325 102,103호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ5MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "동현약국",
    "Address": "서울특별시 강동구 양재대로127길 19 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQxIyQwMCQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "생생약국",
    "Address": "서울특별시 강동구 양재대로 1458 1층 나호 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "준약국",
    "Address": "서울특별시 강동구 진황도로 190 1층 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "새원약국",
    "Address": "서울특별시 강동구 양재대로130길 11 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "대한약국",
    "Address": "서울특별시 강동구 천호대로 1027 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQxMyQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "참좋은온누리약국",
    "Address": "서울특별시 강동구 성안로 156 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "파란약국",
    "Address": "서울특별시 강동구 양재대로 1325 둔촌메디컬센타 101호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "강동메디칼약국",
    "Address": "서울특별시 강동구 올림픽로 686 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "삼성서울약국",
    "Address": "서울특별시 강동구 상일로6길 26 (상일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "경희메디칼온누리약국",
    "Address": "서울특별시 강동구 동남로 889 103호 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 강동구 동남로 889 102호 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "바로드림약국",
    "Address": "서울특별시 강동구 상일로12길 97 101호 (강일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "암사조은온누리약국",
    "Address": "서울특별시 강동구 고덕로 133 상가동 511호 (암사동, 강동롯데캐슬퍼스트아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "신창약국",
    "Address": "서울특별시 강동구 올림픽로 797 1층 102호 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "모주현약국",
    "Address": "서울특별시 강동구 고덕로 390 고덕아르테온아파트(상가1동) 2층 204호 (상일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQwMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "종로광명약국",
    "Address": "서울특별시 강동구 구천면로 664 (상일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "미리암약국",
    "Address": "서울특별시 강동구 동남로81길 100 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "베네시티약국",
    "Address": "서울특별시 강동구 올림픽로 664 3층 342,343호 (천호동, 대우한강베네시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "온누리성원약국",
    "Address": "서울특별시 강동구 구천면로 269-1 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ5OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "길동중앙약국",
    "Address": "서울특별시 강동구 천호대로187길 49 1층 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQxMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "은혜온누리약국",
    "Address": "서울특별시 강동구 구천면로 512-1 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "매일약국",
    "Address": "서울특별시 강동구 양재대로 1335 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 강동구 천호대로 1037 1층 2호 (천호동, 세우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ4OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "라온약국",
    "Address": "서울특별시 강동구 성안로 155 1층 106호 (천호동, 강동역두산위브센티움)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "복조리약국",
    "Address": "서울특별시 강동구 천호대로187길 61 1층 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "강동새경희약국",
    "Address": "서울특별시 강동구 동남로73길 13 1층 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "미소진약국",
    "Address": "서울특별시 강동구 양재대로 1661 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQxMyQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "명일정원약국",
    "Address": "서울특별시 강동구 구천면로 428 204호 (명일동, 센트로빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "온누리삼선약국",
    "Address": "서울특별시 강동구 동남로81길 50 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQxMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "오월애약국",
    "Address": "서울특별시 강동구 천호대로 1107 102호 (길동, SK허브)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ5MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "세종약국",
    "Address": "서울특별시 강동구 동남로 891 현대델리안오피스텔 103호 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "큰사랑약국",
    "Address": "서울특별시 강동구 상암로 44 1층 (천호동, 유정빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQyIyQ5IyQwMCQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "길성약국",
    "Address": "서울특별시 강동구 진황도로 127 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "이레약국",
    "Address": "서울특별시 강동구 올림픽로 787 109호 (암사동, 태성프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQyIyQzIyQwMCQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "한우리유공약국",
    "Address": "서울특별시 강동구 진황도로61길 25 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQyIyQzIyQwMCQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 강동구 올림픽로 651 3층 (천호동, 예경빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "월드약국",
    "Address": "서울특별시 강동구 구천면로 229-1 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "길동스타약국",
    "Address": "서울특별시 강동구 양재대로 1498 1층 (길동, 호석빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "가까운사랑약국",
    "Address": "서울특별시 강동구 양재대로 1576 삼익빌딩 1층 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ2MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "나아약국",
    "Address": "서울특별시 강동구 천호대로162길 50 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "정다운약국",
    "Address": "서울특별시 강동구 진황도로61길 51 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜문화약국",
    "Address": "서울특별시 강동구 구천면로 200 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQyIyQ1IyQwMCQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "명일보룡약국",
    "Address": "서울특별시 강동구 동남로73길 26 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "보생당약국",
    "Address": "서울특별시 강동구 천호대로 1015 지하2층 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQxMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "태양약국",
    "Address": "서울특별시 강동구 양재대로 1637 1층 105호 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 강동구 양재대로89길 16 214호 (성내동, 파크프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "별약국",
    "Address": "서울특별시 강동구 풍성로38길 9 102호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "산들약국",
    "Address": "서울특별시 강동구 고덕로 131 상가동 115호 (암사동, 롯데캐슬퍼스트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ2MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "밝은미소약국",
    "Address": "서울특별시 강동구 상암로 195 108호 (명일동, 에이플러스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "강동정문약국",
    "Address": "서울특별시 강동구 진황도로 74 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "정성약국",
    "Address": "서울특별시 강동구 성내로 77 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "휴베이스 캐슬약국",
    "Address": "서울특별시 강동구 고덕로 131 (암사동, 강동롯데캐슬퍼스트아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQ3IyQwMCQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "친절한오렌지약국",
    "Address": "서울특별시 강동구 양재대로130길 10 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ2MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신연세약국",
    "Address": "서울특별시 강동구 고덕로 88 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "편안한약국",
    "Address": "서울특별시 강동구 천호대로 1089 복합시설동 지1층 B20호 (천호동, 강동역 신동아 파밀리에)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "고덕약국",
    "Address": "서울특별시 강동구 고덕로 353 고덕그라시움아파트(상가1동) 208호 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "위드팜만보약국",
    "Address": "서울특별시 강동구 진황도로61길 52 1,지층 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQxMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "아름다운약국",
    "Address": "서울특별시 강동구 양재대로 1488 4층 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 강동구 상암로 31 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "예일약국",
    "Address": "서울특별시 강동구 양재대로 1603 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQxMyQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "용성약국",
    "Address": "서울특별시 강동구 고덕로 109 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ4OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "제일공안약국",
    "Address": "서울특별시 강동구 풍성로37길 39-7 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ5OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "태화약국",
    "Address": "서울특별시 강동구 양재대로123길 9 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ2MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 강동구 구천면로 305 1층 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "원약국",
    "Address": "서울특별시 강동구 고덕로 353 고덕그라시움아파트(상가1동) 204,205호 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "스마트약국",
    "Address": "서울특별시 강동구 천호대로 997 신라빌딩 3층 302호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQwMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "대자연약국",
    "Address": "서울특별시 강동구 구천면로 291 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "스타약국",
    "Address": "서울특별시 강동구 천호대로 1087 2층 203호 (천호동, 진넥스빌Ⅲ)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQ3MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "정언약국",
    "Address": "서울특별시 강동구 양재대로138길 47 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "보운약국",
    "Address": "서울특별시 강동구 진황도로61길 42 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ5MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "아주약국",
    "Address": "서울특별시 강동구 양재대로128길 9 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQwMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "열린프라자약국",
    "Address": "서울특별시 강동구 천호대로170길 26 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "새가정약국",
    "Address": "서울특별시 강동구 양재대로 1595 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQyIyQ5IyQwMCQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜정원약국",
    "Address": "서울특별시 강동구 천호대로 1200 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "청원약국",
    "Address": "서울특별시 강동구 구천면로 192 천호역 한강 푸르지오시티 1층 110호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "강동약국",
    "Address": "서울특별시 강동구 암사길 53 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "보은약국",
    "Address": "서울특별시 강동구 천호대로157길 30 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ3MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "여인선약국",
    "Address": "서울특별시 강동구 천호대로170길 28 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "온누리삼일약국",
    "Address": "서울특별시 강동구 구천면로42길 17 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ5OSQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 강동구 진황도로 67 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQxMyQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "새실로암약국",
    "Address": "서울특별시 강동구 양재대로 1619 (천호동, 가야빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ5MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "혜민약국",
    "Address": "서울특별시 강동구 천중로51길 56 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ1IyQwMCQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "천호브라운스톤약국",
    "Address": "서울특별시 강동구 천호대로 1006 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ2MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 강동구 풍성로 214 102호 (성내동, 동양빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "경희프라자약국",
    "Address": "서울특별시 강동구 구천면로 245 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQwMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 강동구 풍성로51길 3 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ3MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "정약국",
    "Address": "서울특별시 강동구 진황도로49길 49 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "효약국",
    "Address": "서울특별시 강동구 천호대로 1099 정산타워빌딩 1층 101호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "기쁜샘약국",
    "Address": "서울특별시 강동구 천호대로 1163 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ5MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "고덕경희온누리약국",
    "Address": "서울특별시 강동구 고덕로 256 101호 (명일동, 명성프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 강동구 동남로71길 32 103호 (명일동, 환타지아)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "무지개약국",
    "Address": "서울특별시 강동구 진황도로61길 42 104호 (둔촌동, 둔촌동주상복합)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "선사약국",
    "Address": "서울특별시 강동구 올림픽로 800 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "명일마트종로약국",
    "Address": "서울특별시 강동구 고덕로 276 지하1층 (명일동, 이마트명일점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ1IyQwMCQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "봄봄약국",
    "Address": "서울특별시 강동구 명일로 248 1층 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "뉴욕온누리약국",
    "Address": "서울특별시 강동구 양재대로 1590 1층 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQwMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "준온누리약국",
    "Address": "서울특별시 강동구 올림픽로 783 103호 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ2MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "길동수약국",
    "Address": "서울특별시 강동구 천호대로 1123 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ4MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "상록수약국",
    "Address": "서울특별시 강동구 고덕로10길 53 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ3OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "참한약국",
    "Address": "서울특별시 강동구 구천면로 494 1층 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQyIyQzIyQwMCQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "연당약국",
    "Address": "서울특별시 강동구 양재대로 1655 2층 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ2MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "동서온누리약국",
    "Address": "서울특별시 강동구 풍성로37가길 39 101호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQwMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "백제약국",
    "Address": "서울특별시 강동구 양재대로116길 50 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQwMyQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "건강을준비하는약국",
    "Address": "서울특별시 강동구 구천면로 189 지층 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "순수 한약국",
    "Address": "서울특별시 강동구 아리수로93길 19 202호 (강일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "1층천호약국",
    "Address": "서울특별시 강동구 천호대로 1006 브라운스톤천호 105호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "강동솔약국",
    "Address": "서울특별시 강동구 양재대로 1473 희헌타워 1층 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "석원약국",
    "Address": "서울특별시 강동구 강동대로53길 94 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQxMyQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "허브온누리약국",
    "Address": "서울특별시 강동구 천호대로 1092 106호 (성내동, SK허브진)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQxIyQwMCQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "메디팜강일약국",
    "Address": "서울특별시 강동구 아리수로93길 27 106호 (강일동, 강일타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "태승온누리약국",
    "Address": "서울특별시 강동구 천호대로 1012 1층 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQxMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "새아름약국",
    "Address": "서울특별시 강동구 상암로 11 101동 104호 (암사동, 선사현대아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "이화온누리약국",
    "Address": "서울특별시 강동구 구천면로 233 한양메디스퀘어 1층 109호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "행복한온누리약국",
    "Address": "서울특별시 강동구 동남로73길 26 203호 (명일동, 고덕복합빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 강동구 천호대로159길 13 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "그라시움이화약국",
    "Address": "서울특별시 강동구 고덕로 353 고덕그라시움종합상가 3층 320호 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 강동구 아리수로 421 MIDC빌딩 105호 (강일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "고덕퍼스트약국",
    "Address": "서울특별시 강동구 고덕로 353 고덕그라시움아파트(상가1동) 254,255호 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQxMyQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "필약국",
    "Address": "서울특별시 강동구 올림픽로 664 2층 205호 (천호동, 대우한강베네시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 강동구 올림픽로 781 (암사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "솔약국",
    "Address": "서울특별시 강동구 진황도로 85 105/106호 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQwMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "정든약국",
    "Address": "서울특별시 강동구  양재대로 1594 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "주온누리약국",
    "Address": "서울특별시 강동구 양재대로 1550 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 강동구 구천면로 232 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQwMyQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 강동구 동남로49길 21-12 (둔촌동, 시향)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ2MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "토성약국",
    "Address": "서울특별시 강동구 풍성로 136 상가동 102호 (성내동, 성내동삼성아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ2MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "나은약국",
    "Address": "서울특별시 강동구 양재대로 1620 명일빌딩 101호 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "강약국",
    "Address": "서울특별시 강동구 올림픽로80길 43 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "경희정문약국",
    "Address": "서울특별시 강동구 동남로 885 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "베스트약국",
    "Address": "서울특별시 강동구 양재대로 1325 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "나눔약국",
    "Address": "서울특별시 강동구 구천면로 403 1층 (명일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 강동구 상암로 104 A동 101호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "윤약국",
    "Address": "서울특별시 강동구 양재대로 1365 심포니타워 110호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQwMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "건강한약국",
    "Address": "서울특별시 강동구 구천면로 231 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQyIyQzIyQwMCQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "조이약국",
    "Address": "서울특별시 강동구 천호대로 1006 F동 306호 (성내동, 브라운스톤천호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "강남약국",
    "Address": "서울특별시 강동구 양재대로 1355 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQxMyQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "호랑이약국",
    "Address": "서울특별시 강동구 천호대로 1089 지하1층 B19호 (천호동, 강동역 신동아 파밀리에)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQxMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "강동태평양약국",
    "Address": "서울특별시 강동구 양재대로 1343 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQwMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 강동구 양재대로 1466 1층 102호 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "스타온누리약국",
    "Address": "서울특별시 강동구 아리수로50길 50 4층 405,406,407호 (고덕동, 고덕래미안힐스테이트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQwMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "한림약국",
    "Address": "서울특별시 강동구 성안로 149 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "화인약국",
    "Address": "서울특별시 강동구 양재대로 1579 2층 (천호동, 한영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "늘온누리약국",
    "Address": "서울특별시 강동구 상일로12길 89 101호 (강일동, 리엔타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "경약국",
    "Address": "서울특별시 강동구 올림픽로83길 18 101호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ4OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "덕인약국",
    "Address": "서울특별시 강동구 구천면로 287 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ4OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "7형제약국",
    "Address": "서울특별시 강동구 진황도로 179 1층 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQxMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "리엔약국",
    "Address": "서울특별시 강동구 상일로 74 상가2동 2층 203호 (상일동, 고덕리엔파크3단지아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "둔촌세계로약국",
    "Address": "서울특별시 강동구 양재대로 1319 경일빌딩 1층 106호 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 강동구 풍성로 178 1층 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ5OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "동명약국",
    "Address": "서울특별시 강동구 양재대로 1396 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQwMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "영임약국",
    "Address": "서울특별시 강동구 구천면로 233 110호 (천호동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQxMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "태극약국",
    "Address": "서울특별시 강동구 아리수로76길 43 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ5MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "두레약국",
    "Address": "서울특별시 강동구 고덕로83길 6 101호 (고덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQxMyQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "메디팜자연약국",
    "Address": "서울특별시 강동구 양재대로 1477 1층 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ3MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "수빈온누리약국",
    "Address": "서울특별시 강동구 풍성로 116 (성내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "푸르지오진흥약국",
    "Address": "서울특별시 강동구 명일로 176 1층 (둔촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "동주약국",
    "Address": "서울특별시 강동구 명일로 243 (길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQxMyQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "드림팜약국",
    "Address": "서울특별시 강동구 아리수로93길 27 405-1호 (강일동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQwMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "애플약국",
    "Address": "서울특별시 강서구 양천로 684 1층 (염창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQ1IyQwMCQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "정다운약국",
    "Address": "서울특별시 강서구 까치산로 120 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "월성약국",
    "Address": "서울특별시 강서구 강서로17길 141 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQwMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "준온누리약국",
    "Address": "서울특별시 강서구 양천로 583 우림블루나인비즈니스센터 118호 (염창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 강서구 공항대로41길 65 1층 110호 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ3OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "일심당약국",
    "Address": "서울특별시 강서구 강서로7길 90 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "아름약국",
    "Address": "서울특별시 강서구 양천로 366 4층 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ2MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "고운마음약국",
    "Address": "서울특별시 강서구 양천로 500 1층 112호 (등촌동, 노블리움오피스텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQwMyQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "수명산약국",
    "Address": "서울특별시 강서구 수명로 68-11 발산타워107호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "메디팜인정약국",
    "Address": "서울특별시 강서구 양천로 72 202호 (방화동, 해성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "연수당약국",
    "Address": "서울특별시 강서구 강서로18길 26 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "마곡나루약국",
    "Address": "서울특별시 강서구 마곡서로 157 스프링파크타워 2층 208-2호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ5OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "화곡서울약국",
    "Address": "서울특별시 강서구 강서로 254 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "파랑약국",
    "Address": "서울특별시 강서구 화곡로 339 오선빌딩 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ1IyQwMCQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 강서구 마곡중앙로 36 상가 107-1호 (마곡동, 마곡엠벨리 15단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "건강온누리약국",
    "Address": "서울특별시 강서구 곰달래로 271 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ2MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 강서구 화곡로 152 CUBE152 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "2층즐거운약국",
    "Address": "서울특별시 강서구 양천로 559 가양이마트 2층 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "미래약국",
    "Address": "서울특별시 강서구 양천로14길 23 효성빌딩 1층 101호 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "이수연약국",
    "Address": "서울특별시 강서구 마곡중앙로 59-21 에이스타워2 1층 120호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "바로약국",
    "Address": "서울특별시 강서구 강서로 341 창대교회 1층 2호,3호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "신방화약국",
    "Address": "서울특별시 강서구 양천로 128 103호 (방화동, 한림리첸빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "햇빛온누리약국",
    "Address": "서울특별시 강서구 등촌로 59-1 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "흥부약국",
    "Address": "서울특별시 강서구 공항대로 437 1층 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "마곡스타약국",
    "Address": "서울특별시 강서구 공항대로 168 1층 106-1호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "마곡프라자약국",
    "Address": "서울특별시 강서구 마곡서1로 115-1 마곡헤리움1차 105~106호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQwMyQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 강서구 등촌로 71 1층 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "빠른대학온누리약국",
    "Address": "서울특별시 강서구 마곡중앙4로 74 이웰메디파크 101-103호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ2MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "길약국",
    "Address": "서울특별시 강서구 곰달래로 260 (화곡동, 피앤와이빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "맘온누리약국",
    "Address": "서울특별시 강서구 공항대로 168 117,118호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQxMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "휴베이스비타민약국",
    "Address": "서울특별시 강서구 가로공원로76길 51 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "메디팜푸른약국",
    "Address": "서울특별시 강서구 강서로 293-1 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ2MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "상록수약국",
    "Address": "서울특별시 강서구 월정로30길 102 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ5OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "미주약국",
    "Address": "서울특별시 강서구 방화대로48길 40 108호 (방화동, 도시개발공사)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "화곡태평양약국",
    "Address": "서울특별시 강서구 강서로 205 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ5OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "솔트약국",
    "Address": "서울특별시 강서구 양천로 660 지층 L02호 (염창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ5OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "지혜약국",
    "Address": "서울특별시 강서구 가로공원로76길 73 2층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "메디팜사랑약국",
    "Address": "서울특별시 강서구 화곡로 138 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ4OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "엔씨(NC)약국",
    "Address": "서울특별시 강서구 강서로56길 17 지하1층 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 강서구 양천로 73 108호 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQxIyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "한강메디칼약국",
    "Address": "서울특별시 강서구 허준로 23 107호 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "차오름약국",
    "Address": "서울특별시 강서구 양천로 655 2층 (염창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "엔젤약국",
    "Address": "서울특별시 강서구 양천로 476 금부빌딩 402호 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ5OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "건강샘온누리약국",
    "Address": "서울특별시 강서구  까치산로 73 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ4OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "김포약국",
    "Address": "서울특별시 강서구 방화동로 70 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ5OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "월드팜약국",
    "Address": "서울특별시 강서구 화곡로 324 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "맑은약국",
    "Address": "서울특별시 강서구 양천로 600 1층 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "참미래약국",
    "Address": "서울특별시 강서구 공항대로41길 66 1층 133호 (등촌동, 세신종합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "삼정약국",
    "Address": "서울특별시 강서구 금낭화로23길 25 101호 (방화동, 도시개발6단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "달약국",
    "Address": "서울특별시 강서구 마곡중앙6로 66 퀸즈파크텐 112호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 강서구 등촌로 147 1층 (등촌동, 유석빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "건강한온누리약국",
    "Address": "서울특별시 강서구 가로공원로82길 41-8 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "대성약국",
    "Address": "서울특별시 강서구 강서로 307 서울스타병원빌딩 1층 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "마곡소망약국",
    "Address": "서울특별시 강서구 마곡중앙5로 6 2층 233호 (마곡동, 마곡나루역보타닉푸르지오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "금비약국",
    "Address": "서울특별시 강서구 양천로69길 11 1층 101호 (염창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ2MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "편안한약국",
    "Address": "서울특별시 강서구 강서로18길 14 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQyIyQ3IyQwMCQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "감초약국",
    "Address": "서울특별시 강서구 강서로 38 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQyIyQxIyQwMCQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 강서구 수명로 78 새롬프라자 104호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ5OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "정성가득한약국",
    "Address": "서울특별시 강서구 화곡로 301 원풍빌딩 1층 103호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQwMyQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 강서구 강서로 191 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQyIyQzIyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "발산 93약국",
    "Address": "서울특별시 강서구 공항대로 261 306호 (마곡동, 발산파크프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "금강약국",
    "Address": "서울특별시 강서구 금낭화로 135 411호 (방화동, 금강프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "다나은약국",
    "Address": "서울특별시 강서구 화곡로 194-15 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "곰달래약국",
    "Address": "서울특별시 강서구 곰달래로 226 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "온누리용주약국",
    "Address": "서울특별시 강서구 곰달래로 178 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "마곡새봄약국",
    "Address": "서울특별시 강서구 강서로 463 새싹타워 1층 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "이소약국",
    "Address": "서울특별시 강서구 강서로 242 상가동 4층 17호 (화곡동, 강서힐스테이트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "미즈약국",
    "Address": "서울특별시 강서구 강서로47가길 12 1층 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "발산에이스약국",
    "Address": "서울특별시 강서구 강서로 360 솔레드림 109호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQwMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "마곡열린약국",
    "Address": "서울특별시 강서구 방화대로 294 마곡더블유타워 114, 115호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "강서홈약국",
    "Address": "서울특별시 강서구 화곡로 398 홈플러스강서점앤본사사옥 1층 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "본초당약국",
    "Address": "서울특별시 강서구 강서로45길 49-5 1층 101호,102호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "염창메디칼약국",
    "Address": "서울특별시 강서구 양천로 731 104-1호 (염창동, 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQxMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "조광약국",
    "Address": "서울특별시 강서구 방화동로 45 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "이수약국",
    "Address": "서울특별시 강서구 강서로16길 32 103호 (화곡동, 화창빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ1IyQwMCQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "새미래약국",
    "Address": "서울특별시 강서구 화곡로 196 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQxMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "제일메디칼약국",
    "Address": "서울특별시 강서구 가로공원로 187 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQwMyQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "하나메디칼약국",
    "Address": "서울특별시 강서구 금낭화로 91-2 105호 (방화동, 대승프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQxMyQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 강서구 초원로13길 56 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ2MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "새서울약국",
    "Address": "서울특별시 강서구 양천로57길 9-7 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ5OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "비전약국",
    "Address": "서울특별시 강서구 공항대로 627 1층 (염창동, 대신빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQxMyQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 강서구 초록마을로 37 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "나무약국",
    "Address": "서울특별시 강서구 강서로45길 174 수명산씨티 3층 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQxMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "밝은온누리약국",
    "Address": "서울특별시 강서구 등촌로 177 101동 102호 (등촌동, 경남파크빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "영보약국",
    "Address": "서울특별시 강서구 양천로57길 16 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "예약국",
    "Address": "서울특별시 강서구 공항대로41길 75 108호 (등촌동, 경원프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ2MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "예다인온누리약국",
    "Address": "서울특별시 강서구 양천로 452 1층 105-1호 (등촌동, 예다인상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQyIyQ3IyQwMCQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "다마트약국",
    "Address": "서울특별시 강서구 금낭화로 135 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "김비타약국",
    "Address": "서울특별시 강서구 공항대로 206 나인스퀘어 111호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "유니약국",
    "Address": "서울특별시 강서구 마곡중앙로 161-8 두산더랜드파크 A동 A210호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "가장큰이대약국",
    "Address": "서울특별시 강서구 공항대로 248 111~113, 206호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ3MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "윤약국",
    "Address": "서울특별시 강서구 가로공원로76길 91 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 강서구 공항대로41길 65 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 강서구 화곡로 190 박상춘안과의원 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "행복나무약국",
    "Address": "서울특별시 강서구 강서로 193 101호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "라온365온누리약국",
    "Address": "서울특별시 강서구 화곡로 166 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "샛별약국",
    "Address": "서울특별시 강서구 강서로 154 힐탑빌딩 101호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "방화우리약국",
    "Address": "서울특별시 강서구 양천로 94 1층 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "하나로약국",
    "Address": "서울특별시 강서구 양천로 677 1층 (염창동, 염창하이츠빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "연세약국",
    "Address": "서울특별시 강서구 화곡로 161 대성빌딩 104,105호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "온누리큰사랑약국",
    "Address": "서울특별시 강서구 강서로 64 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ2MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "까치프라자약국",
    "Address": "서울특별시 강서구 강서로 52 104,105호 (화곡동, 화곡판타지아빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "방화프라자약국",
    "Address": "서울특별시 강서구 양천로16길 16 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "화곡메디칼약국",
    "Address": "서울특별시 강서구 가로공원로76길 56 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "하늘수한약국",
    "Address": "서울특별시 강서구 공항대로 269-15 316-1호 (마곡동, 힐스테이트에코마곡)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "마곡하늘약국",
    "Address": "서울특별시 강서구 마곡중앙5로 6 마곡나루역보타닉푸르지오시티 227호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "서울사랑약국",
    "Address": "서울특별시 강서구 공항대로41길 52 버들빌딩 202호 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "초록문약국",
    "Address": "서울특별시 강서구 공항대로 164 류마타워 104호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "강서보건약국",
    "Address": "서울특별시 강서구 공항대로67길 29-26 시우 1층 (염창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ5OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "종로약국",
    "Address": "서울특별시 강서구 방화동로16길 62 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "강서자이온누리약국",
    "Address": "서울특별시 강서구 양천로 401 109-2호 (가양동, 강서한강자이타워A동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQwMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "원약국",
    "Address": "서울특별시 강서구 남부순환로11가길 104 1층 (공항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQwMyQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "우성약국",
    "Address": "서울특별시 강서구 수명로 80 베스트프라자빌딩 102호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "시장약국",
    "Address": "서울특별시 강서구 화곡로 206 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ4MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "동산온누리약국",
    "Address": "서울특별시 강서구 양천로 606 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ3MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "큰덕약국",
    "Address": "서울특별시 강서구 강서로47가길 16 1층 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ2MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "행복한온누리약국",
    "Address": "서울특별시 강서구 수명로 82 102호 (내발산동, 발산로얄타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQxMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "종로당약국",
    "Address": "서울특별시 강서구 양천로57길 36 1층 (가양동, 가양5단지아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQyIyQzIyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "하늘팜약국",
    "Address": "서울특별시 강서구 양천로 461 (가양동, 주영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ5MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "더조은약국",
    "Address": "서울특별시 강서구 곰달래로49길 29 산호빌딩 103호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "국제공항약국",
    "Address": "서울특별시 강서구 하늘길 112 (공항동, 국제선청사3층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "다온약국",
    "Address": "서울특별시 강서구 공항대로 269-15 힐스테이트에코마곡 309-1호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "세란온누리약국",
    "Address": "서울특별시 강서구 강서로 251 세란빌딩 103호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQzIyQ3OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "서울메디약국",
    "Address": "서울특별시 강서구 공항대로 272 하바나빌딩 1층 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "봄봄약국",
    "Address": "서울특별시 강서구 강서로 341 창대교회 1층 5호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 강서구 금낭화로 136 118호 (방화동, 에어뷰)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "21C세계로약국",
    "Address": "서울특별시 강서구 화곡로 173 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQxMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "웰빙약국",
    "Address": "서울특별시 강서구 화곡로68길 103 상가동 106호 (등촌동, 우성아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "열린온누리약국",
    "Address": "서울특별시 강서구 양천로 713 (염창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "메디팜정다운약국",
    "Address": "서울특별시 강서구 마곡중앙5로 87 107호 (마곡동, 우성르보아투)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ3MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "목화약국",
    "Address": "서울특별시 강서구 등촌로5길 5 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQwMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "바이엘약국",
    "Address": "서울특별시 강서구 화곡로 110 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "발산그랜드약국",
    "Address": "서울특별시 강서구 강서로 380 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "마곡하나약국",
    "Address": "서울특별시 강서구 강서로 385 106호 (마곡동, 우성에스비타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "사과약국",
    "Address": "서울특별시 강서구 강서로 391 108호 (마곡동, 문영비즈웍스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "공항시장샘온누리약국",
    "Address": "서울특별시 강서구 방화동로 37 메디스타워 102호 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ3OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "미즈정문약국",
    "Address": "서울특별시 강서구 강서로 299 1층 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "화창한약국",
    "Address": "서울특별시 강서구 공항대로41길 65 132호 (등촌동, 그랜드상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ4MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "산소망약국",
    "Address": "서울특별시 강서구 화곡로63길 133 1층 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQxMyQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 강서구 양천로 690 1층 (염창동, 호서빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ5OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "서연약국",
    "Address": "서울특별시 강서구 양천로57길 10-20 (가양동, 이스타빌 1차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ2MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "해맑은약국",
    "Address": "서울특별시 강서구 방화동로 66 1층 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQyIyQ3IyQwMCQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 강서구 강서로18다길 34 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQwMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "마곡메디칼약국",
    "Address": "서울특별시 강서구 마곡중앙5로 81 107, 108호 (마곡동, 에스비타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "우정약국",
    "Address": "서울특별시 강서구 가로공원로76길 47 1층 (화곡동, 김정호이비인후과의원)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "개화약국",
    "Address": "서울특별시 강서구 양천로 31 1층 (방화동, 푸른빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQwMyQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "다나아약국",
    "Address": "서울특별시 강서구 방화대로7나길 29 (공항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "화곡명문약국",
    "Address": "서울특별시 강서구 화곡로 176-4 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ4MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "대생약국",
    "Address": "서울특별시 강서구 강서로 171 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQwMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "대현온누리약국",
    "Address": "서울특별시 강서구 양천로 556 강서메디칼센터 105호 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ2MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "영일약국",
    "Address": "서울특별시 강서구 양천로 658 (염창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ2MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "강서약국",
    "Address": "서울특별시 강서구 등촌로 79 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "메디팜21세기약국",
    "Address": "서울특별시 강서구 화곡로 164 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQzIyQ2MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "아름드리약국",
    "Address": "서울특별시 강서구 강서로56길 30 1층 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ5MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "메디칼건강약국",
    "Address": "서울특별시 강서구 양천로 104 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQxMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "공항메디칼약국",
    "Address": "서울특별시 강서구 공항대로 38 1층 (공항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ5OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "크리닉약국",
    "Address": "서울특별시 강서구 강서로 261 연세내외과의원 2층 3호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQyIyQ3IyQwMCQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "국민약국",
    "Address": "서울특별시 강서구 곰달래로 225 1,2층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "새싹약국",
    "Address": "서울특별시 강서구 강서로 254 203호 (화곡동, 우장산이편한세상아이파크상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "유약국",
    "Address": "서울특별시 강서구 화곡로 331 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ3OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "새은약국",
    "Address": "서울특별시 강서구 양천로 601 (염창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ5OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "공항약국",
    "Address": "서울특별시 강서구 방화동로 10 (공항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "혜성약국",
    "Address": "서울특별시 강서구 까치산로 43 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "강서연세약국",
    "Address": "서울특별시 강서구 화곡로 346 103호 (화곡동, 귀뚜라미홈시스텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ5OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "미동약국",
    "Address": "서울특별시 강서구 월정로30길 52 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQyIyQ3IyQwMCQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "성혜약국",
    "Address": "서울특별시 강서구 강서로5나길 109 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 강서구 가로공원로76길 94 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQxMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신약국",
    "Address": "서울특별시 강서구 강서로45라길 35 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "우리온누리약국",
    "Address": "서울특별시 강서구 가로공원로76길 100 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "선일약국",
    "Address": "서울특별시 강서구 월정로 160 201호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ1IyQwMCQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "SooPharm수약국",
    "Address": "서울특별시 강서구 화곡로61길 26 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "선약국",
    "Address": "서울특별시 강서구 강서로 194-9 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "명진팜약국",
    "Address": "서울특별시 강서구 마곡중앙로 161-17 보타닉파크타워Ⅰ 110호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQ4OSQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "명문약국",
    "Address": "서울특별시 강서구 허준로 175 101호 (가양동, 가양6단지아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQwMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "구암약국",
    "Address": "서울특별시 강서구 허준로 121 109호 (가양동, 대림아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ4OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "동성약국",
    "Address": "서울특별시 강서구 금낭화로23길 8 123호 (방화동, 동성아파트단지내상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQwMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "남부시장약국",
    "Address": "서울특별시 강서구 등촌로5길 80 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ2MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "송약국",
    "Address": "서울특별시 강서구 양천로 637 104호 (염창동, 삼성아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "에이스약국",
    "Address": "서울특별시 강서구 화곡로 197 1-3호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQyIyQ3IyQwMCQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "부영약국",
    "Address": "서울특별시 강서구 강서로56나길 110 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQyIyQxIyQwMCQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "웰빙국내선약국",
    "Address": "서울특별시 강서구 하늘길 112 3층 (공항동, 국내선청사)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ2MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "새한약국",
    "Address": "서울특별시 강서구 등촌로 173 1층 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "녹십자약국",
    "Address": "서울특별시 강서구 화곡로64길 78 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "주약국",
    "Address": "서울특별시 강서구 공항대로 23 (공항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQwMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "한진약국",
    "Address": "서울특별시 강서구 우현로 26 101동 B202호 (화곡동, 우장산에스케이뷰)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQxMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "온누리성원약국",
    "Address": "서울특별시 강서구 방화동로16길 32 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "보람약국",
    "Address": "서울특별시 강서구 강서로 242 321호 (화곡동, 강서힐스테이트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "가까운천사약국",
    "Address": "서울특별시 강서구 공항대로36길 9 1층 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ2MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "나라약국",
    "Address": "서울특별시 강서구 강서로 27 103호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ5OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "송정온누리약국",
    "Address": "서울특별시 강서구 공항대로 34 (공항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "가양메디칼약국",
    "Address": "서울특별시 강서구 양천로57길 13 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "한솔약국",
    "Address": "서울특별시 강서구 양천로57길 37 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "코끼리약국",
    "Address": "서울특별시 강서구 등촌로 31 2층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "기린약국",
    "Address": "서울특별시 강서구 하늘길 74 (과해동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "우리팜약국",
    "Address": "서울특별시 강서구 강서로 318 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "에스메디약국",
    "Address": "서울특별시 강서구 방화동로 92 에스메디컬 1층 103호 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "동의송도약국",
    "Address": "서울특별시 강서구 강서로54길 79 1층 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "강서종로약국",
    "Address": "서울특별시 강서구 강서로 257 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "정수한약국",
    "Address": "서울특별시 강서구 강서로 263-23 1층 3호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "기쁨약국",
    "Address": "서울특별시 강서구 등촌로5길 2 1층 104, 105호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQyIyQ3IyQwMCQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "가까운중앙약국",
    "Address": "서울특별시 강서구 마곡중앙4로 74 106~107호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQwMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "희망찬약국",
    "Address": "서울특별시 강서구 강서로 43-17 B104호호 (화곡동, 오거닉스타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "프라자약국",
    "Address": "서울특별시 강서구 강서로 267 송화쇼핑센터 1층 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "솔약국",
    "Address": "서울특별시 강서구 양천로 564 등촌동두산위브센티움 131호 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 강서구 화곡로 153 1층 (화곡동, 광유빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "싱싱약국",
    "Address": "서울특별시 강서구 양천로 556 강서메디칼센터 103호 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ4MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "365그린약국",
    "Address": "서울특별시 강서구 강서로 43 B104호 (화곡동, 도양라비앙타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ3MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "이화정문약국",
    "Address": "서울특별시 강서구 마곡중앙4로 74 104~105호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "가까운약국",
    "Address": "서울특별시 강서구 공항대로 426 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQwMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "예성약국",
    "Address": "서울특별시 강서구 강서로 143 1층 (화곡동, 삼화빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ2MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "강서메디칼약국",
    "Address": "서울특별시 강서구 까치산로4길 3 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQwMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "우진약국",
    "Address": "서울특별시 강서구 곰달래로53가길 3 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "햇살온누리약국",
    "Address": "서울특별시 강서구 화곡로 142 114호 (화곡동, 메가박스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQwMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 강서구 양천로59길 46 103호 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ2MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "굿모닝이화약국",
    "Address": "서울특별시 강서구 공항대로 383 1층 4호 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "메디참사랑약국",
    "Address": "서울특별시 강서구 양천로 431 지하1층 (가양동, 홈플러스가양점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "우림약국",
    "Address": "서울특별시 강서구 등촌로 183 1층 (등촌동, 세스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ2MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "성모약국",
    "Address": "서울특별시 강서구 화곡로 313 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "더건강약국",
    "Address": "서울특별시 강서구 강서로 206 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQyIyQxIyQwMCQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 강서구 화곡로 347 111호 (화곡동, 그랜드아이파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ4OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "메디팜대야약국",
    "Address": "서울특별시 강서구 강서로 56 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQyIyQ3IyQwMCQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "화곡부성약국",
    "Address": "서울특별시 강서구 곰달래로 223 화곡동상가 104호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQwMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "비원약국",
    "Address": "서울특별시 강서구 공항대로 525 102호 (등촌동, 비원오피스텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ3MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "화평약국",
    "Address": "서울특별시 강서구 곰달래로 252 (화곡동, 웰피아)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "자연주의약국",
    "Address": "서울특별시 강서구 화곡로 194-26 (화곡동, 모아빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "한우리약국",
    "Address": "서울특별시 강서구 까치산로 151 104호 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQwMyQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "자성당약국",
    "Address": "서울특별시 강서구 방화대로21길 76 (공항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "동방약국",
    "Address": "서울특별시 강서구 강서로 186 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "가양종로약국",
    "Address": "서울특별시 강서구 양천로 460 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQyIyQxIyQwMCQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "용한약국",
    "Address": "서울특별시 강서구 허준로 47 상가동 105호 (가양동, 가양2단지아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ5MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "키즈약국",
    "Address": "서울특별시 강서구 강서로47가길 6 1층 108호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ4MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "태양약국",
    "Address": "서울특별시 강서구 등촌로13길 31 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 강서구 마곡중앙1로 72 305호 (마곡동, 마곡엠밸리10단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "밸런스약국",
    "Address": "서울특별시 강서구 공항대로 237 107호 (마곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ2MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 강서구 공항대로41길 76 로얄프라자106호 (등촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "노을약국",
    "Address": "서울특별시 강서구 까치산로 36 1층 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQwMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "스카이약국",
    "Address": "서울특별시 강서구 하늘길 38 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "한빛약국",
    "Address": "서울특별시 강서구 강서로62길 98 101호 (등촌동, 신한은행등촌점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "일신약국",
    "Address": "서울특별시 강서구 강서로 259 103호 (내발산동, 우장산역엠버리움빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQxMyQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "강서힐약국",
    "Address": "서울특별시 강서구 양천로 45-1 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "마곡정문약국",
    "Address": "서울특별시 강서구 수명로 76 서울메디스테이트빌딩 102호 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ5OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "온누리다나약국",
    "Address": "서울특별시 강서구 방화동로 56 1층 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "천수약국",
    "Address": "서울특별시 강서구 가로공원로76길 63 (화곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQwMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "신라약국",
    "Address": "서울특별시 강서구 방화동로 14 1층 (공항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "내인당약국",
    "Address": "서울특별시 강서구 강서로 301 1층 (내발산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ4OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 강서구 강서로13길 3 (화곡동, 동진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "푸른온누리약국",
    "Address": "서울특별시 강서구 방화대로34길 92 불해빌딩 1층 (방화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "벼리약국",
    "Address": "서울특별시 강서구 허준로 12 1층 103호 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "가양온누리약국",
    "Address": "서울특별시 강서구 허준로 198 가양프라자 1층 104, 105호 (가양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "동방약국",
    "Address": "서울특별시 관악구 인헌6길 9 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ5OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "누리약국",
    "Address": "서울특별시 관악구 관악로 222 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "참조은약국",
    "Address": "서울특별시 관악구 남부순환로 1814 대연빌딩 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQyIyQxIyQwMCQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "새시민약국",
    "Address": "서울특별시 관악구 난우길 4 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "가은약국",
    "Address": "서울특별시 관악구 봉천로 486 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ4OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "관악종로약국",
    "Address": "서울특별시 관악구 남부순환로 1833 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ2MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "365열린약국",
    "Address": "서울특별시 관악구 남부순환로 1615 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "옵티마세원약국",
    "Address": "서울특별시 관악구 쑥고개로 68 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ5MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "관악희망약국",
    "Address": "서울특별시 관악구 관악로 248 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 관악구 남부순환로 1912 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ2MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 관악구 신림로 137 (신림동, 조흥빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ3OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "광선약국",
    "Address": "서울특별시 관악구 은천로 51 은호빌딩 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "대동약국",
    "Address": "서울특별시 관악구 관악로 185 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "서울샤인약국",
    "Address": "서울특별시 관악구 남부순환로 1451 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQyIyQ5IyQwMCQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 관악구 난곡로 194 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "하얀약국",
    "Address": "서울특별시 관악구 난곡로 327-1 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "행복이가득한약국",
    "Address": "서울특별시 관악구 남부순환로 1443 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "마음약국",
    "Address": "서울특별시 관악구 남현길 7 한일프라자 1층 (남현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "그랜드약국",
    "Address": "서울특별시 관악구 인헌길 18 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQwMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "경희으뜸한약국",
    "Address": "서울특별시 관악구 낙성대역길 91 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "고은약국",
    "Address": "서울특별시 관악구 신림로 339 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "효심당한약국",
    "Address": "서울특별시 관악구 남부순환로 1901 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "아이봄약국",
    "Address": "서울특별시 관악구 남부순환로 2056 태림빌딩 지하1층 (남현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "관악그랜드약국",
    "Address": "서울특별시 관악구 신림로 141 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "서울온누리약국",
    "Address": "서울특별시 관악구 난곡로 214 1층 (신림동, 금정빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "우림시장약국",
    "Address": "서울특별시 관악구 난곡로26길 13 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ5MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "엘림온누리약국",
    "Address": "서울특별시 관악구 난곡로 316 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신림4번출구약국",
    "Address": "서울특별시 관악구 남부순환로 1604 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "웰약국",
    "Address": "서울특별시 관악구 관악로 217 동진빌딩 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "한울약국",
    "Address": "서울특별시 관악구 난곡로 50 자연빌딩 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "미소온누리약국",
    "Address": "서울특별시 관악구 난곡로 295 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ1IyQwMCQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "새난곡약국",
    "Address": "서울특별시 관악구 난곡로 210 2층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "관악소망약국",
    "Address": "서울특별시 관악구 남부순환로 1838 2층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQ5IyQwMCQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "오렌지약국",
    "Address": "서울특별시 관악구 관악로 168 1층 111호 (봉천동, 대우디오슈페리움2단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 관악구 남부순환로 1539 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "신한성약국",
    "Address": "서울특별시 관악구 남부순환로 2062 (남현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "이루는약국",
    "Address": "서울특별시 관악구 관악로 234 2층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "아림약국",
    "Address": "서울특별시 관악구 호암로26길 57 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQyIyQxIyQwMCQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "온누리드림약국",
    "Address": "서울특별시 관악구 성현로 80 203호 (봉천동, 관악드림타운주상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ3OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 관악구 호암로26길 1 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 관악구 장군봉1길 56 101호 (봉천동, 우형쇼핑센타)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQwMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "반석온누리약국",
    "Address": "서울특별시 관악구 관악로 195 A동 308호 (봉천동, 관악위버폴리스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "세영약국",
    "Address": "서울특별시 관악구 남부순환로 1479 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "청춘약국",
    "Address": "서울특별시 관악구 남부순환로 1644 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ2MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "관악수약국",
    "Address": "서울특별시 관악구 호암로 600 1층 (신림동, 하나빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQxIyQwMCQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "마더스약국",
    "Address": "서울특별시 관악구 난곡로 226 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "다정약국",
    "Address": "서울특별시 관악구 남부순환로 1485 1층 (신림동, 삼남빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQzIyQwMCQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "유명약국",
    "Address": "서울특별시 관악구 난곡로 202 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "워너비사랑약국",
    "Address": "서울특별시 관악구 남부순환로 2054 1층 (남현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "옵티마건강약국",
    "Address": "서울특별시 관악구 은천로 35 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "신림당약국",
    "Address": "서울특별시 관악구 관천로 17 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "온누리새전일약국",
    "Address": "서울특별시 관악구 법원단지길 37 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "정온누리약국",
    "Address": "서울특별시 관악구 남부순환로 1812 윤건빌딩 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 관악구 양녕로 50 3층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "밝은미소약국",
    "Address": "서울특별시 관악구 양녕로 46 메카플러스 1층 107호 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "유쾌한약국",
    "Address": "서울특별시 관악구 난곡로 217 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "평화약국",
    "Address": "서울특별시 관악구 남부순환로 1784 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ2MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "신미소약국",
    "Address": "서울특별시 관악구 시흥대로 578 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "임약국",
    "Address": "서울특별시 관악구 신림로 318 6층 (신림동, 청암두산위브센티움)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "예주약국",
    "Address": "서울특별시 관악구 남부순환로161길 75 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ1IyQwMCQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "리드팜힘찬약국",
    "Address": "서울특별시 관악구 은천로 109 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQxMyQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "청운약국",
    "Address": "서울특별시 관악구 양녕로 30 1층 (봉천동, 청운빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQwMyQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "난곡프라자약국",
    "Address": "서울특별시 관악구 난곡로 219 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "대림약국",
    "Address": "서울특별시 관악구 낙성대로 22 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 관악구 난곡로 198 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 관악구 남부순환로 2082-33 (남현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "도남희약국",
    "Address": "서울특별시 관악구 난향2길 8 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "늘봄약국",
    "Address": "서울특별시 관악구 인헌길 12 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "서울센터약국",
    "Address": "서울특별시 관악구 관악로 165 홍빌딩 2층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "인헌온누리약국",
    "Address": "서울특별시 관악구 인헌길 35 영빌딩 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "플러스튼튼약국",
    "Address": "서울특별시 관악구 남부순환로 1635 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "동인약국",
    "Address": "서울특별시 관악구 인헌길 76 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "한소망약국",
    "Address": "서울특별시 관악구 신림로 198 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "서강약국",
    "Address": "서울특별시 관악구 문성로 219 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "더푸른약국",
    "Address": "서울특별시 관악구 관악로 195 1층 104호 (봉천동, 관악위버폴리스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ5IyQwMCQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "모두온누리약국",
    "Address": "서울특별시 관악구 남부순환로 1869 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "늘푸른온누리약국",
    "Address": "서울특별시 관악구 남부순환로 1925 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ2MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "태연약국",
    "Address": "서울특별시 관악구 난곡로 305 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ3MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 관악구 남부순환로 1591 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ3MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "세란약국",
    "Address": "서울특별시 관악구 남부순환로161가길 26 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "21세기약국",
    "Address": "서울특별시 관악구 신림로 370 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "나나약국",
    "Address": "서울특별시 관악구 보라매로3길 29 3층 (봉천동, 보라매해태타워아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQyIyQ1IyQwMCQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "밝은세상약국",
    "Address": "서울특별시 관악구 신림로 368 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQyIyQ5IyQwMCQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "양지약국",
    "Address": "서울특별시 관악구 관악로 186 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQyIyQ3IyQwMCQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "관악이화약국",
    "Address": "서울특별시 관악구 봉천로 281 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ2MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "은성온누리약국",
    "Address": "서울특별시 관악구 신림로 210 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ4MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "신지약국",
    "Address": "서울특별시 관악구 신림로 105 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQxMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "파운지약국",
    "Address": "서울특별시 관악구 참숯1길 4 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQxIyQwMCQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "드림삼성약국",
    "Address": "서울특별시 관악구 구암길 106 206호 (봉천동, 관악드림타운 분산상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "원당프라자약국",
    "Address": "서울특별시 관악구 남부순환로248길 15 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "신림프라자약국",
    "Address": "서울특별시 관악구 신림로 271 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "맘이편한약국",
    "Address": "서울특별시 관악구 신림로 357 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "성락약국",
    "Address": "서울특별시 관악구 쑥고개로 86 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQxMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 관악구 은천로25길 69 1층 (봉천동, 삼성프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "우경약국",
    "Address": "서울특별시 관악구 호암로 531-1 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "필약국",
    "Address": "서울특별시 관악구 남부순환로 1605 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "관악온누리약국",
    "Address": "서울특별시 관악구 봉천로 488 1층 2호 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQxMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 관악구 난곡로 351 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 관악구 남부순환로172길 9 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "대명약국",
    "Address": "서울특별시 관악구 신림로 158 1층 1호 (신림동, 영광빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQwMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "푸르지오약국",
    "Address": "서울특별시 관악구 청림6길 3 202호 (봉천동, 관악푸르지오아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "하나로온누리약국",
    "Address": "서울특별시 관악구 은천로 38 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "매일약국",
    "Address": "서울특별시 관악구 인헌길 39 법향빌 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "성신약국",
    "Address": "서울특별시 관악구 남부순환로 1728 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "성보약국",
    "Address": "서울특별시 관악구 남부순환로208길 10 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "한국생약국",
    "Address": "서울특별시 관악구 쑥고개로 71 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 관악구 조원로 128-8 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "태양당약국",
    "Address": "서울특별시 관악구 국회단지길 10 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "왕약국",
    "Address": "서울특별시 관악구 대학5길 17 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "동보당약국",
    "Address": "서울특별시 관악구 관악로 236 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ2MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "봉천프라자약국",
    "Address": "서울특별시 관악구 남부순환로 1734 1층 (봉천동, 주원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "삼성약국",
    "Address": "서울특별시 관악구 신원로 21 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ4MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "참성심약국",
    "Address": "서울특별시 관악구 남부순환로 1862 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ5OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "휴베이스다정약국",
    "Address": "서울특별시 관악구 남부순환로 1944 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ5OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "다나온누리약국",
    "Address": "서울특별시 관악구 관악로 240 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQyIyQ3IyQwMCQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "혜인약국",
    "Address": "서울특별시 관악구 관악로 211 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 관악구 신림로 272 101-2호 (신림동, 대원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "새태평양온누리약국",
    "Address": "서울특별시 관악구 봉천로 616 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ4MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "신림수약국",
    "Address": "서울특별시 관악구 신림로 352 1층 (신림동, 연빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQyIyQxIyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "온누리수경약국",
    "Address": "서울특별시 관악구 난향길 4 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ2MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "신대명약국",
    "Address": "서울특별시 관악구 관악로 233 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "문박사약국",
    "Address": "서울특별시 관악구 양녕로 34 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "낙성대약국",
    "Address": "서울특별시 관악구 남부순환로 1938 1층 (봉천동, 성은빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQyIyQ3IyQwMCQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "밝은미래약국",
    "Address": "서울특별시 관악구 신림로 135 1층 (신림동, 육일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "보라매성심약국",
    "Address": "서울특별시 관악구 봉천로 227 304호 (봉천동, 보라매샤르망)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "사당미소약국",
    "Address": "서울특별시 관악구 과천대로 939 르메이에르강남타운2 3층 (남현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQxMyQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "우성혜민약국",
    "Address": "서울특별시 관악구 관악로30길 12 121호, 122호 (봉천동, 우성아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ2MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "서울대약국",
    "Address": "서울특별시 관악구 관악로 1 2층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ5MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "미향약국",
    "Address": "서울특별시 관악구 관악로 195 408호 (봉천동, 관악위버폴리스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQwMyQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 관악구 신원로 16 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "태림약국",
    "Address": "서울특별시 관악구 장군봉2길 2 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "녹원약국",
    "Address": "서울특별시 관악구 신림로 261 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "한일약국",
    "Address": "서울특별시 관악구 보라매로 12 2층 (봉천동, 관악농협)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQwMyQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "경희미소원한약국",
    "Address": "서울특별시 관악구 난곡로 290 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "순환약국",
    "Address": "서울특별시 관악구 호암로22길 60 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "신화약국",
    "Address": "서울특별시 관악구 관악로 153 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "구명약국",
    "Address": "서울특별시 관악구 봉천로 216 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQwMyQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "백두산약국",
    "Address": "서울특별시 관악구 은천로 37 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "성수온누리약국",
    "Address": "서울특별시 관악구 은천로 105 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ2MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 관악구 남부순환로143나길 7 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQxMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "세이브약국",
    "Address": "서울특별시 관악구 난곡로 220 1층 (신림동, 세이브마트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 관악구 난곡로 367 1층 (신림동, 경신빌딩 )"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "유완약국",
    "Address": "서울특별시 관악구 원신길 142 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ2MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "인수당약국",
    "Address": "서울특별시 관악구 인헌17길 3 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ5OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "이화온누리약국",
    "Address": "서울특별시 관악구 난곡로 53 303호 (신림동, 관악산휴먼시아상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ5MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "동원약국",
    "Address": "서울특별시 관악구 신림로 360-1 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQxMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "늘픔약국",
    "Address": "서울특별시 관악구 남부순환로 1635 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "가까운약국",
    "Address": "서울특별시 관악구 양녕로 46 112호 (봉천동, 메카플러스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQ2MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "착한약국",
    "Address": "서울특별시 관악구 호암로 535 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ4MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "세종약국",
    "Address": "서울특별시 관악구 난곡로31길 5 2동 1층 (신림동, 성수빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "광일약국",
    "Address": "서울특별시 관악구 양녕로 38 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "허브약국",
    "Address": "서울특별시 관악구 남부순환로 1471 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "봉천당약국",
    "Address": "서울특별시 관악구 봉천로 518 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQxMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "조광약국",
    "Address": "서울특별시 관악구 쑥고개로 70 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "한길약국",
    "Address": "서울특별시 관악구 남부순환로 1739 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "신신메디칼약국",
    "Address": "서울특별시 관악구 쑥고개로 59 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ2MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "광장약국",
    "Address": "서울특별시 관악구 관악로40길 47 현대상가 1동 1층 5호 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "허니약국",
    "Address": "서울특별시 관악구 보라매로5길 5 104호 (봉천동, 보라매우성아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "봉천미래약국",
    "Address": "서울특별시 관악구 남부순환로 1733 2층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "호호약국",
    "Address": "서울특별시 관악구 남부순환로 1595 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ2MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "제정약국",
    "Address": "서울특별시 관악구 신림로 383 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQwMyQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "아름다운약국",
    "Address": "서울특별시 관악구 난곡로 299 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ3MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "차약국",
    "Address": "서울특별시 관악구 중앙길 5 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 관악구 쑥고개로 53 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "대성약국",
    "Address": "서울특별시 관악구 청림길 8 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "사당365약국",
    "Address": "서울특별시 관악구 과천대로 955 1층 (남현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 관악구 남부순환로 1714-1 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQwMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "조양약국",
    "Address": "서울특별시 관악구 신사로10길 14 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQxMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "종로프라자약국",
    "Address": "서울특별시 관악구 조원중앙로 20 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 관악구 구암길 98 관악드림타운아파트 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQyIyQ3IyQwMCQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "웃음가득약국",
    "Address": "서울특별시 관악구 남부순환로 1369 1층 (신림동, 관악농협 농산물백화점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "사랑찬약국",
    "Address": "서울특별시 관악구 과천대로 909 남현프라자 지하2층 (남현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "하루약국",
    "Address": "서울특별시 관악구 호암로26길 43 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "문정약국",
    "Address": "서울특별시 관악구 양녕로 63 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQxMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "뿌리약국",
    "Address": "서울특별시 관악구 난우길 14 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQwMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "새푸른약국",
    "Address": "서울특별시 관악구 쑥고개로 122 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "행복약국",
    "Address": "서울특별시 관악구 관악로30길 12 301호 (봉천동, 봉천우성아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "남강약국",
    "Address": "서울특별시 관악구 난곡로 107-1 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQxMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "인제약국",
    "Address": "서울특별시 관악구 원신2길 17 인제약국 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQyIyQ3IyQwMCQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "비타약국",
    "Address": "서울특별시 관악구 원신길 147 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5OSQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "믿음약국",
    "Address": "서울특별시 관악구 봉천로 534 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "태창온누리약국",
    "Address": "서울특별시 관악구 쑥고개로 126-1 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "구약국",
    "Address": "서울특별시 관악구 관악로14길 52 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "난곡비타민약국",
    "Address": "서울특별시 관악구 난곡로 231 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "건강온누리약국",
    "Address": "서울특별시 관악구 남부순환로 1715 101호 (봉천동, 신우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ4MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "일광약국",
    "Address": "서울특별시 관악구 신사로20길 52 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "상쾌한약국",
    "Address": "서울특별시 관악구 신림로 340 르네상스복합쇼핑몰 3층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "1번약국",
    "Address": "서울특별시 관악구 남부순환로 1832 1층 (봉천동, 삼한빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ2MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "프라자약국",
    "Address": "서울특별시 관악구 봉천로 391 115호 (봉천동, 두산아파트에이상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQyIyQ3IyQwMCQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "스카이6층약국",
    "Address": "서울특별시 관악구 남부순환로 1820 6006호 (봉천동, 에그엘로우)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "종로수약국",
    "Address": "서울특별시 관악구 보라매로 4 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ2MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "팜프라자약국",
    "Address": "서울특별시 관악구 신림로 150 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "로뎀약국",
    "Address": "서울특별시 관악구 난곡로 349 1층 102호 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "신성심약국",
    "Address": "서울특별시 관악구 관악로 205 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "다나한약국",
    "Address": "서울특별시 관악구 청룡길 20 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ2MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "새종로약국",
    "Address": "서울특별시 관악구 난곡로 264 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ4OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "주평화약국",
    "Address": "서울특별시 관악구 인헌6길 5 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQwMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "대학당약국",
    "Address": "서울특별시 관악구 원신길 2-1 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "김약국",
    "Address": "서울특별시 관악구 남부순환로 1601-1 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQyIyQ3IyQwMCQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 관악구 남부순환로 1956 지하1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 관악구 난곡로 215 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ3MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "봄내약국",
    "Address": "서울특별시 관악구 신림동5길 31 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQxMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "예원약국",
    "Address": "서울특별시 관악구 쑥고개로 110 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "편한M약국",
    "Address": "서울특별시 관악구 신림로 318 1층 101호 (신림동, 청암두산위브센티움)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "양생약국",
    "Address": "서울특별시 관악구 남부순환로234길 27 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "경성약국",
    "Address": "서울특별시 관악구 남부순환로161길 70 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ5OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "다은온누리약국",
    "Address": "서울특별시 관악구 신림로 169 1층 (신림동, 영창빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "기분좋은약국",
    "Address": "서울특별시 관악구 은천로 110 1층 (봉천동, 더블유에스타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQxMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "영암약국",
    "Address": "서울특별시 관악구 원신2길 34 (신림동, 신림시장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "육당약국",
    "Address": "서울특별시 관악구 법원단지길 20 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "형제약국",
    "Address": "서울특별시 관악구 남부순환로172길 10 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "온누리대산약국",
    "Address": "서울특별시 관악구 시흥대로 560 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQwMyQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "명성프라자약국",
    "Address": "서울특별시 관악구 관악로 231-1 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "승일약국",
    "Address": "서울특별시 관악구 문성로 93 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "새유명온누리약국",
    "Address": "서울특별시 관악구 당곡길 22 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ4OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "강원약국",
    "Address": "서울특별시 관악구 대학길 36 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQyIyQ5IyQwMCQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "두산약국",
    "Address": "서울특별시 관악구 봉천로 391 113호 (봉천동, 두산아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ3MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "팜메이트난곡종합약국",
    "Address": "서울특별시 관악구 난곡로35길 2 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "광장온누리약국",
    "Address": "서울특별시 관악구 신림로 107 1층 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "교보약국",
    "Address": "서울특별시 관악구 남부순환로 1827 1층 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "우일약국",
    "Address": "서울특별시 관악구 난곡로24길 5 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "엘림약국",
    "Address": "서울특별시 관악구 신림로 322 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ4MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "윤선약국",
    "Address": "서울특별시 관악구 신림로 129-1 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "신다정약국",
    "Address": "서울특별시 관악구 관악로 154 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "관악우리약국",
    "Address": "서울특별시 관악구 남부순환로 1630 (신림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ2MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "광주약국",
    "Address": "서울특별시 관악구 관악로 268 (봉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQwMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 구로구 경인로 565 삼영빌딩 5층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQwMyQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "코끼리약국",
    "Address": "서울특별시 구로구 천왕로 32 천왕에이스프라자 103호 (천왕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "메디신약국",
    "Address": "서울특별시 구로구 목동남로 32 (고척동, 보광빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQwMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "온누리자혜약국",
    "Address": "서울특별시 구로구 개봉로 66 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "동의당한약국",
    "Address": "서울특별시 구로구 도림로 31 2층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "디큐브약국",
    "Address": "서울특별시 구로구 경인로 662 (신도림동, 디큐브시티 타워동 지하1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQwMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "대성약국",
    "Address": "서울특별시 구로구 개봉로3길 35 (개봉동, 성은빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQyIyQ3IyQwMCQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "온누리좋은약국",
    "Address": "서울특별시 구로구 가마산로 244 동헌빌딩 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQyIyQ1IyQwMCQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "환도약국",
    "Address": "서울특별시 구로구 구일로4길 46 1층 (구로동, 현대연예인아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ5MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "건강샘온누리약국",
    "Address": "서울특별시 구로구 경인로 661 219동 237호 (신도림동, 신도림1차푸르지오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "메디팜동진약국",
    "Address": "서울특별시 구로구 도림로 75 1층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "구림약국",
    "Address": "서울특별시 구로구 남부순환로105길 52 (가리봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "정약국",
    "Address": "서울특별시 구로구 개봉로 57-1 1층 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQyIyQxIyQwMCQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "1번약국",
    "Address": "서울특별시 구로구 구로동로 132 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ2MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "덕우약국",
    "Address": "서울특별시 구로구 가마산로22길 33 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "구로참조은약국",
    "Address": "서울특별시 구로구 구로동로 78 시몬빌딩 1층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 구로구 구로중앙로 212 영삼빌딩 1층 101호 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 구로구 남부순환로 775 상가106동 103호 (개봉동, 개봉푸르지오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "건강온누리약국",
    "Address": "서울특별시 구로구 고척로21나길 18 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "나은약국",
    "Address": "서울특별시 구로구 구로동로28길 99 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "구로메디칼약국",
    "Address": "서울특별시 구로구 경인로 431 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "금약국",
    "Address": "서울특별시 구로구 고척로 132 서정빌딩 1층 2호 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "제이약국",
    "Address": "서울특별시 구로구 디지털로34길 55 코오롱싸이언스밸리2차 2층 214-1호 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 구로구 개봉로 57 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQyIyQ3IyQwMCQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "맑은약국",
    "Address": "서울특별시 구로구 경인로40길 47 (개봉동, 개봉역)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "신도약국",
    "Address": "서울특별시 구로구 중앙로 60 (고척동, 강산메디칼프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "구로종로약국",
    "Address": "서울특별시 구로구 경인로 193 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "구로시장약국",
    "Address": "서울특별시 구로구 구로동로26길 37 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ2MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "항동푸른약국",
    "Address": "서울특별시 구로구 항동로3길 6 가온 프라자 105호 (항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "대웅프라자약국",
    "Address": "서울특별시 구로구 새말로 93 (구로동, 신도림태영타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "온누리백제약국",
    "Address": "서울특별시 구로구 고척로 212 102호 (고척동, 오토젠빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 구로구 고척로 148 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 구로구 구로동로 115 청보빌딩 지하1층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ5OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "보광약국",
    "Address": "서울특별시 구로구 구로동로38길 19 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQyIyQzIyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "용해약국",
    "Address": "서울특별시 구로구 도림로 29 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQxIyQwMCQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "은약국",
    "Address": "서울특별시 구로구 시흥대로 551 3층 (구로동, 광희빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "구민옵티마약국",
    "Address": "서울특별시 구로구 구로중앙로18길 68 (구로동, 신구로현대아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQwMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "메디칼바른약국",
    "Address": "서울특별시 구로구 공원로7길 40 1층 (구로동, 대영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ5OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "오류온누리약국",
    "Address": "서울특별시 구로구 경인로 201 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQxMyQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "아이사랑태평양약국",
    "Address": "서울특별시 구로구 새말로 15 101호일부,102호 (구로동, 삼전솔하임)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "맑은수약국",
    "Address": "서울특별시 구로구 개봉로 47 1층 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQzIyQ3OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "뿌리약국",
    "Address": "서울특별시 구로구 경인로53길 15 (구로동, 중앙유통단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQxMyQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "제생약국",
    "Address": "서울특별시 구로구 개봉로3가길 57 (개봉동, 제생약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "대우프라자약국",
    "Address": "서울특별시 구로구 고척로 237 (고척동, 부성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "황금당약국",
    "Address": "서울특별시 구로구 디지털로32길 79 1층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "우산약국",
    "Address": "서울특별시 구로구 구로동로 112-2 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "주차장바로약국",
    "Address": "서울특별시 구로구 가마산로 220 (구로동, 동성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "성심약국",
    "Address": "서울특별시 구로구 경인로20길 6 포스시티 104호 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "정성약국",
    "Address": "서울특별시 구로구 경인로 373 2층 (고척동, 문화골든타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ2MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "플러스약국",
    "Address": "서울특별시 구로구 경인로 661 (신도림동, 신도림1차푸르지오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "대우약국",
    "Address": "서울특별시 구로구 천왕로 106 골드프라자 104호 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "초지약국",
    "Address": "서울특별시 구로구 구로동로 240 (구로동, 세일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "바다약국",
    "Address": "서울특별시 구로구 구로중앙로 60 3층 (구로동, 대림오페라타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ5OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "일등약국",
    "Address": "서울특별시 구로구 구로동로 149 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ5MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "수태평양약국",
    "Address": "서울특별시 구로구 고척로 144 두발로빌딩 1층 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ2MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "자명약국",
    "Address": "서울특별시 구로구 디지털로 219 (가리봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 구로구 구로동로 179 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "즐거운약국",
    "Address": "서울특별시 구로구 경인로 320 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQwMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "구로솔약국",
    "Address": "서울특별시 구로구 경인로 433 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "살맛나는온누리약국",
    "Address": "서울특별시 구로구 서해안로 2098 항동프라자 103호 (항동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "구로미소약국",
    "Address": "서울특별시 구로구 서해안로 2338 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 구로구 신도림로 7 금강리빙스텔 123호 (신도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ5IyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "해솔온누리약국",
    "Address": "서울특별시 구로구 구일로4길 30 신영상가 102호 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "세계로온누리약국",
    "Address": "서울특별시 구로구 경인로 643 1층 (신도림동, 동아2차아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "믿음약국",
    "Address": "서울특별시 구로구 고척로21나길 17 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQxMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "미래약국",
    "Address": "서울특별시 구로구 구로동로 145-6 B동 1,2층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ5MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "인정약국",
    "Address": "서울특별시 구로구 서해안로 2296 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "새튼튼약국",
    "Address": "서울특별시 구로구 경인로 661 2층 211-1호 (신도림동, 신도림1차푸르지오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "상산약국",
    "Address": "서울특별시 구로구 중앙로 19 1층 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "에이스약국",
    "Address": "서울특별시 구로구 디지털로 285 104호 (구로동, 에이스트윈타워1차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "한빛약국",
    "Address": "서울특별시 구로구 경인로 164 3층 (오류동, 대일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "오류중앙약국",
    "Address": "서울특별시 구로구 경인로 195 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 구로구 구로중앙로 8 1층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQxMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 구로구 구로동로 149-1 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ2MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "동해물약국",
    "Address": "서울특별시 구로구 구로동로 138 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "칠성약국",
    "Address": "서울특별시 구로구 부일로15길 4 (궁동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ2MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "늘사랑약국",
    "Address": "서울특별시 구로구 개봉로3길 59 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "좋은약국",
    "Address": "서울특별시 구로구 경인로40길 34 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "흥부약국",
    "Address": "서울특별시 구로구 새말로 83 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "남구로약국",
    "Address": "서울특별시 구로구 구로동로 33 (가리봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "한마을약국",
    "Address": "서울특별시 구로구 경인로 382 (개봉동, 한마을아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "한독프라자약국",
    "Address": "서울특별시 구로구 구로동로26길 133 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 구로구 경인로67길 23 (신도림동,대우푸르지오2차 101동 311호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "참조은약국",
    "Address": "서울특별시 구로구 경인로 433-1 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "굿모닝온누리약국",
    "Address": "서울특별시 구로구 경인로67길 23 (신도림동, 신도림2차푸르지오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "세명약국",
    "Address": "서울특별시 구로구 오류로8길 16 세명프라자 201호 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "라라약국",
    "Address": "서울특별시 구로구 고척로 203 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "팜프라자약국",
    "Address": "서울특별시 구로구 디지털로 300 지밸리비즈플라자 지하1층 16호 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "보건당약국",
    "Address": "서울특별시 구로구 구로동로26길 116 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "생천온누리약국",
    "Address": "서울특별시 구로구 경인로59길 8 (신도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "녹십자약국",
    "Address": "서울특별시 구로구 구로동로28길 2 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "메디팜제일약국",
    "Address": "서울특별시 구로구 오리로 1270 (궁동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ2MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "장약국",
    "Address": "서울특별시 구로구 공원로8길 23 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "한솔약국",
    "Address": "서울특별시 구로구 경인로 215 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ5OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "은하약국",
    "Address": "서울특별시 구로구 개봉로 46 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ2MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "신효약국",
    "Address": "서울특별시 구로구 구로동로9길 9 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQxMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "독일약국",
    "Address": "서울특별시 구로구 오리로 1297 (궁동, 청파빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "래미안나나약국",
    "Address": "서울특별시 구로구 디지털로31길 86 (구로동, 삼성래미안아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 구로구 경인로 216 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "태영프라자약국",
    "Address": "서울특별시 구로구 경인로59길 8 (신도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "유풍약국",
    "Address": "서울특별시 구로구 경인로47길 54 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "성인약국",
    "Address": "서울특별시 구로구 개봉로 9 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQxMyQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "상아약국",
    "Address": "서울특별시 구로구 중앙로 100 연세사랑모아여성병원 104,105호 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "서울센타약국",
    "Address": "서울특별시 구로구 구로동로 151 (구로동, 코지하우스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ5MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "종로프라자약국",
    "Address": "서울특별시 구로구 구로중앙로 17 (구로동, 종로프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQwMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "재훈약국",
    "Address": "서울특별시 구로구 시흥대로161가길 17 (구로동, 성은빌라)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "구일중앙약국",
    "Address": "서울특별시 구로구 구일로 110 305호 (구로동, 해원리버파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 구로구 디지털로33길 11 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "새녹십자약국",
    "Address": "서울특별시 구로구 구로중앙로28길 65 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "옵티마건강약국",
    "Address": "서울특별시 구로구 경인로 315 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "샘물약국",
    "Address": "서울특별시 구로구 구로동로20길 6 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ5OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "해솔약국",
    "Address": "서울특별시 구로구 경인로 393-7 일이삼전자타운 2동 1층 120호 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "아름솔약국",
    "Address": "서울특별시 구로구 경인로53길 15 (구로동, 중앙유통단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ5IyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "시티프라자약국",
    "Address": "서울특별시 구로구 경인로 176 1층 105,106호호 (오류동, 시티월드)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ4MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "백세비타민약국",
    "Address": "서울특별시 구로구 디지털로26길 98 101호 (구로동, 디지털탑프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ2MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "미문약국",
    "Address": "서울특별시 구로구 구로동로 77 동해빌딩 지하1층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQwMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "신도림제일약국",
    "Address": "서울특별시 구로구 새말로 110 세아베스틸 1층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "대림약국",
    "Address": "서울특별시 구로구 신도림로 16 주상가동 209호 (신도림동, 대림2차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQwMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "타워약국",
    "Address": "서울특별시 구로구 디지털로 288 1층 104호 (구로동, 대륭포스트타워1차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "구로프라자온누리약국",
    "Address": "서울특별시 구로구 개봉로 30 (개봉동, 로얄타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQyIyQxIyQwMCQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 구로구 구로동로 149 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "차기정약국",
    "Address": "서울특별시 구로구 개봉로3길 76 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ2MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "백두약국",
    "Address": "서울특별시 구로구 오류로8길 26 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "부부약국",
    "Address": "서울특별시 구로구 오류로8길 60 (오류동, 우성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "다드림약국",
    "Address": "서울특별시 구로구 가마산로 211 101호 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "정수메디칼약국",
    "Address": "서울특별시 구로구 구로중앙로 68 101호 (구로동, 신안타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "개성약국",
    "Address": "서울특별시 구로구 경인로 176 308호 (오류동, 시티월드)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ2MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "후문약국",
    "Address": "서울특별시 구로구 가마산로 222 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ2MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "강서약국",
    "Address": "서울특별시 구로구 개봉로19길 21 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 구로구 경서로 6 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "구로약국",
    "Address": "서울특별시 구로구 구로동로 147 MEDI FLOWER 147 1층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQwMyQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "부강약국",
    "Address": "서울특별시 구로구 중앙로14길 27 104호 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ5MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "더블유스토어푸른약국",
    "Address": "서울특별시 구로구 도림로 73 (구로동, 인성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "개봉지예당약국",
    "Address": "서울특별시 구로구 고척로 123-1 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ3OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "훼미리약국",
    "Address": "서울특별시 구로구 고척로 139 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "기린약국",
    "Address": "서울특별시 구로구 구로동로 215-1 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQxMyQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 구로구 고척로 142-1 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "대림우리약국",
    "Address": "서울특별시 구로구 도림로 92 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "시장약국",
    "Address": "서울특별시 구로구 경인로47길 126 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 구로구 구로중앙로12길 38 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "온누리최정숙약국",
    "Address": "서울특별시 구로구 중앙로1길 36 (고척동, 2001아울렛)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQxMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "민트약국",
    "Address": "서울특별시 구로구 경인로 482 (구로동, 롯데마트구로점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ3MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 구로구 시흥대로 547 (구로동, 금강빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "두산약국",
    "Address": "서울특별시 구로구 구로중앙로 16 1층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "새수정약국",
    "Address": "서울특별시 구로구 오리로 1286 (궁동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "365열린약국",
    "Address": "서울특별시 구로구 남부순환로97길 3 KS프리미어빌딩 105호 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ3OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "온누리사랑의약국",
    "Address": "서울특별시 구로구 구로동로15길 17 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQyIyQzIyQwMCQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "세진약국",
    "Address": "서울특별시 구로구 개봉로 63 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "현대파크빌약국",
    "Address": "서울특별시 구로구 공원로 41 (구로동, 현대파크빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQwMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 구로구 오류로8길 57 (오류동, 대성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "태영약국",
    "Address": "서울특별시 구로구 새말로 89 108,109호 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "연세열린약국",
    "Address": "서울특별시 구로구 개봉로 23 (개봉동, 고려크리닉센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQ1IyQwMCQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "아침햇살약국",
    "Address": "서울특별시 구로구 시흥대로 561 (구로동, 동해빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ2MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "수정약국",
    "Address": "서울특별시 구로구 경인로 319 401호 (개봉동, 대림프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "505약국",
    "Address": "서울특별시 구로구 구로동로42길 58 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQyIyQ1IyQwMCQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "온누리십자당약국",
    "Address": "서울특별시 구로구 구로동로 173 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ2MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "개미프라자약국",
    "Address": "서울특별시 구로구 구로동로35길 46 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "세종당약국",
    "Address": "서울특별시 구로구 경인로35길 64 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "장수약국",
    "Address": "서울특별시 구로구 경인로47길 94 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "정제약국",
    "Address": "서울특별시 구로구 개봉로17길 10 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQwMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "정광약국",
    "Address": "서울특별시 구로구 남부순환로97길 11 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "원일약국",
    "Address": "서울특별시 구로구 중앙로15길 29 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "동성약국",
    "Address": "서울특별시 구로구 우마2길 24 (가리봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ5OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "온수약국",
    "Address": "서울특별시 구로구 부일로1길 22 (온수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "W스토아청와약국",
    "Address": "서울특별시 구로구 디지털로 227 (가리봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "스타약국",
    "Address": "서울특별시 구로구 경인로 572 (구로동, 스타팰리스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "초록약국",
    "Address": "서울특별시 구로구 구일로4길 46 204호 (구로동, 현대연예인아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "새서울약국",
    "Address": "서울특별시 구로구 가마산로 268 대림역와이즈플레이스 108호 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ4MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "새우리약국",
    "Address": "서울특별시 구로구 개봉로 71 2층 (개봉동, 강서프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "그린프라자약국",
    "Address": "서울특별시 구로구 구로동로 137 (구로동, GS 칼텍스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "우리네온누리약국",
    "Address": "서울특별시 구로구 디지털로27길 116 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "한중약국",
    "Address": "서울특별시 구로구 구로동로 8 (가리봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 구로구 도림로 67 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQyIyQ1IyQwMCQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "온누리한라약국",
    "Address": "서울특별시 구로구 구일로10길 49 (구로동, 다원그린빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 구로구 중앙로15길 107 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "큰사랑약국",
    "Address": "서울특별시 구로구 구로동로26길 119 1층 (구로동, 정엽빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "은성약국",
    "Address": "서울특별시 구로구 신도림로19길 7 (신도림동, 성광빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "참좋은약국",
    "Address": "서울특별시 구로구 구로중앙로 134 4층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQwMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "명문약국",
    "Address": "서울특별시 구로구 디지털로32길 97-39 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "연세온누리약국",
    "Address": "서울특별시 구로구 신도림로 2 엘림빌딩 1층 (신도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ2MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "모스팜약국",
    "Address": "서울특별시 구로구 새말로 97 신도림테크노마트 지하1층 BS026호 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "새하늘약국",
    "Address": "서울특별시 구로구 개봉로20길 6 (개봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ2MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "종로약국",
    "Address": "서울특별시 구로구 고척로 142 (고척동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "진솔약국",
    "Address": "서울특별시 구로구 경인로 211-1 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ2MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "태양약국",
    "Address": "서울특별시 구로구 경인로 191 (오류동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "참온누리약국",
    "Address": "서울특별시 구로구 오리로 1149 B108호 (오류동, 랑데르)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "라온약국",
    "Address": "서울특별시 구로구 새말로 97 신도림테크노마트 사무동 10층 (구로동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "창동종로약국",
    "Address": "서울특별시 도봉구 노해로63길 84-3 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 도봉구 해등로16길 26 104호 (창동, 타임프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "중앙온누리약국",
    "Address": "서울특별시 도봉구 덕릉로 241 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ2MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "후문한일약국",
    "Address": "서울특별시 도봉구 노해로40길 72 (쌍문동, 쌍문한양아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "신창약국",
    "Address": "서울특별시 도봉구 덕릉로 258 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "쌍문마이팜약국",
    "Address": "서울특별시 도봉구 도봉로141길 11 1층 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "신원약국",
    "Address": "서울특별시 도봉구 노해로63길 78 4층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQyIyQ1IyQwMCQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "이화태평양약국",
    "Address": "서울특별시 도봉구 덕릉로 239 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "파마트열린약국",
    "Address": "서울특별시 도봉구 해등로 218 102호 (쌍문동, 보성상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "나진약국",
    "Address": "서울특별시 도봉구 방학로 223 101호 (방학동, 사천목씨종친회관)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "쌍문약국",
    "Address": "서울특별시 도봉구 도봉로 473-1 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "산들약국",
    "Address": "서울특별시 도봉구 도당로13길 17 1층 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "창동남대문약국",
    "Address": "서울특별시 도봉구 덕릉로 223 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "제생약국",
    "Address": "서울특별시 도봉구 도당로 94 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "방학태평양약국",
    "Address": "서울특별시 도봉구 도당로 80 1층 (방학동, 방학동근생)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQxMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 도봉구 도봉로 551-10 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ3MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "희정약국",
    "Address": "서울특별시 도봉구 마들로 859-19 109호 (도봉동, 한신아파트근린상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ4MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "부광약국",
    "Address": "서울특별시 도봉구 덕릉로 398 120호 (창동, 주공17단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "별약국",
    "Address": "서울특별시 도봉구 도봉로 927 1층 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQxMyQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "신프라자약국",
    "Address": "서울특별시 도봉구 덕릉로 251 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "정민약국",
    "Address": "서울특별시 도봉구 도봉로 887 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQxMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "명산약국",
    "Address": "서울특별시 도봉구 노해로 384 2층 203-1호 (창동, 동아상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQwMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 도봉구 도봉로 452 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "대웅약국",
    "Address": "서울특별시 도봉구 우이천로 298 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 도봉구 도당로 109 방학동상가주택1층 102호 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQyIyQ1IyQwMCQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "백운약국",
    "Address": "서울특별시 도봉구 도봉로 468 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "일충프라자약국",
    "Address": "서울특별시 도봉구 도봉로 575 삼환프라자 103호 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQ5OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "뉴메디슨약국",
    "Address": "서울특별시 도봉구 해등로 255 101동 207호 (쌍문동, 에벤에셀)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "가야온누리약국",
    "Address": "서울특별시 도봉구 노해로65길 17-9 102,103호 (창동, 삼원프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "보화당약국",
    "Address": "서울특별시 도봉구 노해로69길 15 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "스타빌약국",
    "Address": "서울특별시 도봉구 노해로63길 84-9 창동 SR스타빌 3층 302호 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "종로프라자약국",
    "Address": "서울특별시 도봉구 노해로65길 14-3 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "늘기쁜약국",
    "Address": "서울특별시 도봉구 도봉로 726 1층 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQwMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "삼성늘푸른약국",
    "Address": "서울특별시 도봉구 도봉로 476 206호 (창동, 삼성쉐르빌퍼스티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "월드중앙약국",
    "Address": "서울특별시 도봉구 마들로 650 104-2호 (방학동, 도봉월드상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "금빛약국",
    "Address": "서울특별시 도봉구 덕릉로 238 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "새순보당약국",
    "Address": "서울특별시 도봉구 덕릉로 233-5 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQyIyQzIyQwMCQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "쌍문상록수약국",
    "Address": "서울특별시 도봉구 해등로26길 7 (쌍문동, 우진빌딩 110,116호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "메디칼2층약국",
    "Address": "서울특별시 도봉구 도봉로 484 2층 (창동, 청우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQyIyQ1IyQwMCQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "방학세계로약국",
    "Address": "서울특별시 도봉구 방학로 159 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "즐거운약국",
    "Address": "서울특별시 도봉구 노해로63길 79 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQxMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "건강제일녹십자약국",
    "Address": "서울특별시 도봉구 해등로 190 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "청춘약국",
    "Address": "서울특별시 도봉구 도봉로180길 46 1층 101호 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "은약국",
    "Address": "서울특별시 도봉구 도봉로 473 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ2MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "송이약국",
    "Address": "서울특별시 도봉구 도봉로113길 41 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQxMyQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "쉐르빌약국",
    "Address": "서울특별시 도봉구 도봉로 476 109호 (창동, 삼성쉐르빌퍼스티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ4MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "후문약국",
    "Address": "서울특별시 도봉구 도봉로109길 58 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "상록수온누리약국",
    "Address": "서울특별시 도봉구 도당로13길 8 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQwMyQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "아름다운약국",
    "Address": "서울특별시 도봉구 도봉로 551 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ5OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "메디약국",
    "Address": "서울특별시 도봉구 방학로 183 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ5MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "녹십자약국",
    "Address": "서울특별시 도봉구 우이천로4길 32 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQyIyQ3IyQwMCQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 도봉구 도봉로163길 7 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ2MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "광장온누리약국",
    "Address": "서울특별시 도봉구 노해로 389 101~104호 (창동, 제일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ5OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "손온누리약국",
    "Address": "서울특별시 도봉구 도봉로 626 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "자모약국",
    "Address": "서울특별시 도봉구 도봉로133길 14 A동 101호 (쌍문동, 성원하이츠아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "힘찬약국",
    "Address": "서울특별시 도봉구 삼양로 580-4 1층 101호 (쌍문동, 노스브릭)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQ3IyQwMCQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 도봉구 방학로 169 1층 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "신신약국",
    "Address": "서울특별시 도봉구 도봉로113길 16 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ4OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "진성온누리약국",
    "Address": "서울특별시 도봉구 도봉로 681 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "창동이화약국",
    "Address": "서울특별시 도봉구 노해로 341 305호 (창동, 창동신원리베르텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ2MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 도봉구 도봉로118길 11 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ4OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "태양당약국",
    "Address": "서울특별시 도봉구 시루봉로15길 36 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ4MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "초록약국",
    "Address": "서울특별시 도봉구 방학로 163 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "온누리수약국",
    "Address": "서울특별시 도봉구 해등로 190 3층 314호 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "푸른대우약국",
    "Address": "서울특별시 도봉구 덕릉로63가길 61 상가동 203호 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "대한약국",
    "Address": "서울특별시 도봉구 삼양로 586 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ2MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 도봉구 해등로 190 2층 217호 (쌍문동, 신원주상복합2차아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ2MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "성가온누리약국",
    "Address": "서울특별시 도봉구 도당로 133 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "참좋은약국",
    "Address": "서울특별시 도봉구 도봉로 496 1층 102호 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ5IyQwMCQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "아이약국",
    "Address": "서울특별시 도봉구 도봉로 461 2층 (쌍문동, 우림빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "태양약국",
    "Address": "서울특별시 도봉구 도봉로 479 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "청솔동아약국",
    "Address": "서울특별시 도봉구 노해로69길 103 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ2MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "영락온누리약국",
    "Address": "서울특별시 도봉구 시루봉로 290 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "레몬약국",
    "Address": "서울특별시 도봉구 시루봉로 105 1층 111호 (방학동, 신동아상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "메디팜큰사랑약국",
    "Address": "서울특별시 도봉구 도봉로 488 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "방학약국",
    "Address": "서울특별시 도봉구 도봉로 729 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ3MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "유경약국",
    "Address": "서울특별시 도봉구 마들로 684 1층 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "드림온누리약국",
    "Address": "서울특별시 도봉구 마들로 551 상가동 1층 120호 (창동, 쌍용아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ5MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "햇빛약국",
    "Address": "서울특별시 도봉구 도당로13길 16 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ2MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "365일팜코리아약국",
    "Address": "서울특별시 도봉구 도봉로 733 1층 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ3MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "장수당약국",
    "Address": "서울특별시 도봉구 도봉로 859 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "백세약국",
    "Address": "서울특별시 도봉구 도당로15길 12 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ5MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "도봉월드약국",
    "Address": "서울특별시 도봉구 마들로 650 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "하나로약국",
    "Address": "서울특별시 도봉구 마들로11길 20 1층 (창동, 농협창동유통센타)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 도봉구 도봉로 678 홈플러스데스코㈜방학점 지하2층 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQ2MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "웰빙약국",
    "Address": "서울특별시 도봉구 도봉로 604 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQyIyQxIyQwMCQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "대영약국",
    "Address": "서울특별시 도봉구 도봉로129길 26 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQyIyQ5IyQwMCQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 도봉구 노해로69길 25 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ2MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "고명약국",
    "Address": "서울특별시 도봉구 도봉로 724 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 도봉구 도봉로 677 105호 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQxMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "혜민약국",
    "Address": "서울특별시 도봉구 도봉로159길 17 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ2MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "도봉태평양약국",
    "Address": "서울특별시 도봉구 도봉로 821 1층 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQxMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "정대식약국",
    "Address": "서울특별시 도봉구 노해로70길 54 122호 (창동, 주공19단지 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "영훈약국",
    "Address": "서울특별시 도봉구 덕릉로 222 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQyIyQxIyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "서진약국",
    "Address": "서울특별시 도봉구 마들로 686 103호 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "늘편한약국",
    "Address": "서울특별시 도봉구 덕릉로 218-1 1층 (창동, 좌측)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "부부약국",
    "Address": "서울특별시 도봉구 도봉로181길 46 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "더튼튼약국",
    "Address": "서울특별시 도봉구 노해로65길 10 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "엔젤팜약국",
    "Address": "서울특별시 도봉구 방학로3길 121 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ3MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "착한약국",
    "Address": "서울특별시 도봉구 덕릉로 253 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "새보은약국",
    "Address": "서울특별시 도봉구 삼양로154길 42 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "종로세명약국",
    "Address": "서울특별시 도봉구 방학로 176 (방학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 도봉구 마들로 650 3층 319호 (방학동, 도봉월드상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQyIyQzIyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 도봉구 도봉로180나길 34 1층 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQ1IyQwMCQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 도봉구 도봉로150길 43 2층 215호 (방학동, ESA 아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQwMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "민중약국",
    "Address": "서울특별시 도봉구 덕릉로 235 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ3MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "메디슨약국",
    "Address": "서울특별시 도봉구 해등로 255 101동 102호 (쌍문동, 신원상가에벤에셀)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "라파온누리약국",
    "Address": "서울특별시 도봉구 우이천로4길 42 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQxMyQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 도봉구 우이천로 302 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQyIyQxIyQwMCQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "뉴지명약국",
    "Address": "서울특별시 도봉구 덕릉로 236 1층 (창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "용호약국",
    "Address": "서울특별시 도봉구 노해로41길 42 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ3OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "오약국",
    "Address": "서울특별시 도봉구 마들로 657 112호 (방학동, 이에스에이아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQxMyQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 도봉구 마들로 697 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "약손약국",
    "Address": "서울특별시 도봉구 도봉로 601 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQwMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "무지개온누리약국",
    "Address": "서울특별시 도봉구 도봉로 471 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ2MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "유림당약국",
    "Address": "서울특별시 도봉구 해등로 109 104호 (창동, 주공1단지 종합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQwMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "메디팜건강약국",
    "Address": "서울특별시 도봉구 도봉로 487 1층 (쌍문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQxMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 도봉구 마들로 691 1층 (도봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "메디팜동아약국",
    "Address": "서울특별시 동대문구 한천로 55 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "경원약국",
    "Address": "서울특별시 동대문구 고산자로36길 3 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQxIyQ3MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "현지당약국",
    "Address": "서울특별시 동대문구 고산자로 445-1 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "새한약국",
    "Address": "서울특별시 동대문구 약령중앙로 10-5 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQxMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "홈타운약국",
    "Address": "서울특별시 동대문구 장안벚꽃로 107 2층 6호 (장안동, 현대홈타운제1상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ2MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 동대문구 신이문로 39 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ4MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "신우당약국",
    "Address": "서울특별시 동대문구 약령동길 84 1층 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "경동삼우한약국",
    "Address": "서울특별시 동대문구 고산자로36길 3 신관1층 21호,22호 (제기동, 경동시장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQyIyQ3IyQwMCQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "한신약국",
    "Address": "서울특별시 동대문구 제기로 75 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQwMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "한사랑온누리약국",
    "Address": "서울특별시 동대문구 신이문로 41 1층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "영림약국",
    "Address": "서울특별시 동대문구 망우로21길 16 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "정화약국",
    "Address": "서울특별시 동대문구 홍릉로 7 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ2MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "외대조은약국",
    "Address": "서울특별시 동대문구 휘경로 10 1층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "구흥한약국",
    "Address": "서울특별시 동대문구 고산자로 449 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "대학솔약국",
    "Address": "서울특별시 동대문구 안암로 158 1층 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "천사약국",
    "Address": "서울특별시 동대문구 왕산로26길 13 1층 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQxMyQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "남진약국",
    "Address": "서울특별시 동대문구 약령시로 86-1 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "동부대학약국",
    "Address": "서울특별시 동대문구 무학로 122 1층 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "신종로약국",
    "Address": "서울특별시 동대문구 왕산로 261 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ2MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "장안메디칼약국",
    "Address": "서울특별시 동대문구 사가정로 207 104호,105호 (장안동, 삼협메디스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ2MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 동대문구 답십리로66길 95 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "경동시장약국",
    "Address": "서울특별시 동대문구 고산자로 476 1층 (제기동, 서울제기동우체국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "경희메디칼약국",
    "Address": "서울특별시 동대문구 경희대로 24 1층 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "서생당약국",
    "Address": "서울특별시 동대문구 서울시립대로 42 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "금창약국",
    "Address": "서울특별시 동대문구 약령시로 3 1층 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQwMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 동대문구 사가정로 148 141동 211호 (전농동, SK아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 동대문구 왕산로 20 1층 (신설동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQxMyQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "동암당약국",
    "Address": "서울특별시 동대문구 고산자로44길 2 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQyIyQzIyQwMCQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "청운약국",
    "Address": "서울특별시 동대문구 휘경로23길 14 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "동아약국",
    "Address": "서울특별시 동대문구 서울시립대로 31 102-119호 (전농동, 동아아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ5MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "설파약국",
    "Address": "서울특별시 동대문구 전농로 134 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQ4OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "서천당약국",
    "Address": "서울특별시 동대문구 약령중앙로8길 15 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "한가람약국",
    "Address": "서울특별시 동대문구 망우로 77 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ2MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "365종로약국",
    "Address": "서울특별시 동대문구 전농로 38 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ2MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "삼보약국",
    "Address": "서울특별시 동대문구 전농로 24 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신우약국",
    "Address": "서울특별시 동대문구 홍릉로 5-1 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "우리보강약국",
    "Address": "서울특별시 동대문구 약령시로 133 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "장수약국",
    "Address": "서울특별시 동대문구 이문로 135 1층 105호 (이문동, 아정오피스텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "흥명약국",
    "Address": "서울특별시 동대문구 고산자로30길 56 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ2MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "동안메디약국",
    "Address": "서울특별시 동대문구 천호대로17길 75 1층 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ4OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "제일성모약국",
    "Address": "서울특별시 동대문구 약령시로 126 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQwMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "사랑드림약국",
    "Address": "서울특별시 동대문구 이문로 83 1층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQxMyQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "남지약국",
    "Address": "서울특별시 동대문구 한천로11길 43 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "초원옵티마약국",
    "Address": "서울특별시 동대문구 제기로 84 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "이레약국",
    "Address": "서울특별시 동대문구 사가정로 122 전농동하우스토리 3층 313호 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "오로라온누리약국",
    "Address": "서울특별시 동대문구 서울시립대로 92 1층 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "조령약국",
    "Address": "서울특별시 동대문구 장한로 12 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQxMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "신유약국",
    "Address": "서울특별시 동대문구 장한로28가길 1 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQwMyQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "연세약국",
    "Address": "서울특별시 동대문구 전농로16길 11 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQxMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "외대김약국",
    "Address": "서울특별시 동대문구 이문로 125 더 메디칼빌딩 1층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQxMyQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "혜민약국",
    "Address": "서울특별시 동대문구 홍릉로 34-1 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ2MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "명약국",
    "Address": "서울특별시 동대문구 망우로18나길 3 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ5MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "삼오약국",
    "Address": "서울특별시 동대문구 답십리로 64 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "한유약국",
    "Address": "서울특별시 동대문구 한천로 89 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "시장약국",
    "Address": "서울특별시 동대문구 왕산로 143 1층 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ3OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "조현약국",
    "Address": "서울특별시 동대문구 장한로6길 10 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQwMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "답십리백화점약국",
    "Address": "서울특별시 동대문구 전농로 102 1층 (답십리동, 목련빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ5MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "대명당약국",
    "Address": "서울특별시 동대문구 천호대로13길 56 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "킴스팜대보약국",
    "Address": "서울특별시 동대문구 휘경로3길 4 1층 (이문동, 이문동빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "정동약국",
    "Address": "서울특별시 동대문구 전농로 12 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "유한약국",
    "Address": "서울특별시 동대문구 천호대로 295 2층 10호 (답십리동, 우창프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신행당약국",
    "Address": "서울특별시 동대문구 사가정로 148 3층 (전농동, sk아파트스포츠상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ2MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "국민약국",
    "Address": "서울특별시 동대문구 이문로 37 104호 (회기동, 회기역 한일베라체캠퍼스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "경희정문약국",
    "Address": "서울특별시 동대문구 경희대로 22-1 1층 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "다온약국",
    "Address": "서울특별시 동대문구 답십리로 273 한양빌딩 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "동부메디칼약국",
    "Address": "서울특별시 동대문구 무학로 128 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "이룸약국",
    "Address": "서울특별시 동대문구 한천로58길 47 (이문동, 쌍용아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "새싹약국",
    "Address": "서울특별시 동대문구 이문로 136 1층 109호 (이문동, 웰츠타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "장안제일약국",
    "Address": "서울특별시 동대문구 장한로25길 2 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQwMyQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "메디칼갑산약국",
    "Address": "서울특별시 동대문구 망우로 123 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "에스케이행복약국",
    "Address": "서울특별시 동대문구 사가정로 148 141동 312호 (전농동, sk아파트스포츠상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ3OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "경희제일약국",
    "Address": "서울특별시 동대문구 경희대로 19-5 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "조약국",
    "Address": "서울특별시 동대문구 천호대로 133 지하2층 (용두동, 홈플러스 동대문점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQxMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "수인약국",
    "Address": "서울특별시 동대문구 장한로 119 3층 305호 (장안동, 삼성쉐르빌빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "바른손약국",
    "Address": "서울특별시 동대문구 휘경로 34 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "경희자연한약국",
    "Address": "서울특별시 동대문구 이문로9길 8 2층 1호,2호 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "이웃사랑약국",
    "Address": "서울특별시 동대문구 한천로46길 56-4 101호 (장안동, 부성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQyIyQ3IyQwMCQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "수온누리약국",
    "Address": "서울특별시 동대문구 사가정로 122 206호 (전농동, 전농하우스토리)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQwMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 동대문구 전농로 128 1층 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQwMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "강북열린약국",
    "Address": "서울특별시 동대문구 전농로 110 1층 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "늘조은온누리약국",
    "Address": "서울특별시 동대문구 사가정로25길 66 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "쉐르빌우리약국",
    "Address": "서울특별시 동대문구 장한로 119 323호 (장안동, 장안삼성쉐르빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 동대문구 왕산로 151 2층 4,5호 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "한성약국",
    "Address": "서울특별시 동대문구 답십리로 140 세기프라자 106호 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ2MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "하나온누리약국",
    "Address": "서울특별시 동대문구 사가정로 206 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "장안중앙약국",
    "Address": "서울특별시 동대문구 한천로 62 1층 101호 (장안동, 화성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "민중약국",
    "Address": "서울특별시 동대문구 답십리로 9 1층 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQxMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "경희온누리약국",
    "Address": "서울특별시 동대문구 경희대로1가길 32 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "올리브약국",
    "Address": "서울특별시 동대문구 장한로 130 1층 105호 (장안동, 장안빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "중경당약국",
    "Address": "서울특별시 동대문구 장한로 58 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQxMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "기쁜약국",
    "Address": "서울특별시 동대문구 이문로 88 1층 103호 (이문동, 민족통일 대통령 빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 동대문구 천호대로 8 1층 (신설동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ2MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "엄마약국",
    "Address": "서울특별시 동대문구 휘경로 15 4층 402호 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQyIyQzIyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "노아한약국",
    "Address": "서울특별시 동대문구 천장산로7길 62 3층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQwMyQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "최선약국",
    "Address": "서울특별시 동대문구 전농로 36 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "장안미소약국",
    "Address": "서울특별시 동대문구 답십리로 305 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 동대문구 왕산로 185 1층 105호 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 동대문구 한천로 4 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "나나약국",
    "Address": "서울특별시 동대문구 장한로18길 59 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ2MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "뉴메디칼약국",
    "Address": "서울특별시 동대문구 전농로 147 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ5MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "신동서약국",
    "Address": "서울특별시 동대문구 약령시로 2-1 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQwMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신도약국",
    "Address": "서울특별시 동대문구 고산자로 534 103호 (제기동, 한신아파트 상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQxMyQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "청수약국",
    "Address": "서울특별시 동대문구 천호대로25길 81 1층 103호 (용두동, 랜드마크타워1)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQyIyQ1IyQwMCQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "우리재약국",
    "Address": "서울특별시 동대문구 천호대로 289 1층 101호 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "혜중약국",
    "Address": "서울특별시 동대문구 이문로 186 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "보림약국",
    "Address": "서울특별시 동대문구 장한로 115 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ3OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "정다운우리약국",
    "Address": "서울특별시 동대문구 왕산로 127 지하1층 (제기동, 경동대성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQwMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 동대문구 경희대로 15 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ3MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "한림약국",
    "Address": "서울특별시 동대문구 장한로21길 11-12 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "가까운약국",
    "Address": "서울특별시 동대문구 천호대로 313 10호, 11호 (답십리동, 태영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "조은온누리약국",
    "Address": "서울특별시 동대문구 장한로 51 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ2MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "이문메디칼약국",
    "Address": "서울특별시 동대문구 이문로 131 1층 (이문동, 삼일퍼스탑)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "정다운약국",
    "Address": "서울특별시 동대문구 이문로54길 46 1층 108호 (이문동, 이문e편한세상아파트상가1동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQxMyQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "삼익약국",
    "Address": "서울특별시 동대문구 회기로29길 35 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "대흥당약국",
    "Address": "서울특별시 동대문구 답십리로15길 30 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "인영약국",
    "Address": "서울특별시 동대문구 왕산로 118 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "동산약국",
    "Address": "서울특별시 동대문구 왕산로 225 A동 1층 32-1호 (청량리동, 미주상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQxMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "경애약국",
    "Address": "서울특별시 동대문구 사가정로25길 18 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQyIyQxIyQwMCQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "홍약국",
    "Address": "서울특별시 동대문구 답십리로48가길 46 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQxMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "중량약국",
    "Address": "서울특별시 동대문구 망우로 131 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "신보명약국",
    "Address": "서울특별시 동대문구 천호대로79길 66 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "이문우량아약국",
    "Address": "서울특별시 동대문구 신이문로 27 1층 101호 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ2MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "엄마손약국",
    "Address": "서울특별시 동대문구 사가정로 148 141동 108호 (전농동, 전농 SK아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQwMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "보림한약국",
    "Address": "서울특별시 동대문구 이문로1길 25 1층 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "메디컬우리약국",
    "Address": "서울특별시 동대문구 휘경로 43 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "이문태평양약국",
    "Address": "서울특별시 동대문구 이문로 130 1층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "효성당약국",
    "Address": "서울특별시 동대문구 왕산로32길 26 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "크로바약국",
    "Address": "서울특별시 동대문구 망우로 80 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQxMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "원보당약국",
    "Address": "서울특별시 동대문구 약령중앙로 41 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ3MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "성심약국",
    "Address": "서울특별시 동대문구 회기로 185 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ2MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "감초당온누리약국",
    "Address": "서울특별시 동대문구 한천로 242 1층 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQxMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "새성수약국",
    "Address": "서울특별시 동대문구 서울시립대로 116 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQ1IyQwMCQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "늘좋은약국",
    "Address": "서울특별시 동대문구 천호대로 319 1층 102호 (답십리동, 답십리한화오벨리스크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQ3IyQwMCQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "카톨릭대학약국",
    "Address": "서울특별시 동대문구 왕산로 178 1층 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQ3IyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "행복한정약국",
    "Address": "서울특별시 동대문구 이문로 188 1층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "우리들위생약국",
    "Address": "서울특별시 동대문구 망우로 78 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "휘경약국",
    "Address": "서울특별시 동대문구 망우로21가길 10 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQwMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "해동그랜드약국",
    "Address": "서울특별시 동대문구 한천로 186 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQyIyQxIyQwMCQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "뉴프라자약국",
    "Address": "서울특별시 동대문구 고산자로 399 104호,105호 (용두동, 동양프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "맑은샘약국",
    "Address": "서울특별시 동대문구 천호대로83길 39 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "답십리코코약국",
    "Address": "서울특별시 동대문구 답십리로 130 301동 103호 (답십리동, 래미안위브아파트단지내상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "장안수약국",
    "Address": "서울특별시 동대문구 천호대로83길 43-1 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQ5MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "감초당약국",
    "Address": "서울특별시 동대문구 약령중앙로 11 1층 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "하늘후문약국",
    "Address": "서울특별시 동대문구 황물로 168 한성아펠시티 122,123호 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "국제약국",
    "Address": "서울특별시 동대문구 답십리로 252 1층 (장안동, 세현빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ2MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "진선미약국",
    "Address": "서울특별시 동대문구 한천로 86 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQyIyQzIyQwMCQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "새소망약국",
    "Address": "서울특별시 동대문구 답십리로 293 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQzIyQxMyQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "원지당약국",
    "Address": "서울특별시 동대문구 약령중앙로 14-3 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "성부당약국",
    "Address": "서울특별시 동대문구 왕산로 163-1 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQxIyQ2MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "동신약국",
    "Address": "서울특별시 동대문구 하정로5길 1 1층 (신설동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQxIyQxMyQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "한진당약국",
    "Address": "서울특별시 동대문구 고산자로36길 3 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "코아약국",
    "Address": "서울특별시 동대문구 이문로 30 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ5OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "세광약국",
    "Address": "서울특별시 동대문구 왕산로 171 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQwMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "우진당약국",
    "Address": "서울특별시 동대문구 사가정로13길 3 1층 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "자연약국",
    "Address": "서울특별시 동대문구 휘경로 31 1층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ4MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "허브약국",
    "Address": "서울특별시 동대문구 경희대로 19-3 1층 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQxIyQ5OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "새경희약국",
    "Address": "서울특별시 동대문구 경희대로1가길 27 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "바오로약국",
    "Address": "서울특별시 동대문구 왕산로 225 2층 203호 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "신종로사약국",
    "Address": "서울특별시 동대문구 휘경로 49 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "참이화약국",
    "Address": "서울특별시 동대문구 천호대로 307 1층 104호 (답십리동, 클래식타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ2MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 동대문구 사가정로 148 205호 (전농동, sk아파트스포츠상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "건강한약국",
    "Address": "서울특별시 동대문구 왕산로32길 7 4층 6호 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ3OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "덕현당한약국",
    "Address": "서울특별시 동대문구 고산자로 445 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 동대문구 전농로 148 1층 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "본약국",
    "Address": "서울특별시 동대문구 전농로 212 1층 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "행복나무한약국",
    "Address": "서울특별시 동대문구 경희대로 6-1 3층 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "경희다정한약국",
    "Address": "서울특별시 동대문구 답십리로65길 77 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQwMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "삼천당약국",
    "Address": "서울특별시 동대문구 약령동길 41 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "아이약국",
    "Address": "서울특별시 동대문구 장한로32길 19 105동 102호 (장안동, 삼성리치캐슬)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ4OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "지운당한약국",
    "Address": "서울특별시 동대문구 고산자로 469 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ3MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "평생믿는한약국",
    "Address": "서울특별시 동대문구 신이문로 9 (이문동,금호어울림아파트 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "문경한약국",
    "Address": "서울특별시 동대문구 약령중앙로 13 1층 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 동대문구 장한로 129 102호 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQwMyQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "아파트엠약국",
    "Address": "서울특별시 동대문구 무학로26길 16 111호 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQwMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "메디팜사랑약국",
    "Address": "서울특별시 동대문구 망우로18길 6 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ2MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "우량아약국",
    "Address": "서울특별시 동대문구 사가정로 214 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "청솔약국",
    "Address": "서울특별시 동대문구 전농로10길 20 (답십리동, 청솔우성아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ2MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "연수당약국",
    "Address": "서울특별시 동대문구 무학로34길 11 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQyIyQ3IyQwMCQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "신한약국",
    "Address": "서울특별시 동대문구 장한로 170 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "장안약국",
    "Address": "서울특별시 동대문구 답십리로 248 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQxMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "에스케이약국",
    "Address": "서울특별시 동대문구 사가정로 148 222-1호 (전농동, SK아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQyIyQzIyQwMCQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 동대문구 천호대로 273 1층 2호 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "홍릉종로약국",
    "Address": "서울특별시 동대문구 홍릉로 59 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "어깨동무약국",
    "Address": "서울특별시 동대문구 무학로 189 1층 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQxMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "동대문보건약국",
    "Address": "서울특별시 동대문구 고산자로28가길 2 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "새이화약국",
    "Address": "서울특별시 동대문구 장한로 140 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQyIyQ1IyQwMCQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "후문약국",
    "Address": "서울특별시 동대문구 왕산로45길 8 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQyIyQ1IyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "복지약국",
    "Address": "서울특별시 동대문구 천호대로 227 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 동대문구 장한로32길 7 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "4층현약국",
    "Address": "서울특별시 동대문구 천호대로 425 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ2MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "보은한약국",
    "Address": "서울특별시 동대문구 약령중앙로 72-2 203호 (제기동, 윤주빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQxMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 동대문구 답십리로56길 21 상가동 102호 (답십리동, 두산아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "정성약국",
    "Address": "서울특별시 동대문구 서울시립대로 50 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ4MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 동대문구 장한로 22 2층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "경희고황약국",
    "Address": "서울특별시 동대문구 경희대로 17 1층 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ4OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "새린온누리약국",
    "Address": "서울특별시 동대문구 답십리로 266 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQwMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 동대문구 고산자로38길 18 1층 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQxMyQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "경희중앙약국",
    "Address": "서울특별시 동대문구 경희대로 19-9 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQ5OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "삼성엠(M)약국",
    "Address": "서울특별시 동대문구 왕산로 247-1 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "하은약국",
    "Address": "서울특별시 동대문구 사가정로 110 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "혜원사약국",
    "Address": "서울특별시 동대문구 난계로 238 (신설동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "삼화약국",
    "Address": "서울특별시 동대문구 왕산로 207 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQwMyQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "우주약국",
    "Address": "서울특별시 동대문구 장한로 139 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQxMyQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "오렌지약국",
    "Address": "서울특별시 동대문구 한천로 120 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "한국약국",
    "Address": "서울특별시 동대문구 약령시로 123 1층 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "그랜드온누리약국",
    "Address": "서울특별시 동대문구 장한로 14 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "명문온누리약국",
    "Address": "서울특별시 동대문구 사가정로 225 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "넘버원삼육약국",
    "Address": "서울특별시 동대문구 망우로18길 26 1층 (휘경동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQwMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "금신당약국",
    "Address": "서울특별시 동대문구 천호대로 427-4 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "평제약국",
    "Address": "서울특별시 동대문구 약령시로 51 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQxMyQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "코끼리약국",
    "Address": "서울특별시 동대문구 신이문로24길 4 1층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQxMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "푸르지오약국",
    "Address": "서울특별시 동대문구 왕산로 86 푸르지오시티오피스텔동 1층 101호 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "메디약국",
    "Address": "서울특별시 동대문구 회기로 173 1층 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQwMyQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 동대문구 왕산로 176 2층 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "종로프라자약국",
    "Address": "서울특별시 동대문구 사가정로 226 101호~104호 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "민성약국",
    "Address": "서울특별시 동대문구 한천로11길 32 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "신상록수약국",
    "Address": "서울특별시 동대문구 무학로26길 5 1층 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ3OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "경희동문약국",
    "Address": "서울특별시 동대문구 경희대로 19 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ3MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "새동산약국",
    "Address": "서울특별시 동대문구 왕산로 225 미주상가 A동 2층 11-2호 (청량리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "으뜸약국",
    "Address": "서울특별시 동대문구 왕산로 52 102동 104호 (용두동, 신설동역대우아이빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "래미안약국",
    "Address": "서울특별시 동대문구 전농로3길 78-1 1층 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "경희우리약국",
    "Address": "서울특별시 동대문구 경희대로 21 지층, 1층, 2층 (회기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "미소가득약국",
    "Address": "서울특별시 동대문구 장안벚꽃로 107 상가1동 2층 215-1호 (장안동, 장안현대홈타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQwMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 동대문구 전농로 91 (답십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "마장백화점약국",
    "Address": "서울특별시 동대문구 고산자로 410 1층 (용두동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ5OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "미래로약국",
    "Address": "서울특별시 동대문구 이문로 114 한국외국어대학교 글로벌홀 1층 (이문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ5MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "청량리중앙약국",
    "Address": "서울특별시 동대문구 왕산로 214 403호 (전농동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "자연다림한약국",
    "Address": "서울특별시 동대문구 정릉천동로 114-3 202호 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "튼튼하나약국",
    "Address": "서울특별시 동대문구 답십리로 259 1층 (장안동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQyIyQ3IyQwMCQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "경희삼일한약국",
    "Address": "서울특별시 동대문구 약령동길 17 (제기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ5MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "행복드림약국",
    "Address": "서울특별시 동작구 노량진로 90 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "한라약국",
    "Address": "서울특별시 동작구 사당로 301 사당동빌딩 3층 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 동작구 사당로 303 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "김약국",
    "Address": "서울특별시 동작구 노량진로 162 . 1층 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ2MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "오아시스약국",
    "Address": "서울특별시 동작구 양녕로 287 B301호 (상도동, 대우유로카운티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "금성약국",
    "Address": "서울특별시 동작구 사당로16길 68 지하1층 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "정다운약국",
    "Address": "서울특별시 동작구 만양로 19 상가동 3층 311,312호 (노량진동, 신동아리버파크아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "민들레약국",
    "Address": "서울특별시 동작구 보라매로 110 영등포농협 1층 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "2층은약국",
    "Address": "서울특별시 동작구 현충로 75 원불교100년기념관 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "바름약국",
    "Address": "서울특별시 동작구 흑석로 101 1층 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 동작구 신대방1가길 38 105동 3층 309호 (신대방동, 동작상떼빌아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "노들약국",
    "Address": "서울특별시 동작구 노량진로 166 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ1IyQwMCQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "맑은샘약국",
    "Address": "서울특별시 동작구 장승배기로 110 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ3MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 동작구 여의대방로24길 30 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 동작구 동작대로 43 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQxMyQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "유정온누리약국",
    "Address": "서울특별시 동작구 여의대방로22나길 1 1층 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "밝은세상하나약국",
    "Address": "서울특별시 동작구 사당로 236 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQxMyQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 동작구 양녕로38길 2 (상도1동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ2MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "한빛평화약국",
    "Address": "서울특별시 동작구 시흥대로 664 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ5OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "고은온누리약국",
    "Address": "서울특별시 동작구 여의대방로36길 1 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 동작구 상도로 206 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "새싹약국",
    "Address": "서울특별시 동작구 장승배기로 34 1층 101호 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ2MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "상산약국",
    "Address": "서울특별시 동작구 서달로 136-1 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "현명약국",
    "Address": "서울특별시 동작구 등용로 6 (상도동, 크라운플라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "지성약국",
    "Address": "서울특별시 동작구 양녕로 189 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQwMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "신대방수연약국",
    "Address": "서울특별시 동작구 신대방2길 1 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQyIyQ5IyQwMCQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "진원약국",
    "Address": "서울특별시 동작구 노량진로6길 62 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQyIyQzIyQwMCQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "파란약국",
    "Address": "서울특별시 동작구 남부순환로 2057 3층 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "파랑새약국",
    "Address": "서울특별시 동작구 상도로 81 지하1층 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "단골약국",
    "Address": "서울특별시 동작구 보라매로 61-1 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "새미약국",
    "Address": "서울특별시 동작구 동작대로 25 4층 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "메디컬수약국",
    "Address": "서울특별시 동작구 서달로 150 207호, 208호 (흑석동, 해가든상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "해태사랑약국",
    "Address": "서울특별시 동작구 보라매로3길 29 3층 306호 (신대방동, 해태보라매타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3OSQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 동작구 신대방1가길 38 105동 305, 306호 (신대방동, 동작상떼빌아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "상도시장약국",
    "Address": "서울특별시 동작구 상도로22길 46 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQwMyQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "금강약국",
    "Address": "서울특별시 동작구 매봉로 178 B02호 (본동, 마본빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "보라매조은약국",
    "Address": "서울특별시 동작구 보라매로5길 23 지하 122호 (신대방동, 삼성보라매옴니타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQyIyQzIyQwMCQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "아름약국",
    "Address": "서울특별시 동작구 서달로 110-1 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "제당약국",
    "Address": "서울특별시 동작구 국사봉길 97 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "전원약국",
    "Address": "서울특별시 동작구 사당로 244 1호 (사당동, 사당시장 점포)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "해태보라매약국",
    "Address": "서울특별시 동작구 보라매로3길 29 (신대방동,해태보라매타워상가동 1층 28호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQxMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "우방약국",
    "Address": "서울특별시 동작구 시흥대로 638 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQyIyQ5IyQwMCQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "화생약국",
    "Address": "서울특별시 동작구 노량진로6길 26 1층 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQyIyQ1IyQwMCQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 동작구 양녕로 195 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQwMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 동작구 노량진로 155 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "온누리송학대약국",
    "Address": "서울특별시 동작구 장승배기로 119 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQwMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "예하약국",
    "Address": "서울특별시 동작구 성대로 24 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "효성약국",
    "Address": "서울특별시 동작구 상도로 181 (상도동, 효성약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQyIyQzIyQwMCQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "별약국",
    "Address": "서울특별시 동작구 상도로 104 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "밝은미소약국",
    "Address": "서울특별시 동작구 사당로 215 108호 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "성대약국",
    "Address": "서울특별시 동작구 성대로 11 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ5MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "찬솔약국",
    "Address": "서울특별시 동작구 만양로 86 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQxMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "예쁜약국",
    "Address": "서울특별시 동작구 서달로 166 2층 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "메디팜엔비약국",
    "Address": "서울특별시 동작구 노량진로 152 . 1층 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ2MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "희경약국",
    "Address": "서울특별시 동작구 상도로 99 1층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQxMyQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 동작구 만양로 5 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQwMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "큰사랑약국",
    "Address": "서울특별시 동작구 상도로 346 우일빌딩 2층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "건강과행복이열리는중앙메디칼약국",
    "Address": "서울특별시 동작구 흑석로 106-5 1층 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "메디홈약국",
    "Address": "서울특별시 동작구 상도로 174 (상도동, 동서남북빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ3OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "건강온누리약국",
    "Address": "서울특별시 동작구 상도로 202 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ2MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "상도프라자약국",
    "Address": "서울특별시 동작구 상도로 356 1층 (상도동, 교동빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "메디칼우리약국",
    "Address": "서울특별시 동작구 보라매로 106 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "사당프라자약국",
    "Address": "서울특별시 동작구 사당로 230-1 1층 (사당동, 미래빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "우리들온누리약국",
    "Address": "서울특별시 동작구 사당로 196 1층 (사당동, 거묵프리미엄상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "새천년약국",
    "Address": "서울특별시 동작구 상도로 69 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ2MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "대광약국",
    "Address": "서울특별시 동작구 상도로45길 6 (상도1동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQyIyQzIyQwMCQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "아담약국",
    "Address": "서울특별시 동작구 현충로 114-1 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 동작구 상도로 153 1층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "신정약국",
    "Address": "서울특별시 동작구 사당로23바길 9 동작삼성래미안아파트 상가 202호 (사당동, 동작삼성래미안아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "사당소화약국",
    "Address": "서울특별시 동작구 동작대로 7 1층 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4OSQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 동작구 장승배기로10길 47 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ2MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디칼수정약국",
    "Address": "서울특별시 동작구 보라매로 113 105호 (대방동, 코스모빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "보라매서울약국",
    "Address": "서울특별시 동작구 보라매로5길 15 전문건설회관빌딩 지하1층 C-5호 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "우리온누리약국",
    "Address": "서울특별시 동작구 흑석한강로 27 B106호 (흑석동, 흑석한강푸르지오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQ1IyQwMCQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "신중앙약국",
    "Address": "서울특별시 동작구 흑석로 103 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQyIyQzIyQwMCQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "대림온누리약국",
    "Address": "서울특별시 동작구 시흥대로 662 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "친절한약국",
    "Address": "서울특별시 동작구 사당로 224 1층 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQwMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "제중당건강약국",
    "Address": "서울특별시 동작구 동작대로 89 107,108,S-12,S-13호 (사당동, 골든시네마타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQxMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "팜프라자약국",
    "Address": "서울특별시 동작구 남부순환로 2055 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "인화약국",
    "Address": "서울특별시 동작구 만양로 84 102,103호 (노량진동, 삼익주상복합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ2MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "흑석유약국",
    "Address": "서울특별시 동작구 현충로10길 88-6 110호 (흑석동, 흑석한강센트레빌상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "햇살온누리약국",
    "Address": "서울특별시 동작구 상도로 345 1층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQxMyQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "윤당약국",
    "Address": "서울특별시 동작구 시흥대로 644 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQwMyQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "행복이열리는건강약국",
    "Address": "서울특별시 동작구 상도로 301 (상도1동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "시장약국",
    "Address": "서울특별시 동작구 동작대로29길 17 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "에셀약국",
    "Address": "서울특별시 동작구 여의대방로 22 (신대방동, 우성A상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "이정원약국",
    "Address": "서울특별시 동작구 국사봉길 90 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ3MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "은성약국",
    "Address": "서울특별시 동작구 노량진로8길 3 (노량진동, 경성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQ4MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "정성을다하는약국",
    "Address": "서울특별시 동작구 성대로29길 68 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "유성약국",
    "Address": "서울특별시 동작구 등용로14길 65 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "이수약국",
    "Address": "서울특별시 동작구 동작대로29길 24 101호 (사당동, 정현빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQzIyQwMCQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "유림온누리약국",
    "Address": "서울특별시 동작구 사당로 215 107호 (사당동, 서림빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "보라매온누리약국",
    "Address": "서울특별시 동작구 보라매로 93 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQyIyQ1IyQwMCQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "대남약국",
    "Address": "서울특별시 동작구 상도로22길 26 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "고은약국",
    "Address": "서울특별시 동작구 사당로23길 185 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQyIyQ5IyQwMCQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "신안약국",
    "Address": "서울특별시 동작구 장승배기로 139-1 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ2MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "세브란스약국",
    "Address": "서울특별시 동작구 동작대로25길 39 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "명인약국",
    "Address": "서울특별시 동작구 여의대방로 126 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "대일약국",
    "Address": "서울특별시 동작구 동작대로27길 22 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "화천약국",
    "Address": "서울특별시 동작구 동작대로25길 6 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ3OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "은미약국",
    "Address": "서울특별시 동작구 사당로16길 22 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "복지약국",
    "Address": "서울특별시 동작구 사당로 194 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ2MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "명수대약국",
    "Address": "서울특별시 동작구 서달로 151 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ3MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "용강약국",
    "Address": "서울특별시 동작구 노량진로26길 13 (본동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "해가든약국",
    "Address": "서울특별시 동작구 서달로 150 202호 (흑석동, 해가든상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQwMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 동작구 흑석로 106 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQxMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "성모약국",
    "Address": "서울특별시 동작구 상도로 247 1층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "동광약국",
    "Address": "서울특별시 동작구 동작대로 129 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQxMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "동의당약국",
    "Address": "서울특별시 동작구 여의대방로10길 38 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "수산약국",
    "Address": "서울특별시 동작구 노들로 674 노량진수산물도매시장 2층 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "수온누리약국",
    "Address": "서울특별시 동작구 동작대로 65 1층 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "세메론약국",
    "Address": "서울특별시 동작구 여의대방로44길 47 (대방동, 주공상가 101호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "우정약국",
    "Address": "서울특별시 동작구 서달로 144 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ5MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "대방약국",
    "Address": "서울특별시 동작구 등용로 127 103동 203호 (대방동, 현대아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "꿀약국",
    "Address": "서울특별시 동작구 양녕로 186 1층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ5MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "씨에이(CA)정문약국",
    "Address": "서울특별시 동작구 흑석로 108 1~2층 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "성약국",
    "Address": "서울특별시 동작구 상도로15길 143 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQwMyQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "팜팜약국",
    "Address": "서울특별시 동작구 여의대방로 250 104호 (대방동, 대림쇼핑)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "조이온누리약국",
    "Address": "서울특별시 동작구 동작대로 121 지하1층 (사당동, 경원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 동작구 여의대방로 142 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "해뜨는약국",
    "Address": "서울특별시 동작구 양녕로 281 (상도동, 상도빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "광주약국",
    "Address": "서울특별시 동작구 동작대로 127 1층 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "솔약국",
    "Address": "서울특별시 동작구 동작대로17길 3 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQwMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "보건약국",
    "Address": "서울특별시 동작구 장승배기로10길 43 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQyIyQxIyQwMCQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "늘사랑약국",
    "Address": "서울특별시 동작구 상도로 91 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "새비타민약국",
    "Address": "서울특별시 동작구 성대로 52 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "우성당약국",
    "Address": "서울특별시 동작구 여의대방로 22 104호 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ2MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "강림약국",
    "Address": "서울특별시 동작구 시흥대로 668-2 (신대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ3OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "옵티마상도약국",
    "Address": "서울특별시 동작구 상도로53길 6 1층 (상도동, 순현빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ4MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "새중앙약국",
    "Address": "서울특별시 동작구 노량진로 110 113호 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "엄마손약국",
    "Address": "서울특별시 동작구 동작대로29길 69 201호 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 동작구 보라매로5길 23 지하1층 B117호 (신대방동, 삼성보라매옴니타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQxMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "오약국",
    "Address": "서울특별시 동작구 동작대로29길 69 금강산보석불가마사우나 303호 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 동작구 상도로 93 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQwMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "다은약국",
    "Address": "서울특별시 동작구 장승배기로20길 2 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ3MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "노량진종로약국",
    "Address": "서울특별시 동작구 노량진로 234 (본동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQwMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "온누리세종약국",
    "Address": "서울특별시 동작구 동작대로7길 84 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ4MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "이도약국",
    "Address": "서울특별시 동작구 만양로 112 1층 (노량진동, 서원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "라파약국",
    "Address": "서울특별시 동작구 상도로 348 평강빌딩 1층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "다솜약국",
    "Address": "서울특별시 동작구 상도로 82 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "숭실길약국",
    "Address": "서울특별시 동작구 상도로67길 31 1층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "동의보감 한약국",
    "Address": "서울특별시 동작구 사당로22길 3 602호 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "경희서림한약국",
    "Address": "서울특별시 동작구 상도로15길 98 1층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "설약국",
    "Address": "서울특별시 동작구 노량진로 124 1층 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ3OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "금영약국",
    "Address": "서울특별시 동작구 장승배기로 76 1층 (상도동, 대경빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "대우당약국",
    "Address": "서울특별시 동작구 상도로 102 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQyIyQ5IyQwMCQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "옵티마다정약국",
    "Address": "서울특별시 동작구 동작대로29길 69 120,121호 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQwMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "안일약국",
    "Address": "서울특별시 동작구 성대로 76 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "샬롬약국",
    "Address": "서울특별시 동작구 성대로2길 12 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "중앙프라자약국",
    "Address": "서울특별시 동작구 상도로 178 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "유원약국",
    "Address": "서울특별시 동작구 상도로 377 1층 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 동작구 사당로 227 1층 (사당동, 태평약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "교약국",
    "Address": "서울특별시 동작구 상도로 407-5 (상도동, 삼호아파트 상가 109호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "계령약국",
    "Address": "서울특별시 동작구 성대로 32 (상도동, 계령약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "신성약국",
    "Address": "서울특별시 동작구 상도로 331 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ3MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "새종로약국",
    "Address": "서울특별시 동작구 성대로 5 (상도동, 새종로약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ3OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "새보라매약국",
    "Address": "서울특별시 동작구 보라매로5길 5 101호 (신대방동, 보라매우성상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "보라매대학약국",
    "Address": "서울특별시 동작구 보라매로5길 23 101호 (신대방동, 삼성보라매옴니타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQwMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "아임약국",
    "Address": "서울특별시 동작구 만양로 84 2층 208호 (노량진동, 삼익주상복합아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "부산약국",
    "Address": "서울특별시 동작구 성대로 68 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ2MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "상아온누리약국",
    "Address": "서울특별시 동작구 양녕로26길 22 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "가족건강약국",
    "Address": "서울특별시 동작구 등용로 115 101호 (대방동, 엘리시아빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "꿈꾸는약국",
    "Address": "서울특별시 동작구 장승배기로 168 B001호 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQyIyQ1IyQwMCQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "신대방약국",
    "Address": "서울특별시 동작구 상도로 77 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQxMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "이수사랑약국",
    "Address": "서울특별시 동작구 사당로 300 222호 (사당동, 이수자이)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "소화약국",
    "Address": "서울특별시 동작구 여의대방로24나길 2 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQwMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "평화약국",
    "Address": "서울특별시 동작구 남부순환로 2059 1층 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "중문약국",
    "Address": "서울특별시 동작구 흑석로 106-9 2층 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 동작구 여의대방로36길 5 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ5MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "신세계약국",
    "Address": "서울특별시 동작구 사당로 297 (사당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ2MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "약수태평양약국",
    "Address": "서울특별시 동작구 장승배기로 7 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "정성약국",
    "Address": "서울특별시 동작구 여의대방로 250 2층 201호 (대방동, 대림상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "엄마랑약국",
    "Address": "서울특별시 동작구 장승배기로 107 1층 2호 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ5MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "상도온누리약국",
    "Address": "서울특별시 동작구 상도로 297 (상도1동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "아카데미약국",
    "Address": "서울특별시 동작구 보라매로5가길 16 515호 (신대방동, 아카데미타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQyIyQ1IyQwMCQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "천사온누리약국",
    "Address": "서울특별시 동작구 서달로 146 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ4MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "골드약국",
    "Address": "서울특별시 동작구 동작대로 89 504호 (사당동, 골든시네마타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "스마일약국",
    "Address": "서울특별시 동작구 장승배기로 110-1 (노량진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQxMyQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "신세명약국",
    "Address": "서울특별시 동작구 서달로 163 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "바다의별약국",
    "Address": "서울특별시 동작구 상도로 172 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "더블유약국",
    "Address": "서울특별시 동작구 양녕로 264 (상도1동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQxMyQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "윤경약국",
    "Address": "서울특별시 동작구 상도로 65 (대방동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "은하온누리약국",
    "Address": "서울특별시 동작구 사당로2가길 102 119호 (사당동, 사당자이아파트 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "행복한오늘이수약국",
    "Address": "서울특별시 동작구 사당로 308 (사당동, 화인빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "보생당약국",
    "Address": "서울특별시 동작구 서달로 150 108호 (흑석동, 이랜드해가든)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "유약국",
    "Address": "서울특별시 동작구 상도로50길 2-13 (상도1동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQxMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "중앙명성약국",
    "Address": "서울특별시 동작구 흑석로 106-7 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ2MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "대영약국",
    "Address": "서울특별시 동작구 만양로 26 215호 (상도동, 건영아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "강약국",
    "Address": "서울특별시 동작구 서달로 158 (흑석동, 명수대상가104호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "서보약국",
    "Address": "서울특별시 동작구 서달로8길 4 (흑석동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQxMyQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 동작구 상도로 148 (상도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "3층온누리약국",
    "Address": "서울특별시 마포구 월드컵북로 230 305호 (중동, 현대상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQxIyQwMCQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "우정옵티마약국",
    "Address": "서울특별시 마포구 백범로 4 1층 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "망원그랜드약국",
    "Address": "서울특별시 마포구 월드컵로 79 유용빌딩 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ4OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "성심약국",
    "Address": "서울특별시 마포구 독막로 266 105호 (대흥동, 태영아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "수정약국",
    "Address": "서울특별시 마포구 마포대로 63-8 삼창프라자빌딩 1층 104호 (도화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "합정파란문약국",
    "Address": "서울특별시 마포구 월드컵로1길 14 206호 (합정동, 마포 한강 푸르지오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "포도약국",
    "Address": "서울특별시 마포구 마포대로 44 진도빌딩 1층 (도화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQwMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "유명온누리약국",
    "Address": "서울특별시 마포구 만리재옛길 101-1 삼성래미안공덕2차 상가2동 102호 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "합정365약국",
    "Address": "서울특별시 마포구 독막로 14 1층 (합정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "셀약국",
    "Address": "서울특별시 마포구 양화로 72 1층 118호 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "우리 이 약국",
    "Address": "서울특별시 마포구 백범로 8 우정마샹스 오피스텔 비110호 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "대흥365약국",
    "Address": "서울특별시 마포구 백범로 98 1층 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "소담약국",
    "Address": "서울특별시 마포구 성암로 179 한샘상암 1층 (상암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQxIyQwMCQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "정약국",
    "Address": "서울특별시 마포구 마포대로 68 1층 112호 (도화동, 마포아크로타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQxMyQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "아현종로약국",
    "Address": "서울특별시 마포구 굴레방로9길 2 1층 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "나무약국",
    "Address": "서울특별시 마포구 백범로 202 101호 (신공덕동, 마포KCC웰츠타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ2MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "성은약국",
    "Address": "서울특별시 마포구 효창원로 255-1 1층 (공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ2MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "마리약국",
    "Address": "서울특별시 마포구 마포대로 109 2층 (공덕동, 롯데시티호텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ4MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜신마포약국",
    "Address": "서울특별시 마포구 창전로 45 103동 108호 (창전동, 서강한화오벨리스크 단지내 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "효성약국",
    "Address": "서울특별시 마포구 성미산로 91 1층 (성산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "대영약국",
    "Address": "서울특별시 마포구 모래내로7길 44 1층 (성산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "지선약국",
    "Address": "서울특별시 마포구 월드컵북로 185 1층 (성산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ3OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "최국희약국",
    "Address": "서울특별시 마포구 독막로 63 1층 (상수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "현정약국",
    "Address": "서울특별시 마포구 연희로 37 1층 (연남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQyIyQzIyQwMCQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "대흥온누리약국",
    "Address": "서울특별시 마포구 신촌로 160 106호 (대흥동, 이대역스타힐스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ5MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "연세한우리약국",
    "Address": "서울특별시 마포구 서강로 106 1층 (신수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ2MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "신영약국",
    "Address": "서울특별시 마포구 백범로 178 A203-1호 (공덕동, 마포신영지웰)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "신촌성은약국",
    "Address": "서울특별시 마포구 서강로 138 1층 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "해맑은약국",
    "Address": "서울특별시 마포구 마포대로 115-12 211호 (공덕동, 공덕삼성아파트 상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 마포구 독막로 2 2층 (합정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "2층하늘약국",
    "Address": "서울특별시 마포구 월드컵북로 230 201호 (중동, 현대상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "옵티마상원약국",
    "Address": "서울특별시 마포구 월드컵로 75 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "아이비약국",
    "Address": "서울특별시 마포구 만리재로 14 지하 1층 12호 (공덕동, 르네상스타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "수려한약국",
    "Address": "서울특별시 마포구 월드컵북로 137 1층 2호 (성산동, 씨에스타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "햇빛약국",
    "Address": "서울특별시 마포구 마포대로 68 408-2호 (도화동, 마포아크로타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ4MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "성산현대약국",
    "Address": "서울특별시 마포구 월드컵로 205 101호 (성산동, 성산임대아파트 상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQwMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "신유정약국",
    "Address": "서울특별시 마포구 마포대로 181-1 1층 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "유진온누리약국",
    "Address": "서울특별시 마포구 도화4길 73 104호 (도화동, 현대홈타운 상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 마포구 월드컵로13길 34 1층 (망원동, 두드림빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "평화약국",
    "Address": "서울특별시 마포구 양화로 64 서교제일빌딩 2층 202호 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "우대약국",
    "Address": "서울특별시 마포구 만리재로 27 1층 (신공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "구심당약국",
    "Address": "서울특별시 마포구 월드컵로25길 58 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQxMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 마포구 방울내로 70 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "선진약국",
    "Address": "서울특별시 마포구 독막로20길 53 1층 (창전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "보천약국",
    "Address": "서울특별시 마포구 신촌로 266-1 1층 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "미래팜약국",
    "Address": "서울특별시 마포구 양화로 166 지하1층 (동교동, 미래프라자빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "성산연세약국",
    "Address": "서울특별시 마포구 월드컵북로38길 14 408호 (중동, 오윤빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQyIyQ3IyQwMCQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "호산나약국",
    "Address": "서울특별시 마포구 창전로 60 1층 (구수동, 서강빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQxMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "정성약국",
    "Address": "서울특별시 마포구 만리재로 133 3층 (아현동, 계룡빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQzIyQwMCQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "신공덕약국",
    "Address": "서울특별시 마포구 백범로 212 2층 (신공덕동, 대우 월드마크마포)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "원이약국",
    "Address": "서울특별시 마포구 와우산로 94 제2기숙사 지하1층 B110호 (상수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 마포구 월드컵북로 347 1층 (상암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "희약국",
    "Address": "서울특별시 마포구 와우산로 93 1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "사랑이가득한약국",
    "Address": "서울특별시 마포구 월드컵북로 224 209호 (성산동, 청화상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQwMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 마포구 마포대로 190 1층 (공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 마포구 백범로 90 1층 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "신촌온누리약국",
    "Address": "서울특별시 마포구 백범로 24 1층 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "유림약국",
    "Address": "서울특별시 마포구 신촌로 120 1층 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQyIyQ3IyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜상암약국",
    "Address": "서울특별시 마포구 상암산로1길 73 103호 (상암동, 월드프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "상암올리브약국",
    "Address": "서울특별시 마포구 월드컵북로 402 케이지아이티센터 314호 (상암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQwMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "대교약국",
    "Address": "서울특별시 마포구 도화길 10 1층 (도화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "공덕오거리약국",
    "Address": "서울특별시 마포구 새창로 11 1층 (도화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "팰리스약국",
    "Address": "서울특별시 마포구 마포대로 143 220호 (공덕동, 마포공덕파크팰리스 II)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "신일약국",
    "Address": "서울특별시 마포구 손기정로 54 1층 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ3OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "용약국",
    "Address": "서울특별시 마포구 신촌로 102-1 1층 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "서교연세약국",
    "Address": "서울특별시 마포구 양화로 140 1층 (동교동, 남강빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 마포구 숭문길 221 1층 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQwMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "해오름약국",
    "Address": "서울특별시 마포구 대흥로 34 1층 (용강동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "망원우리약국",
    "Address": "서울특별시 마포구 망원로8길 55 구앤윤브릭하우스 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "스마일약국",
    "Address": "서울특별시 마포구 백범로37길 26 1층 (신공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQ3IyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "행복약국",
    "Address": "서울특별시 마포구 연희로 5 지하1층 (동교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "월드약국",
    "Address": "서울특별시 마포구 월드컵북로 502 월드컵파크 프라자 210호 (상암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "미소가득한약국",
    "Address": "서울특별시 마포구 월드컵북로 396 115호 (상암동, 누리꿈스퀘어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "상암월드약국",
    "Address": "서울특별시 마포구 월드컵로 240 2층 (성산동, 홈플러스월드컵점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQyIyQ1IyQwMCQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "샘터약국",
    "Address": "서울특별시 마포구 효창원로97길 10 1층 (공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "정아약국",
    "Address": "서울특별시 마포구 독막로 43 1층 (합정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "온누리약국",
    "Address": "서울특별시 마포구 월드컵북로 126 1층 (성산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "광명약국",
    "Address": "서울특별시 마포구 양화로 191 1층 (동교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "DMC하늘약국",
    "Address": "서울특별시 마포구 월드컵북로 361 302호 (상암동, DMC이안상암2단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQxMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 마포구 포은로 68 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "올리브약국",
    "Address": "서울특별시 마포구 신촌로 88 1층 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQxMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 마포구 대흥로 186-2 1층 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQyIyQ3IyQwMCQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "건우약국",
    "Address": "서울특별시 마포구 마포대로 205-1 1층 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 마포구 동교로 203 1층 (동교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ2MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "유한약국",
    "Address": "서울특별시 마포구 월드컵북로 236 1층 (중동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQxMyQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "홍대옵티마약국",
    "Address": "서울특별시 마포구 양화로 156 117호 (동교동, LG팰리스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "준약국",
    "Address": "서울특별시 마포구 월드컵북로 167 1층 (성산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 마포구 토정로 222 203호 (신수동, 한국출판협동조합)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "중원약국",
    "Address": "서울특별시 마포구 월드컵북로 190 1층 (성산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "즐거운약국",
    "Address": "서울특별시 마포구 큰우물로 53 염리동 106호 (염리동, 마포 네이버타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ4OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "피크약국",
    "Address": "서울특별시 마포구 양화로 61 두암빌딩 1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "그린이화약국",
    "Address": "서울특별시 마포구 양화로 133 B104-5호 (서교동, 서교타워빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "아크로약국",
    "Address": "서울특별시 마포구 마포대로 68 210-2호 (도화동, 마포아크로타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "신명약국",
    "Address": "서울특별시 마포구 신촌로 170 이대역푸르지오시티 상가106호 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQzIyQwMCQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "성산혜민약국",
    "Address": "서울특별시 마포구 월드컵북로 233 217호 (성산동, 성산시영아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ5OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "광실약국",
    "Address": "서울특별시 마포구 도화길 32 101호 (도화동, 삼성프라자상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ2MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "한유약국",
    "Address": "서울특별시 마포구 백범로 96 1층 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "광혜약국",
    "Address": "서울특별시 마포구 숭문길 32 1층 (염리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜덕인약국",
    "Address": "서울특별시 마포구 신촌로 232 1층 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "영진약국",
    "Address": "서울특별시 마포구 망원로8길 67 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ4OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "명성약국",
    "Address": "서울특별시 마포구 월드컵로 87 103호 (망원동, 마포로얄프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQyIyQ3IyQwMCQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "연세약국",
    "Address": "서울특별시 마포구 성미산로10길 44 1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "환도약국",
    "Address": "서울특별시 마포구 방울내로 41 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQxIyQwMCQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "이화바이오약국",
    "Address": "서울특별시 마포구 양화로 156 LG팰리스빌딩 306-1호 (동교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "소나무약국",
    "Address": "서울특별시 마포구 월드컵북로 402 케이지아이티센터 102호 (상암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "하임온누리약국",
    "Address": "서울특별시 마포구 도화길 43 108호 (도화동, 나눔빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "마포웰츠약국",
    "Address": "서울특별시 마포구 백범로 202 201호 (신공덕동, 마포KCC웰츠타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQyIyQxIyQwMCQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "이층약국",
    "Address": "서울특별시 마포구 마포대로 143 210호 (공덕동, 마포공덕파크팰리스II)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "메디칼세영약국",
    "Address": "서울특별시 마포구 월드컵로 159 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "호정약국",
    "Address": "서울특별시 마포구 효창원로 243 1층 (공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "바다약국",
    "Address": "서울특별시 마포구 월드컵북로 69 1층 (성산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "연세참사랑약국",
    "Address": "서울특별시 마포구 서강로 110 1층 (신수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQ3IyQwMCQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "이화메세나약국",
    "Address": "서울특별시 마포구 양화로 45 B105호 (서교동, 메세나폴리스몰)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "코끼리약국",
    "Address": "서울특별시 마포구 백범로 91 1층 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "동경약국",
    "Address": "서울특별시 마포구 신촌로16길 4 1층 101호 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "코코약국",
    "Address": "서울특별시 마포구 망원로 74-1 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "맘스케어약국",
    "Address": "서울특별시 마포구 마포대로 201 (아현동, 마포트라팰리스2차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ5MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "제민약국",
    "Address": "서울특별시 마포구 삼개로 24 101호 (도화동, 용현빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "성모약국",
    "Address": "서울특별시 마포구 백범로 127 1층 (염리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQyIyQ1IyQwMCQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "라이프약국",
    "Address": "서울특별시 마포구 신촌로 190 1층 (염리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 마포구 월드컵로 151 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ2MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "파마트엘지약국",
    "Address": "서울특별시 마포구 양화로 156 116호 (동교동, LG팰리스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "참사랑이화약국",
    "Address": "서울특별시 마포구 연남로 42 상가B동 117호 (연남동, 코오롱하늘채아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQyIyQzIyQwMCQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 마포구 월드컵로14길 5 1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "토정약국",
    "Address": "서울특별시 마포구 토정로32길 13 105호 (토정동, 삼성상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQxMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "망원동약국",
    "Address": "서울특별시 마포구 망원로 69 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ5MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "세명약국",
    "Address": "서울특별시 마포구 마포대로 127 214호 (공덕동, 풍림VIP텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ4OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "독일약국",
    "Address": "서울특별시 마포구 도화4길 19 1층 (도화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "신촌세민약국",
    "Address": "서울특별시 마포구 신촌로 78 1층 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQyIyQ5IyQwMCQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "애오개약국",
    "Address": "서울특별시 마포구 마포대로 204 103호 (아현동, 마포에스케이허브)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "원약국",
    "Address": "서울특별시 마포구 월드컵북로 396 B1070호 (상암동, 누리꿈스퀘어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ1IyQwMCQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "오즈약국",
    "Address": "서울특별시 마포구 토정로31길 24 상가동 B117호 (용강동, e편한세상마포3차아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ2MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 마포구 신촌로 270 308호 (아현동, 수창빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQyIyQ3IyQwMCQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 마포구 신촌로 170 2층 상가 311호 (대흥동, 이대역푸르지오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ3OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "프라자약국",
    "Address": "서울특별시 마포구 신촌로 238 1층 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 마포구 마포대로 68 608호 (도화동, 마포아크로타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "더행복한약국",
    "Address": "서울특별시 마포구 토정로37길 46 지하1층 10,16호 (도화동, 정우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "사랑의약국",
    "Address": "서울특별시 마포구 독막로 10 3층 (합정동, 성지빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "delight이화약국",
    "Address": "서울특별시 마포구 월드컵로3길 14 220호 (합정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "청춘약국",
    "Address": "서울특별시 마포구 마포대로 25 103호 (마포동, 신한디엠빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQxIyQwMCQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "미약국",
    "Address": "서울특별시 마포구 신촌로 174 102호 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ2MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 마포구 마포대로 156 공덕푸르지오시티 121호 (공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 마포구 월드컵북로 396 B1010호 (상암동, 누리꿈스퀘어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "매일여는약국",
    "Address": "서울특별시 마포구 월드컵북로 396 누리꿈스퀘어 B1094호 (상암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "더블유스토어연세약국",
    "Address": "서울특별시 마포구 신촌로 92 1층 (노고산동, 카리스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQwMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "홍익약국",
    "Address": "서울특별시 마포구 양화로 136 지하1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "온누리미소약국",
    "Address": "서울특별시 마포구 월드컵로 29 지하2층 (합정동, JH빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "근화사약국",
    "Address": "서울특별시 마포구 만리재옛길 1 1층 (공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ4MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "예진약국",
    "Address": "서울특별시 마포구 월드컵북로 402 321호 (상암동, KGIT센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 마포구 와우산로 149 1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQxMyQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "대지약국",
    "Address": "서울특별시 마포구 포은로 87 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 마포구 백범로 202 1층 102호 (신공덕동, 마포케이씨씨웰츠타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "홍대참신한약국",
    "Address": "서울특별시 마포구 어울마당로 62 1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ1IyQwMCQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "연남약국",
    "Address": "서울특별시 마포구 양화로21길 31 1층 (동교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "약초원약국",
    "Address": "서울특별시 마포구 동교로9길 28 지1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "합정동산약국",
    "Address": "서울특별시 마포구 양화로 45 C-17호 (서교동, 홈플러스합정점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ5OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "한우리약국",
    "Address": "서울특별시 마포구 망원로 73 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ5MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 마포구 숭문길 215 1층 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "명치약국",
    "Address": "서울특별시 마포구 임정로15길 13 1층 (신공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "메디컬 성모약국",
    "Address": "서울특별시 마포구 월드컵로 73 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQxMyQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "기쁨약국",
    "Address": "서울특별시 마포구 월드컵로 82 1층 (서교동, 소단빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQxMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "성지약국",
    "Address": "서울특별시 마포구 동교로 181 1층 (동교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 마포구 망원로 78 1층 (망원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "종오약국",
    "Address": "서울특별시 마포구 만리재로 130 1층 (공덕동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQwMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "인혜약국",
    "Address": "서울특별시 마포구 만리재로 15 310,311호 (공덕동, 제일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQwMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "참조은약국",
    "Address": "서울특별시 마포구 마포대로 92 1층 (도화동, 효성 해링턴 스퀘어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 마포구 홍익로 1 1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQyIyQxIyQwMCQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "강원약국",
    "Address": "서울특별시 마포구 월드컵북로 25 지하1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 마포구 신촌로 16 1층 (동교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "마래푸약국",
    "Address": "서울특별시 마포구 신촌로34길 37 1층 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQwMyQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 마포구 월드컵북로 361 102호 (상암동, 디엠씨이안 상암2단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "인화약국",
    "Address": "서울특별시 마포구 토정로 219 (신수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "연세프라자약국",
    "Address": "서울특별시 마포구 서강로 97 1층 (창전동, 삼성아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "삼성메디칼약국",
    "Address": "서울특별시 마포구 도화길 32 220호, 221호 (도화동, 삼성프라자상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ3MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "르호봇약국",
    "Address": "서울특별시 마포구 서강로 133 4층 (노고산동, 병우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "허브약국",
    "Address": "서울특별시 마포구 마포대로 73 104호 (도화동, SK허브그린)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ5MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "안생약국",
    "Address": "서울특별시 마포구 와우산로 22 1층 (상수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQyIyQ1IyQwMCQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "상수약국",
    "Address": "서울특별시 마포구 큰우물로 75 1층 4호 (도화동, 성지빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQyIyQzIyQwMCQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "아름다운약국",
    "Address": "서울특별시 마포구 마포대로24길 56 1층 (아현동, 보령빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "이지약국",
    "Address": "서울특별시 마포구 양화로 152 1층 (동교동, 대화빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "청심약국",
    "Address": "서울특별시 마포구 희우정로 42-9 101호 (합정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "홍대365약국",
    "Address": "서울특별시 마포구 와우산로27길 43 1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "자연약국",
    "Address": "서울특별시 마포구 마포대로 195 4단지상가동 205호 (아현동, 마포래미안푸르지오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "이화키즈팜약국",
    "Address": "서울특별시 마포구 마포대로 195 4단지상가동 219호 (아현동, 마포래미안푸르지오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ2MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "비온뒤숲속약국",
    "Address": "서울특별시 마포구 월드컵로 111 104,105호 (망원동, 풍성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "대흥약국",
    "Address": "서울특별시 마포구 대흥로 192-1 1층 (대흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQxMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "참마음약국",
    "Address": "서울특별시 마포구 양화로 73 101호 (서교동, 체리스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "아카데미약국",
    "Address": "서울특별시 마포구 마포대로 52 205호, 206호 (도화동, 고려아카데미텔 II)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "천사약국",
    "Address": "서울특별시 마포구 양화로 48 1층 (합정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "이대5번출구 옵티마 진룡약국",
    "Address": "서울특별시 마포구 대흥로30길 15 1층 (염리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 마포구 양화로 165 상진빌딩 지하1층 (동교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "신촌서울약국",
    "Address": "서울특별시 마포구 신촌로 68 3층 (노고산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "성산진약국",
    "Address": "서울특별시 마포구 월드컵북로38길 14 301호 (중동, 오윤빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 마포구 마포대로24길 4 공덕자이아파트 상가 상가1동 105호 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "도원약국",
    "Address": "서울특별시 마포구 마포대로 52 고려아카데미텔Ⅱ 1층 105호 (도화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "마포보건약국",
    "Address": "서울특별시 마포구 월드컵로 204 이안상암 105호 (성산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "일층약국",
    "Address": "서울특별시 마포구 신촌로 266 1층 (아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "합정녹십자약국",
    "Address": "서울특별시 마포구 독막로 22 청명빌딩 1층 (합정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 마포구 월드컵로 126 1층 (성산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "일출약국",
    "Address": "서울특별시 마포구 독막로 85 1층 (상수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "홍대수약국",
    "Address": "서울특별시 마포구 홍익로3길 11 1층 (서교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "안녕약국",
    "Address": "서울특별시 마포구 월드컵북로54길 25 상암DMC푸르지오시티, S-City 오피스텔동 111호 (상암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "대형약국",
    "Address": "서울특별시 서대문구 북아현로 4 (북아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "영신약국",
    "Address": "서울특별시 서대문구 거북골로14길 32 103호 (북가좌동, DMC아이파크아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "한미약국",
    "Address": "서울특별시 서대문구 수색로 30 지하1층, 1층 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "윤약국",
    "Address": "서울특별시 서대문구 수색로2길 16-1 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "행복가득약국",
    "Address": "서울특별시 서대문구 신촌로 73 1층 (창천동, 거화빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "가까운신촌약국",
    "Address": "서울특별시 서대문구 연세로 40 1~4층 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "우리온누리약국",
    "Address": "서울특별시 서대문구 통일로 87 NH농협생명빌딩 지하1층 (미근동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "새우리온누리약국",
    "Address": "서울특별시 서대문구 통일로 449 1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "은행약국",
    "Address": "서울특별시 서대문구 통일로 455 경인주유소 1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "홍제 오늘약국",
    "Address": "서울특별시 서대문구 통일로 460 2층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ2MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "새서울DMC약국",
    "Address": "서울특별시 서대문구 수색로 56 성공타워1 407호 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "제인약국",
    "Address": "서울특별시 서대문구 통일로 442-3 (홍제동, 1층, 2층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ5OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "백세당약국",
    "Address": "서울특별시 서대문구 응암로 54 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQyIyQ5IyQwMCQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "푸름약국",
    "Address": "서울특별시 서대문구 연희로 122 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "조이약국",
    "Address": "서울특별시 서대문구 통일로 464 4층 (홍제동, 홍제빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ2MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "제중원약국",
    "Address": "서울특별시 서대문구 모래내로 352-3 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ5MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 서대문구 증가로 122 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQwMyQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "새현대약국",
    "Address": "서울특별시 서대문구 홍은중앙로 73 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "보명약국",
    "Address": "서울특별시 서대문구 거북골로 120 206동 2-12호 (남가좌동, 가재울 센트레빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "예원약국",
    "Address": "서울특별시 서대문구 독립문로14길 3 102호 (냉천동, 돈의문센트레빌상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "서린약국",
    "Address": "서울특별시 서대문구 증가로 123 A동 101호 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "독수리약국",
    "Address": "서울특별시 서대문구 연세로 36 독수리빌딩 1층, 2층 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ2MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "명문약국",
    "Address": "서울특별시 서대문구 연희로36길 10 1층 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 서대문구 성산로 492 1층 (대신동, 동관)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "대유약국",
    "Address": "서울특별시 서대문구 모래내로 359 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQyIyQ3IyQwMCQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "굴레방약국",
    "Address": "서울특별시 서대문구 신촌로35길 10 1층 114호 (북아현동, e편한세상신촌4단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQzIyQxMyQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "백제약국",
    "Address": "서울특별시 서대문구 홍은중앙로 98 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "평화약국",
    "Address": "서울특별시 서대문구 증가로 226 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQxMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "일신당약국",
    "Address": "서울특별시 서대문구 신촌로 9 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ2MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "대우약국",
    "Address": "서울특별시 서대문구 통일로40안길 3-1 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "새롬m약국",
    "Address": "서울특별시 서대문구 증가로 85 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQwMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "성우당약국",
    "Address": "서울특별시 서대문구 연희로 114 지층 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "모범약국",
    "Address": "서울특별시 서대문구 증가로 129 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQyIyQ1IyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "영한약국",
    "Address": "서울특별시 서대문구 충정로 71 (충정로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "신보건약국",
    "Address": "서울특별시 서대문구 연세로5길 32 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ5OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "한빛약국",
    "Address": "서울특별시 서대문구 세검정로1길 93 109호 (홍은동, 벽산아파트A상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "부활약국",
    "Address": "서울특별시 서대문구 통일로 189-1 (영천동, 동성건물)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQxMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "동현약국",
    "Address": "서울특별시 서대문구 영천시장길 16 (영천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 서대문구 수색로 48 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 서대문구 연세로 41 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "한사랑온누리약국",
    "Address": "서울특별시 서대문구 신촌로 183 지하1층 (대현동, 유인빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 서대문구 거북골로14길 32 304호 (북가좌동, 가재울아이파크상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "한신약국",
    "Address": "서울특별시 서대문구 통일로 397 B419,420호 (홍제동, 인왕산 한신휴플러스 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "사러가약국",
    "Address": "서울특별시 서대문구 연희맛로 23 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ5OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "은하약국",
    "Address": "서울특별시 서대문구 통일로 463 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "가재울온누리약국",
    "Address": "서울특별시 서대문구 거북골로 120 3동 3-1호 (남가좌동, 가재울센트레빌아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "청솔약국",
    "Address": "서울특별시 서대문구 서소문로 21 지하1층 101호 (충정로3가, 충정타워빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQxMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "기린약국",
    "Address": "서울특별시 서대문구 통일로 468 1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "혜성약국",
    "Address": "서울특별시 서대문구 증가로20가길 89 1층 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "새온약국",
    "Address": "서울특별시 서대문구 충정로 70 웨스트게이트타워 2층 (미근동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "북가좌수약국",
    "Address": "서울특별시 서대문구 응암로 60 경원빌딩 1층 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "도담약국",
    "Address": "서울특별시 서대문구 신촌로35길 10 상가동 2층 206호 (북아현동, e편한세상신촌 4단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "이화사랑약국",
    "Address": "서울특별시 서대문구 수색로 56 3층 309-1호 (북가좌동, 성공타워1)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 서대문구 수색로 100 101동 104호 (북가좌동, DMC래미안e편한세상)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQxMyQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "서대문약국",
    "Address": "서울특별시 서대문구 통일로 177 1층 (옥천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ3MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "유진온누리약국",
    "Address": "서울특별시 서대문구 연희로 85 105호 (연희동, 인사이드빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQyIyQ5IyQwMCQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 서대문구 연세로 36 (창천동, 독수리빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "무악메디칼약국",
    "Address": "서울특별시 서대문구 연희로 407 연희8빌딩 1층 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ2MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "클로버약국",
    "Address": "서울특별시 서대문구 연희로 117 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "연희약국",
    "Address": "서울특별시 서대문구 성산로 317 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ2MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "새서울약국",
    "Address": "서울특별시 서대문구 통일로 441 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ2MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "모래내백화점약국",
    "Address": "서울특별시 서대문구 수색로 38 1층 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ2MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "가좌진약국",
    "Address": "서울특별시 서대문구 모래내로 137 1층 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQxMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "소문난약국",
    "Address": "서울특별시 서대문구 세검정로1길 26-1 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "화인온누리약국",
    "Address": "서울특별시 서대문구 통일로 413 205호 (홍제동, 화인홍제빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ5OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "인왕약국",
    "Address": "서울특별시 서대문구 인왕시장길 18 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQyIyQ1IyQwMCQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "활명당약국",
    "Address": "서울특별시 서대문구 통일로 145-1 (냉천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 서대문구 통일로 402-1 1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "행복한 참약국",
    "Address": "서울특별시 서대문구 수색로 100 4단지 상가1동 1-13호 (북가좌동, DMC래미안e편한세상)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "약손약국",
    "Address": "서울특별시 서대문구 연희로 409 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ3OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "온누리선약국",
    "Address": "서울특별시 서대문구 통일로 131 4층 2호 (충정로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQxMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "세이지약국",
    "Address": "서울특별시 서대문구 이화여대길 52 지하4층 404호 (대현동, 이화여자대학교 ECC)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "바다약국",
    "Address": "서울특별시 서대문구 통일로 205-1 1층 (영천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "세빛약국",
    "Address": "서울특별시 서대문구 응암로 64 1층 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "연희위드팜약국",
    "Address": "서울특별시 서대문구 성산로 521 (대신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "홍제태양약국",
    "Address": "서울특별시 서대문구 통일로 450 1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "모래내약국",
    "Address": "서울특별시 서대문구 수색로 34 1층 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "행운약국",
    "Address": "서울특별시 서대문구 증가로 138 남가좌프라자 1층 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQwMyQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "파크약국",
    "Address": "서울특별시 서대문구 증가로 150 DMC2차아이파크상가 B205호 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQyIyQ3IyQwMCQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 서대문구 수색로 26 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQxMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "위드팜신촌약국",
    "Address": "서울특별시 서대문구 성산로 486 (대신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQyIyQ1IyQwMCQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "꿈이있는약국",
    "Address": "서울특별시 서대문구  통일로 185-1 (영천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "알파약국",
    "Address": "서울특별시 서대문구 통일로 448 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "우리마을홍제약국",
    "Address": "서울특별시 서대문구 통일로 440 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "홍연약국",
    "Address": "서울특별시 서대문구 홍연길 87 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 서대문구 거북골로 67 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "삼성약국",
    "Address": "서울특별시 서대문구 연희맛로 28 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "홍은약국",
    "Address": "서울특별시 서대문구 가좌로 65 1층 102호 (홍은동, 서강주상복합아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ5MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "솔약국",
    "Address": "서울특별시 서대문구 수색로 32 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "엘리트약국",
    "Address": "서울특별시 서대문구 신촌로 99 5층 (창천동, 엘리트빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ2MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "홍인약국",
    "Address": "서울특별시 서대문구 통일로34길 48 216호 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜 보건약국",
    "Address": "서울특별시 서대문구 통일로 435 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ2MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "명신당약국",
    "Address": "서울특별시 서대문구 홍제천로 14 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 서대문구 수색로 100 3-7-1호 (북가좌동, DMC래미안e편한세상 단지내상가 1BL)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "창일약국",
    "Address": "서울특별시 서대문구 인왕시장길 12 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "세원약국",
    "Address": "서울특별시 서대문구 모래내로15길 48 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQxMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "서울솔약국",
    "Address": "서울특별시 서대문구 통일로 452 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "가까운약국",
    "Address": "서울특별시 서대문구 모래내로 364 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQxMyQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "명약국",
    "Address": "서울특별시 서대문구 신촌로 109 신촌르메이에르타운5 1층 111-2호 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "솔벗약국",
    "Address": "서울특별시 서대문구 세검정로 72 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ5OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "정도약국",
    "Address": "서울특별시 서대문구 북아현로 6 (북아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQwMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 서대문구 세무서길 12 1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQyIyQ3IyQwMCQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "세란약국",
    "Address": "서울특별시 서대문구 연세로 39 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "홈케어하나약국",
    "Address": "서울특별시 서대문구 통일로39가길 10-2 1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "이층약국",
    "Address": "서울특별시 서대문구 홍은중앙로3길 9 203호 (홍은동, 북한산 두산 위브)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "강약국",
    "Address": "서울특별시 서대문구 세검정로1길 7 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ2MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "참진온누리약국",
    "Address": "서울특별시 서대문구 북아현로 52 (북아현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQxMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "용한약국",
    "Address": "서울특별시 서대문구 거북골로 154 111호 (북가좌동, 삼호상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ4MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "은혜온누리약국",
    "Address": "서울특별시 서대문구 수색로 56 125호 (북가좌동, 성공타워1)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQxMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "이대행복한 약국",
    "Address": "서울특별시 서대문구 이화여대길 33 (대현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQwMyQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "구룡약국",
    "Address": "서울특별시 서대문구 세무서길 78 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ4OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "8번가위드팜약국",
    "Address": "서울특별시 서대문구 성산로 515 석란 1층 (대신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "레몬약국",
    "Address": "서울특별시 서대문구 통일로 510 상가동 지2층 107호 (홍은동, 북한산 더샵)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQwMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "이인치한약국",
    "Address": "서울특별시 서대문구 이화여대길 63 3층 (대현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "명음약국",
    "Address": "서울특별시 서대문구 신촌로35길 10 117호 (북아현동, e편한세상신촌 4단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQyIyQ1IyQwMCQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "광혜약국",
    "Address": "서울특별시 서대문구 성산로17길 5 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "효제약국",
    "Address": "서울특별시 서대문구 세검정로 32 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "초원약국",
    "Address": "서울특별시 서대문구 이화여대8길 62 107, 108호 (북아현동, 두산아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 서대문구 연희로 262-29 1층 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 서대문구 통일로 433 조이빌딩 지하1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQxIyQwMCQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "신촌대로 약국",
    "Address": "서울특별시 서대문구 신촌로 121 아남오피스텔 1층 103호 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "소생약국",
    "Address": "서울특별시 서대문구 응암로 81 1층 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 서대문구 가재울로6길 53-61 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "진성약국",
    "Address": "서울특별시 서대문구 증가로 247 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQwMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "완약국",
    "Address": "서울특별시 서대문구 세검정로1길 115 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "은하약국",
    "Address": "서울특별시 서대문구 명지대3길 1 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "나라약국",
    "Address": "서울특별시 서대문구 가재울미래로 2 별동상가 102호 (남가좌동, DMC파크뷰자이)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQyIyQ1IyQwMCQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "대학온누리약국",
    "Address": "서울특별시 서대문구 홍은중앙로 100-1 (홍은동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQyIyQ1IyQwMCQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "세연약국",
    "Address": "서울특별시 서대문구 연세로 50 1층 (신촌동, 연대동문회관)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "에버그린약국",
    "Address": "서울특별시 서대문구 신촌역로 7 신촌푸르지오시티 103호 (대현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "해그린약국",
    "Address": "서울특별시 서대문구 통일로 356 1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQxMyQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "북가좌온누리에약국",
    "Address": "서울특별시 서대문구 증가로 241 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 서대문구 연세로11길 4 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "연희종로약국",
    "Address": "서울특별시 서대문구 연희로 109 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 서대문구 연희로 94 (연희동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "아현파란문약국",
    "Address": "서울특별시 서대문구 신촌로35길 10 지하1층 B417호 (북아현동, e편한세상신촌4단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQxMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "일심약국",
    "Address": "서울특별시 서대문구 연세로 42 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "거북당약국",
    "Address": "서울특별시 서대문구 응암로 53 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "현우약국",
    "Address": "서울특별시 서대문구 연세로 29-1 1층 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "소명약국",
    "Address": "서울특별시 서대문구 모래내로15길 68 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ5OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "필온누리약국",
    "Address": "서울특별시 서대문구 신촌로 89 (창천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "연세메디칼약국",
    "Address": "서울특별시 서대문구 응암로 100 (북가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQyIyQ1IyQwMCQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "혜민약국",
    "Address": "서울특별시 서대문구 통일로34길 35 2층 219, 230호 (홍제동, 현대종합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ5OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "훈민약국",
    "Address": "서울특별시 서대문구 통일로 107 (미근동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 서대문구 통일로 464 3층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQwMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "오약국",
    "Address": "서울특별시 서대문구 거북골로 120 206동 지하2층 상가2-4호 (남가좌동, 동부센트레빌아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "푸른온누리약국",
    "Address": "서울특별시 서대문구 문화촌길 6 승희빌딩 1층 (홍제동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQ1IyQwMCQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 서대문구 통일로 413 6층 604호 (홍제동, 연세스포츠센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 서대문구 증가로 98 1층 (남가좌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "새서독약국",
    "Address": "서울특별시 성동구 행당로 129 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "성수햇살약국",
    "Address": "서울특별시 성동구 아차산로 120 베델 플레이스 3층 302호 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 성동구 고산자로 255 (도선동,K타워 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "스타빌약국",
    "Address": "서울특별시 성동구 왕십리로 309 3층 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "명동온누리약국",
    "Address": "서울특별시 성동구 고산자로 164 107호 (행당동, 행당한신아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ2MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "어울림이층약국",
    "Address": "서울특별시 성동구 독서당로40길 39 2층 (옥수동, 옥수 어울림)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "약사랑옵티마약국",
    "Address": "서울특별시 성동구 난계로 35 (금호동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "태화약국",
    "Address": "서울특별시 성동구 아차산로7길 2 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "정민약국",
    "Address": "서울특별시 성동구 용답중앙3나길 24 (용답동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 성동구 독서당로 378 (응봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "왕십리약국",
    "Address": "서울특별시 성동구 무학봉길 92 (하왕십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜대림약국",
    "Address": "서울특별시 성동구 행당로 87 331호 (행당동, 대림리빙프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "용하약국",
    "Address": "서울특별시 성동구 용답중앙27길 6 1층 (용답동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "은하약국",
    "Address": "서울특별시 성동구 장터길 32-1 (금호동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 성동구 마장로 300 (마장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQwMyQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "스마일온누리약국",
    "Address": "서울특별시 성동구 뚝섬로 377 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ2MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "정은약국",
    "Address": "서울특별시 성동구 장터길 34 1층 (금호동4가, 남지빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "어울림온누리약국",
    "Address": "서울특별시 성동구 한림말1길 16 1층 (옥수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "맑은샘약국",
    "Address": "서울특별시 성동구 금호로 117 상가동 지2층 28-1호 (금호동2가, 금호자이1차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ2MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "수지약국",
    "Address": "서울특별시 성동구 마장로 289 3층 (마장동, 엠디빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "염광약국",
    "Address": "서울특별시 성동구 아차산로 116 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ3MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜보배약국",
    "Address": "서울특별시 성동구 아차산로7길 19 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQyIyQzIyQwMCQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "국제약국",
    "Address": "서울특별시 성동구 독서당로 288-1 (금호동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "성모약국",
    "Address": "서울특별시 성동구 뚝섬로 388 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "신성림약국",
    "Address": "서울특별시 성동구 마조로 24 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQyIyQxIyQwMCQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "한양약국",
    "Address": "서울특별시 성동구 마조로 17 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQyIyQzIyQwMCQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "세심약국",
    "Address": "서울특별시 성동구 마장로35길 76 1층 (마장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ3MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 성동구 독서당로 218 (옥수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQyIyQ3IyQwMCQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "동틀약국",
    "Address": "서울특별시 성동구 동일로 135 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 성동구 왕십리로 236-1 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "제민약국",
    "Address": "서울특별시 성동구 성덕정길 137 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "상도약국",
    "Address": "서울특별시 성동구 왕십리로21길 19 행당시장 1층 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "21세기메디칼약국",
    "Address": "서울특별시 성동구 무수막길 97 (금호동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "상보약국",
    "Address": "서울특별시 성동구 동일로 83 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "신라약국",
    "Address": "서울특별시 성동구 광나루로11길 26-1 (송정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "예전약국",
    "Address": "서울특별시 성동구 왕십리로20길 34 (홍익동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "성수메디칼약국",
    "Address": "서울특별시 성동구 아차산로 113 삼진빌딩 3층 302호 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQxMyQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "새왕약국",
    "Address": "서울특별시 성동구 광나루로 325 (송정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ2MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "진로약국",
    "Address": "서울특별시 성동구 성덕정길 106 (성수동2가,승재빌딩 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "유연약국",
    "Address": "서울특별시 성동구 왕십리로 410 상가 L동 3층 318호 (하왕십리동, 센트라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ5MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "미소진약국",
    "Address": "서울특별시 성동구 장터길 19 (금호동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQwMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 성동구 고산자로 234 402호 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "민제약국",
    "Address": "서울특별시 성동구 마장로35길 76 304호 (마장동, 현대아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ2MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "정성약국",
    "Address": "서울특별시 성동구 마장로 209 (홍익동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQxMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "평안약국",
    "Address": "서울특별시 성동구 고산자로6길 40 117호 (행당동, 레몬프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ4OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "중앙종로약국",
    "Address": "서울특별시 성동구 용답중앙15길 1 (용답동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "공중약국",
    "Address": "서울특별시 성동구 성덕정길 105 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ5MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "성산약국",
    "Address": "서울특별시 성동구 고산자로 234 7층 (행당동, 나래타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQxMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 성동구 사근동길 4 1층 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "뚝섬스타약국",
    "Address": "서울특별시 성동구 아차산로 42 지하1층 (성수동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQyIyQzIyQwMCQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "시대약국",
    "Address": "서울특별시 성동구 마장로 321 (마장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ2MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "영화당약국",
    "Address": "서울특별시 성동구 사근동길 53 (사근동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "건국약국",
    "Address": "서울특별시 성동구 아차산로 92 광명타워 1층 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "자이팜약국",
    "Address": "서울특별시 성동구 고산자로2길 67 서울숲리버뷰자이(상가1동) 상가동 2층 1203호 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "옥수온누리약국",
    "Address": "서울특별시 성동구 매봉길 48 106호 (옥수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "삼성약국",
    "Address": "서울특별시 성동구 성덕정17길 1 1층 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 성동구 왕십리로 410 D동 비103호 (하왕십리동, 센트라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ3MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "백두산약국",
    "Address": "서울특별시 성동구 서울숲2길 47 (성수동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "미소어울림약국",
    "Address": "서울특별시 성동구 독서당로40길 39 옥수 어울림 211호 (옥수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "이레약국",
    "Address": "서울특별시 성동구 성덕정길 78 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 성동구 독서당로 303-2 1층 (금호동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "새희망약국",
    "Address": "서울특별시 성동구 천호대로 308 2층 (용답동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 성동구 아차산로 41 (성수동1가,삼성빌딩 지하1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQxMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "자연온누리약국",
    "Address": "서울특별시 성동구 뚝섬로 400 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "종로약국",
    "Address": "서울특별시 성동구 사근동길 2 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "신수정약국",
    "Address": "서울특별시 성동구 성덕정길 149 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "보명약국",
    "Address": "서울특별시 성동구 독서당로 280-7 (금호동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "하이온누리약국",
    "Address": "서울특별시 성동구 행당로 87 107호 (행당동, 행당동 대림아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQwMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "기린약국",
    "Address": "서울특별시 성동구 독서당로 175 (옥수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜호정약국",
    "Address": "서울특별시 성동구 성수일로 39 (성수동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "옥수대한약국",
    "Address": "서울특별시 성동구 독서당로 223 래미안 옥수 리버젠 상가 지하 209호 (옥수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "유명한약국",
    "Address": "서울특별시 성동구 독서당로 295 1층 (금호동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 성동구 왕십리로 410 G동 204호 (하왕십리동, 센트라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQwMyQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "허브약국",
    "Address": "서울특별시 성동구 금호로 158-2 지1층 (금호동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQwMyQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 성동구 왕십리로 271-1 1층 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ2MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "신동광약국",
    "Address": "서울특별시 성동구 무수막길 82 (금호동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQwMyQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "메디팜푸른약국",
    "Address": "서울특별시 성동구 무학로 33 104호 (하왕십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "행운약국",
    "Address": "서울특별시 성동구 왕십리로 381 1층 (하왕십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "지안약국",
    "Address": "서울특별시 성동구 왕십리광장로 17 왕십리민자역사 4층 OV3-1호 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ2MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "비트플렉스약국",
    "Address": "서울특별시 성동구 왕십리광장로 17 (행당동, 비트플랙스내 2층 A05,06)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "선영약국",
    "Address": "서울특별시 성동구 마장로 187 (홍익동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQxMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "신금호약국",
    "Address": "서울특별시 성동구 행당로 1 1층 (금호동1가, 로타리빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신동아약국",
    "Address": "서울특별시 성동구 왕십리로 92 (성수동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "우당약국",
    "Address": "서울특별시 성동구 연무장7길 6 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 성동구 왕십리로 315 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "혜민약국",
    "Address": "서울특별시 성동구 마조로 30 1층 (행당동, 미진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "후문약국",
    "Address": "서울특별시 성동구 마조로 22-3 1층 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "실로암약국",
    "Address": "서울특별시 성동구 용답중앙15길 11 (용답동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "방초한약국",
    "Address": "서울특별시 성동구 난계로 114-31 2층 (하왕십리동, 금호베스트빌 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "대풍약국",
    "Address": "서울특별시 성동구 사근동길 6 (행당동, 한양제일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "이수프라자약국",
    "Address": "서울특별시 성동구 왕십리로 309 101호 (행당동, 이수이스타빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ2MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "옥수벽산약국",
    "Address": "서울특별시 성동구 한림말길 56 1층 (옥수동, 벽산빌라트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQwMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "화생약국",
    "Address": "서울특별시 성동구 행당로 1 (금호동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQyIyQzIyQwMCQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "대중약국",
    "Address": "서울특별시 성동구 왕십리로 379 (하왕십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "해오름약국",
    "Address": "서울특별시 성동구 독서당로 220 102호 (옥수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQwMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "메디팜한솔약국",
    "Address": "서울특별시 성동구 행당로 84 132호 (행당동, 행당한진타운종합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "부원약국",
    "Address": "서울특별시 성동구 성덕정길 80 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "성수종로약국",
    "Address": "서울특별시 성동구 아차산로7길 21 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "건강한약국",
    "Address": "서울특별시 성동구 왕십리로 320-1 1층 (도선동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "성동온누리약국",
    "Address": "서울특별시 성동구 난계로 36 1층 (금호동1가, 제일의원)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQxMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "왕약국",
    "Address": "서울특별시 성동구 광나루로 323 (송정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQwMyQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "수명약국",
    "Address": "서울특별시 성동구 왕십리로 94-2 1층 (성수동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ5MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "보람약국",
    "Address": "서울특별시 성동구 한림말길 50 106호 (옥수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ4OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 성동구 자동차시장1길 85 (용답동,1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ4MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "이화한솔약국",
    "Address": "서울특별시 성동구 고산자로 342 (마장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 성동구 무학로 33 206호 (하왕십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "연세우리약국",
    "Address": "서울특별시 성동구 왕십리로 296-1 조흥은행 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "153온누리약국",
    "Address": "서울특별시 성동구 왕십리로 410 K동 106호 (하왕십리동, 센트라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 성동구 독서당로 384 중앙노인정 102호 (응봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "수정약국",
    "Address": "서울특별시 성동구 독서당로 300 (금호동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQyIyQ5IyQwMCQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "행복이열리는건강약국",
    "Address": "서울특별시 성동구 성수이로 113 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "한샘약국",
    "Address": "서울특별시 성동구 무학로2길 7 1층 102호 (도선동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 성동구 성덕정길 34 (성수동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "대한약국",
    "Address": "서울특별시 성동구 동호로 100 511호 (금호동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ4MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "선약국",
    "Address": "서울특별시 성동구 아차산로7길 7 1층 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ2MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "도담약국",
    "Address": "서울특별시 성동구 왕십리로 410 상가L동 221-1, 222호 (하왕십리동, 센트라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "서울숲팜프라자약국",
    "Address": "서울특별시 성동구 왕십리로 50 지하 1층 (성수동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "더밝은약국",
    "Address": "서울특별시 성동구 마조로9길 15 1층 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQyIyQzIyQwMCQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "부일약국",
    "Address": "서울특별시 성동구 왕십리로 275-1 (행당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신이화약국",
    "Address": "서울특별시 성동구 용답중앙13길 2 1층 (용답동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQ4OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "더힘찬약국",
    "Address": "서울특별시 성동구 독서당로 302 3층 (금호동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "금호우리약국",
    "Address": "서울특별시 성동구 장터길 24 설당빌딩 1층 (금호동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQyIyQ3IyQwMCQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "나무약국",
    "Address": "서울특별시 성동구 금호로 94 금호힐오피스텔 2층 201호 (금호동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "신세계약국",
    "Address": "서울특별시 성동구 성덕정길 127 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "삼일약국",
    "Address": "서울특별시 성동구 장터길 49 (금호동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "도원약국",
    "Address": "서울특별시 성동구 장터길 45-1 (금호동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "한신약국",
    "Address": "서울특별시 성동구 왕십리로 410 상가L동 216호 (하왕십리동, 센트라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "성은약국",
    "Address": "서울특별시 성동구 상원길 59 (성수동1가, 쌍용아파트(상가B))"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "유림약국",
    "Address": "서울특별시 성동구 무학봉13길 1 (하왕십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "새대우약국",
    "Address": "서울특별시 성동구 용답25길 14 (용답동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "영민약국",
    "Address": "서울특별시 성동구 성수일로10길 32 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "새인선약국",
    "Address": "서울특별시 성동구 광나루로11길 41-1 1층 (송정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "우인약국",
    "Address": "서울특별시 성동구 왕십리로 339 (하왕십리동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 성동구 고산자로 253 (도선동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "메디팜일진약국",
    "Address": "서울특별시 성동구 용답중앙길 80-1 (용답동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "텐즈힐약국",
    "Address": "서울특별시 성동구 마장로 137 221동 2층 110호 (상왕십리동, 텐즈힐)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQ1IyQwMCQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "정성온누리약국",
    "Address": "서울특별시 성동구 왕십리로 410 상가L동 3층 319호 (하왕십리동, 센트라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQ1IyQwMCQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 성동구 왕십리로 410 상가L동 2층 210-1호 (하왕십리동, 센트라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQwMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "산호약국",
    "Address": "서울특별시 성동구 왕십리로 328-1 산호약국 1층 (도선동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "대우약국",
    "Address": "서울특별시 성동구 독서당로 276 (금호동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ4MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "효민프라자약국",
    "Address": "서울특별시 성동구 마조로 64 (마장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQxMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "다나을약국",
    "Address": "서울특별시 성동구 장터1길 2 (금호동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "행복이열리는약국",
    "Address": "서울특별시 성동구 독서당로 299-2 1층 (금호동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "한진약국",
    "Address": "서울특별시 성동구 행당로 84 309-1호 (행당동, 행당 한진타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 성동구 마장로 291 3층 (마장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 성동구 성덕정길 79 1층 (성수동2가, 정화빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ5OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "금호프라자약국",
    "Address": "서울특별시 성동구 독서당로 302 1층 (금호동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "옵티마뚝도시장약국",
    "Address": "서울특별시 성동구 성덕정길 96-1 (성수동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "미소담약국",
    "Address": "서울특별시 성북구 보국문로 49 1층 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "옵티마시민약국",
    "Address": "서울특별시 성북구 보문로 93 1층 (보문동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "모아약국",
    "Address": "서울특별시 성북구 화랑로11길 23 1층 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "선한약국",
    "Address": "서울특별시 성북구 길음로 20 길음뉴타운,래미안길음3차아파트 상가 514호, 515호 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "래미안약국",
    "Address": "서울특별시 성북구 숭인로 50 상가동 2302호 (길음동, 래미안길음센터피스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQwMyQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "정원약국",
    "Address": "서울특별시 성북구 돌곶이로 176 1층 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "백세약국",
    "Address": "서울특별시 성북구  아리랑로 117-5 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "봄온누리약국",
    "Address": "서울특별시 성북구 장위로 112 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQyIyQ1IyQwMCQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "하나온누리약국",
    "Address": "서울특별시 성북구 화랑로 95 (하월곡동, 새서울신용협동조합)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "웰팜약국",
    "Address": "서울특별시 성북구 길음로13길 22 상가동 210호 (길음동, 길음뉴타운7단지두산위브아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQwMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "사랑플러스약국",
    "Address": "서울특별시 성북구 한천로 713 래미안장위퍼스트하이 516동 105호 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQwMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "동인약국",
    "Address": "서울특별시 성북구 동소문로 107 (동선동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQyIyQxIyQwMCQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "혜조약국",
    "Address": "서울특별시 성북구 종암로21길 128 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "남정약국",
    "Address": "서울특별시 성북구 보문로 71-1 (보문동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "신세원약국",
    "Address": "서울특별시 성북구 길음로7길 6 길음뉴타운9단지래미안 상가 1층 7호 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQyIyQzIyQwMCQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "백경약국",
    "Address": "서울특별시 성북구 돌곶이로 34 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "삼원약국",
    "Address": "서울특별시 성북구 종암로 120 (종암동, 금강빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQzIyQ3MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "정릉메디칼약국",
    "Address": "서울특별시 성북구 정릉로 326 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ5MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "송원온누리약국",
    "Address": "서울특별시 성북구 종암로 132 201호 (종암동, 종암우림카이저팰리스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "이화프라자약국",
    "Address": "서울특별시 성북구 보국문로 50 지하1층 B105호 (정릉동, 청수프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "유민약국",
    "Address": "서울특별시 성북구 동소문로 127-2 1층 (동선동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "바른온누리약국",
    "Address": "서울특별시 성북구 화랑로 76 112-1호 (하월곡동, 코업스타클래스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 성북구 돌곶이로27길 79 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQxIyQwMCQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 성북구 화랑로40길 54 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ2MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "모당약국",
    "Address": "서울특별시 성북구 아리랑로5길 1 (동소문동7가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQxMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "동성온누리약국",
    "Address": "서울특별시 성북구 안암로 105 (안암동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "덕성온누리약국",
    "Address": "서울특별시 성북구 아리랑로 89 102호 (돈암동, 일신건영휴먼빌 상가 )"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ5IyQwMCQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "좋은약국",
    "Address": "서울특별시 성북구 장월로1길 23 1층 (상월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ5MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "두리온누리약국",
    "Address": "서울특별시 성북구 종암로 85 1층 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQxMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "개미약국",
    "Address": "서울특별시 성북구 장월로 128 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "정릉약국",
    "Address": "서울특별시 성북구 보국문로 45 1층 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQyIyQ3IyQwMCQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 성북구 삼양로 66 B01호 (길음동, 동부크리닉)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQxMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "영생약국",
    "Address": "서울특별시 성북구 종암로5길 36 상가동 1호 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQyIyQzIyQwMCQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜믿음약국",
    "Address": "서울특별시 성북구 돌곶이로 45 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 성북구 동소문로 248 105동 지하75호 (길음동, 삼부아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "온누리민우약국",
    "Address": "서울특별시 성북구 돌곶이로22길 49 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "홀리데이약국",
    "Address": "서울특별시 성북구 종암로 123 104호 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "정릉아름드리약국",
    "Address": "서울특별시 성북구 보국문로 33 1층 106호 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "보문약국",
    "Address": "서울특별시 성북구 보문로 123 1층 (보문동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신흥약국",
    "Address": "서울특별시 성북구 보국문로 76 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "두리약국",
    "Address": "서울특별시 성북구 돌곶이로 37 1층 (석관동, 상지빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "허브약국",
    "Address": "서울특별시 성북구 보국문로 160 1층 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "메디칼팜약국",
    "Address": "서울특별시 성북구 오패산로 49 3층 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQwMyQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "그약국",
    "Address": "서울특별시 성북구 보국문로 46 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "나약국",
    "Address": "서울특별시 성북구 장위로15길 1 1층 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "아이사랑약국",
    "Address": "서울특별시 성북구 정릉로31길 6 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQwMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "중앙프라자약국",
    "Address": "서울특별시 성북구 동소문로 94 1층 (동소문동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "아이메디칼약국",
    "Address": "서울특별시 성북구 동소문로46길 18 101호 (하월곡동, 삼전솔하임3차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ2MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "한미약국",
    "Address": "서울특별시 성북구 종암로 97 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "월곡약국",
    "Address": "서울특별시 성북구 화랑로11길 6 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "온누리청수약국",
    "Address": "서울특별시 성북구 보국문로 164 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQwMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "조일약국",
    "Address": "서울특별시 성북구 삼선교로10길 38 (삼선동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "해오름약국",
    "Address": "서울특별시 성북구 솔샘로25길 20 211호 (정릉동, 풍림아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "삼층약국",
    "Address": "서울특별시 성북구 동소문로 248 102동 314-1호 (길음동, 삼부아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "큰사랑약국",
    "Address": "서울특별시 성북구 동소문로 66 (동소문동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "백화점약국",
    "Address": "서울특별시 성북구 돌곶이로 61 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQyIyQ1IyQwMCQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "백두산약국",
    "Address": "서울특별시 성북구 고려대로 78 (안암동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 성북구 장위로 107 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "돌곶이온누리약국",
    "Address": "서울특별시 성북구 화랑로 248 장위뉴타워 102호, 102-1호 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQxMyQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "새부산약국",
    "Address": "서울특별시 성북구 돌곶이로 152 1층 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "보림약국",
    "Address": "서울특별시 성북구 동소문로 15 1층 (동소문동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "성북녹십자약국",
    "Address": "서울특별시 성북구 동소문로 32 (동소문동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "가까운행복약국",
    "Address": "서울특별시 성북구 고려대로13길 8 1층 (안암동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "서현약국",
    "Address": "서울특별시 성북구 정릉로 308 1층 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "프라임온누리약국",
    "Address": "서울특별시 성북구 월계로40길 7 1층 109호,110호 (장위동, 센트럴타운상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "우주온누리약국",
    "Address": "서울특별시 성북구 아리랑로 15 102호 (동소문동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQzIyQ5OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "화인온누리약국",
    "Address": "서울특별시 성북구 종암로 167 4층 404-1호 (하월곡동, 동일하이빌뉴시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "금강약국",
    "Address": "서울특별시 성북구 안암로 103 1층 (안암동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "길음시장약국",
    "Address": "서울특별시 성북구 길음로9길 50 101호 (길음동, 길음뉴타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "육층약국",
    "Address": "서울특별시 성북구 동소문로 106 유타 6층 (동선동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ3OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 성북구 동소문로 181 1층 (돈암동, 성북성심빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQwMyQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "명소약국",
    "Address": "서울특별시 성북구 돌곶이로 28 1층 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "나바론약국",
    "Address": "서울특별시 성북구 동소문로3길 4 정화빌딩 1층 (동소문동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "미소드림약국",
    "Address": "서울특별시 성북구 동소문로 10 1층 (동소문동2가, 카프리빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "이층봄약국",
    "Address": "서울특별시 성북구 보문로 183 2층 (삼선동4가, 논현빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 성북구 정릉로 322 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 성북구 고려대로 82 (안암동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 성북구  아리랑로 3 (동소문동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ2MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "온누리성모약국",
    "Address": "서울특별시 성북구 성북로4길 52 417동 1102호 (돈암동, 한신한진아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ3MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "민성약국",
    "Address": "서울특별시 성북구 종암로27길 13 101호 (종암동, 도원프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "화성약국",
    "Address": "서울특별시 성북구 오패산로 73 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQwMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "운용약국",
    "Address": "서울특별시 성북구 회기로 9 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQzIyQwMyQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "다정약국",
    "Address": "서울특별시 성북구 서경로 27 1층 (정릉동, 예닮빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQxMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "동부약국",
    "Address": "서울특별시 성북구  숭인로2길 61-0 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "스타온누리약국",
    "Address": "서울특별시 성북구 동소문로 14-1 1층 (동소문동2가, 로석빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "준약국",
    "Address": "서울특별시 성북구 성북로5길 2 (성북동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "미래약국",
    "Address": "서울특별시 성북구 고려대로 85 (안암동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "햇님약국",
    "Address": "서울특별시 성북구 길음로 33 상가A동 지하1층 2호 (길음동, 길음뉴타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 성북구 장위로 57 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "길음메디칼약국",
    "Address": "서울특별시 성북구 길음로 2 1층 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQ1IyQwMCQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "성북성모약국",
    "Address": "서울특별시 성북구 종암로 78 1층 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ3MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "메디팜백약국",
    "Address": "서울특별시 성북구 오패산로 57 1층 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ2MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "성북월드팜약국",
    "Address": "서울특별시 성북구 화랑로19길 83 1층 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "팜케어건강약국",
    "Address": "서울특별시 성북구 돌곶이로 60 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQyIyQ1IyQwMCQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "안세약국",
    "Address": "서울특별시 성북구 동소문로7길 2 (동소문동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ2MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "스마일약국",
    "Address": "서울특별시 성북구 보문로 180 1층 (삼선동4가, 삼선동빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "사랑받는 약국",
    "Address": "서울특별시 성북구 정릉로36길 28 1층 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ5MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "인정온누리약국",
    "Address": "서울특별시 성북구 삼선교로 14 (삼선동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "정약국",
    "Address": "서울특별시 성북구 종암로24가길 53 210호 (종암동, 종암SK아파트상가 )"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "관문약국",
    "Address": "서울특별시 성북구 장위로 177 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 성북구 장위로 110 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQyIyQ3IyQwMCQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 성북구 고려대로 89 (안암동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQwMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "W스토어 참좋은약국",
    "Address": "서울특별시 성북구 동소문로 34 1층 (동소문동3가, 연진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ3OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "새석관약국",
    "Address": "서울특별시 성북구 돌곶이로 57 1층 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "새국민약국",
    "Address": "서울특별시 성북구 화랑로 91 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "뉴대원약국",
    "Address": "서울특별시 성북구 화랑로 248 1층 101호 (석관동, 장위뉴타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQwMyQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "길약국",
    "Address": "서울특별시 성북구 성북로4길 52 3층 418-2302호 (돈암동, 스카이프라자 서관)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 성북구 장월로 146 1층 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "정릉열린약국",
    "Address": "서울특별시 성북구 보국문로 40-3 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQwMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "조아약국",
    "Address": "서울특별시 성북구 화랑로 87 1층 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 성북구 돌곶이로 25 (석관동, 씨티홈)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "더사랑약국",
    "Address": "서울특별시 성북구 아리랑로 16 1층 104호 (동선동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "센터피스정약국",
    "Address": "서울특별시 성북구 숭인로 50 상가동 2108호 (길음동, 래미안길음센터피스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQxMyQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "멜론약국",
    "Address": "서울특별시 성북구 보국문로 53 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQyIyQzIyQwMCQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 성북구 종암로 93 1층 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ1IyQwMCQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "동민약국",
    "Address": "서울특별시 성북구 오패산로 99 102호 (하월곡동, 동민빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "동선한약국",
    "Address": "서울특별시 성북구 동소문로26다길 17 1층 (동선동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "가까운약국",
    "Address": "서울특별시 성북구 보문로 44 (보문동7가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQyIyQ3IyQwMCQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "건강한약국",
    "Address": "서울특별시 성북구 동소문로42길 14 1층 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQwMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "아이팜약국",
    "Address": "서울특별시 성북구 길음로 103 304호 (길음동, 대우상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "삼성약국",
    "Address": "서울특별시 성북구 동소문로 190 103호 (돈암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "아름다운약국",
    "Address": "서울특별시 성북구 길음로 33 상가B동 지층 17,18,19호 (길음동, 길음뉴타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "365약국",
    "Address": "서울특별시 성북구 동소문로 321 1층 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ4OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "새롬약국",
    "Address": "서울특별시 성북구 장위로 58 1층 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "명신약국",
    "Address": "서울특별시 성북구 종암로 180 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "올리브한성약국",
    "Address": "서울특별시 성북구  동소문로 18-1 (동소문동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "대림당약국",
    "Address": "서울특별시 성북구 동소문로 231 1층 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "파란하늘약국",
    "Address": "서울특별시 성북구 성북로4길 52 417동 501호 (돈암동, 한신한진아파트제상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "수보약국",
    "Address": "서울특별시 성북구 솔샘로6길 63 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQyIyQ1IyQwMCQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "지선약국",
    "Address": "서울특별시 성북구 장위로 127-1 한양빌딩 2층 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQyIyQ5IyQwMCQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "석산약국",
    "Address": "서울특별시 성북구 오패산로1길 1 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQxMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "새보건약국",
    "Address": "서울특별시 성북구 화랑로 67 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 성북구 보문로34길 59 1층 (동선동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "편안한약국",
    "Address": "서울특별시 성북구 동소문로20다길 2 1층 (동선동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "상락약국",
    "Address": "서울특별시 성북구 보국문로 4 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "월곡정약국",
    "Address": "서울특별시 성북구 화랑로 76 코업스타클래스 지하1층 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "새비홍약국",
    "Address": "서울특별시 성북구 한천로 580 1층 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "월곡보건약국",
    "Address": "서울특별시 성북구 화랑로 61 1층 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "공원내 아이사랑약국",
    "Address": "서울특별시 성북구 동소문로44길 17 102동 105호, 106호 (하월곡동, 성북힐스테이트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 성북구 길음로 20 래미안길음3차아파트상가 1층 116호 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "청춘한약국",
    "Address": "서울특별시 성북구 종암로 167 141,142호 (하월곡동, 동일하이빌뉴시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQyIyQ5IyQwMCQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "한솔약국",
    "Address": "서울특별시 성북구 동소문로 57-1 (동소문동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQwMyQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "알파약국",
    "Address": "서울특별시 성북구  장위로 42-1 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "세원약국",
    "Address": "서울특별시 성북구 동소문로20가길 51 (동선동1가, 수국빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQwMyQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "인현약국",
    "Address": "서울특별시 성북구 돌곶이로41길 33 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "십자약국",
    "Address": "서울특별시 성북구 숭인로2길 82 2층 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "수진약국",
    "Address": "서울특별시 성북구 돌곶이로 134 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "새성신약국",
    "Address": "서울특별시 성북구 동소문로 125 골든타워 1층 101호 (동선동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "소원약국",
    "Address": "서울특별시 성북구 개운사길 2 1층 (안암동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "종암약국",
    "Address": "서울특별시 성북구 종암로 80 1층 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "제창약국",
    "Address": "서울특별시 성북구 정릉로27길 41 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "옵티마대우미약국",
    "Address": "서울특별시 성북구 성북로2길 8 1층 (동소문동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ2MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "선화약국",
    "Address": "서울특별시 성북구 돌곶이로 67 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "용수약국",
    "Address": "서울특별시 성북구 동소문로13나길 111 (동소문동7가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ2MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "새민우약국",
    "Address": "서울특별시 성북구 북악산로 845 203동 301호 (정릉동, 정릉쌍용아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "민정약국",
    "Address": "서울특별시 성북구 북악산로22길 2 (돈암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "회생약국",
    "Address": "서울특별시 성북구 지봉로20길 57 (보문동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "정인약국",
    "Address": "서울특별시 성북구 정릉로36길 50 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "강원약국",
    "Address": "서울특별시 성북구 아리랑로 117-7 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "세종약국",
    "Address": "서울특별시 성북구 보국문로 168 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQyIyQ1IyQwMCQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "국민약국",
    "Address": "서울특별시 성북구 정릉로10길 42-2 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "대영약국",
    "Address": "서울특별시 성북구 월곡로5길 66 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "온누리두산약국",
    "Address": "서울특별시 성북구 화랑로48길 16 101호 (석관동, 두산아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQxMyQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "가람약국",
    "Address": "서울특별시 성북구 삼양로8길 3-28 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "연약국",
    "Address": "서울특별시 성북구 동소문로 12 지층 (동소문동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQxMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "보람약국",
    "Address": "서울특별시 성북구 장위로 123 1층 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ2MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "연세정약국",
    "Address": "서울특별시 성북구 화랑로 201 (장위동, 대영치과)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "사랑의약국",
    "Address": "서울특별시 성북구 종암로 115 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQwMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "옵티마e-편한약국",
    "Address": "서울특별시 성북구 삼양로13길 45 401호 (길음동, 길음뉴타운,e편한세상 대림상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "콩약국",
    "Address": "서울특별시 성북구 길음로 20 길음뉴타운,래미안길음3차아파트 상가 3층 315호 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQwMyQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "힘챤약국",
    "Address": "서울특별시 성북구 보국문로 16-1 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "참약사약국",
    "Address": "서울특별시 성북구 종암로 122 1층 (종암동, 시원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "현약국",
    "Address": "서울특별시 성북구 북악산로 844 상가동 지하층 102-1호 (돈암동, 브라운스톤 돈암 아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "월곡우리약국",
    "Address": "서울특별시 성북구 월계로 52 (하월곡동, 에스엠메디칼)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "계산온누리약국",
    "Address": "서울특별시 성북구 동소문로20길 43 (동선동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 성북구 종암로21길 3 (종암동, 용진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ2MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "21세기고려약국",
    "Address": "서울특별시 성북구 고려대로 80 (안암동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQyIyQ1IyQwMCQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "부민약국",
    "Address": "서울특별시 성북구 화랑로13길 9 1층 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ2MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "맑은샘온누리약국",
    "Address": "서울특별시 성북구  보문로 157 (삼선동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "광혜당약국",
    "Address": "서울특별시 성북구 장월로 88-1 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "청십자약국",
    "Address": "서울특별시 성북구 보문로 99 1층 (보문동5가, 영광빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "신정릉우리약국",
    "Address": "서울특별시 성북구 보국문로 43 103호 (정릉동, 야원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "하얀약국",
    "Address": "서울특별시 성북구 아리랑로 9 산맥프라자 2층 202호 (동소문동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "호수온누리약국",
    "Address": "서울특별시 성북구 동소문로47길 12 1층 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5OSQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "신중앙약국",
    "Address": "서울특별시 성북구 종암로 68 1층 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 성북구 보문로 94 (보문동4가, 화성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "한강약국",
    "Address": "서울특별시 성북구 도봉로 3 1층 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQyIyQ5IyQwMCQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "자산약국",
    "Address": "서울특별시 성북구 화랑로5길 42 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQyIyQ5IyQwMCQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "구원약국",
    "Address": "서울특별시 성북구 오패산로 16 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQxMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 성북구 동소문로 16-1 (동소문동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "대원약국",
    "Address": "서울특별시 성북구 돌곶이로14길 51 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ2MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "온누리진호약국",
    "Address": "서울특별시 성북구 돌곶이로 36-1 (석관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "정주약국",
    "Address": "서울특별시 성북구 오패산로 63 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQyIyQzIyQwMCQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "선약국",
    "Address": "서울특별시 성북구 돌곶이로41길 10 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "아가페온누리약국",
    "Address": "서울특별시 성북구 정릉로 274 1층 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQxMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 성북구 동소문로 71 (동소문동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ4OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "청솔약국",
    "Address": "서울특별시 성북구 한천로 743 (장위동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "스타약국",
    "Address": "서울특별시 성북구 동소문로 92 1층 (동소문동5가, 강윤빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ5OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 성북구 보국문로16길 31 (정릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "도담약국",
    "Address": "서울특별시 성북구 동소문로 305 지층 (길음동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "지민약국",
    "Address": "서울특별시 성북구 삼선교로 87 (삼선동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ2MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "동서옵티마약국",
    "Address": "서울특별시 성북구 동소문로 302 1층 (하월곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 성북구 종암로19길 17 양지빌딩 104호 (종암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "신길프라자약국",
    "Address": "서울특별시 영등포구 도신로 120 (신길동,신영빌딩 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "반석온누리약국",
    "Address": "서울특별시 영등포구 영등포로 33 108호 (양평동2가,비즈타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "삼남매약국",
    "Address": "서울특별시 영등포구 여의대방로 417 대교상가 1층 110호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQ1IyQwMCQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "천지당약국",
    "Address": "서울특별시 영등포구 시흥대로 659 1층 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "공원온누리약국",
    "Address": "서울특별시 영등포구 신길로 252 (영등포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQwMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "장원옵티마약국",
    "Address": "서울특별시 영등포구 신길로 147 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 영등포구 도신로 90 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQxMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "유명약국",
    "Address": "서울특별시 영등포구 도신로60길 2 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "경희행복한약국",
    "Address": "서울특별시 영등포구 영등포로 131 (당산동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "보현약국",
    "Address": "서울특별시 영등포구 신풍로 77 A동 지하2층 116호 (신길동, 래미안에스티움)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "나무약국",
    "Address": "서울특별시 영등포구 도림로 158 대림빌딩 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "여의도약국",
    "Address": "서울특별시 영등포구 여의나루로 40 (여의도동, 여의도역 지하1층 1,2번 출입구 쪽 개찰구 옆)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "우리집약국",
    "Address": "서울특별시 영등포구 시흥대로 659-1 1층 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "오늘약국",
    "Address": "서울특별시 영등포구 시흥대로 635 대림메디컬빌딩 1층 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "신세계약국",
    "Address": "서울특별시 영등포구 시흥대로 675 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "다나스약국",
    "Address": "서울특별시 영등포구 여의대방로 83 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "문래스타약국",
    "Address": "서울특별시 영등포구 선유로9길 10 SK V1 Center 1층 105호 (문래동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "조아약국",
    "Address": "서울특별시 영등포구 문래로 191 1층 102-1호 (영등포동4가, 영등포 대성 그랑그루)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 영등포구 영등포로34길 12 1층 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "우신약국",
    "Address": "서울특별시 영등포구 영등포로 250-1 (영등포동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "경도약국",
    "Address": "서울특별시 영등포구 여의대방로 383 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 영등포구 신길로 141 지하층 2호 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQwMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "신길약국",
    "Address": "서울특별시 영등포구 도신로 235 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ2MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "누가약국",
    "Address": "서울특별시 영등포구 디지털로 367 1층 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "동보약국",
    "Address": "서울특별시 영등포구 영중로 22 (영등포동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "쉐르빌약국",
    "Address": "서울특별시 영등포구 당산로45길 1 (당산동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 영등포구 문래로 83 (문래동3가, 아라비즈타워 209호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ4MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "애지약국",
    "Address": "서울특별시 영등포구 영등포로80길 15 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "팜약국",
    "Address": "서울특별시 영등포구  국제금융로2길 7 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ2MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "수온누리약국",
    "Address": "서울특별시 영등포구  선유로 63 (문래동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "여의도마트약국",
    "Address": "서울특별시 영등포구 여의동로3길 10 지하1층 B01호 (여의도동, 여의도자이)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "건강한세상대한약국",
    "Address": "서울특별시 영등포구 국제금융로 108 (여의도동,은하빌딩 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "21세기신천지약국",
    "Address": "서울특별시 영등포구 영등포로 232-1 (영등포동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQxIyQ2MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 영등포구 여의대방로 379 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ4OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "장수약국",
    "Address": "서울특별시 영등포구 신풍로 46 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "우리팜약국",
    "Address": "서울특별시 영등포구 영등포로36길 6 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ3MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "인동약국",
    "Address": "서울특별시 영등포구 영등포로11길 9 (양평동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQwMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "보라매약국",
    "Address": "서울특별시 영등포구 신풍로 113 (신길동,시원빌딩 103호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "약산약국",
    "Address": "서울특별시 영등포구 도신로 208 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "세성심약국",
    "Address": "서울특별시 영등포구 시흥대로187길 1 지하1, 1층 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 영등포구 영중로 61 극동방송 (영등포동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "해빛온누리약국",
    "Address": "서울특별시 영등포구 영신로34길 10 1층 108호 (영등포동4가, 영남빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "친절한성심정문약국",
    "Address": "서울특별시 영등포구 시흥대로 681 삼성YJ그랜드빌딩 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "당산스타약국",
    "Address": "서울특별시 영등포구 양평로 22 1층 (당산동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ3OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "웃는내일약국",
    "Address": "서울특별시 영등포구  선유로 64 (문래동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ3MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "힘찬약국",
    "Address": "서울특별시 영등포구 디지털로37길 9-5 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQxMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "아이비하늘약국",
    "Address": "서울특별시 영등포구 국제금융로 86 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "미서약국",
    "Address": "서울특별시 영등포구 국제금융로7길 15 1층 2012호 (여의도동, 여의상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "영등포진약국",
    "Address": "서울특별시 영등포구 영중로 63 1층 (영등포동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ2MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "대림타워약국",
    "Address": "서울특별시 영등포구 가마산로48길 16 302호 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ3OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "엄마약국",
    "Address": "서울특별시 영등포구 대림로29길 19 1층 (대림동, 대화빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "나래약국",
    "Address": "서울특별시 영등포구 도림로 192 (대림동, 동성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "여의도씨티약국",
    "Address": "서울특별시 영등포구 여의대방로 375 (여의도동,아일렉스타워 109호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ5OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "중앙온누리약국",
    "Address": "서울특별시 영등포구 여의대방로 417 213호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ4MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "미래약국",
    "Address": "서울특별시 영등포구 여의대방로65길 12 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "온누리유진약국",
    "Address": "서울특별시 영등포구 영등포로 356 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQxMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "선경약국",
    "Address": "서울특별시 영등포구 국제금융로2길 24 삼성생명(주)여의도 빌딩 1층4호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "21세기약국",
    "Address": "서울특별시 영등포구 여의대방로 177 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "옥광약국",
    "Address": "서울특별시 영등포구 대림로 247 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "수인옵티마약국",
    "Address": "서울특별시 영등포구 영등포로 32 (양평동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "대성모약국",
    "Address": "서울특별시 영등포구 시흥대로 655 1층 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ2MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "신세명약국",
    "Address": "서울특별시 영등포구 도림로 209 105호 (신길동, 미성상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "우리조운약국",
    "Address": "서울특별시 영등포구 도림로 206 1층 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "영등포메디칼약국",
    "Address": "서울특별시 영등포구 영중로8길 6 성남빌딩 B동 1층 104호 (영등포동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 영등포구 선유로 138 롯데마트 양평점 지하1층 (양평동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQzIyQwMCQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "포도나무약국",
    "Address": "서울특별시 영등포구 선유로 70 우리벤처타운2 2동 2층 209-1호 (문래동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "해그린약국",
    "Address": "서울특별시 영등포구 여의대방로 375 아일렉스타워 108호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQwMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "팜프라자약국",
    "Address": "서울특별시 영등포구 여의나루로 50 한국교직원공제회관 B1층 3호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "무지개약국",
    "Address": "서울특별시 영등포구 선유로 76 동국메뜨리앙 3층 305호 (문래동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ5IyQwMCQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "온유약국",
    "Address": "서울특별시 영등포구 여의공원로 13 한국방송공사 신관동 2층 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ5IyQwMCQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "이화메디약국",
    "Address": "서울특별시 영등포구 당산로 122 우미빌딩 1층 102호 (당산동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQwMyQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "래미안온누리약국",
    "Address": "서울특별시 영등포구 당산로 214 (당산동5가,삼성래미안4차아파트 상가 109-1)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "햇살온누리약국",
    "Address": "서울특별시 영등포구 당산로 223 (당산동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "신풍약국",
    "Address": "서울특별시 영등포구 신길로 36-1 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "김약국",
    "Address": "서울특별시 영등포구  대림로22길 37 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 영등포구 경인로102길 13 3층 (영등포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 영등포구 국제금융로 112 1층 (여의도동, 상아빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "메디컬수약국",
    "Address": "서울특별시 영등포구 영등포로 81-1 메디컬수약국 (양평동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "늘푸른이화약국",
    "Address": "서울특별시 영등포구 영신로32길 20 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "녹십자약국",
    "Address": "서울특별시 영등포구 대림로 157 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQxMyQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "한강약국",
    "Address": "서울특별시 영등포구 버드나루로7길 7 (영등포동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "고은약국",
    "Address": "서울특별시 영등포구 영신로 259 (당산동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "보은당약국",
    "Address": "서울특별시 영등포구 당산로 163 (당산동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQyIyQzIyQwMCQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "보건약국",
    "Address": "서울특별시 영등포구 국제금융로7길 22 (여의도동,대교B상가 114호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "별담은온누리약국",
    "Address": "서울특별시 영등포구 국회대로54길 10 판매시설 13동 3층 8호 (영등포동7가, 아크로타워 스퀘어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "성심제일약국",
    "Address": "서울특별시 영등포구 시흥대로 663 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "친절약국",
    "Address": "서울특별시 영등포구 영신로34길 10 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "대교약국",
    "Address": "서울특별시 영등포구 여의대방로 383 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ5OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 영등포구 당산로 166 (당산동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신우리약국",
    "Address": "서울특별시 영등포구 여의나루로 42 (여의도동,여의도종합상가 406호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "수정프라자약국",
    "Address": "서울특별시 영등포구 양평로22길 7 (양평동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "신풍도약국",
    "Address": "서울특별시 영등포구 도신로29다길 12 (도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "한마음국회약국",
    "Address": "서울특별시 영등포구 의사당대로 1 국회 국회소통관동 1층 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ5MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 영등포구 신길로 28 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "서울대림약국",
    "Address": "서울특별시 영등포구 시흥대로 667-1 1,2층 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "휴베이스미소약국",
    "Address": "서울특별시 영등포구 선유서로 117 1층 102호 (양평동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "태령약국",
    "Address": "서울특별시 영등포구 신길로 157 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "영등포제일약국",
    "Address": "서울특별시 영등포구 영중로 51-1 (영등포동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ4OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "천사약국",
    "Address": "서울특별시 영등포구 국회대로76길 33 4층 403호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQ1IyQwMCQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "피플팜문래약국",
    "Address": "서울특별시 영등포구  당산로 34-0 (문래동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "경명약국",
    "Address": "서울특별시 영등포구 선유서로25길 5-1 (양평동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQyIyQ1IyQwMCQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "나눔약국",
    "Address": "서울특별시 영등포구 여의대방로53길 23 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 영등포구 영신로19길 23 (영등포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "종로온누리약국",
    "Address": "서울특별시 영등포구 시흥대로187길 12 상가동 103호 (대림동, 대림동현대아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQwMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "뉴성모제일약국",
    "Address": "서울특별시 영등포구 여의대방로62길 2 봉덕빌딩 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "대원약국",
    "Address": "서울특별시 영등포구 당산로 34 (문래동3가,4층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "신대흥약국",
    "Address": "서울특별시 영등포구 영등포로 157 (당산동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQwMyQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "성모메디컬약국",
    "Address": "서울특별시 영등포구 영중로 45 지하1층 101호 (영등포동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "여의도미소약국",
    "Address": "서울특별시 영등포구 국제금융로6길 30 백상빌딩 317호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "여의도대학약국",
    "Address": "서울특별시 영등포구 63로 45 7동 1층 19호 (여의도동, 여의도시범아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "노아약국",
    "Address": "서울특별시 영등포구 의사당대로 26 더하우스소호 1층 102호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 영등포구 신길로 181-1 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ5OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "삼정약국",
    "Address": "서울특별시 영등포구 국제금융로 70 (여의도동, 미원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ4MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "대림백화점약국",
    "Address": "서울특별시 영등포구 신길로 40 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "마음약국",
    "Address": "서울특별시 영등포구 선유로 59 (문래동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQwMyQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "아이비약국",
    "Address": "서울특별시 영등포구 여의나루로 42 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "당산열린약국",
    "Address": "서울특별시 영등포구 양평로 32 (당산동6가, 누가빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "디오빌약국",
    "Address": "서울특별시 영등포구 당산로 222 (당산동5가,당산디오빌 206호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "프라자약국",
    "Address": "서울특별시 영등포구 선유로 42 (문래동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "온누리평안약국",
    "Address": "서울특별시 영등포구 양평로24길 9 (양평동5가, 한신아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "수범약국",
    "Address": "서울특별시 영등포구 경인로 835 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ2MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "소화약국",
    "Address": "서울특별시 영등포구 버드나루로7길 7 (영등포동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "송약국",
    "Address": "서울특별시 영등포구 디지털로 413 101호 송약국 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "수산약국",
    "Address": "서울특별시 영등포구  대림로34길 12 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "성우약국",
    "Address": "서울특별시 영등포구 여의대로 24 전국경제인연합회회관 지하1층 114-2호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "유림약국",
    "Address": "서울특별시 영등포구 양평로 95-1 (양평동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "행복한수약국",
    "Address": "서울특별시 영등포구 영중로2길 1 1층 (영등포동3가, 대선빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ3OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "로얄약국",
    "Address": "서울특별시 영등포구 국회대로37길 25 (당산동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "미솔약국",
    "Address": "서울특별시 영등포구  신길로 149 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "건강온누리약국",
    "Address": "서울특별시 영등포구  신풍로 113 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQxMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "대건약국",
    "Address": "서울특별시 영등포구 양평로 99 (양평동4가,1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "다영약국",
    "Address": "서울특별시 영등포구 도신로60길 7 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "온누리정문약국",
    "Address": "서울특별시 영등포구 버드나루로7길 9 1층 (영등포동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "타워약국",
    "Address": "서울특별시 영등포구 63로 36 (여의도동,리버타워빌딩 103호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQyIyQzIyQwMCQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "지현약국",
    "Address": "서울특별시 영등포구 영등포로 399-5 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "신당약국",
    "Address": "서울특별시 영등포구 도림로113길 3-2 (도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "청운약국",
    "Address": "서울특별시 영등포구 시흥대로175길 2 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "부용약국",
    "Address": "서울특별시 영등포구 시흥대로177길 17-1 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "아람약국",
    "Address": "서울특별시 영등포구 여의대방로 87 1층 (신길동, 대신빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "임약국",
    "Address": "서울특별시 영등포구 경인로79길 4 (문래동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "은하약국",
    "Address": "서울특별시 영등포구 국회대로70길 22 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "우당약국",
    "Address": "서울특별시 영등포구 국제금융로 108-6 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "럭키약국",
    "Address": "서울특별시 영등포구 여의대로 128 (여의도동, LG트윈타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "대화약국",
    "Address": "서울특별시 영등포구 국제금융로6길 33 (여의도동, 맨하탄빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "후생약국",
    "Address": "서울특별시 영등포구 국제금융로 78 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "미성온누리약국",
    "Address": "서울특별시 영등포구 도신로29길 28 (영등포동, 영등포푸르지오2단지아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "하나로약국",
    "Address": "서울특별시 영등포구 영등포로 208-1 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "백상약국",
    "Address": "서울특별시 영등포구 국제금융로6길 30 백상빌딩 1층 103호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "구민약국",
    "Address": "서울특별시 영등포구 당산로 142-1 (당산동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "중앙메디칼약국",
    "Address": "서울특별시 영등포구 가마산로 582 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQyIyQ1IyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신새별약국",
    "Address": "서울특별시 영등포구 도림로 487-1 (문래동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "동신당약국",
    "Address": "서울특별시 영등포구 양산로 138-1 (당산동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ5MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "한우리약국",
    "Address": "서울특별시 영등포구 의사당대로 97 (여의도동,교보증권빌딩 지하1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "새희망약국",
    "Address": "서울특별시 영등포구 영등포로 146-1 (당산동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "보생사약국",
    "Address": "서울특별시 영등포구 영등포로 400 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "새금강약국",
    "Address": "서울특별시 영등포구 시흥대로181길 10-4 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "서진약국",
    "Address": "서울특별시 영등포구 대림로 245 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQxMyQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "양모약국",
    "Address": "서울특별시 영등포구 가마산로61길 14-1 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQwMyQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "정성온누리약국",
    "Address": "서울특별시 영등포구 신길로 36 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "한중약국",
    "Address": "서울특별시 영등포구 디지털로37길 20 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "태령약국",
    "Address": "서울특별시 영등포구 신길로 157 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "이도온누리약국",
    "Address": "서울특별시 영등포구 당산로31길 14 1층 (당산동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "피보약국",
    "Address": "서울특별시 영등포구 영등포로 180-1 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQxMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "대흥약국",
    "Address": "서울특별시 영등포구 신길로39길 13 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "정명약국",
    "Address": "서울특별시 영등포구 의사당대로 108 1층 119호 (여의도동, 아일렉스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 영등포구 국제금융로6길 33 1층 104호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "금강온누리약국",
    "Address": "서울특별시 영등포구 영중로 10-1 (영등포동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "당산수약국",
    "Address": "서울특별시 영등포구 양평로 53 (당산동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "메디칼푸른약국",
    "Address": "서울특별시 영등포구 양평로 16 1층 105호 (당산동6가, 당산동 대정프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQxMyQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "햇님온누리약국",
    "Address": "서울특별시 영등포구 의사당대로 108 304호 (여의도동, 아일렉스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "당산삼성약국",
    "Address": "서울특별시 영등포구 당산로44길 3 (당산동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "더블유스토어아름다운약국",
    "Address": "서울특별시 영등포구 영중로 6 (영등포동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "행복약국",
    "Address": "서울특별시 영등포구 양평로 127 (양평동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 영등포구 도림로 322 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "윤중약국",
    "Address": "서울특별시 영등포구 여의나루로 42 여의도종합상가 1층 115호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "성심바른약국",
    "Address": "서울특별시 영등포구 신길로 18 103호 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "왕온누리약국",
    "Address": "서울특별시 영등포구 영중로24길 3 영오빌딩 101호 (영등포동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "맑은수약국",
    "Address": "서울특별시 영등포구 여의대방로 65 돈보스코청소년센터 2층 8호 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ4OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "우리안약국",
    "Address": "서울특별시 영등포구 영신로34길 5 1층 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5OSQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "봄빛약국",
    "Address": "서울특별시 영등포구 국회대로70길 12 대산빌딩 1층 101호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 영등포구 경인로 775 1동 103층 (문래동3가, 에이스하이테크시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "새울림약국",
    "Address": "서울특별시 영등포구 영등포로 390 1층 101호 (신길동, 프리가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQwMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "영등포시장약국",
    "Address": "서울특별시 영등포구 영중로 62 1층 (영등포동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "가까운약국",
    "Address": "서울특별시 영등포구 당산로 34 로데오 쇼핑몰 1층 (문래동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "맨하탄길약국",
    "Address": "서울특별시 영등포구 국제금융로6길 33 1층 127호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ2MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "미소로약국",
    "Address": "서울특별시 영등포구 영신로 238 (영등포동8가,101호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "선화온누리약국",
    "Address": "서울특별시 영등포구 도신로58길 17 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ5OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "새서울약국",
    "Address": "서울특별시 영등포구 영등포로86길 14-1 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ4OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "도림우리들약국",
    "Address": "서울특별시 영등포구 도신로15길 40 (도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "송앤김약국",
    "Address": "서울특별시 영등포구 도신로 88 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "화랑온누리약국",
    "Address": "서울특별시 영등포구 신길로 42 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "365열린약국",
    "Address": "서울특별시 영등포구 영중로 119 리마크빌 영등포 2층 204-2호 (영등포동8가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "헤르바당산역약국",
    "Address": "서울특별시 영등포구 양평로 40 당산역 지하1층 (당산동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ2MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "정민약국",
    "Address": "서울특별시 영등포구 선유서로 40 1층 112호 (문래동6가, 베어스타운아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "정제약국",
    "Address": "서울특별시 영등포구 도영로 49 (도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "문래건강한약국",
    "Address": "서울특별시 영등포구 영등포로 118 성지빌딩 1층 1,2호 (당산동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "영인약국",
    "Address": "서울특별시 영등포구 도림로 190 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQyIyQ1IyQwMCQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "정안약국",
    "Address": "서울특별시 영등포구 여의대방로35길 36 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "예지약국",
    "Address": "서울특별시 영등포구 도신로 87 (도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "건강드림약국",
    "Address": "서울특별시 영등포구 영중로 70 1층 (영등포동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "해경아는약국",
    "Address": "서울특별시 영등포구 여의대방로69길 28 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "종대약국",
    "Address": "서울특별시 영등포구 도림로 352 (도림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "서울성모약국",
    "Address": "서울특별시 영등포구 도림로 157 대림빌딩 1층 102호 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "다인약국",
    "Address": "서울특별시 영등포구 선유로 70 2층 206-2호 (문래동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 영등포구 영등포로 130 상가동 1층 104,105호 (당산동1가, 진로아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "판도라조은약국",
    "Address": "서울특별시 영등포구 영중로 60 1층 (영등포동5가, 유니온빌딩(판도라 내부))"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 영등포구 국제금융로2길 37 3층 306-1호 (여의도동, 에스트레뉴)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "명성약국",
    "Address": "서울특별시 영등포구 도림로 152-4 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ2MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "신영약국",
    "Address": "서울특별시 영등포구 신풍로 33 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "부부정약국",
    "Address": "서울특별시 영등포구 양평로 64 1층 (당산동6가, 경진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQxMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "대림미소약국",
    "Address": "서울특별시 영등포구 도림로 135 1층 107,108호 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ5OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "뉴그랜드약국",
    "Address": "서울특별시 영등포구 대림로 212 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQwMyQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "일등약국",
    "Address": "서울특별시 영등포구 도림로 152-6 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQwMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "우리시장약국",
    "Address": "서울특별시 영등포구 디지털로 445 1층 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ2MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "새성심약국",
    "Address": "서울특별시 영등포구 양평로 102 (양평동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQyIyQxIyQwMCQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 영등포구 영중로 15 타임스퀘어 지하1층 128-2호 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "화일온누리약국",
    "Address": "서울특별시 영등포구 도신로64길 24 1층 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "대명약국",
    "Address": "서울특별시 영등포구 영신로19길 7 (영등포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "신풍시장약국",
    "Address": "서울특별시 영등포구 가마산로 433-1 1층 1호 (신길동, SG메디피움)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "여의도성모약국",
    "Address": "서울특별시 영등포구 63로 45 (여의도동, 여의도시범아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "기림약국",
    "Address": "서울특별시 영등포구 대림로34길 29 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "대림대학약국",
    "Address": "서울특별시 영등포구 시흥대로187길 3 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "바른메디컬약국",
    "Address": "서울특별시 영등포구 여의대방로 145 1층 (신길동, 세인트빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "보라매미소약국",
    "Address": "서울특별시 영등포구 신풍로 93 메트하임 1층 114,116,117호 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQxMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "선유도온누리약국",
    "Address": "서울특별시 영등포구 양평로 129 (양평동5가,1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "맑은약국",
    "Address": "서울특별시 영등포구 당산로 42 (문래동3가,삼성홈플러스빌딩 지하1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "온누리대광약국",
    "Address": "서울특별시 영등포구 도림로38길 4 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ2MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "이레약국",
    "Address": "서울특별시 영등포구 디지털로 375 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "새보람약국",
    "Address": "서울특별시 영등포구 당산로31길 6 (당산동3가, 영등포병원)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ5OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "영등포21세기온누리약국",
    "Address": "서울특별시 영등포구 당산로36길 12 (당산동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "100세약국",
    "Address": "서울특별시 영등포구 양평로 24 (당산동6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQyIyQxIyQwMCQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "오약국",
    "Address": "서울특별시 영등포구 당산로 163 (당산동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQwMyQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "대림약국",
    "Address": "서울특별시 영등포구 도림로 155 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "스타약국",
    "Address": "서울특별시 영등포구 도림로48길 4 1층 5호 (대림동, 대림스타빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "천우약국",
    "Address": "서울특별시 영등포구 영등포로 231-1 1층 (영등포동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 영등포구 가마산로 439-1 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "주영온누리약국",
    "Address": "서울특별시 영등포구 영신로 9 1층 (영등포동, 주영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 영등포구 영등포로86길 16 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "수정약국",
    "Address": "서울특별시 영등포구 영등포로36길 16 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 영등포구 영중로 66 1층 (영등포동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "민약국",
    "Address": "서울특별시 영등포구 가마산로69가길 12 3층 303호 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "여의도플러스약국",
    "Address": "서울특별시 영등포구 여의공원로 101 C.C.M.M빌딩 B117호 (여의도동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "서울대학약국",
    "Address": "서울특별시 영등포구 버드나루로7길 3 경동미르웰 여의도 1층 105호 (영등포동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ5OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "세종로약국",
    "Address": "서울특별시 영등포구 여의대방로 197 (신길동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "해정약국",
    "Address": "서울특별시 영등포구 도림로 150 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "산호약국",
    "Address": "서울특별시 영등포구 대림로 73 1층 1호 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQ5OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "범일약국",
    "Address": "서울특별시 영등포구 영중로 54 (영등포동5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 영등포구 도신로29사길 1 1층 (영등포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQyIyQ3IyQwMCQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 영등포구 도림로 158 (대림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ3MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "초원약국",
    "Address": "서울특별시 영등포구 영중로 31 (영등포동4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ2MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "서울중앙약국",
    "Address": "서울특별시 용산구 청파로 378 1층 (동자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "종로프라자약국",
    "Address": "서울특별시 용산구 한강대로23길 55 (한강로3가, 이마트내)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "이태원수약국",
    "Address": "서울특별시 용산구 보광로 125 2층 (이태원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "코끼리약국",
    "Address": "서울특별시 용산구 보광로 30 2층 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 용산구 백범로 287 1층 (효창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 용산구 원효로 171 신영빌딩 1층 (원효로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "새건우약국",
    "Address": "서울특별시 용산구 후암로 91-1 (동자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "보승약국",
    "Address": "서울특별시 용산구 우사단로4길 42-1 1층 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "신태양약국",
    "Address": "서울특별시 용산구 우사단로2길 23 신태양약국 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ2MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "문화약국",
    "Address": "서울특별시 용산구  장문로 114-1 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQxMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "신보영약국",
    "Address": "서울특별시 용산구 한강대로 154 (한강로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "은정약국",
    "Address": "서울특별시 용산구 후암로 7-1 (후암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQyIyQ1IyQwMCQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 용산구 이촌로 264 (이촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQxMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "남선약국",
    "Address": "서울특별시 용산구 원효로 166 103호 (원효로2가, 원효아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 용산구 후암로 41 1층 (후암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "양지약국",
    "Address": "서울특별시 용산구 이촌로 248 11동 103-1호 (이촌동, 한강맨션)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 용산구 백범로 283 (효창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ2MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "원효종로엠약국",
    "Address": "서울특별시 용산구 원효로41길 58-1 (원효로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "서현약국",
    "Address": "서울특별시 용산구 이촌로 200 지히1층 104호 (이촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQxMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "메디팜나은약국",
    "Address": "서울특별시 용산구 한강대로 211 110호 (한강로1가, 대우월드마크용산)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQwMyQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 용산구 대사관로 60-1 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQxMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "해란약국",
    "Address": "서울특별시 용산구 청파로47길 53 1층 (청파동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ5OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "국제약국",
    "Address": "서울특별시 용산구 한강대로 290-1 (남영동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ5MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "문약국",
    "Address": "서울특별시 용산구 독서당로 67 205호 (한남동, 서울빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQwMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "옵티마찬미약국",
    "Address": "서울특별시 용산구 대사관로30길 17 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "새무림약국",
    "Address": "서울특별시 용산구 한강대로 55 (한강로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "동광약국",
    "Address": "서울특별시 용산구 장문로 66-1 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQxMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "동아약국",
    "Address": "서울특별시 용산구 회나무로 16 (이태원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "민약국",
    "Address": "서울특별시 용산구 한강대로23길 55 용산민자역사내 3층 (한강로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "행복을 주는 약국",
    "Address": "서울특별시 용산구 새창로 70 212호 (도원동, 도원동삼성래미안)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQxMyQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "용산오늘약국",
    "Address": "서울특별시 용산구 새창로 217 용산토투밸리 1층 (한강로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQzIyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "이촌사랑약국",
    "Address": "서울특별시 용산구 이촌로 300 제1호 (이촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQzIyQwMCQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "2층써밋약국",
    "Address": "서울특별시 용산구 한강대로 69 상가동 2층 222-2호 (한강로2가, 용산푸르지오써밋)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "이촌약국",
    "Address": "서울특별시 용산구 이촌로 224 301호 (이촌동, 리버뷰맨션)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ5IyQwMCQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "우리서울약국",
    "Address": "서울특별시 용산구 한강대로 95 2층 207호 (한강로2가, 래미안용산)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQxMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "분홍약국",
    "Address": "서울특별시 용산구 녹사평대로32길 47 1층 (이태원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ5MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "시온약국",
    "Address": "서울특별시 용산구 독서당로 67 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ5OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "미라클약국",
    "Address": "서울특별시 용산구 한강대로 259 109호 (갈월동, 고려에이트리움)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "나음약국",
    "Address": "서울특별시 용산구 한강대로 95 제지하1층 제1비157호 (한강로2가, 래미안용산 더 센트럴)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "메디팜미래로약국",
    "Address": "서울특별시 용산구 청파로47길 40 (청파동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "3층 파란문 약국",
    "Address": "서울특별시 용산구 한강대로 69 3층 305-1호 (한강로2가, 용산푸르지오써밋)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "신세계약국",
    "Address": "서울특별시 용산구 장문로 94 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ2MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "용산약국",
    "Address": "서울특별시 용산구 한강대로 92 지층 (한강로2가, LS용산타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ2MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "세계약국",
    "Address": "서울특별시 용산구 원효로 171 (원효로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQxMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "가장큰태평양약국",
    "Address": "서울특별시 용산구 대사관로 52 1층 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQxMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "다니엘약국",
    "Address": "서울특별시 용산구 이촌로 103 1층 (한강로3가, 천일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 용산구 대사관로 60 1층 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ3MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "건강한약국",
    "Address": "서울특별시 용산구 효창원로93길 2 (청파동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "사랑온누리약국",
    "Address": "서울특별시 용산구 이촌로 224 2층 207,208,219호 (이촌동, 리버뷰맨션)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQxMyQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "사랑플러스약국",
    "Address": "서울특별시 용산구 한강대로 258 (남영동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQxMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "실로암약국",
    "Address": "서울특별시 용산구 청파로 101 10동 특1호 (한강로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQxMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "가까운우리약국",
    "Address": "서울특별시 용산구 대사관로31길 7-10 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "하이약국",
    "Address": "서울특별시 용산구 한강대로 256 1층 (남영동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "숙명온누리약국",
    "Address": "서울특별시 용산구 청파로47길 66 (청파동2가, 중하빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "부자약국",
    "Address": "서울특별시 용산구 대사관로30가길 1 1층 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "참온누리약국",
    "Address": "서울특별시 용산구 신흥로 150-1 (후암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "대한당약국",
    "Address": "서울특별시 용산구 우사단로10길 42 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "굿윌정약국",
    "Address": "서울특별시 용산구 후암로 47 1층 (후암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ5MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "새평화약국",
    "Address": "서울특별시 용산구 후암로57길 37 1층 (동자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQwMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "소명약국",
    "Address": "서울특별시 용산구 우사단로 43 (이태원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "명진약국",
    "Address": "서울특별시 용산구 신흥로36길 1 (후암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "보현온누리약국",
    "Address": "서울특별시 용산구 신흥로20길 1 (용산동2가, 세명치과)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "새서부약국",
    "Address": "서울특별시 용산구 한강대로 293 (갈월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "신명약국",
    "Address": "서울특별시 용산구 후암로28길 38 남산리치빌 (후암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "우정약국",
    "Address": "서울특별시 용산구 백범로 341 A동 315호 (원효로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "풍전약국",
    "Address": "서울특별시 용산구 원효로25길 31 (원효로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "삼정약국",
    "Address": "서울특별시 용산구 원효로19길 72-1 1층 (원효로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQxMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "보림사약국",
    "Address": "서울특별시 용산구 한강대로62나길 20 (용산동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "신정제약국",
    "Address": "서울특별시 용산구 한강대로 50 (한강로3가, 신정재약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQyIyQ1IyQwMCQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "임상약국",
    "Address": "서울특별시 용산구 이촌로14길 16 (이촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQxMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "메디팜최약국",
    "Address": "서울특별시 용산구 청파로 324 1층 (청파동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQxMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "온누리정도약국",
    "Address": "서울특별시 용산구 원효로53길 9 (원효로2가, 정도약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQwMyQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "편한약국",
    "Address": "서울특별시 용산구 이촌로 303 107호 (이촌동, 현대아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "수명약국",
    "Address": "서울특별시 용산구 신흥로 141 (용산동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "신용산약국",
    "Address": "서울특별시 용산구 한강대로15길 9-18 (한강로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQyIyQxIyQwMCQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "가정약국",
    "Address": "서울특별시 용산구 청파로 333 (청파동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQwMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "금보약국",
    "Address": "서울특별시 용산구 원효로 51 110호 (산천동, 삼성테마트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "경인약국",
    "Address": "서울특별시 용산구 새창로14길 50 (용문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "한국약국",
    "Address": "서울특별시 용산구 이촌로 303 21동 112호 (이촌동, 현대아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "동오약국",
    "Address": "서울특별시 용산구 보광로 18 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQyIyQ1IyQwMCQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "메디팜한진약국",
    "Address": "서울특별시 용산구  이촌로18길 5 (이촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ2MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "한라약국",
    "Address": "서울특별시 용산구 보광로 124 (이태원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "팜그린약국",
    "Address": "서울특별시 용산구 청파로 74 전자랜드 1층 A147호 (한강로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQwMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "명진당약국",
    "Address": "서울특별시 용산구 청파로 387 (서계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ3MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "다정약국",
    "Address": "서울특별시 용산구 한강대로104길 51 1층 (동자동, 남영빌딩(제1호))"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "삼희약국",
    "Address": "서울특별시 용산구 한강대로 68 1층 (한강로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 용산구 한강대로 312 2층 (갈월동, 하나은행, 우태하피부과, 서울약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ1IyQwMCQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "힐링약국",
    "Address": "서울특별시 용산구 신흥로 53 1층 (용산동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ3MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "세브레스약국",
    "Address": "서울특별시 용산구 대사관로 56 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "온누리백합약국",
    "Address": "서울특별시 용산구 후암로 33-3 1층 (후암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "보광프라자약국",
    "Address": "서울특별시 용산구 보광로 35 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 용산구 후암로 43-2 1층 (후암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "기영약국",
    "Address": "서울특별시 용산구 대사관로31길 7-5 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "동부약국",
    "Address": "서울특별시 용산구 이촌로 245 (이촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "수복약국",
    "Address": "서울특별시 용산구 새창로12길 12 (도원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "이층성장약국",
    "Address": "서울특별시 용산구 이촌로 224 210-1, 209, 217호 (이촌동, 한강쇼핑센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQxMyQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "성도약국",
    "Address": "서울특별시 용산구 회나무로 25 (이태원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "용산대학약국",
    "Address": "서울특별시 용산구 대사관로 58 용산대학약국 1층 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "한남더힐한약국",
    "Address": "서울특별시 용산구 한남대로46길 26 1층 1호 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "용약국",
    "Address": "서울특별시 용산구 대사관로24길 6 (한남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQyIyQ1IyQwMCQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "신효창프라자약국",
    "Address": "서울특별시 용산구 백범로 285 (효창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQwMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "정화약국",
    "Address": "서울특별시 용산구 두텁바위로 11 (갈월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQyIyQ1IyQwMCQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "인원약국",
    "Address": "서울특별시 용산구 신흥로20길 5 (용산동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "센트럴파란문약국",
    "Address": "서울특별시 용산구 한강대로 95 2층 RB208-1호 (한강로2가, 래미안용산 더 센트럴)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "알파약국",
    "Address": "서울특별시 용산구 보광로 46 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "신용산수약국",
    "Address": "서울특별시 용산구 한강대로 109 용성비즈텔 지하2층 227,233호 (한강로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "효창약국",
    "Address": "서울특별시 용산구 백범로 259 지층 (효창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "현대온누리약국",
    "Address": "서울특별시 용산구 이촌로 280 1층 1호 (이촌동, 명지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQwMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "구온누리약국",
    "Address": "서울특별시 용산구 만리재로 134 1층 (서계동, 힐타워빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQwMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "연희온누리약국",
    "Address": "서울특별시 용산구 한강대로 297 2층 (갈월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "서안약국",
    "Address": "서울특별시 용산구 효창원로 142 (효창동, 중앙병원)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ3MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "시티온누리약국",
    "Address": "서울특별시 용산구 한강대로 283 (갈월동, 시티파크타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ2MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "백경약국",
    "Address": "서울특별시 용산구 원효로41길 38 (원효로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQzIyQ5MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "구일온누리약국",
    "Address": "서울특별시 용산구 이촌로 303 21동 109호 (이촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "승현약국",
    "Address": "서울특별시 용산구 효창원로 271-1 (서계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "예사랑약국",
    "Address": "서울특별시 용산구 이촌로 352 103호 (용산동6가, 신동아쇼핑)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "신우성약국",
    "Address": "서울특별시 용산구 한강대로77길 10 (갈월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "정다운약국",
    "Address": "서울특별시 용산구 원효로 155 1층 (원효로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQxMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "소아제일약국",
    "Address": "서울특별시 용산구 청파로 383-8 (서계동, 청운가든)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "카카오약국 cacao pharmacy",
    "Address": "서울특별시 용산구 녹사평대로40길 63 1층 (이태원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 용산구 한강대로23길 55 아이파크몰 리빙파크 6층 218호 (한강로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신진약국",
    "Address": "서울특별시 용산구 우사단로 2-1 1층 104호 (보광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "공감365온누리약국",
    "Address": "서울특별시 용산구 한강대로 100 아모레퍼시픽 지하1층 B106-2호 (한강로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ2MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "래미안스타약국",
    "Address": "서울특별시 용산구 한강대로 95 지하2층 RB208호 (한강로2가, 래미안용산)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQxMyQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "대성옵티마약국",
    "Address": "서울특별시 용산구 회나무로 23 (이태원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ5OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "홍주약국",
    "Address": "서울특별시 용산구 이촌로 206 3층 (이촌동, 국민은행PB센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ5MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 은평구 은평터널로 196 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ4MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "홍약국",
    "Address": "서울특별시 은평구 연서로 246 203호 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ5OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "더행복약국",
    "Address": "서울특별시 은평구 은평로 200-1 가동 1층 (응암동, 삼영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "팜스토리약국",
    "Address": "서울특별시 은평구 은평로 111 은평이마트 8층 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQwMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "새우리약국",
    "Address": "서울특별시 은평구 통일로 715 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "동산약국",
    "Address": "서울특별시 은평구 통일로87길 5 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ3MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "푸른솔약국",
    "Address": "서울특별시 은평구 통일로87길 12 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "참진약국",
    "Address": "서울특별시 은평구 역말로 40 무궁화빌딩 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 은평구 진관4로 17 820동 1층 113호 (진관동, 은평뉴타운상림마을)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "소망온누리약국",
    "Address": "서울특별시 은평구 가좌로5길 22-1 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ5IyQwMCQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 은평구 응암로 162 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ5MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "하나로약국",
    "Address": "서울특별시 은평구 연서로 277-1 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "연도약국",
    "Address": "서울특별시 은평구 은평로 144 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQxMyQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "베드로약국",
    "Address": "서울특별시 은평구 통일로 709 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "연세희망약국",
    "Address": "서울특별시 은평구 연서로 175 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 은평구 은평로 197-2 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "은평자연약국",
    "Address": "서울특별시 은평구 서오릉로 162 1층 103호 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜경약국",
    "Address": "서울특별시 은평구 응암로22길 15-1 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQxMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "하이팜약국",
    "Address": "서울특별시 은평구 통일로 1050 2층 (진관동, 롯데마트은평점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ3OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "조일약국",
    "Address": "서울특별시 은평구 연서로34길 7 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ3OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "상쾌한온누리약국",
    "Address": "서울특별시 은평구 역말로 101 토마스빌딩 101호 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ5OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "연서메디칼약국",
    "Address": "서울특별시 은평구 연서로 253-9 1층 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQyIyQ1IyQwMCQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "기림약국",
    "Address": "서울특별시 은평구 응암로22길 8 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ2MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "은평온누리약국",
    "Address": "서울특별시 은평구 은평로 170 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "조아약국",
    "Address": "서울특별시 은평구 응암로 223 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "메디팜삼보약국",
    "Address": "서울특별시 은평구 연서로 332 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "참조은약국",
    "Address": "서울특별시 은평구 증산로 297 (증산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQyIyQzIyQwMCQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "세원약국",
    "Address": "서울특별시 은평구 갈현로 8 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "청우약국",
    "Address": "서울특별시 은평구 은평로9길 13 103호 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "메디팜건강약국",
    "Address": "서울특별시 은평구 수색로 270-1 (수색동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ4MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "수민약국",
    "Address": "서울특별시 은평구 연서로 222 102호 (대조동, 유니온빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "유진약국",
    "Address": "서울특별시 은평구 서오릉로 166 유풍빌딩 1층 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQxMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 은평구 불광로 54 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "오온누리약국",
    "Address": "서울특별시 은평구 진흥로 97 1층 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQwMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "장수약국",
    "Address": "서울특별시 은평구 응암로 248 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "성환약국",
    "Address": "서울특별시 은평구 진흥로1길 23 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 은평구 서오릉로 138 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ5OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "신명약국",
    "Address": "서울특별시 은평구 은평로 226 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "메디팜새경약국",
    "Address": "서울특별시 은평구 갈현로 87 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "정다운온누리약국",
    "Address": "서울특별시 은평구 갈현로 260 1층 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 은평구 응암로 323 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 은평구 통일로 842 범서빌딩 2층 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "녹번온누리약국",
    "Address": "서울특별시 은평구 통일로 626 유림빌딩 101호 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "시민약국",
    "Address": "서울특별시 은평구 은평로 136 은경빌딩 104호 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 은평구 불광로 27 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQxMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "밝은미소약국",
    "Address": "서울특별시 은평구 갈현로 15 1층 103호 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQxMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "불광다올약국",
    "Address": "서울특별시 은평구 통일로 728 1층 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ2MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "기린약국",
    "Address": "서울특별시 은평구 서오릉로 79 아름빌딩 1층 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ2MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "미도파약국",
    "Address": "서울특별시 은평구 응암로 264 서울빌딩 1층 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "원약국",
    "Address": "서울특별시 은평구 은평로 121 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQxMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "곰약국",
    "Address": "서울특별시 은평구 연서로 73 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "불광온누리약국",
    "Address": "서울특별시 은평구 통일로 732 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "증산약국",
    "Address": "서울특별시 은평구 증산로3길 6 (증산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "바로약국",
    "Address": "서울특별시 은평구 통일로 723-1 제일쇼핑 2층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQxMyQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "청구프라자약국",
    "Address": "서울특별시 은평구 통일로83길 5-6 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "해오름온누리약국",
    "Address": "서울특별시 은평구 응암로 215 103호 (응암동, 명남더블레스아파트2차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "명성약국",
    "Address": "서울특별시 은평구 통일로 805 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ4OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 은평구 연서로 35 1층 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "애플약국",
    "Address": "서울특별시 은평구 진관2로 57-7 B106호 (진관동, 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ5OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "초록약국",
    "Address": "서울특별시 은평구 수색로 191 (증산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "경하프라자약국",
    "Address": "서울특별시 은평구 서오릉로 157 (구산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ2MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "온누리연세약국",
    "Address": "서울특별시 은평구 연서로 181 1층 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQxMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "성실약국",
    "Address": "서울특별시 은평구 갈현로11길 26 지층 (구산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ2MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 은평구 은평로 193-2 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQwMyQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "은빛약국",
    "Address": "서울특별시 은평구 통일로87길 2 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "행복이꽃피는약국",
    "Address": "서울특별시 은평구 가좌로 271 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "안녕약국",
    "Address": "서울특별시 은평구 불광로 119 불광빌딩 1층 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "은평천사약국",
    "Address": "서울특별시 은평구 통일로 1034 1,2층 135,136,137,226,227호 (진관동, 은평스카이뷰자이)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "성모자이약국",
    "Address": "서울특별시 은평구 통일로 1034 1층 129,130,131호 (진관동, 은평스카이뷰자이)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "가까운우리약국",
    "Address": "서울특별시 은평구 통일로 1031 1층 101호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "봄햇살약국",
    "Address": "서울특별시 은평구 통일로 833 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "주차편한약국",
    "Address": "서울특별시 은평구 통일로 1030 은평헤스티아 지하1층 103,104호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "은혜성모약국",
    "Address": "서울특별시 은평구 통일로 1030 은평헤스티아 103호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "구파발성모약국",
    "Address": "서울특별시 은평구 진관2로 12 메이플카운티2차 1층 108호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ5MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "노벨온누리약국",
    "Address": "서울특별시 은평구 연서로 1 105호 (역촌동, 리더스파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "솔약국",
    "Address": "서울특별시 은평구 진관4로 77 702동 113호 (진관동, 은평뉴타운상림마을)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "은평오렌지약국",
    "Address": "서울특별시 은평구 진관2로 29-21 113,114호 (진관동, 드림스퀘어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "아름다운달과별약국",
    "Address": "서울특별시 은평구 통일로 855-8 (갈현동, 연신내진원와이타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ2MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "호호약국",
    "Address": "서울특별시 은평구 서오릉로 139 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "유성약국",
    "Address": "서울특별시 은평구 통일로 741 2층 (대조동, 이연빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "메디팜승윤약국",
    "Address": "서울특별시 은평구 가좌로 325 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "한겨레약국",
    "Address": "서울특별시 은평구 연서로 219 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "뉴타운메디컬약국",
    "Address": "서울특별시 은평구 진관3로 70 821동 상가 115호 (진관동, 은평뉴타운상림마을)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQxMyQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "메디팜상록약국",
    "Address": "서울특별시 은평구 서오릉로 191 1층 (구산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ2MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 은평구 진흥로 133 1층 101호 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQwMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "다온약국",
    "Address": "서울특별시 은평구 은평로 123 1층 101호 (응암동, 응암아네스트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "가톨릭정문약국",
    "Address": "서울특별시 은평구 통일로 1031 1층 102호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQwMyQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "신사프라자약국",
    "Address": "서울특별시 은평구 갈현로 16 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신보광사약국",
    "Address": "서울특별시 은평구 통일로 725-2 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ2MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "구세약국",
    "Address": "서울특별시 은평구 응암로 181 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ5OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "건강밝은약국",
    "Address": "서울특별시 은평구 연서로 216 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ3OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "고일약국",
    "Address": "서울특별시 은평구 증산로3길 8 (증산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ4OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "온누리민생약국",
    "Address": "서울특별시 은평구 통일로87길 5-10 1층 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ4MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "세종약국",
    "Address": "서울특별시 은평구 불광로 25 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ5OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "예일태평양약국",
    "Address": "서울특별시 은평구 연서로 137 (구산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQwMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "새응암온누리약국",
    "Address": "서울특별시 은평구 응암로 183 1층 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "대조약국",
    "Address": "서울특별시 은평구 서오릉로 140 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ2MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "연세스타약국",
    "Address": "서울특별시 은평구 연서로 183-12 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "정문온누리약국",
    "Address": "서울특별시 은평구 진흥로 196 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQxMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "수플러스온누리약국",
    "Address": "서울특별시 은평구 연서로 146 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQwMyQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "천사약국",
    "Address": "서울특별시 은평구 통일로 856 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "보건약국",
    "Address": "서울특별시 은평구 증산로9길 3 1층 101호 (증산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQyIyQ3IyQwMCQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "믿음메디칼약국",
    "Address": "서울특별시 은평구 응암로 213 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "이레약국",
    "Address": "서울특별시 은평구 통일로 738 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "고은약국",
    "Address": "서울특별시 은평구 은평로 8 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 은평구 불광로 104 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "새서울약국",
    "Address": "서울특별시 은평구 서오릉로 134 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQwMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 은평구 진관3로 20 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "성모제일약국",
    "Address": "서울특별시 은평구 통일로 1030 은평헤스티아 102, 202호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "큰사랑온누리약국",
    "Address": "서울특별시 은평구 서오릉로 149 (구산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "일호약국",
    "Address": "서울특별시 은평구 서오릉로 211 (구산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "불광프라자약국",
    "Address": "서울특별시 은평구 불광로 17 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "연신종로약국",
    "Address": "서울특별시 은평구 연서로32길 3 (불광동, 남재빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ3MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "대림약국",
    "Address": "서울특별시 은평구 은평터널로 65 101호,110호 (수색동, 대림한숲타운아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "우리사랑약국",
    "Address": "서울특별시 은평구 은평로 108 1층 103호 (응암동, 메트로럭스주상복합APT)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "은평이화약국",
    "Address": "서울특별시 은평구 응암로22길 22 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQxMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "건강한세상약국",
    "Address": "서울특별시 은평구 증산로15길 7 (증산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "사랑온누리약국",
    "Address": "서울특별시 은평구 서오릉로 46 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQxMyQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "형제약국",
    "Address": "서울특별시 은평구 가좌로 241 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "홍문약국",
    "Address": "서울특별시 은평구 통일로 724 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "제일프라자약국",
    "Address": "서울특별시 은평구 갈현로 82 303호 (역촌동, 제일프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "제안약국",
    "Address": "서울특별시 은평구 연서로11길 19 (구산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "수정약국",
    "Address": "서울특별시 은평구 응암로 328 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ3OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "정다운약국",
    "Address": "서울특별시 은평구 진흥로 137 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQxMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "큰솔약국",
    "Address": "서울특별시 은평구 연서로 12 청암빌딩 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "보은당약국",
    "Address": "서울특별시 은평구 응암로22길 28-6 1층 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 은평구 통일로 875 (갈현동, 흥진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 은평구 갈현로 257 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "타운약국",
    "Address": "서울특별시 은평구 통일로 855-8 연신내진원와이타운 102호 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "우리정다운약국",
    "Address": "서울특별시 은평구 갈현로41길 10-1 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ2MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 은평구 은평로 5 1층 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ1IyQwMCQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "태정온누리약국",
    "Address": "서울특별시 은평구 진관2로 15-46 108,109호 (진관동, 메트로프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "초원약국",
    "Address": "서울특별시 은평구 은평로10길 4 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQwMyQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "신세계약국",
    "Address": "서울특별시 은평구 진흥로12길 3 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQyIyQzIyQwMCQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "연신내영재약국",
    "Address": "서울특별시 은평구 연서로 246 (불광동, 타워클리닉)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "속편한약국",
    "Address": "서울특별시 은평구 갈현로 206 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQwMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "가나약국",
    "Address": "서울특별시 은평구 서오릉로 46 201동  상가 104호 (녹번동, 녹번2차 현대아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜대원약국",
    "Address": "서울특별시 은평구 진흥로1길 2 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "시장약국",
    "Address": "서울특별시 은평구 연서로 257 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 은평구 통일로 871 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ2MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "건강한약국",
    "Address": "서울특별시 은평구 진관2로 57 B105호 (진관동, 은평뉴타운우물골)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "열린프라자약국",
    "Address": "서울특별시 은평구 통일로 750 (불광동, 경일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "희래약국",
    "Address": "서울특별시 은평구 서오릉로18길 6-17 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "대우약국",
    "Address": "서울특별시 은평구 통일로 749 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ5OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "아람한약국",
    "Address": "서울특별시 은평구 은평로 96 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "조은백화점약국",
    "Address": "서울특별시 은평구 응암로 201 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "신우리약국",
    "Address": "서울특별시 은평구 가좌로 329 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ5OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신일약국",
    "Address": "서울특별시 은평구 은평로 156 1층 101호 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQwMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 은평구 서오릉로 41-17 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "맑은약국",
    "Address": "서울특별시 은평구 진관2로 57-7 253동 104호 (진관동, 은평뉴타운우물골)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "가람약국",
    "Address": "서울특별시 은평구 통일로 1030 은평헤스티아 1,2층 101, 201호호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 은평구 서오릉로2길 17-5 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQyIyQ3IyQwMCQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신바오로약국",
    "Address": "서울특별시 은평구 통일로 1030 은평헤스티아 1층 111,112호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "영창당약국",
    "Address": "서울특별시 은평구 통일로 843 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "민들레약국",
    "Address": "서울특별시 은평구 응암로 179 1층 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "녹번건강약국",
    "Address": "서울특별시 은평구 통일로 630-1 지하1층 B101-1호 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "왕약국",
    "Address": "서울특별시 은평구 은평로 137 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "디엠씨4번출구약국",
    "Address": "서울특별시 은평구 수색로 175 1층 003호 (증산동, 6호선 디지털미디어시티역)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "행복약국",
    "Address": "서울특별시 은평구 은평로 52-3 1층 (신사동, 홍인근생주택)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQxMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "백련산 허준약국",
    "Address": "서울특별시 은평구 응암로 196 1층 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "새종로약국",
    "Address": "서울특별시 은평구 응암로 226-1 (응암동, 한양빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ3OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "한솔약국",
    "Address": "서울특별시 은평구 갈현로 14 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "유승약국",
    "Address": "서울특별시 은평구 역말로9길 1 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 은평구 증산서길 73 (증산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "응암프라자약국",
    "Address": "서울특별시 은평구 응암로 192 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "이정약국",
    "Address": "서울특별시 은평구 갈현로33길 27 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 은평구 연서로 331-1 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "소원약국",
    "Address": "서울특별시 은평구 수색로 256 (수색동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "선우약국",
    "Address": "서울특별시 은평구 은평로 52 (신사동, 명성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "신사새서울약국",
    "Address": "서울특별시 은평구 은평로 29 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "예사랑온누리약국",
    "Address": "서울특별시 은평구 갈현로11길 43 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "정온누리약국",
    "Address": "서울특별시 은평구 서오릉로 196 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "효제메디컬약국",
    "Address": "서울특별시 은평구 서오릉로 204 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "은평제일약국",
    "Address": "서울특별시 은평구 불광로 60 104호 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "함께하는약국",
    "Address": "서울특별시 은평구 수색로 264-1 (수색동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQyIyQxIyQwMCQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 은평구 진관4로 48-17 103호 (진관동, 은평뉴타운상림마을821동상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "연신내메디칼약국",
    "Address": "서울특별시 은평구 연서로 246 104호 (불광동, 타워크리닉)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "예진약국",
    "Address": "서울특별시 은평구 갈현로 81 (역촌동, 그린빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "연신우리약국",
    "Address": "서울특별시 은평구 통일로 839 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ2MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "온누리새소망약국",
    "Address": "서울특별시 은평구 은평터널로 65 1-3, 2-2호 (수색동, 대림한숲타운아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQwMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "남대문약국",
    "Address": "서울특별시 은평구 통일로87길 19 1층 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 은평구 통일로 1030 은평헤스티아 B101호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "은나라약국",
    "Address": "서울특별시 은평구 갈현로 258 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQxMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "건강샘약국",
    "Address": "서울특별시 은평구 갈현로 300 206호 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "영약국",
    "Address": "서울특별시 은평구 은평로10길 5 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "은평메디칼약국",
    "Address": "서울특별시 은평구 백련산로 91 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "미르약국",
    "Address": "서울특별시 은평구 백련산로 84 211호 (응암동, 백련산 힐스테이트 2차(211동상가))"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "구산이화약국",
    "Address": "서울특별시 은평구 서오릉로 217-5 (구산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "청수약국",
    "Address": "서울특별시 은평구 진흥로 150 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "은평프라자약국",
    "Address": "서울특별시 은평구 증산로15길 6 (신사동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "해맑은약국",
    "Address": "서울특별시 은평구 응암로 188-1 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQwMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "서부새생명약국",
    "Address": "서울특별시 은평구 역말로 72 (역촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQwMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "청룡중앙약국",
    "Address": "서울특별시 은평구 가좌로 233 연희타워 103호 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ3OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "제민약국",
    "Address": "서울특별시 은평구 갈현로 253 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQwMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "유정약국",
    "Address": "서울특별시 은평구 연서로 258 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "큰사랑약국",
    "Address": "서울특별시 은평구 응암로 166 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 은평구 통일로 863 (갈현동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "불광우리들약국",
    "Address": "서울특별시 은평구 통일로 710 (불광동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQxMyQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "진호메디칼약국",
    "Address": "서울특별시 은평구 통일로 723 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQwMyQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 은평구 응암로 248-1 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQwMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "올리브약국",
    "Address": "서울특별시 은평구 응암로 308 (응암동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 은평구 서오릉로 203 (구산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "365미소약국",
    "Address": "서울특별시 은평구 진관3로 11 1층 (진관동, 은평뉴타운 힐데스하임)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "이층약국",
    "Address": "서울특별시 은평구 연서로 9 2층 205(상가)호 (역촌동, 센타폴리스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "365구생약국",
    "Address": "서울특별시 은평구 통일로 739 1층 (대조동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "어진온누리약국",
    "Address": "서울특별시 은평구 진관2로 19 107호 (진관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 은평구 은평로 219 1층 (녹번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "태평양리드팜약국",
    "Address": "서울특별시 은평구 응암로 235 (응암동, 대성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ4OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 종로구 지봉로 37-1 1층 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "건강한세상약국",
    "Address": "서울특별시 종로구 새문안로 21 (평동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "경희궁햇살약국",
    "Address": "서울특별시 종로구 송월길 99 203동 2218호 (홍파동, 경희궁자이 2단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "종로수약국",
    "Address": "서울특별시 종로구 종로 226 송화빌딩 1층 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "서울혜화약국",
    "Address": "서울특별시 종로구 대학로 123 1층, 2층일부 (명륜4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "대명약국",
    "Address": "서울특별시 종로구 종로 256-1 대명빌딩 1층 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "유한약국",
    "Address": "서울특별시 종로구 종로 230-2 1층 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "내자약국",
    "Address": "서울특별시 종로구 사직로 107 1층 (내자동, 한빛빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQ3IyQwMCQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "잔소리약국",
    "Address": "서울특별시 종로구 창덕궁1길 31 지층 (계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "우정약국",
    "Address": "서울특별시 종로구 종로 200-4 제우빌딩 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "광교약국",
    "Address": "서울특별시 종로구 청계천로 49 (관철동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "성진약국",
    "Address": "서울특별시 종로구 창경궁로 271-1 (혜화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQzIyQxMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "옥인온누리약국",
    "Address": "서울특별시 종로구 자하문로2길 4 103호 (적선동, 경복빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ4OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "수도약국",
    "Address": "서울특별시 종로구 인사동길 40 (관훈동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "민약국",
    "Address": "서울특별시 종로구 사직로12길 26 (내자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ2MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "동서약국",
    "Address": "서울특별시 종로구 종로 222 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "종로세란약국",
    "Address": "서울특별시 종로구 종로41길 4 (종로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 종로구 창경궁로34길 18-5 1층 (명륜2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 종로구 경교장길 35 3136호 (평동, 경희궁자이 3단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "혜화약국",
    "Address": "서울특별시 종로구 혜화로 8 (혜화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "종오약국",
    "Address": "서울특별시 종로구 종로 195-1 1층 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ2MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 종로구 혜화로 2 1층 (혜화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "종로온누리약국",
    "Address": "서울특별시 종로구 종로 293 1층 (창신동, 하나저축은행)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 종로구 종로 335 1층 (창신동, 원풍빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "숭인약국",
    "Address": "서울특별시 종로구 종로 407 (숭인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ2MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "백화점약국",
    "Address": "서울특별시 종로구 종로 234-1 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ5OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "단골온누리약국",
    "Address": "서울특별시 종로구 지봉로 50 (숭인동, 필빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ4OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "지영오행당약국",
    "Address": "서울특별시 종로구 성균관로 32-2 (명륜2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ3OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 종로구 창경궁로 158 (원남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "효성약국",
    "Address": "서울특별시 종로구 창신길 95 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "동인약국",
    "Address": "서울특별시 종로구 창신길 11 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "이약국",
    "Address": "서울특별시 종로구 지봉로 43 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ2MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "시민약국",
    "Address": "서울특별시 종로구 자하문로 2 (적선동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ2MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "새현대약국",
    "Address": "서울특별시 종로구 사직로 130 38호 (적선동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "연약국",
    "Address": "서울특별시 종로구 종로 137 2층 (종로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ4MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "청자약국",
    "Address": "서울특별시 종로구 명륜길 70 (명륜3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "동호약국",
    "Address": "서울특별시 종로구 성균관로 53 (명륜3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQyIyQxIyQwMCQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "한독약국",
    "Address": "서울특별시 종로구 동숭길 52 (동숭동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQwMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "대경약국",
    "Address": "서울특별시 종로구 종로51나길 2 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "정성약국",
    "Address": "서울특별시 종로구 종로 399 (숭인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQyIyQ1IyQwMCQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "승보약국",
    "Address": "서울특별시 종로구 종로 162 1층 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQwMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "서울종로약국",
    "Address": "서울특별시 종로구 대학로 117 (명륜4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQzIyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "올리브약국",
    "Address": "서울특별시 종로구 새문안로 91 지하1층 (신문로1가, 고려빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "종각3층다정약국",
    "Address": "서울특별시 종로구 종로 70 3층 (관철동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "명문약국",
    "Address": "서울특별시 종로구 통일로 254 1층 (무악동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQyIyQxIyQwMCQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "충신약국",
    "Address": "서울특별시 종로구 율곡로 259 (충신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQyIyQ1IyQwMCQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "인성약국",
    "Address": "서울특별시 종로구 통일로 250 (무악동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "송이약국",
    "Address": "서울특별시 종로구 종로 19 르메이에르종로타운1 2층 206-1호 (종로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ3OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "새종로약국",
    "Address": "서울특별시 종로구 종로 199-2 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "푸른소나무약국",
    "Address": "서울특별시 종로구 삼봉로 81 207호 (수송동, 두산위브파빌리온)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "온유약국",
    "Address": "서울특별시 종로구 종로 205 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "신백제약국",
    "Address": "서울특별시 종로구 종로 243 1층 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "신세계약국",
    "Address": "서울특별시 종로구 종로 124-1 (종로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "숭인다모아약국",
    "Address": "서울특별시 종로구 지봉로8길 54 (숭인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 종로구 경교장길 35 3137호 (평동, 경희궁자이 3단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQxMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "금왕약국",
    "Address": "서울특별시 종로구 창신5길 19 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ5MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "유성약국",
    "Address": "서울특별시 종로구 동호로 408 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "정민약국",
    "Address": "서울특별시 종로구 대학로9길 37 (명륜4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ4MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 종로구 자하문로17길 23 (통인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "삼원약국",
    "Address": "서울특별시 종로구 새문안로 103-1 1층 (신문로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "창신종로약국",
    "Address": "서울특별시 종로구 창신길 47 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQxMyQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 종로구 대학로5길 53 1층 (연건동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "송송약국",
    "Address": "서울특별시 종로구 종로 19 르메이에르종로타운1 1층 116-1호 (종로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "따뜻한약국",
    "Address": "서울특별시 종로구 종로 19 르메이에르종로타운1 304-1호 (종로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "세종약국",
    "Address": "서울특별시 종로구 세종대로23길 54 세종빌딩 지하1층 130호 (당주동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "하트약국",
    "Address": "서울특별시 종로구 대학로 128 1층 (동숭동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQwMyQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "열린온누리약국",
    "Address": "서울특별시 종로구 숭인동길 21 (숭인동, 종로청계힐스테이트상가 가동 101호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQxMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "신두산약국",
    "Address": "서울특별시 종로구 지봉로 39-1 1층 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "종로백세약국",
    "Address": "서울특별시 종로구 종로 221 1층 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQxMyQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "대서울약국",
    "Address": "서울특별시 종로구 창경궁로 158 2층 (원남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "서울온누리약국",
    "Address": "서울특별시 종로구 대학로5길 54 1층 (연건동, 우욱하우스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "참조은약국",
    "Address": "서울특별시 종로구 종로 266 동대문종합시장 A동 7층 705호 (종로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQwMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 종로구 종로 204 1,2층 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "동아약국",
    "Address": "서울특별시 종로구 종로 192 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQwMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "종로우리약국",
    "Address": "서울특별시 종로구 종로 202 1층 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "파랑새약국",
    "Address": "서울특별시 종로구 대학로 121 1층 (명륜4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "정다운약국",
    "Address": "서울특별시 종로구 종로 339 1층 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "엄마약국",
    "Address": "서울특별시 종로구 종로 193-1 1층 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "정원약국",
    "Address": "서울특별시 종로구 통일로 262 4호 1층 (무악동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "세검정약국",
    "Address": "서울특별시 종로구 세검정로6길 104 1층 (신영동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "종로백제약국",
    "Address": "서울특별시 종로구 종로 235 백제약국 1층 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "신서대문대학약국",
    "Address": "서울특별시 종로구 경교장1길 1 1,2층 (교남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "종로오가약국",
    "Address": "서울특별시 종로구 종로 213-1 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ3MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "성심약국",
    "Address": "서울특별시 종로구 지봉로 61 1층 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQwMyQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "옥광약국",
    "Address": "서울특별시 종로구 창경궁로 162-1 (원남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "종로5가미래약국",
    "Address": "서울특별시 종로구 종로 211-1 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 종로구 종로 33 지하1층 B104호 (청진동, 그랑서울)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "엄약국",
    "Address": "서울특별시 종로구 종로 227 (종로5가, 엄약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "동대문연약국",
    "Address": "서울특별시 종로구 종로 272 동대문종합시장 신관 신관동 지하1층 018호 (종로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ4OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "창신사랑온누리약국",
    "Address": "서울특별시 종로구 지봉로 77-3 1층 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "힐링약국",
    "Address": "서울특별시 종로구 종로5길 13 삼공빌딩 지하1층 (청진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ4OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "현대온누리약국",
    "Address": "서울특별시 종로구 율곡로 75 지하1층 (계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "메디칼서울약국",
    "Address": "서울특별시 종로구 대학로9길 6 (명륜4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "세검약국",
    "Address": "서울특별시 종로구 자하문로 306 (홍지동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 종로구 자하문로 58 1층 (창성동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "보광약국",
    "Address": "서울특별시 종로구 대학로 93-3 1층 (연건동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQwMyQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "대도약국",
    "Address": "서울특별시 종로구 우정국로 38-1 1층 (견지동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신아산약국",
    "Address": "서울특별시 종로구 종로 255-2 1층 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "신동화약국",
    "Address": "서울특별시 종로구 종로 267-1 (종로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "성당약국",
    "Address": "서울특별시 종로구 수표로 115 1층 (낙원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQxMyQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "종로약국",
    "Address": "서울특별시 종로구 종로 195 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "새동서약국",
    "Address": "서울특별시 종로구 동호로 403 19호 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "국일약국",
    "Address": "서울특별시 종로구 종로16길 12 (관철동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "새성은약국",
    "Address": "서울특별시 종로구 돈화문로 35-1 103호 (묘동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ3OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "종근당약국",
    "Address": "서울특별시 종로구 종로 230-1 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQxMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "국화약국",
    "Address": "서울특별시 종로구 평창11길 3 1층 (평창동, 쇼핑센타뉴본)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQxMyQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 종로구 종로 115 403호 (종로3가, 낙원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "믿음약국",
    "Address": "서울특별시 종로구 종로 335-1 지하1층 (창신동, 명제빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "파란문약국",
    "Address": "서울특별시 종로구 송월길 155 1층 4112, 4113호 (교북동, 경희궁자이 4단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "바로약국",
    "Address": "서울특별시 종로구 종로 33 지하1층 137호 (청진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQyIyQzIyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "함춘약국",
    "Address": "서울특별시 종로구 대학로 93 대한성공회 대학로교회 1,2층 (연건동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQwMyQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "소담약국",
    "Address": "서울특별시 종로구 성균관로 18 (명륜2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ2MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "경일약국",
    "Address": "서울특별시 종로구 평창문화로 35 (평창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ2MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "동시약국",
    "Address": "서울특별시 종로구 종로 202-1 (종로4가, 동흥빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "광장약국",
    "Address": "서울특별시 종로구 창경궁로13길 1 1층 (예지동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "대박약국",
    "Address": "서울특별시 종로구 종로 19 3층 327호 (종로1가, 르메이에르종로타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "푸른온누리약국",
    "Address": "서울특별시 종로구 새문안로 19 (평동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 종로구 삼봉로 74 (청진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ5OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "신코아약국",
    "Address": "서울특별시 종로구 종로12길 23 1층 (관철동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "광화문윤약국",
    "Address": "서울특별시 종로구 세종대로 159 4층 (세종로)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQyIyQ1IyQwMCQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 종로구 경교장길 5 1.2층 (교남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "세민약국",
    "Address": "서울특별시 종로구 자하문로7길 73 (누하동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "인제약국",
    "Address": "서울특별시 종로구 종로 194 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQxMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "글로리아약국",
    "Address": "서울특별시 종로구 평창문화로 75 A109호 (평창동, 글로리아타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "마이팜약국",
    "Address": "서울특별시 종로구 통일로16길 2 (무악동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "대한약국",
    "Address": "서울특별시 종로구 대학로5길 57 1,2층 (연건동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ4OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 종로구 율곡로 204 (연건동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "캐슬온누리약국",
    "Address": "서울특별시 종로구 종로 347 207호 (숭인동, 롯데캐슬천지인상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "영화약국",
    "Address": "서울특별시 종로구 종로41길 47 (종로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 종로구 창경궁로 160 1,2층 (원남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "행복약국",
    "Address": "서울특별시 종로구 종로 19 323호 (종로1가, 르메이에르종로타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "서울위드팜약국",
    "Address": "서울특별시 종로구 대학로 119 1, 2층 (명륜4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ2MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "서대문권약국",
    "Address": "서울특별시 종로구 새문안로 15-1 1층 (평동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "종각팜약국",
    "Address": "서울특별시 종로구 종로 68 대한기독교서회 1층 (종로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 종로구 종로 128 302호 (종로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQwMyQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "안국온누리약국",
    "Address": "서울특별시 종로구 삼일대로 461 101동 203호 (경운동, 운현궁에스케이허브)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "은성약국",
    "Address": "서울특별시 종로구 삼일대로 434 (낙원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ5MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "독일약국",
    "Address": "서울특별시 종로구 종로 314 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ5MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "한일약국",
    "Address": "서울특별시 종로구 창경궁로11길 3 (예지동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "보령약국",
    "Address": "서울특별시 종로구 종로 203 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQyIyQxIyQwMCQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "플러스약국",
    "Address": "서울특별시 종로구 종로 78 1층 (종로2가, 미려빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "김해약국",
    "Address": "서울특별시 종로구 종로 206 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "인앤아웃약국",
    "Address": "서울특별시 종로구 종로 19 421호 (종로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "안국3층약국",
    "Address": "서울특별시 종로구 율곡로 47 305호 (안국동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQxMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "혜화수약국",
    "Address": "서울특별시 종로구 대명길 29 1층 (명륜4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ2MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "제신약국",
    "Address": "서울특별시 종로구 종로 266 D동 (종로6가, 동대문종합시장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "삼보약국",
    "Address": "서울특별시 종로구 수표로 92 (관수동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5OSQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "참자연약국",
    "Address": "서울특별시 종로구 송월길 99 1층 2156호 (홍파동, 경희궁자이 2단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "광화문123약국",
    "Address": "서울특별시 종로구 삼봉로 44 1층 (청진동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "위드팜바로드림약국",
    "Address": "서울특별시 종로구 경교장길 35 3150호 (평동, 경희궁자이 3단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "유약국",
    "Address": "서울특별시 종로구 경교장길 35 3146,3147호 (평동, 경희궁자이 3단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "위드팜삼정바로약국",
    "Address": "서울특별시 종로구 경교장길 35 3152,3153,3154호 (평동, 경희궁자이 3단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "호수약국",
    "Address": "서울특별시 종로구 삼봉로 57 호수빌딩 지하1층 (수송동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQyIyQxIyQwMCQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "일등약국",
    "Address": "서울특별시 종로구 경교장길 35 상가동 3148,3149호 (평동, 경희궁자이 3단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ5MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "동남약국",
    "Address": "서울특별시 종로구 종로 124 (종로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "백수약국",
    "Address": "서울특별시 종로구 종로 233-1 신화빌딩 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQyIyQzIyQwMCQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 종로구 통일로 246-10 113호 (무악동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "예은약국",
    "Address": "서울특별시 종로구 진흥로 456 1층 (구기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQyIyQ3IyQwMCQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "새명성약국",
    "Address": "서울특별시 종로구 새문안로 85 1층 (신문로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "보람약국",
    "Address": "서울특별시 종로구 종로 326 (창신동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 종로구 종로 22 606호 (서린동, 인주빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "공생약국",
    "Address": "서울특별시 종로구 종로 228 1층 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "명륜시장약국",
    "Address": "서울특별시 종로구 성균관로 56-1 (명륜1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 종로구 창경궁로 162-2 (원남동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "종로한사랑약국",
    "Address": "서울특별시 종로구 종로 344 309호 (숭인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "종로프라자약국",
    "Address": "서울특별시 종로구 자하문로 63 (옥인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "센트로약국",
    "Address": "서울특별시 종로구 우정국로 26 1층 1-9c호 (공평동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "보생약국",
    "Address": "서울특별시 종로구 종로 197-2 (종로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQyIyQ3IyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 종로구 돈화문로9가길 20 (돈의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "보성온누리약국",
    "Address": "서울특별시 종로구 명륜길 22 (명륜1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "부광약국",
    "Address": "서울특별시 종로구 종로 223-1 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQyIyQzIyQwMCQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 종로구 옥인길 32-5 (옥인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 종로구 진흥로 432 1층 3호 (구기동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "대흥사약국",
    "Address": "서울특별시 종로구 돈화문로6가길 40 (봉익동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 종로구 새문안로 17 2층 (평동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ2MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "일신약국",
    "Address": "서울특별시 종로구 종로 224 1층 (종로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "남영약국",
    "Address": "서울특별시 종로구 삼일대로 461 (경운동, 운현궁SK허브)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "케이온누리약국",
    "Address": "서울특별시 중구 명동7길 20 1, 2층 (명동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQyIyQ3IyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "명동하이약국",
    "Address": "서울특별시 중구 명동7길 14 1, 2, 3층 (명동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ4MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 중구 다산로 230 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQwMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "온누리센터원약국",
    "Address": "서울특별시 중구 을지로5길 26 (수하동, 미래에셋센터원빌딩 지하1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQyIyQzIyQwMCQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "새삼성약국",
    "Address": "서울특별시 중구 남대문로 16-1 (남대문로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "우리네약국",
    "Address": "서울특별시 중구 동호로10길 30 103호,104호 (신당동, 약수하이츠 상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "독일사약국",
    "Address": "서울특별시 중구 마장로9길 45 1층 (황학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 중구 퇴계로 447 218-1호 (황학동, 황학 아크로타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "을지약국",
    "Address": "서울특별시 중구 을지로 170 1층 107호 (을지로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "웰니스약국",
    "Address": "서울특별시 중구 명동10길 51 나인트리호텔 1층 (충무로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "서울하이약국",
    "Address": "서울특별시 중구 세종대로 11-1 1층 (남대문로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "홍신약국",
    "Address": "서울특별시 중구 남대문로9길 40 센터플레이스(Center Place) 108-1호 (다동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜늘봄약국",
    "Address": "서울특별시 중구 다산로 223 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "대해약국",
    "Address": "서울특별시 중구 퇴계로 393-1 써니캐슬 1층 101호 (흥인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "대우사약국",
    "Address": "서울특별시 중구 세종대로 22 (남대문로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQxMyQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "신라약국",
    "Address": "서울특별시 중구 남대문로9길 16 (다동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQwMyQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "솔약국",
    "Address": "서울특별시 중구 퇴계로 447 108,109호 (황학동, 황학 아크로타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ2MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "지하근화사약국",
    "Address": "서울특별시 중구 을지로 131 11호 (을지로3가, 지하상가3구역)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ3MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 중구 동호로 196 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 중구 을지로 251 1층 (을지로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "월드탑약국",
    "Address": "서울특별시 중구 남대문로 81 롯데백화점 본점 9층 (소공동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "왕자약국",
    "Address": "서울특별시 중구 다산로36길 11 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "올리브약국",
    "Address": "서울특별시 중구 퇴계로 222 (필동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "연합약국",
    "Address": "서울특별시 중구 퇴계로 120 1층 (남산동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "하이약국",
    "Address": "서울특별시 중구 명동9가길 12 3층 (을지로2가, 메트로알이지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 중구 세종대로21길 63 (태평로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ2MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "명동중앙약국",
    "Address": "서울특별시 중구 명동8나길 49 (충무로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQyIyQ3IyQwMCQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "대화약국",
    "Address": "서울특별시 중구 동호로5길 22 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ3MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "무릉약국",
    "Address": "서울특별시 중구 창경궁로1길 38 (충무로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQwMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "하얀약국",
    "Address": "서울특별시 중구 마른내로 8-1 (저동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "사랑의약국",
    "Address": "서울특별시 중구 남대문로 117 동아빌딩 지하1층 (다동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQyIyQzIyQwMCQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "명동사랑약국",
    "Address": "서울특별시 중구 퇴계로 109 (충무로1가,1층 102호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "한국희귀필수의약품센터",
    "Address": "서울특별시 중구 무교로 6 12층(을지로1가 16, 금세기빌딩) (을지로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 중구 장충단로 201 1층 (장충동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ2MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "약수온누리약국",
    "Address": "서울특별시 중구 다산로 112 신양빌딩 지하1층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 중구 무교로 32 4층 (무교동, 효령빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "자연주의약국",
    "Address": "서울특별시 중구 다산로 90 1층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "에이스약국",
    "Address": "서울특별시 중구 세종대로 136 1층 (무교동, 파이낸스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "유쾌한약국",
    "Address": "서울특별시 중구 다산로 172-1 1층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 중구 세종대로7길 37 지하1층 (순화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQxMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "모드니온누리약국",
    "Address": "서울특별시 중구 서소문로 116 지하1층 (서소문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "메디칼하나약국",
    "Address": "서울특별시 중구 다산로 134 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "사랑제일약국",
    "Address": "서울특별시 중구 충무로 48 2층 (초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "판도라숭례문약국",
    "Address": "서울특별시 중구 세종대로 13 1층 (남대문로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "명동천사약국",
    "Address": "서울특별시 중구 남대문로 68 3층 (명동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQwMyQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "신평화약국",
    "Address": "서울특별시 중구 청계천로 298 1층 가9호 (신당동, 신평화상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 중구 청계천로 100 시그니쳐타워 지하1층 (수표동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "기풍약국",
    "Address": "서울특별시 중구 다산로40길 56 1층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "기쁨이 넘치는 약국",
    "Address": "서울특별시 중구 다산로39길 17 1층 (무학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "동대문허브약국",
    "Address": "서울특별시 중구 장충단로 263 밀리오레상가건물 13층 6호 (을지로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ5OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 중구 다산로 245 (무학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "남산우리약국",
    "Address": "서울특별시 중구 소공로 35 102호 (회현동1가, 남산롯데캐슬아이리스상가 102호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "굿약국",
    "Address": "서울특별시 중구 명동길 45 1,2층 (명동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "샬롬약국",
    "Address": "서울특별시 중구 을지로 55 4층 (을지로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQwMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "금오약국",
    "Address": "서울특별시 중구 퇴계로 61 3층 (남창동, 금오빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQxMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "동화약국",
    "Address": "서울특별시 중구 다산로34길 47 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQyIyQ3IyQwMCQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "동국약국",
    "Address": "서울특별시 중구 서애로1길 16 (필동3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "신중앙약국",
    "Address": "서울특별시 중구 퇴계로 436 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "심해경희한약국",
    "Address": "서울특별시 중구 퇴계로87길 15 1층 (황학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "행복한약수약국",
    "Address": "서울특별시 중구 동호로 193 3층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQyIyQ3IyQwMCQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "신정약국",
    "Address": "서울특별시 중구 다산로 32 203호 (신당동, 남산타운5상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "신삼성대학약국",
    "Address": "서울특별시 중구 퇴계로46길 17 1층 (묵정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "오렌지약국",
    "Address": "서울특별시 중구 을지로 100 지하1층 (을지로2가, 파인에비뉴)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQ5IyQwMCQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "샘물온누리약국",
    "Address": "서울특별시 중구 퇴계로88길 45 1층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ2MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "서현온누리약국",
    "Address": "서울특별시 중구 퇴계로 61 (남창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ3MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "보생당약국",
    "Address": "서울특별시 중구 퇴계로 189 동화빌딩 (필동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "스마트약국",
    "Address": "서울특별시 중구 장충단로 253 1층 194호 (을지로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQxMyQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "아이약국",
    "Address": "서울특별시 중구 명동8가길 20 1층 (충무로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "왕솔약국",
    "Address": "서울특별시 중구 남대문로 36 (회현동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ3OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "인우약국",
    "Address": "서울특별시 중구 중림로 21 (중림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "금천약국",
    "Address": "서울특별시 중구 남대문로1길 2 (북창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ5MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "을지로5가보영약국",
    "Address": "서울특별시 중구 동호로 376 (방산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "코코약국",
    "Address": "서울특별시 중구 을지로 56 1층 (을지로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "유네스코약국",
    "Address": "서울특별시 중구 명동길 26 402호 (명동2가, 유네스코빌딩 )"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "중부사약국",
    "Address": "서울특별시 중구 을지로30길 58 (오장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "온누리정일약국",
    "Address": "서울특별시 중구 청파로 437 (중림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 중구 청계천로 400 지하2층 (황학동, 롯데캐슬베네치아아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQwMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "광희약국",
    "Address": "서울특별시 중구 퇴계로 322 정미식품 (광희동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "알파약국",
    "Address": "서울특별시 중구 마장로9길 34 1층 (황학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "충정로조은약국",
    "Address": "서울특별시 중구 중림로2길 6 1층 (중림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "필약국",
    "Address": "서울특별시 중구 필동로 14 103호 (필동2가, 대평빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ3OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 중구 마른내로 10 (저동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 중구 남대문로10길 9 2층 204호 (삼각동, 경기빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQxIyQwMCQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "신당조은약국",
    "Address": "서울특별시 중구 퇴계로 457 (황학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "좋은약국",
    "Address": "서울특별시 중구 다산로 114-8 1층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ2MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 중구 퇴계로88길 42 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "인원약국",
    "Address": "서울특별시 중구 중림로 2 (중림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQwMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "조동약국",
    "Address": "서울특별시 중구 삼일대로 363 지하1층 11호 (장교동, 장교빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQxMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "오약국",
    "Address": "서울특별시 중구 무교로 21 (무교동, 코오롱아케이드)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ5MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "방약국",
    "Address": "서울특별시 중구 을지로33길 2 (을지로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "한미약국",
    "Address": "서울특별시 중구 청계천로 318 1층 가48호 (신당동, 동평화시장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "광진약국",
    "Address": "서울특별시 중구 다산로27길 6-14 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "아세아약국",
    "Address": "서울특별시 중구 충무로4길 2 (초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "신성약국",
    "Address": "서울특별시 중구 다산로 215 경북여인숙 1층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQwMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 중구 동호로 171 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "희구약국",
    "Address": "서울특별시 중구 남대문시장4길 37 (남창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "정원약국",
    "Address": "서울특별시 중구 세종대로18길 10 (태평로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜광주약국",
    "Address": "서울특별시 중구 퇴계로6길 5 (회현동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "왕란약국",
    "Address": "서울특별시 중구 을지로44길 20 (광희동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ4MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "새열린약국",
    "Address": "서울특별시 중구 명동길 26 703호 (명동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "신우리약국",
    "Address": "서울특별시 중구 마른내로 13 (저동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 중구 다산로 185 5층 501호 (신당동, 신흥빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQxIyQwMCQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "허브약국",
    "Address": "서울특별시 중구 다산로 82 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "대도약국",
    "Address": "서울특별시 중구 퇴계로 183 (필동1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQxMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "장수약국",
    "Address": "서울특별시 중구 퇴계로86길 6 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQwMyQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "예솔약국",
    "Address": "서울특별시 중구 청파로 464 103동 207호 (중림동, 브라운스톤서울)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "메디팜신웅약국",
    "Address": "서울특별시 중구 퇴계로87길 15-8 (황학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQwMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "다산온누리약국",
    "Address": "서울특별시 중구 다산로 133-1 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQxMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "백현약국",
    "Address": "서울특별시 중구 난계로23길 1 (황학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ5OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "연세약국",
    "Address": "서울특별시 중구 통일로 10 (남대문로5가, 연세빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQxMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "새우리약국",
    "Address": "서울특별시 중구 동호로 177 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "주원약국",
    "Address": "서울특별시 중구 퇴계로 438-1 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "평화약국",
    "Address": "서울특별시 중구 남대문시장길 21 1층 (남대문로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "약수소망약국",
    "Address": "서울특별시 중구 동호로 189 톰캣프라자 1층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "옵티마봄약국",
    "Address": "서울특별시 중구 서애로1길 11 114호 (충무로5가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ1IyQwMCQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "서울수약국",
    "Address": "서울특별시 중구 만리재로 177 한라비발디 센트랄상가 9호 (만리동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQwMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "한일약국",
    "Address": "서울특별시 중구 서소문로 109 (서소문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQyIyQ5IyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "남시약국",
    "Address": "서울특별시 중구 남대문로 18 (남대문로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "서울왕약국",
    "Address": "서울특별시 중구 남대문로 22 (남대문로3가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "세계약국",
    "Address": "서울특별시 중구 남대문로 72 바-2호 (남대문로2가, 명동지하쇼핑센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "영진약국",
    "Address": "서울특별시 중구 충무로 30-2 (초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQyIyQxIyQwMCQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "금성약국",
    "Address": "서울특별시 중구 동호로33길 5 (오장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "시티약국",
    "Address": "서울특별시 중구 퇴계로 409 흥화브라운 오피스텔 1층 101호 (흥인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "명동모모약국",
    "Address": "서울특별시 중구 남대문로 68 5층 (명동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "명동명약국",
    "Address": "서울특별시 중구 남대문로7길 11 태양빌딩 1층 (소공동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "명동플러스약국",
    "Address": "서울특별시 중구 명동9길 23 한양빌딩 1, 2층 (을지로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "별약국",
    "Address": "서울특별시 중구 동호로 163 3층 302호 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ4OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "건강백세약국",
    "Address": "서울특별시 중구 서소문로 12 (중림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQwMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "한중약국",
    "Address": "서울특별시 중구 서소문로 120 지하1층 (서소문동, ENA 센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ3MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "새원약국",
    "Address": "서울특별시 중구 명동길 52 (명동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ3OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "상산약국",
    "Address": "서울특별시 중구 퇴계로 435 1층 (황학동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "청계약국",
    "Address": "서울특별시 중구 청계천로 14 한국정보화진흥원 1층 (무교동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQxMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "아름약국",
    "Address": "서울특별시 중구 퇴계로46길 35 1층 (묵정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ4MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "수연약국",
    "Address": "서울특별시 중구 서소문로 138 101호 (태평로2가, 대한일보빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "청실약국",
    "Address": "서울특별시 중구 무교로 15 1층 (무교동, 남강건설회관빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "회현약국",
    "Address": "서울특별시 중구 퇴계로 36 삼선빌딩 302호 (남창동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 중구 다산로 258 1층 102호 (흥인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ2MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "메디홈약국",
    "Address": "서울특별시 중구 소공로 58 화-2호 (충무로1가, 회현지하상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQxMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "옵티마서울약국",
    "Address": "서울특별시 중구 한강대로 416 1층 9-1호 (남대문로5가, 서울스퀘어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "참조은약국",
    "Address": "서울특별시 중구 을지로 158 106호 (을지로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ2MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "신한제일약국",
    "Address": "서울특별시 중구 마장로 11 5층 502호 (신당동, 신한빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQ5OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "동문약국",
    "Address": "서울특별시 중구 을지로41길 14 (을지로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ3OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "백조약국",
    "Address": "서울특별시 중구 세종대로21길 61 (태평로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "부일약국",
    "Address": "서울특별시 중구 청구로14길 45 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "을지수온누리약국",
    "Address": "서울특별시 중구 마른내로 12 1,2층 (저동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQyIyQ1IyQwMCQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 중구 퇴계로 213 301-1호 (충무로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "힘찬약국",
    "Address": "서울특별시 중구 장충단로13길 7 401호 (을지로6가, 을호빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "센츄럴팜약국",
    "Address": "서울특별시 중구 한강대로 405 2층 (봉래동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "원진온누리약국",
    "Address": "서울특별시 중구 을지로 164 베스트웨스턴호텔국도 1층 (을지로4가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "타워약국",
    "Address": "서울특별시 중구 퇴계로 447 B동 318호 (황학동,황학아크로타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "서울시니어스약국",
    "Address": "서울특별시 중구 다산로 72 1층 (신당동, 서울시니어스타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "국민약국",
    "Address": "서울특별시 중구 을지로41길 22 (을지로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ4MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "13층약국",
    "Address": "서울특별시 중구 서소문로 116 유원빌딩 1304호 (서소문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQxIyQwMCQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "2층바른약국",
    "Address": "서울특별시 중구 다산로11길 3 2층 (신당동, 약수JK빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "신등원약국",
    "Address": "서울특별시 중구 수표로 9 (충무로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQxMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "원정약국",
    "Address": "서울특별시 중구 청구로 70 1층 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "새생명약국",
    "Address": "서울특별시 중구 다산로 32 1층 124호 (신당동, 남산타운5상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디케어약국",
    "Address": "서울특별시 중구 서소문로 136 1층 (태평로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "명약국",
    "Address": "서울특별시 중구 남대문로9길 51 효덕빌딩 5층 (을지로1가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "대풍약국",
    "Address": "서울특별시 중구 동호로11길 43 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "수정약국",
    "Address": "서울특별시 중구 장충단로 195 1, 지하1층 (쌍림동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "5층사랑약국",
    "Address": "서울특별시 중구 서소문로 103 배재빌딩 511호 (서소문동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ4MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "명동약국",
    "Address": "서울특별시 중구 퇴계로 123 8층 (충무로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "오성약국",
    "Address": "서울특별시 중구 퇴계로41길 51 (인현동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "평화약국",
    "Address": "서울특별시 중구 동호로 180 202호 대승빌딩 (신당동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 중구 명동8길 47 (충무로2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "제니스약국",
    "Address": "서울특별시 중구 다산로46길 17 2층 213호 (흥인동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "약수하나약국",
    "Address": "서울특별시 중구 다산로 111 1층 (신당동, 한미빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQxMyQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "연세드림약국",
    "Address": "서울특별시 중구 을지로 255 1층 (을지로6가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQxMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "양지약국",
    "Address": "서울특별시 중구 수표로 23 영락빌딩 1층 101-B호 (저동2가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "온누리대웅약국",
    "Address": "서울특별시 송파구 마천로 345 1층 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "송파사거리약국",
    "Address": "서울특별시 송파구 송파대로 387 1층 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ3MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "방이메디칼약국",
    "Address": "서울특별시 송파구 가락로 277 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "싱싱헬리오약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 2036호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQwMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "송파우리약국",
    "Address": "서울특별시 송파구 토성로 65 (풍납동, 태양상가 108호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "위드팜잠실나루역약국",
    "Address": "서울특별시 송파구 송파대로 624 (신천동, 잠실나루역구내 제215-08호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ5OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "프리마약국",
    "Address": "서울특별시 송파구 올림픽로4길 42 109호 (잠실동, 프리마상가 109호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "미래아산약국",
    "Address": "서울특별시 송파구 강동대로 63 1층 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ2MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "금강약국",
    "Address": "서울특별시 송파구 가락로 82 102호 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "새조은약국",
    "Address": "서울특별시 송파구 송파대로 369 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "오렌지약국",
    "Address": "서울특별시 송파구 송파대로 380 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQyIyQzIyQwMCQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "락희온누리약국",
    "Address": "서울특별시 송파구 송파대로 381 1층 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "강약국",
    "Address": "서울특별시 송파구 중대로 135 아이티벤처타워 동관 104호 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "참소망약국",
    "Address": "서울특별시 송파구 양재대로 1222 올림픽프라자 3층 15호 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQyIyQ1IyQwMCQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "굿데이약국",
    "Address": "서울특별시 송파구 송파대로 570 2층 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQ5MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "송파드림온누리약국",
    "Address": "서울특별시 송파구 가락로 61 1층 102호 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "가장빠른천사약국",
    "Address": "서울특별시 송파구 강동대로 74 1층 103호 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "민약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 3041호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQxMyQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "신아산약국",
    "Address": "서울특별시 송파구 강동대로7길 4 1층 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 송파구 오금로31길 3 우성빌딩 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "정다운약국",
    "Address": "서울특별시 송파구 오금로 487 1층 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "다사랑약국",
    "Address": "서울특별시 송파구 올림픽로43길 26 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "나무약국",
    "Address": "서울특별시 송파구 중대로 24 상가 1동 1층 111-1호 (문정동, 올림픽훼밀리타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 송파구 송파대로 345 상가 1A동 1045호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "하나메디칼약국",
    "Address": "서울특별시 송파구 오금로 504 1층 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "시장온누리약국",
    "Address": "서울특별시 송파구 바람드리길 52 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "윤약국",
    "Address": "서울특별시 송파구 백제고분로 365 1층 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQyIyQ3IyQwMCQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "가락온누리약국",
    "Address": "서울특별시 송파구 동남로 207 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ2MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "가장큰현대아산약국",
    "Address": "서울특별시 송파구 강동대로 67 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "다정약국",
    "Address": "서울특별시 송파구 백제고분로 349 자재백화점 1층 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "참좋은약국",
    "Address": "서울특별시 송파구 중대로 105 가락 ID TOWER 104호 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQ1IyQwMCQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "방이코끼리약국",
    "Address": "서울특별시 송파구 마천로 53 2층 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQwMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "트램온누리약국",
    "Address": "서울특별시 송파구 위례광장로 136 E동 205호 (장지동, 위례아이파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ5MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "메디팜푸른약국",
    "Address": "서울특별시 송파구 동남로 189 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "메디팜하나약국",
    "Address": "서울특별시 송파구 송파대로 365 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQwMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "다인약국",
    "Address": "서울특별시 송파구 올림픽로 76 1층 104-1호 (잠실동, J타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQxMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "새웅약국",
    "Address": "서울특별시 송파구 삼전로 75 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQwMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "온누리캐슬프라자약국",
    "Address": "서울특별시 송파구 올림픽로 269 (신천동, 롯데캐슬프라자 127호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "일선약국",
    "Address": "서울특별시 송파구 가락로11길 8 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "위래약국",
    "Address": "서울특별시 송파구 백제고분로 262 2층 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "새하나약국",
    "Address": "서울특별시 송파구 강동대로 71 1층 (풍납동, 신흥빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 송파구 오금로 247 건양빌딩 1층 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "월드중앙약국",
    "Address": "서울특별시 송파구 올림픽로35길 112 101,102호 (신천동, 장미아파트 비상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ2MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "숲약국",
    "Address": "서울특별시 송파구 석촌호수로 68 (잠실동, A동 1층, 지층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ2MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "가락약국",
    "Address": "서울특별시 송파구 송파대로 286 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "올리브약국",
    "Address": "서울특별시 송파구 강동대로7길 3 1층 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "사거리현대약국",
    "Address": "서울특별시 송파구 올림픽로 491 1층 (풍납동, 세제빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ5MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "메디팜우주약국",
    "Address": "서울특별시 송파구 올림픽로35길 10 B동 212-호 (신천동, 파크리오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "봄봄약국",
    "Address": "서울특별시 송파구 동남로 317 103호 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 송파구 백제고분로 457 다우빌딩 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "365바른약국",
    "Address": "서울특별시 송파구 가락로 94 1층 103호 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "이안약국",
    "Address": "서울특별시 송파구 중대로10길 5 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "장미미소약국",
    "Address": "서울특별시 송파구 올림픽로35길 112 제2동 3층 20호 (신천동, 장미아파트 비상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ2MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "석촌온누리약국",
    "Address": "서울특별시 송파구 송파대로 438 103호 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQwMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "문정약국",
    "Address": "서울특별시 송파구 동남로4길 25 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQzIyQ5MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "3층메디칼약국",
    "Address": "서울특별시 송파구 양재대로 1222 23-1호및 23호(일부호 (방이동, 올림픽프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQxMyQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "중앙당약국",
    "Address": "서울특별시 송파구 오금로38길 5-25 (가락동, 현대상가 101호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ2MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 송파구 위례성대로20길 31 1층 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "중앙프라자약국",
    "Address": "서울특별시 송파구 마천로57길 4 1층 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQzIyQwMCQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "녹십자약국",
    "Address": "서울특별시 송파구 올림픽로 130 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQzIyQwMCQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "키즈플러스약국",
    "Address": "서울특별시 송파구 올림픽로 240 (잠실동, 웰빌센타동 A-104호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "크게열린약국",
    "Address": "서울특별시 송파구 강동대로 59-3 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "명약국",
    "Address": "서울특별시 송파구 거마로 62 효명빌딩 1층 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "삼청약국",
    "Address": "서울특별시 송파구 오금로32길 42 (송파동, 현대상가 104호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ4MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "팜코리아약국",
    "Address": "서울특별시 송파구 가락로 99 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 송파구 가락로 113 (석촌동, 금도빌딩 104호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "미소진약국",
    "Address": "서울특별시 송파구 올림픽로 119 (잠실동, 파인애플상가 5B29-2호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "에스케이약국",
    "Address": "서울특별시 송파구 법원로 128 문정에스케이브이원지엘메트로시티 CG121호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ2MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "평화약국",
    "Address": "서울특별시 송파구 양재대로 932 5층 7호 (가락동, 가락동도매시장 내 가락몰업무동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "옵티마100세약국",
    "Address": "서울특별시 송파구 마천로41길 9 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "사람사랑약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 5007호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "뉴프라임약국",
    "Address": "서울특별시 송파구 송파대로 278 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQxIyQwMCQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "애플약국",
    "Address": "서울특별시 송파구 올림픽로 119 잠실파인애플상가 제3에이 12-1호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "크리스마스약국",
    "Address": "서울특별시 송파구 올림픽로 119 잠실파인애플상가 2층 2A02호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "헬리오메디칼약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 2023호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "지하철약국",
    "Address": "서울특별시 송파구 올림픽로 265 (잠실동, 잠실역지하상가 B-13호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "오메디약국",
    "Address": "서울특별시 송파구 올림픽로37길 130 파크리오 파크리오상가A동 3층 316호 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ3MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "송파새길약국",
    "Address": "서울특별시 송파구 송파대로 145 문정 오벨리스크 108호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "더함약국",
    "Address": "서울특별시 송파구 올림픽로 145 리센츠 4층 4B01호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "성조약국",
    "Address": "서울특별시 송파구 동남로 136 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "하나로약국",
    "Address": "서울특별시 송파구 마천로 264 흥일빌딩 1층 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQyIyQ3IyQwMCQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "훼미리약국",
    "Address": "서울특별시 송파구 중대로 68 (문정동, 훼미리샤르망 106호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ4MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "호원약국",
    "Address": "서울특별시 송파구 송파대로45길 12 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ3OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "경인약국",
    "Address": "서울특별시 송파구 가락로42길 9 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQyIyQ5IyQwMCQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "도래약국",
    "Address": "서울특별시 송파구 마천로 341 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQwMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "이화약산온누리약국",
    "Address": "서울특별시 송파구 가락로 211 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "남매약국",
    "Address": "서울특별시 송파구 오금로64길 4 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQxMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "은세약국",
    "Address": "서울특별시 송파구 올림픽로 509 (풍납동, J빌딩 1층2호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "문정우리들약국",
    "Address": "서울특별시 송파구 법원로 114 엠스테이트 C-218호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "명생약국",
    "Address": "서울특별시 송파구 백제고분로41길 31 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ4OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "우림약국",
    "Address": "서울특별시 송파구 오금로 477 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ4OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "아산약국",
    "Address": "서울특별시 송파구 토성로 26 104, 105호 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQyIyQ3IyQwMCQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "새독일약국",
    "Address": "서울특별시 송파구 송파대로 372 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ5OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "신방이약국",
    "Address": "서울특별시 송파구 가락로 245 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQxMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "감람약국",
    "Address": "서울특별시 송파구 문정로13길 11-10 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ5MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "명문약국",
    "Address": "서울특별시 송파구 마천로41길 20 1층 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 송파구 백제고분로 276 202호 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "청호봄약국",
    "Address": "서울특별시 송파구 석촌호수로 118 4층 403호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ4MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "도움약국",
    "Address": "서울특별시 송파구 백제고분로22길 36 1층 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "잠실미소약국",
    "Address": "서울특별시 송파구 올림픽로35가길 16 홈플러스잠실점 B1층 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "소백약국",
    "Address": "서울특별시 송파구 양산로 12 세신거여훼미리타운 1층 107호 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQwMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "가가호호조은약국",
    "Address": "서울특별시 송파구 토성로 16 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "더하늘약국",
    "Address": "서울특별시 송파구 올림픽로 119 잠실파인애플상가 3층 3B12호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "타워약국",
    "Address": "서울특별시 송파구 올림픽로 96 동신빌딩 105호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "셀럽약국",
    "Address": "서울특별시 송파구 올림픽로 145 리센츠 2층 2A29호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "문정건강약국",
    "Address": "서울특별시 송파구 송파대로 98 선도빌딩 1층 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "파크리오오렌지약국",
    "Address": "서울특별시 송파구 올림픽로37길 130 파크리오 A동 5층 516호 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQwMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "아이파크약국",
    "Address": "서울특별시 송파구 위례광장로 230 B동 207호 (장지동, 위례2차아이파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQxMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "동서울약국",
    "Address": "서울특별시 송파구 강동대로 61-1 지층 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "은하약국",
    "Address": "서울특별시 송파구 양재대로 1164 홍일빌딩 6층 1호 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "레이크이화약국",
    "Address": "서울특별시 송파구 석촌호수로 135 레이크팰리스 A동 122호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "송파24약국",
    "Address": "서울특별시 송파구 송파대로 111, 하비오길 111 하비오길 송파대로202동 161호 (문정동, 파크하비오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ5IyQwMCQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "송파미소약국",
    "Address": "서울특별시 송파구 올림픽로35길 10 B동 308-1호 (신천동, 파크리오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ2MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "새잠실365약국",
    "Address": "서울특별시 송파구 올림픽로 145 리센츠 3층 제3에이33호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "영림약국",
    "Address": "서울특별시 송파구 올림픽로 203 (잠실동, 중앙상가 150호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ2MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "친절한약국",
    "Address": "서울특별시 송파구 올림픽로32길 13 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ2MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "도영약국",
    "Address": "서울특별시 송파구 오금로 507 거여빌딩 1층 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "독수리약국",
    "Address": "서울특별시 송파구 중대로 135 (가락동, IT벤처타워 동관 101호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQxMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "가장편한대영약국",
    "Address": "서울특별시 송파구 강동대로 74 108동 101,102,지하102호 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "신화약국",
    "Address": "서울특별시 송파구 올림픽로12길 34 (잠실동, 103호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "송파새롬약국",
    "Address": "서울특별시 송파구 송파대로28길 27 (가락동, 성원상떼빌 102동 202호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "프라자약국",
    "Address": "서울특별시 송파구 양재대로 1222 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "천사약국",
    "Address": "서울특별시 송파구 새말로8길 27 1층 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ2MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "헬로팜약국",
    "Address": "서울특별시 송파구 올림픽로12길 5 정호빌딩 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "마천서울약국",
    "Address": "서울특별시 송파구 거마로 58 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQxMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "한가족약국",
    "Address": "서울특별시 송파구 송파대로 423 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 송파구 백제고분로48길 17 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "지앤미약국",
    "Address": "서울특별시 송파구 동남로 215 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "온누리엄마손약국",
    "Address": "서울특별시 송파구 송파대로 415 1층 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "보성약국",
    "Address": "서울특별시 송파구 성내천로 212 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 송파구 백제고분로50길 31 1층 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQwMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "행복한우리약국",
    "Address": "서울특별시 송파구 풍성로25길 41 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "미르약국",
    "Address": "서울특별시 송파구 토성로 65 2층 202-2호 (풍납동, 태양상가 202-2호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ2MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "모범약국",
    "Address": "서울특별시 송파구 백제고분로 258 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ2MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "누가신약국",
    "Address": "서울특별시 송파구 송파대로 383 (석촌동, 1층 3호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ2MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "쌍용약국",
    "Address": "서울특별시 송파구 올림픽로4길 48 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ3OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "스타약국",
    "Address": "서울특별시 송파구 송파대로 562 (신천동, 한빛프라자 3층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "남일온누리약국",
    "Address": "서울특별시 송파구 올림픽로 435 309호 (신천동, 파크리오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "송파태양약국",
    "Address": "서울특별시 송파구 백제고분로48길 22 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQwMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "오약국",
    "Address": "서울특별시 송파구 백제고분로 386 1층 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ3OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "일번약국",
    "Address": "서울특별시 송파구 토성로 21 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "옵티마하나약국",
    "Address": "서울특별시 송파구 올림픽로51길 30 (풍납동, 대아(아)상가 1층14호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "이화제니약국",
    "Address": "서울특별시 송파구 거마로 4 102호 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "영약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 5층 5001호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "헬리오라라약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 4028호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ3MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "밝은중앙약국",
    "Address": "서울특별시 송파구 강동대로 73 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "선수촌약국",
    "Address": "서울특별시 송파구 올림픽로4길 17 (잠실동, 아시아선수촌상가 1-137호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQwMyQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "종우약국",
    "Address": "서울특별시 송파구 양재대로 1222 (방이동, 올림픽프라자상가 1층 94호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "보람약국",
    "Address": "서울특별시 송파구 위례성대로 136 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "시그니처약국",
    "Address": "서울특별시 송파구 올림픽로 300 롯데월드타워앤드롯데월드몰 지하1층 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "차돌약국",
    "Address": "서울특별시 송파구 백제고분로 232 남양빌딩 104호 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "라미약국",
    "Address": "서울특별시 송파구 올림픽로8길 20 잠실아이파크 1층 A115호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "위드팜가까운지하철약국",
    "Address": "서울특별시 송파구 올림픽로37길 130 파크리오 124,125,126호 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "트리지움자연약국",
    "Address": "서울특별시 송파구 석촌호수로 61 트리지움 5층 514-2호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "정문다사랑약국",
    "Address": "서울특별시 송파구 강동대로 65 토성빌딩 1층 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ2MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "미래약국",
    "Address": "서울특별시 송파구 오금로 518 3층 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "극동약국",
    "Address": "서울특별시 송파구 동남로18길 9 (가락동, 극동아파트상가 104호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ2MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "루터약국",
    "Address": "서울특별시 송파구 올림픽로35다길 42 한국루터회관 1층 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQyIyQxIyQwMCQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "동서약국",
    "Address": "서울특별시 송파구 마천로5길 4 (오금동, 4층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "송파그랜드약국",
    "Address": "서울특별시 송파구 문정로4길 14 1층 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "맑은샘약국",
    "Address": "서울특별시 송파구 동남로 236 2층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "스타온누리약국",
    "Address": "서울특별시 송파구 삼전로 99 대성빌딩 1층 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "도담약국",
    "Address": "서울특별시 송파구 동남로 209 1층 101호 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "바른삼성약국",
    "Address": "서울특별시 송파구 백제고분로 126 오룡빌딩 101호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "더블유약국",
    "Address": "서울특별시 송파구 올림픽로 100 효창타워 1층 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "성원큰사랑약국",
    "Address": "서울특별시 송파구 송파대로28길 27 102동 201호 (가락동, 송파성원쌍떼빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "송파제일약국",
    "Address": "서울특별시 송파구 동남로 217 동희빌딩 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ3MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "방이프라자약국",
    "Address": "서울특별시 송파구 가락로 244 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQ1IyQwMCQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "마천푸른솔약국",
    "Address": "서울특별시 송파구 거마로 60 1층 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "보니약국",
    "Address": "서울특별시 송파구 송파대로 385 성룡빌딩 102호 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "새솔약국",
    "Address": "서울특별시 송파구 마천로 41 수기빌딩 2층 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "화인약국",
    "Address": "서울특별시 송파구 중대로 80 (문정동, 롯데마트 3층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "왕약국",
    "Address": "서울특별시 송파구 백제고분로 261 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ2MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "후생약국",
    "Address": "서울특별시 송파구 마천로45길 15 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "코끼리약국",
    "Address": "서울특별시 송파구 석촌호수로 78 (잠실동, 1층 30호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "사랑의약국",
    "Address": "서울특별시 송파구 가락로28길 3 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "우성약국",
    "Address": "서울특별시 송파구 올림픽로4길 42 (잠실동, 우상나상가 3층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 송파구 중대로 24 (문정동, 훼밀리상가 131호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "천호푸른약국",
    "Address": "서울특별시 송파구 바람드리길 62 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQwMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "온누리옥산약국",
    "Address": "서울특별시 송파구 동남로 141 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "성심약국",
    "Address": "서울특별시 송파구 마천로 190 (오금동, 청전빌딩 104호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "팜플러스약국",
    "Address": "서울특별시 송파구 송파대로28길 43 1층 101-2호 (가락동, 송파KCC웰츠타워 101-2호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "메디슨약국",
    "Address": "서울특별시 송파구 송이로 111 (가락동, 청석빌딩 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ5MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "우리온누리약국",
    "Address": "서울특별시 송파구 석촌호수로 61 4층 411호 (잠실동, 트리지움상가 4층 411호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQwMyQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "참행복한약국",
    "Address": "서울특별시 송파구 송이로 76 뉴스타트병원 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "정약국",
    "Address": "서울특별시 송파구 충민로2길 28 대진플라자2 1층 105호 (장지동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "맑은온누리약국",
    "Address": "서울특별시 송파구 새말로 125 어은회관 107호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 송파구 송이로 150 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQxMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "영진약국",
    "Address": "서울특별시 송파구 한가람로 448 (풍납동, 한가람상가 102호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQxMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "단비온누리약국",
    "Address": "서울특별시 송파구 올림픽로 145 1층 A27호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "초록약국",
    "Address": "서울특별시 송파구 올림픽로37길 130 파크리오 A상가동 307호 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "메디팜우리약국",
    "Address": "서울특별시 송파구 올림픽로 119 1층 A12호 (잠실동, 파인애플상가 1층 A12호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "온누리배명약국",
    "Address": "서울특별시 송파구 가락로 26 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "소나무약국",
    "Address": "서울특별시 송파구 중대로 80 (문정동, 롯데마트 지1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "유한약국",
    "Address": "서울특별시 송파구 올림픽로 104 (잠실동, 동성빌딩 1층 3호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQyIyQ3IyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "박순영온누리약국",
    "Address": "서울특별시 송파구 마천로7길 6 117호,118호 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQxMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 송파구 가락로 166 1층 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜더미소약국",
    "Address": "서울특별시 송파구 충민로2길 24 리더스프라자 104호 (장지동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ2MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "문정이화약국",
    "Address": "서울특별시 송파구 법원로 114 엠스테이트 C동 214호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQxIyQwMCQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 송파구 올림픽로 119 (잠실동, 파인애플상가 3A04호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 송파구 백제고분로 279 1층 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 송파구 가락로 158 1층 102호 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQxMyQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "프라자사랑약국",
    "Address": "서울특별시 송파구 백제고분로 438 1층 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "삼성수약국",
    "Address": "서울특별시 송파구 올림픽로35길 123 2층 203호 (신천동, 향군타워 2층 203호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "보영약국",
    "Address": "서울특별시 송파구 성내천로34길 24-1 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQwMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "하비온누리약국",
    "Address": "서울특별시 송파구 송파대로 111 205동 414호 (문정동, 파크하비오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ3OSQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "가까운이화약국",
    "Address": "서울특별시 송파구 강동대로 74 잠실올림픽아이파크상가 1층 108호, 지층 B103호 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQwMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "리센츠약국",
    "Address": "서울특별시 송파구 올림픽로 145 리센츠 3층 3A36호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "정온누리약국",
    "Address": "서울특별시 송파구 백제고분로 210 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ5OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "믿음약국",
    "Address": "서울특별시 송파구 중대로 24 (문정동, 훼밀리상가 136호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "대교약국",
    "Address": "서울특별시 송파구 가락로 153 1층 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "송파프라자약국",
    "Address": "서울특별시 송파구 가락로 112 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "리오약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 2009호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "온누리솔약국",
    "Address": "서울특별시 송파구 올림픽로35길 112 2동 303호 (신천동, 장미아파트 비상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "수프라자약국",
    "Address": "서울특별시 송파구 거마로 61 1층 (마천동, 강동중앙의원)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "메디팜석촌약국",
    "Address": "서울특별시 송파구 삼학사로 81 1층 (삼전동, 서울빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 송파구 석촌호수로 61 (잠실동, 트리지움상가 305호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "갤러리약국",
    "Address": "서울특별시 송파구 올림픽로 212 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "풍납라파약국",
    "Address": "서울특별시 송파구 바람드리길 33 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ2MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "송파중앙약국",
    "Address": "서울특별시 송파구 오금로 91 1층 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ5MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "온누리건강약국",
    "Address": "서울특별시 송파구 양재대로 1222 (방이동, 올림픽프라자상가 2층 10호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "아산큰길약국",
    "Address": "서울특별시 송파구 올림픽로 493 풍납동 N빌딩 1층 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "한결약국",
    "Address": "서울특별시 송파구 올림픽로35길 124 2동 410,411호 (신천동, 장미아파트 에이상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 송파구 마천로 25 1층 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "새중일약국",
    "Address": "서울특별시 송파구 오금로 300 (가락동, 김해빌딩 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQxIyQwMCQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "서울그랜드약국",
    "Address": "서울특별시 송파구 백제고분로 212 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "큰사랑약국",
    "Address": "서울특별시 송파구 동남로 211 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQwMyQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "신한약국",
    "Address": "서울특별시 송파구 올림픽로 106 (잠실동, 상록빌딩 3층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQwMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "대동약국",
    "Address": "서울특별시 송파구 가락로 175 1층 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ5MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "주온누리약국",
    "Address": "서울특별시 송파구 백제고분로 490 거보산업(주) 1층 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "건강샘약국",
    "Address": "서울특별시 송파구 백제고분로 275 1층 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "농수산약국",
    "Address": "서울특별시 송파구 양재대로 932 B동 B1층 03-1호 (가락동, 가락동 농수산물도매시장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "녹원약국",
    "Address": "서울특별시 송파구 백제고분로50길 26 1층 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 송파구 거마로 66 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "석촌솔약국",
    "Address": "서울특별시 송파구 송파대로45길 4 1층 101호 (석촌동, 호반빌라)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQxMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "위례푸른약국",
    "Address": "서울특별시 송파구 위례광장로 193 1층 (장지동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ2MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "두리약국",
    "Address": "서울특별시 송파구 송이로 239 도은빌딩 1층 4호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQxMyQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "새그린약국",
    "Address": "서울특별시 송파구 토성로 58 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQ3MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "오금중앙약국",
    "Address": "서울특별시 송파구 위례성대로20길 33 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ3OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "마천행복한약국",
    "Address": "서울특별시 송파구 마천로51길 2 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "새희망약국",
    "Address": "서울특별시 송파구 송파대로 422 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ2MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "거여서울약국",
    "Address": "서울특별시 송파구 오금로 505 (거여동, 101호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ2MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "웰약국",
    "Address": "서울특별시 송파구 양재대로 1222 3층 219-2호 (방이동, 올림픽프라자상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "방이수약국",
    "Address": "서울특별시 송파구 백제고분로 469 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQzIyQ2MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 송파구 동남로 138 1층 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ4MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "스마트약국",
    "Address": "서울특별시 송파구 오금로 508 스타빌딩 1층 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "해피홈약국",
    "Address": "서울특별시 송파구 오금로 512 207호 (거여동, 거여역2차쌍용아파트 207호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 송파구 올림픽로 212 (잠실동, 갤러리아팰리스 2층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ4MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "시그마약국",
    "Address": "서울특별시 송파구 올림픽로 289 (신천동, 시그마빌딩 지하1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQyIyQ5IyQwMCQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "오렌지온누리약국",
    "Address": "서울특별시 송파구 오금로11길 37 101호 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQxIyQwMCQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "대학약국",
    "Address": "서울특별시 송파구 강동대로 57 1, 2층 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "송파온누리약국",
    "Address": "서울특별시 송파구 오금로32길 28 104호 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 송파구 올림픽로35가길 9 219호 (신천동, 잠실 푸르지오 월드마크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ2MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 송파구 오금로 420 한라산업개발빌딩 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "피나팜맑은약국",
    "Address": "서울특별시 송파구 송파대로 201 송파 테라타워2 B동 144호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 송파구 올림픽로 119 잠실파인애플상가 2층 60~61호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "장생당약국",
    "Address": "서울특별시 송파구 마천로 237 신동아아파트 상가동 104호 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "늘봄약국",
    "Address": "서울특별시 송파구 토성로 78 (풍납동, 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQwMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "보건당약국",
    "Address": "서울특별시 송파구 백제고분로27길 39 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "힐링약국",
    "Address": "서울특별시 송파구 오금로36길 4-17 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ2MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "위례정약국",
    "Address": "서울특별시 송파구 위례광장로 199 성희프라자 109호 (장지동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ3OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "정민약국",
    "Address": "서울특별시 송파구 마천로 68 1층 3호 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "아산메디칼약국",
    "Address": "서울특별시 송파구 강동대로 61 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ5MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "이화온누리약국",
    "Address": "서울특별시 송파구 마천로 295-1 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ2MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "미성송파약국",
    "Address": "서울특별시 송파구 송파대로 374 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "중의당약국",
    "Address": "서울특별시 송파구 새말로 134 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "3층하나약국",
    "Address": "서울특별시 송파구 올림픽로35길 112 (신천동, 장미B상가 315호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "석촌사랑약국",
    "Address": "서울특별시 송파구 송파대로 437 1층 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQxMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "몸사랑한약국",
    "Address": "서울특별시 송파구 석촌호수로 61 지층 B104호 (잠실동, 트리지움상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ2MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "경희생한약국",
    "Address": "서울특별시 송파구 송파대로 345 3B동 지하1층 1026호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ2MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "일층가락약국",
    "Address": "서울특별시 송파구 양재대로 932 105호 (가락동, 가락몰 관리업무동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 송파구 백제고분로 162 대양빌딩 1층 103호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ5OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "석촌한우리약국",
    "Address": "서울특별시 송파구 송파대로 441 청호빌딩 1층 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "진메디칼약국",
    "Address": "서울특별시 송파구 마천로57길 7 1층 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQ1IyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "그린스타약국",
    "Address": "서울특별시 송파구 오금로32길 35 104호 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "감초당약국",
    "Address": "서울특별시 송파구 백제고분로41길 11 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "참플러스약국",
    "Address": "서울특별시 송파구 백제고분로 463 웅산빌딩 201호 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "자담한약국",
    "Address": "서울특별시 송파구 백제고분로42길 19 1층 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ2MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "송파윤한약국",
    "Address": "서울특별시 송파구 동남로18길 12 106호 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "안성약국",
    "Address": "서울특별시 송파구  오금로 414 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "정선약국",
    "Address": "서울특별시 송파구 백제고분로 127 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQyIyQzIyQwMCQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "서울약국",
    "Address": "서울특별시 송파구 송이로31길 4 1층 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ2MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "뉴시티약국",
    "Address": "서울특별시 송파구 석촌호수로 160 102호 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "그랜드약국",
    "Address": "서울특별시 송파구 마천로 35 1층 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ2MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "오층조은약국",
    "Address": "서울특별시 송파구 동남로 193 (가락동, 쌍용프라자상가 503호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ2MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "우리헬리오약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 4층 4011호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 3055호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "손약국",
    "Address": "서울특별시 송파구 백제고분로 405 1층 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "윤정온누리약국",
    "Address": "서울특별시 송파구 오금로49길 31 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "한솔약국",
    "Address": "서울특별시 송파구 백제고분로45길 5 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "새건영약국",
    "Address": "서울특별시 송파구 새말로8길 6 1층 (문정동, 광덕빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "헬리오이화약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 1층 1002호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "개롱약국",
    "Address": "서울특별시 송파구 오금로 396 1층 114호 (가락동, 에스케이허브파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQwMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "구인약국",
    "Address": "서울특별시 송파구 성내천로 261 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "황제약국",
    "Address": "서울특별시 송파구 백제고분로 381 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ5OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "시티온누리약국",
    "Address": "서울특별시 송파구 송파대로 366 1층 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQwMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "유창온누리약국",
    "Address": "서울특별시 송파구 송파대로 288 신정빌딩 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ4OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 송파구 오금로31길 11 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQwMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 송파구 올림픽로 145 5층 (잠실동, 리센츠상가 5B15호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 송파구 백제고분로 466 1층 (방이동, 세나빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "문정온누리약국",
    "Address": "서울특별시 송파구 송파대로 167 문정역테라타워 지하1층 G132호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "트리풀약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 3011호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "샤인약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 4024호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "환승센터약국",
    "Address": "서울특별시 송파구 잠실로 156 잠실광역환승센터 지하1층 101호 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ3MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "지혜온누리약국",
    "Address": "서울특별시 송파구 석촌호수로 58 (잠실동, 동신빌딩 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQyIyQ5IyQwMCQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "시티약국",
    "Address": "서울특별시 송파구 올림픽로 116 1층 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "월드타워약국",
    "Address": "서울특별시 송파구 올림픽로 300 지하1층 (신천동, 롯데마트월드타워점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "엘스3층 온누리약국",
    "Address": "서울특별시 송파구 올림픽로 119 3B5호 (잠실동, 잠실파인애플상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "해오름약국",
    "Address": "서울특별시 송파구 올림픽로35길 124 4층 7호 (신천동, 장미아파트 에이상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQxMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 송파구 송파대로 451 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ2MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "가장친절한정문앞중앙약국",
    "Address": "서울특별시 송파구 강동대로 74 상가동 104,105,106,107,204호 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQwMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 송파구 양재대로60길 3-12 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "우진약국",
    "Address": "서울특별시 송파구 마천로 191 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "동아약국",
    "Address": "서울특별시 송파구 올림픽로 114 2층 (잠실동, 서경빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "잠실메디신약국",
    "Address": "서울특별시 송파구 백제고분로 168 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 송파구 석촌호수로 100 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "로데오약국",
    "Address": "서울특별시 송파구 동남로3길 3 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ3MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "에벤에셀약국",
    "Address": "서울특별시 송파구 송파대로 558 1층 103호 (신천동, 월드타워빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ4MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "매일여는온누리약국",
    "Address": "서울특별시 송파구 백제고분로 187 1층 103,104호 (잠실동, 파크인수)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQwMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "웰빙팜건강프라자약국",
    "Address": "서울특별시 송파구 백제고분로 216 (삼전동, 청송빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "더건강약국",
    "Address": "서울특별시 송파구 중대로 193 주식회사홈캐스트 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "반가운약국",
    "Address": "서울특별시 송파구 송이로 166 상가 102동 101호 (가락동, 가락우성2차아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 송파구 풍성로 55 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "한스약국",
    "Address": "서울특별시 송파구 정의로8길 7 한스 102호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "잠실프라자약국",
    "Address": "서울특별시 송파구 백제고분로 171 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "메디팜양의약국",
    "Address": "서울특별시 송파구 올림픽로 212 2층 220호 (잠실동, 갤러리아팰리스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ3MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "산돌약국",
    "Address": "서울특별시 송파구 백제고분로46길 9 (송파동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ4MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "온누리봄빛약국",
    "Address": "서울특별시 송파구 양산로10길 4 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQyIyQ3IyQwMCQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "새힘온누리약국",
    "Address": "서울특별시 송파구 마천로 137 (오금동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "지용약국",
    "Address": "서울특별시 송파구 백제고분로48길 27 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "방이종로약국",
    "Address": "서울특별시 송파구 마천로 29 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "송파샘약국",
    "Address": "서울특별시 송파구 송파대로 345 1A동 2040호 (가락동, 헬리오시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "영보약국",
    "Address": "서울특별시 송파구 백제고분로 202 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "가까운새서울약국",
    "Address": "서울특별시 송파구 토성로 18 1층, 지층 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQwMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "포도나무약국",
    "Address": "서울특별시 송파구 송파대로32길 15 209호 (가락동, 가락금호아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "베스트약국",
    "Address": "서울특별시 송파구 백제고분로 214 (삼전동, 서울외과빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ2MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "삼원약국",
    "Address": "서울특별시 송파구 올림픽로37길 130 파크리오 A동 317호 (신천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 송파구 오금로 404 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "나루역사거리현대약국",
    "Address": "서울특별시 송파구 올림픽로 435 (신천동, 파크리오A상가 163, 164호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "스마일약국",
    "Address": "서울특별시 송파구 올림픽로 119 (잠실동, 잠실파인애플상가4층4B07호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "시온약국",
    "Address": "서울특별시 송파구 백제고분로27길 19 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "삼전종로약국",
    "Address": "서울특별시 송파구 백제고분로 203 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQxMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "새동산약국",
    "Address": "서울특별시 송파구 풍성로25가길 11 (풍납동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "해성약국",
    "Address": "서울특별시 송파구 가락로 111 (석촌동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "동의삼성약국",
    "Address": "서울특별시 송파구 거마로22길 49 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "윤호약국",
    "Address": "서울특별시 송파구 마천로 311 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQxMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "송파하나약국",
    "Address": "서울특별시 송파구 마천로41길 1 1층 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "늘조은온누리약국",
    "Address": "서울특별시 송파구 동남로18길 45 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 송파구 올림픽로35길 10 파크리오상가B동 202-1호 (신천동, 파크리오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQwMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "참한약국",
    "Address": "서울특별시 송파구 충민로 52 (문정동, 가든5웍스 BF1086)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ5OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "상일약국",
    "Address": "서울특별시 송파구 올림픽로35가길 11 (신천동, 한신코아 110호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQyIyQ3IyQwMCQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "예사랑약국",
    "Address": "서울특별시 송파구 백제고분로 446 송암빌딩 2층 201호 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ2MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "고바우약국",
    "Address": "서울특별시 송파구 마천로41길 21 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQ4MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "대한약국",
    "Address": "서울특별시 송파구 법원로11길 11 문정현대지식산업센터1-1 A동 101호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQxIyQwMCQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "테라약국",
    "Address": "서울특별시 송파구 송파대로 167 문정역테라타워 A동 216호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "가든파이브약국",
    "Address": "서울특별시 송파구 충민로 66 1층 F-1001호 (문정동, 가든파이브라이프 1층, F-1001호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 송파구 송파대로 111 205동 305호 (문정동, 파크하비오)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "으뜸약국",
    "Address": "서울특별시 송파구 충민로2길 24 리더스프라자 103호 (장지동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "새롬약국",
    "Address": "서울특별시 송파구 석촌호수로 130 신원빌딩 206호 (삼전동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ4MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "한독약국",
    "Address": "서울특별시 송파구 중대로 80 문정프라자 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ5OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "메디팜대신M약국",
    "Address": "서울특별시 송파구 송이로 87 1층 (가락동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "행복약국",
    "Address": "서울특별시 송파구 양산로 42 (거여동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ5OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "기쁨약국",
    "Address": "서울특별시 송파구 위례광장로 200 101(일부),102호 (장지동, 에스비트램스퀘어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "가든건강약국",
    "Address": "서울특별시 송파구 충민로 52 가든파이브웍스 S동 307호 (문정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "온누리건강약국",
    "Address": "서울특별시 송파구 백제고분로12길 17 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "천명약국",
    "Address": "서울특별시 송파구 오금로 95 1층 (방이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ2MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "고운약국",
    "Address": "서울특별시 송파구 송이로32길 37 201동 1층 04호 (문정동, 문정푸르지오아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "오로라약국",
    "Address": "서울특별시 송파구 성내천로33길 9 1층 (마천동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQyIyQ3IyQwMCQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "동의보감한약국",
    "Address": "서울특별시 송파구 위례광장로 270 1층 G113호 (장지동, 송파와이즈더샵)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "새내수약국",
    "Address": "서울특별시 송파구 석촌호수로 61 트리지움상가 402-1호 (잠실동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "일층약국",
    "Address": "서울특별시 중랑구 용마산로 434 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ3MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "칠칠약국",
    "Address": "서울특별시 중랑구 동일로 778 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "이지약국",
    "Address": "서울특별시 중랑구 면목로 398 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "수정온누리약국",
    "Address": "서울특별시 중랑구 동일로 933 1층 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQwMyQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "자연약국",
    "Address": "서울특별시 중랑구 망우로 377 (상봉동, 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "활기찬약국",
    "Address": "서울특별시 중랑구 동일로 887 삼삼메디컬빌딩 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "황약국",
    "Address": "서울특별시 중랑구 망우로 402 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ4MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "온누리건강약국",
    "Address": "서울특별시 중랑구 봉화산로 215 1층 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "동남약국",
    "Address": "서울특별시 중랑구 신내로 45 해성빌딩 1층 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ4OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "한울약국",
    "Address": "서울특별시 중랑구 망우로 353 지하1층 (상봉동, 상봉 프레미어스 엠코)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 중랑구 사가정로49길 50 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "365프라자약국",
    "Address": "서울특별시 중랑구 공릉로 63 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQwMyQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "늘푸른온누리약국",
    "Address": "서울특별시 중랑구 면목로27길 80 80동 (면목동, 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ5MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "동부약국",
    "Address": "서울특별시 중랑구 망우로 503 동부약국 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "일월약국",
    "Address": "서울특별시 중랑구 겸재로9길 53 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ2MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "신강약국",
    "Address": "서울특별시 중랑구 면목로 224 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ2MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "정우약국",
    "Address": "서울특별시 중랑구 봉화산로 189 (신내동, 상가동 107호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQwMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 중랑구 봉우재로 40 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "로얄약국",
    "Address": "서울특별시 중랑구 망우로 247 로얄스포츠센터 1층 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 중랑구 망우로 271 (상봉동, 서울중랑우체국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "3층엠코약국",
    "Address": "서울특별시 중랑구 망우로 353 C동 309호 (상봉동, 현대엠코이노시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 중랑구 신내역로 165 203호 (신내동, 신내우디안2단지상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "단풍약국",
    "Address": "서울특별시 중랑구 동일로 680 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ5MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "종로태평양약국",
    "Address": "서울특별시 중랑구 동일로 917 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQxMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 중랑구 신내로 128 근린생활시설동 1층 (신내동, 동성아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "상봉 태평양약국",
    "Address": "서울특별시 중랑구 면목로 481 오렌지타워 1층 101호 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQxMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "고려약국",
    "Address": "서울특별시 중랑구 상봉로 49 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ5MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "온누리사랑약국",
    "Address": "서울특별시 중랑구 용마산로 438 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQwMyQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "수성약국",
    "Address": "서울특별시 중랑구 신내로 115 113호 (신내동, 도시개발(아)10단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "세화당약국",
    "Address": "서울특별시 중랑구 중랑역로 21 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "채움약국",
    "Address": "서울특별시 중랑구 봉화산로 39 HJ빌딩 1층 103호 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ2MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "서울동산약국",
    "Address": "서울특별시 중랑구 신내로16길 17 1층 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "백십자약국",
    "Address": "서울특별시 중랑구 면목로48길 12 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "제일한사랑약국",
    "Address": "서울특별시 중랑구 망우로 505 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "오성약국",
    "Address": "서울특별시 중랑구 신내로 72 원빌딩 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "우성약국",
    "Address": "서울특별시 중랑구 동일로 675 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQwMyQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "연세약국",
    "Address": "서울특별시 중랑구 망우로63길 5 연세약국 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "건명약국",
    "Address": "서울특별시 중랑구 면목로 421 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "통일로약국",
    "Address": "서울특별시 중랑구 용마산로 435 통일로약국 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ2MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "동호일층약국",
    "Address": "서울특별시 중랑구 동일로 925 1층 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "하나로약국",
    "Address": "서울특별시 중랑구 망우로 192 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "늘푸른솔약국",
    "Address": "서울특별시 중랑구 겸재로 178 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "참약사엠바른약국",
    "Address": "서울특별시 중랑구 겸재로 164 1층 103호 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "다솜약국",
    "Address": "서울특별시 중랑구 면목로 475 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQxMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "상아약국",
    "Address": "서울특별시 중랑구 용마산로 494 상아빌딩 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "종로약국",
    "Address": "서울특별시 중랑구 면목로 319 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "다올약국",
    "Address": "서울특별시 중랑구 봉우재로 232 현문학원 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "친절한 명성약국",
    "Address": "서울특별시 중랑구 신내로16길 17 1층 104호 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 중랑구 동일로 803 1층 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "새우림약국",
    "Address": "서울특별시 중랑구 망우로62길 7 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 중랑구 신내로 225 266호 (신내동, 디아뜨갤러리)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQxMyQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "시온약국",
    "Address": "서울특별시 중랑구 면목로 426 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "우정약국",
    "Address": "서울특별시 중랑구 망우로 428 우정약국 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ4OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "아산약국",
    "Address": "서울특별시 중랑구 공릉로 73 1층 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQyIyQ3IyQwMCQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "타워약국",
    "Address": "서울특별시 중랑구 봉화산로 194 710호 (신내동, 신아타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 중랑구 망우로 413 삼영빌딩 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQxMyQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "우리종로약국",
    "Address": "서울특별시 중랑구 용마산로 501 우리약국 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "사가정약국",
    "Address": "서울특별시 중랑구 사가정로51길 3 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ2MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "삼흥약국",
    "Address": "서울특별시 중랑구 망우로 463 1층 103호 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ2MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "초록약국",
    "Address": "서울특별시 중랑구 용마산로 426 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "동아약국",
    "Address": "서울특별시 중랑구 동일로130길 52 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 중랑구 면목로 490 1층 (상봉동, 상봉타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "한빛약국",
    "Address": "서울특별시 중랑구 겸재로 225 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "유앤아이온누리약국",
    "Address": "서울특별시 중랑구 공릉로2길 13 도림빌딩 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "클로버팜약국",
    "Address": "서울특별시 중랑구 사가정로49길 49 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "송이온누리약국",
    "Address": "서울특별시 중랑구 신내로 211 212호 (신내동, 금강리빙스텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "연세메디칼약국",
    "Address": "서울특별시 중랑구 동일로 890 1층 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 중랑구 신내로 135 신내9단지아파트 제상가1동 1층 117호 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "양지약국",
    "Address": "서울특별시 중랑구 동일로 865 1층 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQwMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "먹골온누리약국",
    "Address": "서울특별시 중랑구 공릉로 59 1층 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "조이약국",
    "Address": "서울특별시 중랑구 용마산로 497 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ5MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 중랑구 망우로 474 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "봉화신세계약국",
    "Address": "서울특별시 중랑구 신내로 211 130,131호 (신내동, 금강리빙스텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "솔빛약국",
    "Address": "서울특별시 중랑구 면목로 456 한성빌딩 3층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "녹색건강약국",
    "Address": "서울특별시 중랑구 면목로55길 25 완진빌딩 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ4OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "그랜드약국",
    "Address": "서울특별시 중랑구 사가정로 399 동부빌딩 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ3MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "은혜당약국",
    "Address": "서울특별시 중랑구 망우로32길 49 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "새대우약국",
    "Address": "서울특별시 중랑구 동일로 852 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ5OSQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 중랑구 망우로 198 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 중랑구 동일로 775 그린빌딩 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "오거리약국",
    "Address": "서울특별시 중랑구 면목로33길 33 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "팜코리아약국",
    "Address": "서울특별시 중랑구 면목로 352 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "메디컬수약국",
    "Address": "서울특별시 중랑구 면목로 430 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "큰사랑약국",
    "Address": "서울특별시 중랑구 용마산로117길 45 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "이안온누리약국",
    "Address": "서울특별시 중랑구 면목로 305 1층 (면목동, 성일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQxMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "삼부약국",
    "Address": "서울특별시 중랑구 망우로 410 5층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "백세약국",
    "Address": "서울특별시 중랑구 신내로 82 1층 109호 (신내동, 금강빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ2MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "푸른솔약국",
    "Address": "서울특별시 중랑구 봉우재로 66 103,104호 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQwMyQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "밝은온누리약국",
    "Address": "서울특별시 중랑구 동일로 634 덕천빌딩 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "원약국",
    "Address": "서울특별시 중랑구 망우로 353 C동 313호 (상봉동, 상봉 프레미어스 엠코)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQwMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "다정옵티마약국",
    "Address": "서울특별시 중랑구 동일로143길 29 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "프라자미약국",
    "Address": "서울특별시 중랑구 면목로 311 삼원빌딩 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "평화약국",
    "Address": "서울특별시 중랑구 면목로 418 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4OSQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 중랑구 면목로 419 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "365밝은약국",
    "Address": "서울특별시 중랑구 면목로39길 8 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ2MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "마트약국",
    "Address": "서울특별시 중랑구 동일로 932 301호 (묵동, 묵동자이아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "대일약국",
    "Address": "서울특별시 중랑구 상봉중앙로1길 32 1층 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "이즈약국",
    "Address": "서울특별시 중랑구 망우로 411 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ4MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 중랑구 망우로 403 3층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "면목종로약국",
    "Address": "서울특별시 중랑구 겸재로 121 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "면목약국",
    "Address": "서울특별시 중랑구 겸재로 194 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "새우정약국",
    "Address": "서울특별시 중랑구 동일로169길 9 1층 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQxMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "미래약국",
    "Address": "서울특별시 중랑구 겸재로 113 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "화이트약국",
    "Address": "서울특별시 중랑구 사가정로 395 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "대한약국",
    "Address": "서울특별시 중랑구 신내로16길 17 105호 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "정민약국",
    "Address": "서울특별시 중랑구 용마산로 502 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQ4MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "정성약국",
    "Address": "서울특별시 중랑구 동일로 752 219호 (중화동, 한신프라자상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "송정약국",
    "Address": "서울특별시 중랑구 면목로 495 1층 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQwMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "한신약국",
    "Address": "서울특별시 중랑구 동일로101길 63 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "준약국",
    "Address": "서울특별시 중랑구 겸재로 180 지층 (면목동, 안민빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQxMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "엔파트약국",
    "Address": "서울특별시 중랑구 망우로 203 2층 203,204호 (중화동, 중화동주상복합)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "가나안약국",
    "Address": "서울특별시 중랑구 봉우재로 39 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "동성약국",
    "Address": "서울특별시 중랑구 겸재로 84 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQxMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "온누리신용약국",
    "Address": "서울특별시 중랑구 중랑천로 114-1 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "성지약국",
    "Address": "서울특별시 중랑구 공릉로12가길 52 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ2MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "부민당약국",
    "Address": "서울특별시 중랑구 면목로91길 26 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQxMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "신성모약국",
    "Address": "서울특별시 중랑구 용마산로 424 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "세일약국",
    "Address": "서울특별시 중랑구 면목로45길 36 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "성재약국",
    "Address": "서울특별시 중랑구 사가정로45길 41 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQyIyQ3IyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "로데오약국",
    "Address": "서울특별시 중랑구 면목로 330 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQxMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "대영진약국",
    "Address": "서울특별시 중랑구 용마공원로 16 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ3OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "방약국",
    "Address": "서울특별시 중랑구 면목로 260 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "상봉햇살약국",
    "Address": "서울특별시 중랑구 상봉로 118 E-마트 상봉점 4층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQyIyQ1IyQwMCQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "편한약국",
    "Address": "서울특별시 중랑구 봉화산로 190 신내2동 관상복합청사 102호 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ5MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "정다운온누리약국",
    "Address": "서울특별시 중랑구 사가정로 401 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQxMyQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "새봉화약국",
    "Address": "서울특별시 중랑구 신내로 211 203-A호 (신내동, 금강리빙스텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "면목백화점약국",
    "Address": "서울특별시 중랑구 용마산로 328 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQ3IyQ3MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "구산약국",
    "Address": "서울특별시 중랑구 공릉로2길 7 구산빌딩 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ3MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "새시장약국",
    "Address": "서울특별시 중랑구 망우로62길 81 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "홍약국",
    "Address": "서울특별시 중랑구 면목로 310 3층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQwMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "튼튼약국",
    "Address": "서울특별시 중랑구 면목로 358 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQwMyQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "오렌지약국",
    "Address": "서울특별시 중랑구 망우로 473 무궁화빌딩 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "홍성백약국",
    "Address": "서울특별시 중랑구 중랑역로 150 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "우리보건약국",
    "Address": "서울특별시 중랑구 사가정로51길 45 우리보건약국 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQxMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "영일온누리약국",
    "Address": "서울특별시 중랑구 면목로 457 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "바른성심약국",
    "Address": "서울특별시 중랑구 용마산로 503 1층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "동삼약국",
    "Address": "서울특별시 중랑구 면목로 344-1 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "손약국",
    "Address": "서울특별시 중랑구 중랑역로 62 1층 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "약산약국",
    "Address": "서울특별시 중랑구 겸재로 217 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "아이사랑약국",
    "Address": "서울특별시 중랑구 용마산로 309 지층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "바르다, 허약국",
    "Address": "서울특별시 중랑구 망우로 305 지하1층 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "정문약국",
    "Address": "서울특별시 중랑구 신내로16길 17 101호 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "햇살 온누리약국",
    "Address": "서울특별시 중랑구 사가정로 384 1층 101호 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ2MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "삼우약국",
    "Address": "서울특별시 중랑구 면목로 257 전내과,소아과 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQwMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 중랑구 봉화산로 105 (상봉동, 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ4MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "은행약국",
    "Address": "서울특별시 중랑구 동일로 796 신한은행 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 중랑구 봉우재로 239 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQwMyQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "믿음약국",
    "Address": "서울특별시 중랑구 봉우재로43길 24 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ3OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 중랑구 신내로 82 금강프라자 1층 108호 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 중랑구 망우로 412 기성빌딩 2층 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "건강제일온누리약국",
    "Address": "서울특별시 중랑구 동일로 786 1층 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "태릉프라자약국",
    "Address": "서울특별시 중랑구 중랑역로 51 태능프라자약국 1층 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 중랑구 망우로71길 39 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQwMyQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "팜필리아약국",
    "Address": "서울특별시 중랑구 동일로 932 202동 216,217호 (묵동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQwMyQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "국제약국",
    "Address": "서울특별시 중랑구 봉화산로 194 신아타운 1층 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQwMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "원플러스약국",
    "Address": "서울특별시 중랑구 신내로 201 1층 (신내동, 홈플러스 서울 신내점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ2MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "대신약국",
    "Address": "서울특별시 중랑구 동일로 802 1층 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "한우리약국",
    "Address": "서울특별시 중랑구 망우로 412 4층 (망우동, 기성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "선화약국",
    "Address": "서울특별시 중랑구 망우로 441 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQyIyQ5IyQwMCQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "무궁화약국",
    "Address": "서울특별시 중랑구 면목로 303 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ5OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "우선약국",
    "Address": "서울특별시 중랑구 봉화산로 61 1층 (중화동, 정신빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQxMyQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "보람온누리약국",
    "Address": "서울특별시 중랑구 신내로21길 16 204호 (묵동, 신내두산아파트 상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "단비약국",
    "Address": "서울특별시 중랑구 봉화산로 194 7층 705호 (신내동, 신아타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "뉴월드약국",
    "Address": "서울특별시 중랑구 겸재로49길 18 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQxMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "면목그랜드약국",
    "Address": "서울특별시 중랑구 사가정로 404 1층,지층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "유심약국",
    "Address": "서울특별시 중랑구 봉화산로 217 (신내동, 오상빌딩내)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQxMyQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "인제약국",
    "Address": "서울특별시 중랑구 망우로 214 1층 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ5OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "예인약국",
    "Address": "서울특별시 중랑구 면목로 415 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQxMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "새하늘약국",
    "Address": "서울특별시 중랑구 겸재로 185 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5OSQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "스타약국",
    "Address": "서울특별시 중랑구 망우로 216 1층 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQxMyQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "성경온누리약국",
    "Address": "서울특별시 중랑구 망우로 478 (망우동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQxMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 중랑구 상봉중앙로1길 12 1층 (상봉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQxIyQwMCQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "서울메디칼약국",
    "Address": "서울특별시 중랑구 신내로16길 17 103호 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "편안한약국",
    "Address": "서울특별시 중랑구 사가정로 398 JS빌딩 1층 (면목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQxMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "덕수약국",
    "Address": "서울특별시 중랑구 중랑역로 33 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "대원사약국",
    "Address": "서울특별시 중랑구 중랑역로 90 대원메디컬빌딩 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ4OSQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 중랑구 신내로 50-3 선일빌딩 (신내동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "탑약국",
    "Address": "서울특별시 중랑구 망우로 171 (중화동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "매일여는약국",
    "Address": "서울특별시 양천구 목동동로 233-1 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQyIyQxIyQwMCQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "메디팜신정교약국",
    "Address": "서울특별시 양천구 신목로 36 102호 (신정동, 대보빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQwMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 양천구 곰달래로5길 17 신월프라자 1층 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "엘림약국",
    "Address": "서울특별시 양천구 목동로3길 57 (신정동, 양천아파트 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "성심약국",
    "Address": "서울특별시 양천구 목동중앙북로 128 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "온누리학마을약국",
    "Address": "서울특별시 양천구 신정로14길 6 103호 (신정동, 학마을상가 1단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "보현약국",
    "Address": "서울특별시 양천구 목동중앙남로4길 9 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ3MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "서남온누리약국",
    "Address": "서울특별시 양천구 신정이펜2로 14 (신정동, 서남 프라자2)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ2MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "신월시장약국",
    "Address": "서울특별시 양천구 곰달래로13길 20-1 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "보람약국",
    "Address": "서울특별시 양천구 목동중앙본로 97 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "새우리약국",
    "Address": "서울특별시 양천구 국회대로10길 9 1층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "목동파라곤약국",
    "Address": "서울특별시 양천구 목동서로 155 목동파라곤 지하1층 7호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ2MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "청송온누리약국",
    "Address": "서울특별시 양천구 목동중앙본로7길 45 108호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "신목약국",
    "Address": "서울특별시 양천구 목동중앙로 85 지하1층 104호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "하늘사랑약국",
    "Address": "서울특별시 양천구 목동동로 293 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "목동센트럴약국",
    "Address": "서울특별시 양천구 신월로 170 1층 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "홍삼약국",
    "Address": "서울특별시 양천구 중앙로 253 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "제성약국",
    "Address": "서울특별시 양천구 목동중앙본로7길 48 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQwMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "동신약국",
    "Address": "서울특별시 양천구 목동동로12길 17 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ5OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "목동세명약국",
    "Address": "서울특별시 양천구 목동중앙북로 27 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "목동조은약국",
    "Address": "서울특별시 양천구 목동서로 70 관리동 상가109호 (목동, 목동신시가지아파트2단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ3OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "팜메이트하나로약국",
    "Address": "서울특별시 양천구 오목로 68 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQxMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "옵티마금약국",
    "Address": "서울특별시 양천구 목동중앙남로 100 102동 상가106호 (목동, 성원아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ4OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 양천구 목동중앙남로11길 4 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "온누리유미숙약국",
    "Address": "서울특별시 양천구 목동로 185 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "테마프라자약국",
    "Address": "서울특별시 양천구 목동서로 389 101호 (신정동, 테마상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "새목동약국",
    "Address": "서울특별시 양천구 목동서로 37 (목동, 하이베라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQxMyQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "제민약국",
    "Address": "서울특별시 양천구 곰달래로10길 9 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ5OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "목동약국",
    "Address": "서울특별시 양천구 오목로 232 112호 (신정동, 보성상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "소중한약국",
    "Address": "서울특별시 양천구 오목로 64 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "진생약국",
    "Address": "서울특별시 양천구 곰달래로 20 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "승주약국",
    "Address": "서울특별시 양천구 오목로 196 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "상마약국",
    "Address": "서울특별시 양천구 신목로 100-6 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "홍일태평양약국",
    "Address": "서울특별시 양천구 목동로 229 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "한결약국",
    "Address": "서울특별시 양천구 오목로 344 (목동, 청학빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ3OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 양천구 월정로 127 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "심지약국",
    "Address": "서울특별시 양천구 오목로 197 1층 (신정동, 이스트만빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "새열린약국",
    "Address": "서울특별시 양천구 신목로 34 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "우성메디칼약국",
    "Address": "서울특별시 양천구 지양로 78 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "중앙제일약국",
    "Address": "서울특별시 양천구 신목로 84 1층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 양천구 목동중앙남로 3 4층 (목동, 선훈아이엔지빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 양천구 중앙로 247 1층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQwMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "온누리조은약국",
    "Address": "서울특별시 양천구 곰달래로5길 30 (신월동, 은성아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "홍익후문약국",
    "Address": "서울특별시 양천구 목동중앙서로2길 9 1층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQwMyQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "우주약국",
    "Address": "서울특별시 양천구 목동서로 280 (신정동, 목동아파트 8단지 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ5OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "문화약국",
    "Address": "서울특별시 양천구 지양로3길 10-1 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "보룡약국",
    "Address": "서울특별시 양천구 목동중앙북로 3 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3OSQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "백석메디칼약국",
    "Address": "서울특별시 양천구 곰달래로 47 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "한울약국",
    "Address": "서울특별시 양천구 오목로 299 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "소망이 샘솟는 느티나무 한약국",
    "Address": "서울특별시 양천구 목동서로 400 108호 (신정동, 목동아파트10단지B상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQxMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "삼주약국",
    "Address": "서울특별시 양천구 신목로 86 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQwMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "경민약국",
    "Address": "서울특별시 양천구 신월로10길 16 (신월동, 삼성아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ2MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "동일프라자약국",
    "Address": "서울특별시 양천구 신정로7길 60-5 107호 (신정동, 동일프라자빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "신왕약국",
    "Address": "서울특별시 양천구 남부순환로40길 50 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQyIyQxIyQwMCQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 양천구 오목로 193 1층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQzIyQ2MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 양천구 공항대로 618 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "백십자약국",
    "Address": "서울특별시 양천구 신월로 176 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQxMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "건강한우리약국",
    "Address": "서울특별시 양천구 지양로 22 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQwMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "모아약국",
    "Address": "서울특별시 양천구 남부순환로59길 9 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "창대온누리약국",
    "Address": "서울특별시 양천구 목동중앙북로 13-1 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "신월메디칼약국",
    "Address": "서울특별시 양천구 남부순환로 329 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "더선약국",
    "Address": "서울특별시 양천구 공항대로 630 1층 (목동, 어바니엘)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ2MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "송약국",
    "Address": "서울특별시 양천구 오목로 325 지하1층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "상쾌한해든약국",
    "Address": "서울특별시 양천구 목동서로 256 4층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ4MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 양천구 목동서로 340 104,105호 (신정동, 목동신시가지아파트9단지 에이상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ2MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "해든아침약국",
    "Address": "서울특별시 양천구 목동동로 293 1층 26,27호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQwMyQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 양천구 곰달래로5길 30 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQyIyQ3IyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "목동복지약국",
    "Address": "서울특별시 양천구 목동동로 430 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "목동온누리약국",
    "Address": "서울특별시 양천구 목동동로 55 101,102호 (신정동, 밀레니엄프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 양천구 남부순환로72길 20 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "호성약국",
    "Address": "서울특별시 양천구 중앙로36길 16-1 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "대우실로암약국",
    "Address": "서울특별시 양천구 월정로50길 10 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "코끼리약국",
    "Address": "서울특별시 양천구 등촌로 142 1층 103호, 104호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "한약국",
    "Address": "서울특별시 양천구 월정로 57 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "햇살애약국",
    "Address": "서울특별시 양천구 목동중앙북로 95 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "예인약국",
    "Address": "서울특별시 양천구 지양로 82 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 양천구 중앙로 275 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 양천구 오목로 322 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ4MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 양천구 지양로 73 1층 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 양천구 목동남로4길 2 207호 (신정동, 세양청마루2차주상복합)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "새무지개약국",
    "Address": "서울특별시 양천구 신월로 282 2층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "팜빌편안약국",
    "Address": "서울특별시 양천구 목동중앙본로 40 1층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "메디팜성화약국",
    "Address": "서울특별시 양천구 남부순환로40길 63 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신정하나약국",
    "Address": "서울특별시 양천구 신목로 33 1층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQwMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "이펜약국",
    "Address": "서울특별시 양천구 신정이펜2로 12 105호 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "온누리은혜약국",
    "Address": "서울특별시 양천구 신정로 293 112, 114호 (신정동, 신트리 1단지 A상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ4MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "무지개약국",
    "Address": "서울특별시 양천구 등촌로 214 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQxMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "월드약국",
    "Address": "서울특별시 양천구 목동서로 77 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "오렌지라임약국",
    "Address": "서울특별시 양천구 목동로 223 2층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "종로프라자약국",
    "Address": "서울특별시 양천구 목동로27길 5 1층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "동일약국",
    "Address": "서울특별시 양천구 월정로 139-1 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ3OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "해든이화약국",
    "Address": "서울특별시 양천구 목동동로 435 103,104호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "별약국",
    "Address": "서울특별시 양천구 오목로 345 목동 슬로우스퀘어 108호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "코코약국",
    "Address": "서울특별시 양천구 등촌로 32 목동태영프라자 106호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "신국경약국",
    "Address": "서울특별시 양천구 목동중앙본로 113 2동 104호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "세왕약국",
    "Address": "서울특별시 양천구 중앙로 235 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "한솔약국",
    "Address": "서울특별시 양천구 목동동로 63 109호 (신정동, 대영프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQyIyQ1IyQwMCQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "경남약국",
    "Address": "서울특별시 양천구 목동서로 38 상가A동 107호, 113호 (목동, 목동신시가지아파트1단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQyIyQ1IyQwMCQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "미라클약국",
    "Address": "서울특별시 양천구 목동동로 379 113호 (목동, 광장상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ5OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "백세약국",
    "Address": "서울특별시 양천구 남부순환로 405 그라비스 102동 101호 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ3OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "가람약국",
    "Address": "서울특별시 양천구 공항대로 564 1층 5호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "동의림생약국",
    "Address": "서울특별시 양천구 목동서로 133-2 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "새누리약국",
    "Address": "서울특별시 양천구 등촌로 32 목동태영프라자 102호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQxMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "팜코리아약국",
    "Address": "서울특별시 양천구 등촌로 26 1층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ2MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "새롬약국",
    "Address": "서울특별시 양천구 오목로 70 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "신세기약국",
    "Address": "서울특별시 양천구 곰달래로5길 42 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "엄마손약국",
    "Address": "서울특별시 양천구 지양로 30 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "행림약국",
    "Address": "서울특별시 양천구 목동동로 130 129호 (신정동, 목동14단지 B상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "목동한미약국",
    "Address": "서울특별시 양천구 목동남로4길 2 118~123호 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ3OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "메디팜금빛약국",
    "Address": "서울특별시 양천구 목동동로 379 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "목동벧엘약국",
    "Address": "서울특별시 양천구 목동동로 430 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "목동정문약국",
    "Address": "서울특별시 양천구 목동동로 435 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "신정이화약국",
    "Address": "서울특별시 양천구 신월로 304 1층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "프라자약국",
    "Address": "서울특별시 양천구 중앙로32길 55 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ3OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "경희메디칼약국",
    "Address": "서울특별시 양천구 남부순환로59길 6 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQwMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "2층소망약국",
    "Address": "서울특별시 양천구 월정로 50 209호 (신월동, 청솔아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQxIyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 양천구 신월로 177 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ2MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "메디칼중앙약국",
    "Address": "서울특별시 양천구 오목로 312 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "다민약국",
    "Address": "서울특별시 양천구 신정이펜2로 20 401호 (신정동, 서남프라자1)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ5OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 양천구 남부순환로 654 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "청솔약국",
    "Address": "서울특별시 양천구 월정로 50 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "이안약국",
    "Address": "서울특별시 양천구 국회대로 252 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ5OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "가까운온누리약국",
    "Address": "서울특별시 양천구 목동서로 349 센트럴프라자 106호 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "메디팜금성약국",
    "Address": "서울특별시 양천구 남부순환로40가길 15-1 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQxMyQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "일준약국",
    "Address": "서울특별시 양천구 오목로 48 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQxMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "소망온누리약국",
    "Address": "서울특별시 양천구 지양로 68 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ3MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "대우마이빌약국",
    "Address": "서울특별시 양천구 공항대로 552 1층 (목동, 대우마이빌빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "동인프라자약국",
    "Address": "서울특별시 양천구 남부순환로40길 13 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ4OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "우리이화약국",
    "Address": "서울특별시 양천구 남부순환로 330 신월동 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "연성약국",
    "Address": "서울특별시 양천구 중앙로 262 1층 102호 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ4OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "보리약국",
    "Address": "서울특별시 양천구 신월로 338 1층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "보미진온누리약국",
    "Address": "서울특별시 양천구 등촌로 224 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "에이치약국",
    "Address": "서울특별시 양천구 오목로 300 206동 110호 (목동, 현대하이페리온2)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "조아약국",
    "Address": "서울특별시 양천구 목동동로 73 107호 (신정동, 양지빌딩ll)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ2MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "태평양온누리약국",
    "Address": "서울특별시 양천구 신월로 314 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ5MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 양천구 중앙로 298 문화트윈타워 101호 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQwMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "마트온누리약국",
    "Address": "서울특별시 양천구 오목로 299 지하101호 (목동, 목동트라팰리스 웨스턴에비뉴)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "수정약국",
    "Address": "서울특별시 양천구 중앙로 276 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ3MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "행복한김약국",
    "Address": "서울특별시 양천구 신정이펜1로 50 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "레스큐약국",
    "Address": "서울특별시 양천구 목동서로 49 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "예주약국",
    "Address": "서울특별시 양천구 목동서로 67 109,110호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ4OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "행복한문약국",
    "Address": "서울특별시 양천구 남부순환로 356 1층 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "영민약국",
    "Address": "서울특별시 양천구 목동동로 430 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "김약국",
    "Address": "서울특별시 양천구 지양로 75 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 양천구 목동중앙본로28길 1 1층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "목동행복한약국",
    "Address": "서울특별시 양천구 목동동로 309 지1층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "미그린약국",
    "Address": "서울특별시 양천구 신월로 341 4층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQxMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "41약국",
    "Address": "서울특별시 양천구 목동동로 293 현대41타워 1층 36호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQwMyQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "오이한약국",
    "Address": "서울특별시 양천구 목동중앙본로7길 37 101호 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQxMyQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "목동세계로약국",
    "Address": "서울특별시 양천구 목동동로12길 45 (목동, 삼익아파트 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "로데오약국",
    "Address": "서울특별시 양천구 신정중앙로 103 1층 (신정동, 담우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3OSQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "박약국",
    "Address": "서울특별시 양천구 목동중앙북로 10 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "내외약국",
    "Address": "서울특별시 양천구 신월로 165 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 양천구 곰달래로13길 58 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "팜스토리약국",
    "Address": "서울특별시 양천구 목동서로 170 홈플러스목동점 지하2층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQ1IyQwMCQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "행복한온누리약국",
    "Address": "서울특별시 양천구 목동동로8길 23 메리트윈 상가동 105호 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ5MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "나눔약국",
    "Address": "서울특별시 양천구 목동중앙로 95 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ4MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "좋은약국",
    "Address": "서울특별시 양천구 남부순환로59길 2 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQyIyQ1IyQwMCQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "양천뿌리약국",
    "Address": "서울특별시 양천구 지양로 74 1층 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "신세계약국",
    "Address": "서울특별시 양천구 신정로 312 107호 (신정동, 목동뉴프라자상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "맑은약국",
    "Address": "서울특별시 양천구 중앙로29길 61 상가동 108호 (신월동, 신정뉴타운롯데캐슬)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "건강온누리약국",
    "Address": "서울특별시 양천구 오목로 350 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "이준약국",
    "Address": "서울특별시 양천구 신월로 187 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "도담약국",
    "Address": "서울특별시 양천구 목동중앙남로4길 4 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQwMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "새서울온누리약국",
    "Address": "서울특별시 양천구 공항대로 558 1층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ5OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "보생약국",
    "Address": "서울특별시 양천구 공항대로 624 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQwMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "메디팜장약국",
    "Address": "서울특별시 양천구 목동남로4길 32 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQxMyQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "호약국",
    "Address": "서울특별시 양천구 월정로 165 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "샘약국",
    "Address": "서울특별시 양천구 화곡로 51 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "인지온누리약국",
    "Address": "서울특별시 양천구 신정중앙로 107 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQwMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "목동즐거운약국",
    "Address": "서울특별시 양천구 목동로 210 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ4OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "드림온누리약국",
    "Address": "서울특별시 양천구 목동중앙본로 68-1 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ2MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "조일약국",
    "Address": "서울특별시 양천구 신월로 168 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "믿음약국",
    "Address": "서울특별시 양천구 목동중앙북로7가길 61 103호 (목동, 리치스케어)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "옵티마자연약국",
    "Address": "서울특별시 양천구 신목로 102 (목동, 대경프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "신월우리약국",
    "Address": "서울특별시 양천구 월정로 51 104호 (신월동, 청송프라임)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "한성약국",
    "Address": "서울특별시 양천구 목동로 201 1층 (신정동, 한성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQyIyQ1IyQwMCQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "메디칼으뜸약국",
    "Address": "서울특별시 양천구 신정이펜2로 12 이펜하우스타워 104호 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQxMyQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "메디팜서울약국",
    "Address": "서울특별시 양천구 목동동로 59 104호 (신정동, 로얄프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "서강약국",
    "Address": "서울특별시 양천구 목동중앙본로 126 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "가정약국",
    "Address": "서울특별시 양천구 목동중앙본로 128-2 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQwMyQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "유명약국",
    "Address": "서울특별시 양천구  신월로 164 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ5OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "강약국",
    "Address": "서울특별시 양천구 화곡로 105 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "경창약국",
    "Address": "서울특별시 양천구 월정로 53 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "구룡약국",
    "Address": "서울특별시 양천구 목동서로 340 상가비동 129호 (신정동, 목동신시가지아파트9단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "목동건강약국",
    "Address": "서울특별시 양천구 목동로27길 6 1층 (신정동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 양천구 목동중앙로 71 2층 (목동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ2MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "연세약국",
    "Address": "서울특별시 양천구 화곡로4길 21 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQwMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "다올약국",
    "Address": "서울특별시 양천구 남부순환로40길 7 (신월동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "천지인약국",
    "Address": "서울특별시 양천구 중앙로 282 (신정동, 에이스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "한림약국",
    "Address": "서울특별시 양천구 중앙로32길 61 102호 (신정동, 현대프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQyIyQ3IyQwMCQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "행복약국",
    "Address": "서울특별시 양천구 남부순환로59길 3 1층 102호 (신월동, 우영아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQxMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "위드팜서초역약국",
    "Address": "서울특별시 서초구 반포대로 138 양진빌딩 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ5MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "곰돌이스타약국",
    "Address": "서울특별시 서초구 방배로 226 3층 303호 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQyIyQxIyQwMCQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "늘편한약국",
    "Address": "서울특별시 서초구 서초대로74길 3 윤빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQwMyQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "서초로하스약국",
    "Address": "서울특별시 서초구 서초중앙로 39 21세기 병원 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQxMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 서초구 서초중앙로 230 105호 (반포동, 동화반포프라자빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ5MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "방배프라자약국",
    "Address": "서울특별시 서초구 방배중앙로29길 3 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "진흥온누리약국",
    "Address": "서울특별시 서초구 서초대로 389 1층 105,106호 (서초동, 진흥상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ2MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "연두약국",
    "Address": "서울특별시 서초구 태봉로 70 우면프라자Ι 110호 (우면동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "방배세명약국",
    "Address": "서울특별시 서초구 동작대로 114 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQxMyQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "수정약국",
    "Address": "서울특별시 서초구 논현로 67 1층 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ3OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "샘터약국",
    "Address": "서울특별시 서초구 서초중앙로 230 101호 (반포동, 동화반포프라자빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "숲약국",
    "Address": "서울특별시 서초구 잠원로 148 107호 (잠원동, 잠원연합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "나은약국",
    "Address": "서울특별시 서초구 남부순환로287길 9-1 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "신명성약국",
    "Address": "서울특별시 서초구 서래로8길 1 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ2MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "서초당약국",
    "Address": "서울특별시 서초구 서초중앙로 107 (서초동, 삼화빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "양재로하스약국",
    "Address": "서울특별시 서초구 강남대로 48-6 1층 101호 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 서초구 신반포로 176 125호 (반포동, 센트럴시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ5OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "보람약국",
    "Address": "서울특별시 서초구 서초중앙로 239 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ3OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "아란약국",
    "Address": "서울특별시 서초구 서운로 216 GDA주니어스쿨 203호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "열린약국",
    "Address": "서울특별시 서초구 동작대로 130 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "소화약국",
    "Address": "서울특별시 서초구 방배로 87 1층 1호 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ2MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "킴스약국",
    "Address": "서울특별시 서초구 잠원로 69 1층 (잠원동, 킴스클럽)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQyIyQ1IyQwMCQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "서초미소약국",
    "Address": "서울특별시 서초구 서초중앙로 230 408호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ3OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 서초구 서초중앙로22길 8 행림약품 1층 2호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQwMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "늘픔약국",
    "Address": "서울특별시 서초구 헌릉로8길 9-8 1층 108호 (내곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "한샘약국",
    "Address": "서울특별시 서초구 신반포로 205 6동 1층 (잠원동, 반포쇼핑)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "이오당약국",
    "Address": "서울특별시 서초구 동산로6길 38 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ2MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "행복약국",
    "Address": "서울특별시 서초구 사임당로 151 145,146호 (서초동, 무지개쇼핑)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "연세온누리약국",
    "Address": "서울특별시 서초구 신반포로 177 3동 1층 55호,56호 (잠원동, 반포쇼핑)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQzIyQ3MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 서초구 효령로 394 102호 (서초동, 시범빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQxMyQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "제이약국",
    "Address": "서울특별시 서초구 서초대로 323 삼풍프라자 1층 6호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ3MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 서초구 서초대로 302 102호 (서초동, 인앤인빌딩 )"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "기쁨약국",
    "Address": "서울특별시 서초구 효령로 396 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ4OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "브라운스톤약국",
    "Address": "서울특별시 서초구 서초대로 334 1층 105호 (서초동, 브라운스톤)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQwMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "반포프라자약국",
    "Address": "서울특별시 서초구 신반포로 329 1층 5호 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQwMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "건강과행복이열리는약국",
    "Address": "서울특별시 서초구 서초대로 307 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "메디칼허브약국",
    "Address": "서울특별시 서초구 강남대로 615 1층 (잠원동, 금정빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "다솜약국",
    "Address": "서울특별시 서초구 신반포로 41 K동 12호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ5OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 서초구 동작대로 134 5층 (방배동, 가나안빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ1IyQ3MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "생각하는약국",
    "Address": "서울특별시 서초구 청계산로9길 70 105호 (내곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ2MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "빛샘온누리약국",
    "Address": "서울특별시 서초구 서초대로 331 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ4OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "강남메디칼약국",
    "Address": "서울특별시 서초구 방배로 174 1층 (방배동, 태창빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQyIyQzIyQwMCQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "스마일약국",
    "Address": "서울특별시 서초구 동작대로 132 지하2층 (방배동, 안석빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "푸른온누리약국",
    "Address": "서울특별시 서초구 바우뫼로35길 28 1층 (양재동, 고원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "펜타약국",
    "Address": "서울특별시 서초구 서초대로78길 48 (서초동, 송림빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "평강약국",
    "Address": "서울특별시 서초구 서초중앙로24길 55 306호 (서초동, 중앙서초플라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "서초아트약국",
    "Address": "서울특별시 서초구 반포대로 58 201동 12호 (서초동, 서초아트자이상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "플러스엔약국",
    "Address": "서울특별시 서초구 강남대로53길 7 102호 (서초동, 애니타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "이수온누리약국",
    "Address": "서울특별시 서초구 동작대로 108 304호 (방배동, 디오슈페리움2차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "더블유스토어하이약국",
    "Address": "서울특별시 서초구 사임당로 39 한성빌딩 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQwMyQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 서초구 신반포로 100 래미안 퍼스티지 신반포역상가 2층 210호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "하나로약국",
    "Address": "서울특별시 서초구 청계산로 10 1층 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "행복을여는서래약국",
    "Address": "서울특별시 서초구 서래로5길 3 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ5MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "메디팜 동양약국",
    "Address": "서울특별시 서초구 사임당로 157 릿타워 410호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5MiQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "구심약국",
    "Address": "서울특별시 서초구 동광로3길 70 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ3OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "자이프라자약국",
    "Address": "서울특별시 서초구 잠원로 24 1층 (반포동, 반포자이프라자상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "현대영약국",
    "Address": "서울특별시 서초구 강남대로 375 4층 (서초동, 서초현대타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ5OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "주앙약국",
    "Address": "서울특별시 서초구 방배로 39 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "다사랑약국",
    "Address": "서울특별시 서초구 서초대로74길 11 지하2층 (서초동, 삼성전자빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQxMyQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "정은약국",
    "Address": "서울특별시 서초구 방배중앙로 140 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "서초백화점약국",
    "Address": "서울특별시 서초구 효령로 279 1층 (서초동, 상경빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ5MiQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "양재메디칼약국",
    "Address": "서울특별시 서초구 동산로 64 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ2MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "메디팜나리약국",
    "Address": "서울특별시 서초구 서운로 208 1층 106호 (서초동, 삼호종합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "임마누엘온누리약국",
    "Address": "서울특별시 서초구 방배로 244 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3OSQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "서래비비약국",
    "Address": "서울특별시 서초구 방배로 232 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "모아약국",
    "Address": "서울특별시 서초구 성촌길 34 지하1층 (우면동, (주)삼성전자서울R&D캠퍼스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "바른온누리약국",
    "Address": "서울특별시 서초구 방배로 108 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ3OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "메디케어약국",
    "Address": "서울특별시 서초구 신반포로 157 405호 (잠원동, 일동빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "샘약국",
    "Address": "서울특별시 서초구 사임당로 38 큐브플러스 2층 202-2호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "유킹스파머시메디바움약국",
    "Address": "서울특별시 서초구 효령로 177 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "파스텔약국",
    "Address": "서울특별시 서초구 신반포로33길 27 파스텔프라자 103호 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "서경약국",
    "Address": "서울특별시 서초구 방배로 95 2층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ5IyQwMCQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "퍼스트케어약국",
    "Address": "서울특별시 서초구 강남대로 381 두산베어스텔 304호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ3OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 서초구 서초중앙로 45 1층 102호 (서초동, 서초레몬)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "녹십자약국",
    "Address": "서울특별시 서초구 방배로25길 4 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "교대사랑약국",
    "Address": "서울특별시 서초구 서초대로 335 (서초동, 서흥빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQxMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 서초구 반포대로 114 지하1층 102호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "조달약국",
    "Address": "서울특별시 서초구 반포대로 235 지하1층 (반포동, 효성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQxMyQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "샛별약국",
    "Address": "서울특별시 서초구 서초중앙로24길 27 226호 (서초동, G5센트럴프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQxMyQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "하이팜약국",
    "Address": "서울특별시 서초구 사임당로 178 이즈타워 103호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ5OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "서초내곡약국",
    "Address": "서울특별시 서초구 청계산로 189 1층 105호 (신원동, 내곡드림시티 Ⅱ)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQwMyQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "위드팜수약국",
    "Address": "서울특별시 서초구 사평대로 205 4,5층 BP4-1A호 (반포동, CENTRALCITY반포천 복개주차장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQwMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "구룡수약국",
    "Address": "서울특별시 서초구 논현로31길 41 1층 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQwMyQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "반원온누리약국",
    "Address": "서울특별시 서초구 잠원로3길 40 태남홀딩스 1층 103-2호 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQ1IyQwMCQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "서초늘푸른약국",
    "Address": "서울특별시 서초구 잠원로8길 25 117호 (잠원동, 대림아파트상가 )"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜메트로약국",
    "Address": "서울특별시 서초구 효령로2길 4 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQxMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "우면메디칼약국",
    "Address": "서울특별시 서초구 태봉로 62 105호 (우면동, 네이처프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 서초구 서운로 39 1층 101호 (서초동, 원진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "에이스온누리약국",
    "Address": "서울특별시 서초구 방배로 76 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "강남사랑약국",
    "Address": "서울특별시 서초구 효령로 12 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "남부장수약국",
    "Address": "서울특별시 서초구 동산로 60 1층 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "유경약국",
    "Address": "서울특별시 서초구 방배중앙로 167 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "아이약국",
    "Address": "서울특별시 서초구 서초대로77길 55 에이프로 스퀘어 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQxMyQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "새열린약국",
    "Address": "서울특별시 서초구 강남대로 449-3 보보빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "가온약국",
    "Address": "서울특별시 서초구 강남대로 465 교보타워 B동 지상1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ2MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "다인약국",
    "Address": "서울특별시 서초구 남부순환로 2614 302호 (양재동, 한솔로이젠트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "반포자이중앙약국",
    "Address": "서울특별시 서초구 잠원로 24 408호 (반포동, 반포자이프라자상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQyIyQ3IyQwMCQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "푸른솔약국",
    "Address": "서울특별시 서초구 서초대로 317 1층 (서초동, 건원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQyIyQ3IyQwMCQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "사랑의약국",
    "Address": "서울특별시 서초구 신반포로 165 2동 1층 1-2호 (잠원동, 반포쇼핑타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQxMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 서초구 효령로 229 서울빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ2MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "스타약국",
    "Address": "서울특별시 서초구 강남대로 437 대원빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "온새미약국",
    "Address": "서울특별시 서초구 방배로 223 1층 1호 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "동해물약국",
    "Address": "서울특별시 서초구 동광로12가길 42 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ4OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 서초구 헌릉로8길 45 2층 203호 (내곡동, 서초 포레스타 2단지)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQxMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 서초구 신반포로 205 403호 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "동우약국",
    "Address": "서울특별시 서초구 남부순환로356길 15 111,112,126호 (양재동, 양재종합시장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQxMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "양재시민의숲수약국",
    "Address": "서울특별시 서초구 마방로2길 57 101호 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "세화약국",
    "Address": "서울특별시 서초구 신반포로 100 406호 (반포동, 래미안퍼스티지신반포역상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "씨티약국",
    "Address": "서울특별시 서초구 강남대로 597 1층 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "두리약국",
    "Address": "서울특별시 서초구 사임당로 180 201호 (서초동, 보원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "천사약국",
    "Address": "서울특별시 서초구 사평대로 205 4층 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ3MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "아크로비스타약국",
    "Address": "서울특별시 서초구 서초중앙로 188 지하1층 지하에이-132호 (서초동, 아크로비스타)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "메디컬제일약국",
    "Address": "서울특별시 서초구 방배로 225 1층 (방배동, 성은빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4OSQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 서초구 방배로 32 2층 2호 (방배동, 방배쇼핑센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "원약국",
    "Address": "서울특별시 서초구 서초중앙로 36 1층 (서초동, 준영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQwMyQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "아라약국",
    "Address": "서울특별시 서초구 서초대로77길 3 111호 (서초동, 아라타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "기린약국",
    "Address": "서울특별시 서초구 잠원로 24 130호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 서초구 사평대로56길 7 1층 106호 (서초동, 서초한일유앤아이주상복합)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ3OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 서초구 사임당로 138 101호 (서초동, 신동아아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQyIyQ3IyQwMCQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "대영약국",
    "Address": "서울특별시 서초구 잠원로14길 29 125호 (잠원동, 설악복지센타)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ2MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "새드림약국",
    "Address": "서울특별시 서초구 강남대로 435 주류성빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "늘기쁜약국",
    "Address": "서울특별시 서초구 효령로 200 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "영약국",
    "Address": "서울특별시 서초구 강남대로 415 8층 (서초동, 대동빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4OSQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "에스약국",
    "Address": "서울특별시 서초구 서초대로40길 77 102호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ5MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "숨온누리약국",
    "Address": "서울특별시 서초구 서초대로 114 102호 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "신논현올리브약국",
    "Address": "서울특별시 서초구 강남대로 507 1층 (반포동, 신태양빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQ3MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "고연뿌리약국",
    "Address": "서울특별시 서초구 신반포로 188 지하1층 (반포동, 강남고속터미널역)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ4OSQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "한영온누리약국",
    "Address": "서울특별시 서초구 방배로 36 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ5MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "민들레약국",
    "Address": "서울특별시 서초구 강남대로30길 58 1층 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQyIyQ5IyQwMCQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 서초구 법원로2길 23 101호 (서초동, 한성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "서초온누리약국",
    "Address": "서울특별시 서초구 서초대로 310 지하1층 (서초동, 소망빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQwMyQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 서초구 사평대로57길 54 1층 (반포동, 여호수아빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQwMyQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "강남약국",
    "Address": "서울특별시 서초구 강남대로 463 지하1층 102호 (서초동, 리젠타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "반포다정약국",
    "Address": "서울특별시 서초구 반포대로 287 138호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "굿약국",
    "Address": "서울특별시 서초구 서초대로77길 24 강남 지웰타워2 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "에이티약국",
    "Address": "서울특별시 서초구 강남대로 27 지하1층 (양재동, AT센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQwMyQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "뿌리약국",
    "Address": "서울특별시 서초구 방배로 177 (방배동, 레마빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQxMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "장수알파약국",
    "Address": "서울특별시 서초구 서초중앙로 38 정원빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQxMyQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "신원약국",
    "Address": "서울특별시 서초구 강남대로10길 60-1 101호 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQyIyQzIyQwMCQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "이든약국",
    "Address": "서울특별시 서초구 남부순환로 2636 1층 (양재동, 성문빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ5MiQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "반포소망약국",
    "Address": "서울특별시 서초구 서초중앙로 227 3층 (반포동, 진일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "서초메이플약국",
    "Address": "서울특별시 서초구 남부순환로347길 101 1층 (서초동, 조이빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5OSQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "더하늘약국",
    "Address": "서울특별시 서초구 강남대로 509 1층 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "한성약국",
    "Address": "서울특별시 서초구 신반포로 257 지하1층 (잠원동, 뉴타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ5IyQwMCQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "아라타워아이약국",
    "Address": "서울특별시 서초구 서초대로77길 3 1202호 (서초동, 아라타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQzIyQxMyQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "한일약국",
    "Address": "서울특별시 서초구 법원로 15 지하1층 (서초동, 정곡빌딩 서관)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQyIyQxIyQwMCQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "세진약국",
    "Address": "서울특별시 서초구 서초중앙로 125 1층 105호 (서초동, 로이어즈타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "티파니약국",
    "Address": "서울특별시 서초구 고무래로 18 1층 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQwMyQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 서초구 방배로 115 1층 (방배동, 방배메디칼빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "나을약국",
    "Address": "서울특별시 서초구 서초중앙로 138 3층 (서초동, 우림빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "초이스약국",
    "Address": "서울특별시 서초구 강남대로 375 104호 (서초동, 서초현대타워아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ2MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "논현온누리약국",
    "Address": "서울특별시 서초구 강남대로 541 1층 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ5OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "버클리약국",
    "Address": "서울특별시 서초구 신반포로15길 29 2층 (반포동, 신반포상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "성지약국",
    "Address": "서울특별시 서초구 방배로 268 103호 (방배동, 삼호상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQxMyQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "방배대한약국",
    "Address": "서울특별시 서초구 동작대로 118 107호 (방배동, 방배예다인)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ4OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "홈케어방배약국",
    "Address": "서울특별시 서초구 서초대로 24 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ3OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "영보서초프라자약국",
    "Address": "서울특별시 서초구 방배로 88 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "한신메디칼약국",
    "Address": "서울특별시 서초구 잠원로 94 지층 (잠원동, 한신상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQyIyQ1IyQwMCQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "신청사구내약국",
    "Address": "서울특별시 서초구 반포대로 217 지하1층 (반포동, 조달청사별관동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "보물섬약국",
    "Address": "서울특별시 서초구 잠원로 24 414호 (반포동, 반포자이플라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "신오약국",
    "Address": "서울특별시 서초구 강남대로61길 7 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ4OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "신사스타약국",
    "Address": "서울특별시 서초구 강남대로 621 1층 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "양재프라자약국",
    "Address": "서울특별시 서초구 강남대로 224 1층 104호 (양재동, 한신휴플러스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQwMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "남영약국",
    "Address": "서울특별시 서초구 동광로 75 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ2MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "고명약국",
    "Address": "서울특별시 서초구 바우뫼로 23 101,102호 (우면동, 선일상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "환승약국",
    "Address": "서울특별시 서초구 강남대로 221 107호 (양재동, 양재역환승주차장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "사랑손약국",
    "Address": "서울특별시 서초구 서초대로38길 12 103호 (서초동, 마제스타시티타워원)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ2MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 서초구 서초중앙로 229 1층 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "에이트약국",
    "Address": "서울특별시 서초구 강남대로 423 한승빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "즐거운약국",
    "Address": "서울특별시 서초구 동광로1길 112 206호 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5OSQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 서초구 동작대로 38 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQxMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 서초구 중앙로 582 103호 (우면동, 서초타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQyIyQ5IyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "양재신세계약국",
    "Address": "서울특별시 서초구 매헌로 34 한일빌딩 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQxMyQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "모닝온누리약국",
    "Address": "서울특별시 서초구 강남대로 341 지하1층 (서초동, 삼원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "사당13번약국",
    "Address": "서울특별시 서초구 방배천로 5-3 1층 (방배동, 도양빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "알파약국",
    "Address": "서울특별시 서초구 사임당로 181 102호 (서초동, 대일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "시스템약국",
    "Address": "서울특별시 서초구 방배중앙로23길 1 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ5OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "서초삼성약국",
    "Address": "서울특별시 서초구 서초대로74길 23 102호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "스마트온누리약국",
    "Address": "서울특별시 서초구 강남대로53길 7 강남애니타워 101호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQwMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "위드팜솔약국",
    "Address": "서울특별시 서초구 사평대로 205 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 서초구 서초대로 3-4 1층 101-3호 (방배동, 방배디오슈페리움)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ5MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "금화온누리약국",
    "Address": "서울특별시 서초구 반포대로 287 125호 (반포동, 래미안퍼스티지중심상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ2MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "삼미약국",
    "Address": "서울특별시 서초구 주흥길 8 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "고속터미널약국",
    "Address": "서울특별시 서초구 신반포로 194 서울고속버스터미널 본관동1층 쇼케이스1호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ2MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "서초제일약국",
    "Address": "서울특별시 서초구 방배로 111 1층 (방배동, 근복빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "신우성약국",
    "Address": "서울특별시 서초구 잠원로4길 54 매일종합상가 309호 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQwMyQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "행복나눔약국",
    "Address": "서울특별시 서초구 잠원로 24 406호 (반포동, 반포자이플라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "팜메이트대학당약국",
    "Address": "서울특별시 서초구 서초중앙로22길 40 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 서초구 신반포로 41 1층 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ2MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "약원한약국",
    "Address": "서울특별시 서초구 신반포로 38 1층 10호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 서초구 반포대로30길 82 우서빌딩 1층 102호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQwMyQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "세븐약국",
    "Address": "서울특별시 서초구 서초대로 240 지하1층 B02호 (서초동, 서초동 동일하이빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "메디팜은강약국",
    "Address": "서울특별시 서초구 잠원로14길 29 104호 (잠원동, 설악복지센타)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "8층약국",
    "Address": "서울특별시 서초구 서초중앙로 125 로이어즈타워 8층 803호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 서초구 서초중앙로 42 블루핀타워 B110호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "엔티약국",
    "Address": "서울특별시 서초구 효령로 292 서울남부터미널 117호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ4MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "경희정산한약국",
    "Address": "서울특별시 서초구 방배로 57 1층 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQyIyQ3IyQwMCQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "도일약국",
    "Address": "서울특별시 서초구 사평대로55길 10 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQwMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "3층한사랑약국",
    "Address": "서울특별시 서초구 반포대로 287 311호 (반포동, 래미안퍼스티지중심상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQyIyQxIyQwMCQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "한약국",
    "Address": "서울특별시 서초구 강남대로 545-4 1층 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "씨케이광생약국",
    "Address": "서울특별시 서초구 강남대로 559 1층 101호 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQxMyQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "오약국",
    "Address": "서울특별시 서초구 서래로 46 1층 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "뿌리본약국",
    "Address": "서울특별시 서초구 남부순환로 2585 25호 (서초동, 양재역)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "양재소망약국",
    "Address": "서울특별시 서초구 언남1길 3 1층 102호 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "서초21세기약국",
    "Address": "서울특별시 서초구 신반포로23길 30 1층 (잠원동, 반원상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "자이수약국",
    "Address": "서울특별시 서초구 사평대로45길 10-25 109-2호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "구슬약국",
    "Address": "서울특별시 서초구 서초중앙로 113 영한빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ5MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "내방약국",
    "Address": "서울특별시 서초구 방배로 125 2층 2호 (방배동, 영신빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQxMyQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "일이약국",
    "Address": "서울특별시 서초구 서초대로 306 1층 (서초동, 진영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "십자당약국",
    "Address": "서울특별시 서초구 남부순환로339길 53 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "대림약국",
    "Address": "서울특별시 서초구 사임당로 105 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "다보약국",
    "Address": "서울특별시 서초구 서초대로40길 77 101호 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQwMyQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "온누리동성약국",
    "Address": "서울특별시 서초구 동작대로 194 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQwMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "정신약국",
    "Address": "서울특별시 서초구 방배로 196 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ3OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "방일약국",
    "Address": "서울특별시 서초구 방배로13길 31 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQwMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "이층은약국",
    "Address": "서울특별시 서초구 서초중앙로 230 2층 208호 (반포동, 동화반포프라자상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "아임약국",
    "Address": "서울특별시 서초구 강남대로 439 1층 102호 (서초동, 유화빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "지티타워약국",
    "Address": "서울특별시 서초구 서초대로 411 지하1층 (서초동, 지티타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3OSQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "잠원스타약국",
    "Address": "서울특별시 서초구 잠원로4길 33-2 잠원동 스타빌딩 111호 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQxMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "신세기약국",
    "Address": "서울특별시 서초구 신반포로 219 8동 106호 (잠원동, 반포쇼핑)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQwMyQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "슈퍼빌온누리약국",
    "Address": "서울특별시 서초구 서초중앙로 15 106호 (서초동, 현대슈퍼빌상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQyIyQxIyQwMCQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "해맑은약국",
    "Address": "서울특별시 서초구 남부순환로350길 4 2층 (양재동, 대진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ3OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "보현약국",
    "Address": "서울특별시 서초구 방배로13길 7 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQwMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "수도약국",
    "Address": "서울특별시 서초구 동광로 65 (방배동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ2MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "초록약국",
    "Address": "서울특별시 서초구 바우뫼로7길 8 501호 (우면동, 세신상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "메디안약국",
    "Address": "서울특별시 서초구 강남대로 455 3층 305호 (서초동, 강남태영데시앙루브)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "영동프라자약국",
    "Address": "서울특별시 서초구 강남대로 521-4 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "서리풀약국",
    "Address": "서울특별시 서초구 서리풀길 1 102호 (서초동, 자연빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ4OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "메딕스약국",
    "Address": "서울특별시 서초구 고무래로 32 반포트라이엄프메딕스빌딩 107호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "서초늘봄약국",
    "Address": "서울특별시 서초구 서초대로38길 12 지하2층 (서초동, 마제스타시티,힐스테이트서리풀)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "약사랑약국",
    "Address": "서울특별시 서초구 강남대로 221 양재역환승주차장 3층 303호 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "미래약국",
    "Address": "서울특별시 서초구 고무래로 90-7 서초쇼핑 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ5OSQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "서광약국",
    "Address": "서울특별시 서초구 남부순환로315길 104 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "나무약국",
    "Address": "서울특별시 서초구 명달로 106 원영빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "신사행복나눔약국",
    "Address": "서울특별시 서초구 강남대로 605 휴먼TOWER 104호 (잠원동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQzIyQ4MiQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "아주약국",
    "Address": "서울특별시 서초구 신반포로 22 H-33호 (반포동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQwMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜유일약국",
    "Address": "서울특별시 서초구 효령로46길 14 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQxMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "자연약국",
    "Address": "서울특별시 서초구 효령로68길 114 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "양재팜24약국",
    "Address": "서울특별시 서초구 남부순환로350길 36 1층 (양재동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQxMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "호두온누리약국",
    "Address": "서울특별시 서초구 남부순환로 2449 삼원빌딩 1층 (서초동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "21세기보배약국",
    "Address": "서울특별시 노원구 덕릉로 780 4,5,6호 (상계동, 동아불암아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "남북약국",
    "Address": "서울특별시 노원구 상계로27길 15 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "참빛약국",
    "Address": "서울특별시 노원구 동일로 986 102동 1층 131-A호 (공릉동, 노원 프레미어스 엠코)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "나현약국",
    "Address": "서울특별시 노원구 상계로12길 41 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ2MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "한신약국",
    "Address": "서울특별시 노원구 한글비석로48길 6 101호 (상계동, 한신2차아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ3OSQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "노원종로약국",
    "Address": "서울특별시 노원구 동일로 1102 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 노원구 한글비석로 471 (주)맥스아웃 상계빌딩 4층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4OSQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "메디팜샛별약국",
    "Address": "서울특별시 노원구 동일로 1547 동남빌딩 1층 102호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "우리조은약국",
    "Address": "서울특별시 노원구 동일로 1689 2층 206호 (상계동, 하이베라스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ2MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "i튼튼약국",
    "Address": "서울특별시 노원구 동일로 1059 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 노원구 한글비석로 264 312호 (중계동, 그랜드프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "재성약국",
    "Address": "서울특별시 노원구 노해로 452 107호 (상계동, 노빌리안골드빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQxMyQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 노원구 섬밭로 134 114동 105-5호 (공릉동, 풍림아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ3MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "행복을주는약국",
    "Address": "서울특별시 노원구 동일로 1036 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "종로프라자약국",
    "Address": "서울특별시 노원구 동일로 1353 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQwMyQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "희망약국",
    "Address": "서울특별시 노원구 동일로230가길 15 103호 (상계동, 우방아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "성심온누리약국",
    "Address": "서울특별시 노원구 석계로 49 (월계동, 현대아파트 주상가 122호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "상계하나로약국",
    "Address": "서울특별시 노원구 한글비석로48길 13 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQxMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "건강한약국",
    "Address": "서울특별시 노원구 석계로9길 25 1층 오른쪽점포호 (월계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "행복약국",
    "Address": "서울특별시 노원구 동일로 985 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQyIyQxIyQwMCQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "국약국",
    "Address": "서울특별시 노원구 한글비석로 383 2층 26호 (중계동, 삼창타워프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "딸기약국",
    "Address": "서울특별시 노원구 화랑로51길 78 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "신흥약국",
    "Address": "서울특별시 노원구 공릉로 323 1층 (하계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ5MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "당고개약국",
    "Address": "서울특별시 노원구 상계로 309-1 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQzIyQwMyQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "자인당약국",
    "Address": "서울특별시 노원구 노해로 506 112호 (상계동, 주공6단지 바상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ5MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "화랑온누리약국",
    "Address": "서울특별시 노원구 공릉로 150 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "마들소아약국",
    "Address": "서울특별시 노원구 동일로 1538 12단지 종합상가 2층 201호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ2MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "동방약국",
    "Address": "서울특별시 노원구 노해로 456 동방빌딩 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "중계상록수약국",
    "Address": "서울특별시 노원구 중계로 218 원광빌딩 1층 102호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 노원구 동일로 1392 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "구름약국",
    "Address": "서울특별시 노원구 섬밭로 152 공릉아파트2단지상가 1층 101호 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ3MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "황인재약국",
    "Address": "서울특별시 노원구 초안산로1길 18 101호 (월계동, 주공아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ2MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "서부약국",
    "Address": "서울특별시 노원구 동일로 1551 삼전빌딩 1층 101,102,107,108호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQxMyQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "인덕약국",
    "Address": "서울특별시 노원구 월계로 370 (월계동, 희성프라자 105호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ5OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "연세약국",
    "Address": "서울특별시 노원구 노해로 492 204호 (상계동, 프린스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQyIyQzIyQwMCQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "무지개온누리약국",
    "Address": "서울특별시 노원구 화랑로 325 (월계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "무궁화약국",
    "Address": "서울특별시 노원구 한글비석로 77 한성여객(주) (하계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQxMyQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "보건약국",
    "Address": "서울특별시 노원구 노원로 333 104호 (중계동, 시영3단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "열린온누리약국",
    "Address": "서울특별시 노원구 공릉로 173 1층 (공릉동, 메디홈즈빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "장수메디컬약국",
    "Address": "서울특별시 노원구 동일로 1077 1층 (공릉동, 스테이션빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3MiQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "바른손약국",
    "Address": "서울특별시 노원구 한글비석로 56 107호 (하계동, 미성아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 노원구 상계로10길 12 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ4MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "미즈약국",
    "Address": "서울특별시 노원구 한글비석로 269 105호 (중계동, 마들프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "청백약국",
    "Address": "서울특별시 노원구 월계로45가길 94 101호 (월계동, 청백아파트4단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQxMyQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "상계사랑약국",
    "Address": "서울특별시 노원구 한글비석로 383 삼창타워프라자 1층 62,63,64,79,80,81호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ2MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "노원메디칼약국",
    "Address": "서울특별시 노원구 동일로 1401 201호 (상계동, 상아빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ4MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "하니약국",
    "Address": "서울특별시 노원구 동일로 1099 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "아이사랑약국",
    "Address": "서울특별시 노원구 노원로34길 112 1층 (상계동, 코럴빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQxMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "상아온누리약국",
    "Address": "서울특별시 노원구 동일로 1401 1층 (상계동, 상아빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQxMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "목원약국",
    "Address": "서울특별시 노원구 상계로37길 29 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ2MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "수락100세약국",
    "Address": "서울특별시 노원구 동일로 1673 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQxMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "하님약국",
    "Address": "서울특별시 노원구 한글비석로 410 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "21세기상계약국",
    "Address": "서울특별시 노원구 동일로 1548 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ2MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "샘물약국",
    "Address": "서울특별시 노원구 노원로 43 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ2MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "다정약국",
    "Address": "서울특별시 노원구 한글비석로14길 8 105호 (중계동, 주공2단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "푸른솔약국",
    "Address": "서울특별시 노원구 공릉로58가길 14 1층 (하계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "중계열방약국",
    "Address": "서울특별시 노원구 한글비석로 250 2층 222호 (중계동, 그린코아빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ2MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 노원구 노원로 246 욱현하이브 105호 (하계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "태능약국",
    "Address": "서울특별시 노원구 공릉로 99 서울동아의원 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQzIyQwMCQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "정성약국",
    "Address": "서울특별시 노원구 한글비석로 263 성모빌딩 302-1호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQzIyQwMCQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "연수온누리약국",
    "Address": "서울특별시 노원구 동일로197길 11 공삼빌딩 102호 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQxMyQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "한빛온누리약국",
    "Address": "서울특별시 노원구 동일로203가길 29 211 일부,212호 (중계동, 브라운스톤중계)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "연세현약국",
    "Address": "서울특별시 노원구 한글비석로 436-1 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4OSQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "신태평약국",
    "Address": "서울특별시 노원구 광운로 45 (월계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ5MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "석사민주약국",
    "Address": "서울특별시 노원구 한글비석로 253 2층 205호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5MiQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 노원구 동일로 1677 1층 (상계동, 제성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "마들한중약국",
    "Address": "서울특별시 노원구 동일로 1529 합동빌딩 203호 마들한중약국 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "수락프라자약국",
    "Address": "서울특별시 노원구 동일로 1669 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "옵티마건강약국",
    "Address": "서울특별시 노원구 동일로204가길 34 110호 (중계동, 씨앤미빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4MiQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "바다약국",
    "Address": "서울특별시 노원구 동일로 1361 208호 (상계동, 상계주공2단지아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3OSQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "수암약국",
    "Address": "서울특별시 노원구 광운로 57 1층 (월계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 노원구 동일로203가길 29 258호,259호 (중계동, 브라운스톤중계)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQyIyQ3IyQwMCQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "동일약국",
    "Address": "서울특별시 노원구 동일로 1343 305호 (상계동, 동일프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ2MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "창희약국",
    "Address": "서울특별시 노원구 한글비석로 253 세신프라자빌딩 4층 405호 일부호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQyIyQ3IyQwMCQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "월계프라자약국",
    "Address": "서울특별시 노원구 초안산로5길 12 110호 (월계동, 월계프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ3OSQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "종로모범약국",
    "Address": "서울특별시 노원구 덕릉로 730 107호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQwMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "참조은약국",
    "Address": "서울특별시 노원구 상계로3길 10 한일빌딩 106호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQwMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "유성약국",
    "Address": "서울특별시 노원구 덕릉로 459-37 123호 (상계동, 주공1단지 가상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQyIyQxIyQwMCQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "화랑대약국",
    "Address": "서울특별시 노원구 노원로1길 67 302호 (공릉동, 대덕프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "평강상록수약국",
    "Address": "서울특별시 노원구 동일로 1545 102호,103호 (상계동, 현대골드씨티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQwMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "더조은약국",
    "Address": "서울특별시 노원구 한글비석로 235 하나프라자빌딩 4층 405호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ3MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "마들하나로약국",
    "Address": "서울특별시 노원구 동일로 1529 303호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQwMyQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "1층호약국",
    "Address": "서울특별시 노원구 한글비석로 383 1층 일부호 (중계동, 삼창타워프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "태양프라자약국",
    "Address": "서울특별시 노원구 덕릉로 773 상계이씨빌딩 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 노원구 석계로 95 (월계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ3OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "다사랑약국",
    "Address": "서울특별시 노원구 한글비석로 254 305호 (중계동, 대명프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ5MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "튼튼온누리약국",
    "Address": "서울특별시 노원구 수락산로 232 미네르바빌딩 102호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ3MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "금강약국",
    "Address": "서울특별시 노원구 한글비석로 365 1층 (중계동, 데미안빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQxMyQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "미래팜약국",
    "Address": "서울특별시 노원구 노해로 492 102호, 103호 (상계동, 프린스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "동산약국",
    "Address": "서울특별시 노원구 동일로 1280 1층 109호,110호 (중계동, 무지개아파트단지내상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ4MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 노원구 한글비석로 384 319호 (중계동, 대호프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ4MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 노원구 노해로 482 4층 (상계동, 덕영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQxMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "건강약국",
    "Address": "서울특별시 노원구 화랑로 463 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ4OSQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "중앙메디칼약국",
    "Address": "서울특별시 노원구 공릉로46길 23 203호 (공릉동, 한보상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 노원구 동일로 1361 206,207호 (상계동, 상계주공2단지아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ3MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "푸른바다약국",
    "Address": "서울특별시 노원구 화랑로 337 106호, 107호 (월계동, 인현빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ5MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 노원구 공릉로 187 3층 303호 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ3MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "부용온누리약국",
    "Address": "서울특별시 노원구 덕릉로73길 18 102호 (중계동, 태인빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "새하늘약국",
    "Address": "서울특별시 노원구 동일로 1308 1층 (중계동, 정안프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ4MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 노원구 동일로 1550 206호 (상계동, 고려프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQwMyQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 노원구 동일로 1279 211호 (중계동, 중계그린아파트 비이상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ5MiQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "소담약국",
    "Address": "서울특별시 노원구 상계로1길 14-11 A동 103호 (상계동, 하이웰빙상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQxMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "중계우리들약국",
    "Address": "서울특별시 노원구 동일로204가길 12 지하2층 (중계동, 홈플러스중계점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "소나무약국",
    "Address": "서울특별시 노원구 노원로 330 롯데마트 지하1층 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "새고운약국",
    "Address": "서울특별시 노원구 동일로 1003 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQyIyQ3IyQwMCQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "올리브약국",
    "Address": "서울특별시 노원구 동일로203가길 29 205호, 206호 (중계동, 브라운스톤중계)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzIxIyQyIyQxIyQwMCQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "지혜약국",
    "Address": "서울특별시 노원구 공릉로59길 18 102호 (하계동, 삼성시티빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQxMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "기쁨약국",
    "Address": "서울특별시 노원구 노원로26길 181 1층 (상계동, 청자빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ2MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "삼호성심약국",
    "Address": "서울특별시 노원구 마들로 111 308호 (월계동, 삼호아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "석계태평양약국",
    "Address": "서울특별시 노원구 화랑로 321 (월계동, 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQwMyQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "밝은미소약국",
    "Address": "서울특별시 노원구 석계로3길 3 (월계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "노원프라자약국",
    "Address": "서울특별시 노원구 동일로 1345 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ3OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "친절한약국",
    "Address": "서울특별시 노원구 노해로75길 14-2 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "중계수암약국",
    "Address": "서울특별시 노원구 덕릉로 694 1층 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQwMyQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "상계온누리약국",
    "Address": "서울특별시 노원구 동일로 1678 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 노원구 노해로 485 101호 (상계동, 금정빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQzIyQwMCQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "나눔약국",
    "Address": "서울특별시 노원구 동일로216길 70 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ5OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 노원구 동일로 1028 한의학명가 1층 106호 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 노원구 섬밭로 229 206-1호 (하계동, 벽산상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "한마음온누리약국",
    "Address": "서울특별시 노원구 한글비석로 56 미성아파트상가 105호 (하계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "우약국",
    "Address": "서울특별시 노원구 섬밭로 209 109호 (하계동, 벽산상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "원자프라자온누리약국",
    "Address": "서울특별시 노원구 공릉로46가길 17-19 1층 (공릉동, 윤탁노블레스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ5OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "뉴석계프라자약국",
    "Address": "서울특별시 노원구 석계로 2 (월계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3OSQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "서경약국",
    "Address": "서울특별시 노원구 한글비석로48길 6 202호 (상계동, 한신2차아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ4MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "세일약국",
    "Address": "서울특별시 노원구 한글비석로 24 108호 (하계동, 하계5단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "대호약국",
    "Address": "서울특별시 노원구 한글비석로 384 대호프라자 317호, 318호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "밝은약국",
    "Address": "서울특별시 노원구 동일로 1005 1층 (공릉동, 대정빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ4MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "동문약국",
    "Address": "서울특별시 노원구 공릉로59나길 78-10 (하계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 노원구 노해로 452 101호, 102호 (상계동, 노빌리안골드)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "하계약국",
    "Address": "서울특별시 노원구 공릉로58가길 8 (하계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "혜인약국",
    "Address": "서울특별시 노원구 노원로34길 92 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "우성약국",
    "Address": "서울특별시 노원구 한글비석로 463 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQ3IyQwMCQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "초록약국",
    "Address": "서울특별시 노원구 한글비석로 384 대호프라자 315호, 316호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQyIyQxIyQwMCQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 노원구 상계로 119 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQyIyQ3IyQwMCQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "열방약국",
    "Address": "서울특별시 노원구 덕릉로 779 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "장생약국",
    "Address": "서울특별시 노원구 섬밭로 263 롯데상가1층 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQxIyQ4OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "누리약국",
    "Address": "서울특별시 노원구 월계로45길 21 203호 (월계동, 롯데캐슬루나아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ4OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "성흔메디카약국",
    "Address": "서울특별시 노원구 한글비석로 265 102호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQyIyQ5IyQwMCQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "건강샘온누리약국",
    "Address": "서울특별시 노원구 동일로243길 33 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "다온약국",
    "Address": "서울특별시 노원구 노해로 495 삼성빌딩 1층 102,103호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "준효약국",
    "Address": "서울특별시 노원구 공릉로 138 준효약국 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "메디칼우리약국",
    "Address": "서울특별시 노원구 동일로 1044 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "다모아약국",
    "Address": "서울특별시 노원구 동일로 1379 105,106호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "위드팜대학약국",
    "Address": "서울특별시 노원구 한글비석로 56 1층 10호 (하계동, 미성아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ5MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "화인팜약국",
    "Address": "서울특별시 노원구 중계로 160 204호 (중계동, 화인상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQxMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "복음약국",
    "Address": "서울특별시 노원구 마들로 31 214호 (월계동, 그랑빌아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQwMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "삼호약국",
    "Address": "서울특별시 노원구 마들로 111 207, 208호 (월계동, 나상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ3MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "하나로약국",
    "Address": "서울특별시 노원구 초안산로 7 105호 (월계동, 월계2단지주공아파트종합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ5MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "한결약국",
    "Address": "서울특별시 노원구 노해로 494 207호 (상계동, 고려빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "라라약국",
    "Address": "서울특별시 노원구 동일로203가길 29 271호, 272호 (중계동, 중계브라운스톤)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "은빛약국",
    "Address": "서울특별시 노원구 동일로245가길 41 109호 (상계동, 은빛2단지아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ1IyQwMCQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "백세약국",
    "Address": "서울특별시 노원구 동일로 1002 101호 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "뉴크로바약국",
    "Address": "서울특별시 노원구 누원로 22 크로바상가 101호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "노원행복한약국",
    "Address": "서울특별시 노원구 상계로 63-7 1층 (상계동, 청우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "상계종로약국",
    "Address": "서울특별시 노원구 한글비석로 363 1층 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQwMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "오피앙약국",
    "Address": "서울특별시 노원구 동일로 1701 110-1호 (상계동, 오피앙오스피스텔 상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "보윤약국",
    "Address": "서울특별시 노원구 동일로192길 20 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQxMyQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "하얀약국",
    "Address": "서울특별시 노원구 동일로197길 21 우성빌딩 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQwMyQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "장약국",
    "Address": "서울특별시 노원구 노해로 488 106호 (상계동, 근호빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "재민약국",
    "Address": "서울특별시 노원구 공릉로 147 2층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "월계우리약국",
    "Address": "서울특별시 노원구 마들로 111 214호 (월계동, 삼호나상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ5OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "싱싱약국",
    "Address": "서울특별시 노원구 수락산로 190 203호 (상계동, 희락상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "365행복약국",
    "Address": "서울특별시 노원구 한글비석로 57 지하1층 (하계동, 세이브존)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "상계1번약국",
    "Address": "서울특별시 노원구 한글비석로20길 23-1 1층 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "노원약국",
    "Address": "서울특별시 노원구 노해로 501 1층 103호 (상계동, 노원빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "수성약국",
    "Address": "서울특별시 노원구 상계로1길 66 1층 102호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQxMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "손약국",
    "Address": "서울특별시 노원구 상계로3길 10 한일빌딩 304호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQxIyQ3IyQ3OSQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "유림약국",
    "Address": "서울특별시 노원구 동일로230가길 15 101호 (상계동, 우방아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ4OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "온누리영광약국",
    "Address": "서울특별시 노원구 동일로228길 35 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "한샘약국",
    "Address": "서울특별시 노원구 상계로27길 7 중앙빌딩 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "봄날약국",
    "Address": "서울특별시 노원구 마들로 31 제주상가동 110호 (월계동, 그랑빌아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "이화봄봄약국",
    "Address": "서울특별시 노원구 동일로 1645 에이동 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "청년약국",
    "Address": "서울특별시 노원구 공릉로 213 102동 103호 (공릉동, 동신아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "정다운약국",
    "Address": "서울특별시 노원구 초안산로2라길 26 상가동 204호 (월계동, 월계센트럴아이파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "미래약국",
    "Address": "서울특별시 노원구 상계로5길 32 금호프라자 110호, 111호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ2MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "자연약국",
    "Address": "서울특별시 노원구 동일로237길 40 101호 (상계동, 대한빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQxMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디팜은아약국",
    "Address": "서울특별시 노원구 덕릉로126길 11 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "월계약국",
    "Address": "서울특별시 노원구 월계로45길 28 1층 2-3호 (월계동, 월계아파트형 공장내)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "세브란스약국",
    "Address": "서울특별시 노원구 섬밭로 229 201호 (하계동, 벽산상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQwMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "경화당약국",
    "Address": "서울특별시 노원구 화랑로 337 (월계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQxMyQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "중계약국",
    "Address": "서울특별시 노원구 중계로14길 29 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQxMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "창덕약국",
    "Address": "서울특별시 노원구 동일로182길 20 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "삼기약국",
    "Address": "서울특별시 노원구 중계로 120 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQxMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "후문약국",
    "Address": "서울특별시 노원구 공릉로59나길 64 (하계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "태능삼호약국",
    "Address": "서울특별시 노원구 화랑로 425-47 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQyIyQ3IyQwMCQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "건강과행복이열리는약국",
    "Address": "서울특별시 노원구 한글비석로 242 113호, 114호 (중계동, 삼부프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "백경약국",
    "Address": "서울특별시 노원구 동일로217가길 11 1층 (상계동, 대일빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQxMyQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "백약국",
    "Address": "서울특별시 노원구 동일로 1350 105호, 106호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQxMyQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "씨앤미3층온누리약국",
    "Address": "서울특별시 노원구 동일로204가길 34 씨앤미복합빌딩 308호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "샘약국",
    "Address": "서울특별시 노원구 한글비석로 270 스카이타워 1층 103호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 노원구 한글비석로 470 1층 (상계동, 동서기업빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQyIyQzIyQwMCQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "소화약국",
    "Address": "서울특별시 노원구 상계로 320 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQwMyQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "상계동문약국",
    "Address": "서울특별시 노원구 동일로 1352 1층 (상계동, 형인빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ5MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "신동아약국",
    "Address": "서울특별시 노원구 마들로3길 15 월계이마트 2층 (월계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ4OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "영신약국",
    "Address": "서울특별시 노원구 한글비석로24길 57 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQxMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "연수약국",
    "Address": "서울특별시 노원구 상계로 65 304호 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 노원구 동일로 1101 2층 (공릉동, 하니빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ2MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "좋은약국",
    "Address": "서울특별시 노원구 노해로 502 1층 (상계동, KT노원플라자별관)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "미션약국",
    "Address": "서울특별시 노원구 동일로 1533 102호 (상계동, 백산빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "연세참사랑약국",
    "Address": "서울특별시 노원구 동일로 992 101호 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ4OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "후생약국",
    "Address": "서울특별시 노원구 동일로227길 26 2층 (상계동, 상계주공아파트15단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ5OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "온누리보람약국",
    "Address": "서울특별시 노원구 한글비석로 474 153호 (상계동, 보람상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "우리사랑약국",
    "Address": "서울특별시 노원구 노원로19길 23 1층 105호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ4MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "한빛약국",
    "Address": "서울특별시 노원구 월계로55길 4 111호 (월계동, 사슴아파트2단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQwMyQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 노원구 노해로 480 (상계동, 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ5OSQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 노원구 월계로 370 103호, 104호 (월계동, 희성프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQwMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "아름다운온누리약국",
    "Address": "서울특별시 노원구 동일로 1370 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ4MiQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "건강플러스약국",
    "Address": "서울특별시 노원구 상계로1길 38 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ3MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "온누리약국",
    "Address": "서울특별시 노원구 상계로5길 12 112호, 113호 (상계동, 동양메이저상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQxMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 노원구 동일로203가길 29 2층 290호 (중계동, 브라운스톤중계)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQyIyQ3IyQwMCQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "상계우리들약국",
    "Address": "서울특별시 노원구 한글비석로 416 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ4OSQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "마들소망약국",
    "Address": "서울특별시 노원구 동일로 1530 105호 (상계동, 다모아빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "용화당약국",
    "Address": "서울특별시 노원구 노원로16길 21 106호 (하계동, 주공9단지아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "활기찬약국",
    "Address": "서울특별시 노원구 한글비석로 359 의암빌딩 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ4OSQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "이손약국",
    "Address": "서울특별시 노원구 공릉로32길 56 101호 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ4MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "the사랑약국",
    "Address": "서울특별시 노원구 한글비석로 331 중계주공3단지아파트단지내상가 101호 (중계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ2MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "백조약국",
    "Address": "서울특별시 노원구 공릉로46길 3 102호 (공릉동, 평화타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "길약국",
    "Address": "서울특별시 노원구 상계로 306 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ3OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 노원구 한글비석로 253 305호 (중계동, 세신프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4OSQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "시온약국",
    "Address": "서울특별시 노원구 한글비석로 459 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "건민약국",
    "Address": "서울특별시 노원구 동일로191길 23 1층 (공릉동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "마음약국",
    "Address": "서울특별시 노원구 동일로 1417 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ2MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 노원구 상계로27길 32 105호, 106호 (상계동, 대명빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "참말로 친절한 약국",
    "Address": "서울특별시 노원구  동일로 1382 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQwMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "새빛약국",
    "Address": "서울특별시 노원구 동일로 1405 국민은행노원지점 1층 (상계동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "호림약국",
    "Address": "서울특별시 광진구 동일로30길 28 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQzIyQ5MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "비전약국",
    "Address": "서울특별시 광진구 동일로18길 73 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "해인약국",
    "Address": "서울특별시 광진구 아차산로33길 63 1층 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ2MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "예담한약국",
    "Address": "서울특별시 광진구 자양로5길 36 1층 3,4호 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "신성온누리약국",
    "Address": "서울특별시 광진구 면목로 127 1층 (중곡동, 신성그랜드타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ2MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "쉐르빌대학약국",
    "Address": "서울특별시 광진구 구의강변로 106 105호 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "스타시티약국",
    "Address": "서울특별시 광진구 아차산로 290 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQxMyQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "신영신약국",
    "Address": "서울특별시 광진구 자양로 42 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "옵티마자양미소약국",
    "Address": "서울특별시 광진구 뚝섬로 606 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "행복한약국",
    "Address": "서울특별시 광진구 자양로15길 27 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzQxIyQxIyQ3IyQ2MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "삼육오약국",
    "Address": "서울특별시 광진구 동일로 86 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQwMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "자양하나약국",
    "Address": "서울특별시 광진구 자양로9길 77 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ5OSQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "옵티마세란약국",
    "Address": "서울특별시 광진구 자양로13길 47 1층 (자양동, 욱영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQwMyQzNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "서울온누리약국",
    "Address": "서울특별시 광진구 구의강변로 99 (구의동, 용천빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ4MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "프라자사랑약국",
    "Address": "서울특별시 광진구 능동로 315 1층 (중곡동, 대남빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "서울제일약국",
    "Address": "서울특별시 광진구 긴고랑로 47 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ5MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "진영약국",
    "Address": "서울특별시 광진구 아차산로57길 42 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQ3IyQ2MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "신대영약국",
    "Address": "서울특별시 광진구 구의강변로 22 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQyIyQzIyQwMCQzNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "현약국",
    "Address": "서울특별시 광진구 광나루로 508 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQxMyQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "새동산약국",
    "Address": "서울특별시 광진구 능동로 378 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQxMyQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "인정온누리약국",
    "Address": "서울특별시 광진구 뚝섬로 655 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ3MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "광진프라자약국",
    "Address": "서울특별시 광진구 면목로 113-1 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQxMyQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 광진구 아차산로 219 (화양동, 삼영빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "건대지하철약국",
    "Address": "서울특별시 광진구 능동로 110 (화양동, 7호선 건대입구역)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "더클래식약국",
    "Address": "서울특별시 광진구 능동로 90 1층 104-2호 (자양동, 더클래식500)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "건대온누리약국",
    "Address": "서울특별시 광진구 능동로 110 스타시티영존 지하2층 B203-1,204호 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "종우약국",
    "Address": "서울특별시 광진구 동일로 34 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ3MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "스마트온누리약국",
    "Address": "서울특별시 광진구 동일로 92-1 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "중곡열린약국",
    "Address": "서울특별시 광진구 능동로51길 44 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "용상약국",
    "Address": "서울특별시 광진구 아차산로 626 (광장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "일송약국",
    "Address": "서울특별시 광진구 광나루로 606 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQxMyQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "백온누리약국",
    "Address": "서울특별시 광진구 면목로 174 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "세란약국",
    "Address": "서울특별시 광진구 천호대로 635 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "참조은약국",
    "Address": "서울특별시 광진구 광나루로 366 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQ2MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "자양열린약국",
    "Address": "서울특별시 광진구 자양로13길 73 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ5OSQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "온누리극동약국",
    "Address": "서울특별시 광진구 아차산로 552 (광장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQyIyQxIyQwMCQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "자양약국",
    "Address": "서울특별시 광진구 자양로 88 광영빌딩 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ2MiQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "뚝도약국",
    "Address": "서울특별시 광진구 뚝섬로 595 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ4MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "기쁨약국",
    "Address": "서울특별시 광진구 면목로 190 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "힘찬약국",
    "Address": "서울특별시 광진구 뚝섬로 631-1 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQzIyQwMCQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "튼튼온누리약국",
    "Address": "서울특별시 광진구 아차산로 450-2 1층 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "서문사랑약국",
    "Address": "서울특별시 광진구 용마산로23길 28 내담터 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ3OSQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "혜성약국",
    "Address": "서울특별시 광진구 능동로3길 5 111호 (자양동, 한강현대아파트종합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4OSQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 광진구 아차산로 375 크레신타워3차 1층 107호 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ4OSQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "혜원약국",
    "Address": "서울특별시 광진구 면목로 173 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQxMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "소망온누리약국",
    "Address": "서울특별시 광진구 능동로 318 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ3MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "우리온누리약국",
    "Address": "서울특별시 광진구 광나루로 614 (구의동, 만택빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQwMyQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "큰별약국",
    "Address": "서울특별시 광진구 뚝섬로59길 67 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ5IyQ4OSQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "신백구약국",
    "Address": "서울특별시 광진구 군자로 86-1 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4MiQzNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "메디칼약국",
    "Address": "서울특별시 광진구 광나루로 355 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQxIyQ5MiQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "연약국",
    "Address": "서울특별시 광진구 아차산로 241 (화양동, 연한빌딩 4층 403호)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ2MiQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "광진온누리약국",
    "Address": "서울특별시 광진구 아차산로69길 8 103, 104호 (광장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQ4OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "스마일약국",
    "Address": "서울특별시 광진구 아차산로 546 104호 (광장동, 삼성아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQyIyQ3IyQwMCQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 광진구 능동로 18 105호 (자양동, 이튼타워리버3차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ4OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "햇살온누리약국",
    "Address": "서울특별시 광진구 능동로13길 39 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQxMyQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "종로온누리약국",
    "Address": "서울특별시 광진구 자양로 115 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4OSQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "금성약국",
    "Address": "서울특별시 광진구 자양로 112 111호,112호,113호 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQyIyQxIyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 광진구 자양로11길 6-8 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "현대온누리약국",
    "Address": "서울특별시 광진구 광나루로56길 85 테크노-마트21 지하1층 D-12호 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQyIyQ3IyQwMCQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "느티나무약국",
    "Address": "서울특별시 광진구 자양로 87 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3OSQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "군자역우리약국",
    "Address": "서울특별시 광진구 천호대로 556 1층 (능동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "청구약국",
    "Address": "서울특별시 광진구 아차산로 502 진넥스 오딧세이 106,107호 (광장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ2MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "건대역약국",
    "Address": "서울특별시 광진구 아차산로 218 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ4OSQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "21세기약국",
    "Address": "서울특별시 광진구 용마산로 49 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQxMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "대화약국",
    "Address": "서울특별시 광진구 동일로 278 나성빌딩 1층 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ5OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "햇빛약국",
    "Address": "서울특별시 광진구 능동로 110 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ5MiQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "아나파약국",
    "Address": "서울특별시 광진구 면목로 168 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "조광옵티마약국",
    "Address": "서울특별시 광진구 긴고랑로9길 29 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "미소약국",
    "Address": "서울특별시 광진구 면목로 126 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ3MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "다온약국",
    "Address": "서울특별시 광진구 긴고랑로 41 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 광진구 자양로13길 4-1 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "온누리강변프라자약국",
    "Address": "서울특별시 광진구 광나루로56길 63 현대프라임아파트 프라자 107,108,109호 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "화양백화점약국",
    "Address": "서울특별시 광진구 광나루로 351 1층 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ4MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "봉화약국",
    "Address": "서울특별시 광진구 긴고랑로 31 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQwMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 광진구 광나루로 604 진넥스 베르디엠 2층 202호 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQwMyQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "다솜약국",
    "Address": "서울특별시 광진구 천호대로 671 (구의동, 파크타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "백조온누리약국",
    "Address": "서울특별시 광진구 면목로 113 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ4MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "수도약국",
    "Address": "서울특별시 광진구 광나루로 529 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "동서울약국",
    "Address": "서울특별시 광진구 강변역로 50 124호 (구의동, 동서울터미널빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ3OSQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "푸른온누리약국",
    "Address": "서울특별시 광진구 천호대로 527 (중곡동, 거산빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQyNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "광진백화점약국",
    "Address": "서울특별시 광진구 자양로 43 1층 3호 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "아차산하이약국",
    "Address": "서울특별시 광진구 자양로 287 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "미래약국",
    "Address": "서울특별시 광진구 군자로 85 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQwMyQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "완미약국",
    "Address": "서울특별시 광진구 자양로 194 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ3OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 광진구 자양로 95 (자양동, 도광빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "종합약국",
    "Address": "서울특별시 광진구 긴고랑로 106 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "광제사약국",
    "Address": "서울특별시 광진구 면목로 130 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ3OSQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "신성모약국",
    "Address": "서울특별시 광진구 뚝섬로24길 3 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ2MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "군자백화점약국",
    "Address": "서울특별시 광진구 천호대로 574 (능동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "포도원온누리약국",
    "Address": "서울특별시 광진구 능동로 265 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ4OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "선약국",
    "Address": "서울특별시 광진구 용마산로 8 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ4OSQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "센터온누리약국",
    "Address": "서울특별시 광진구 능동로 420 (중곡동, 성문빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ5OSQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜백악관약국",
    "Address": "서울특별시 광진구 용마산로 4 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "구의온누리약국",
    "Address": "서울특별시 광진구 자양로 285 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "천사약국",
    "Address": "서울특별시 광진구 능동로 409 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ4MiQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "그랜드약국",
    "Address": "서울특별시 광진구 아차산로29길 55 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQyIyQxIyQwMCQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 광진구 용마산로 23 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "레몬약국",
    "Address": "서울특별시 광진구 아차산로 478 4층 (구의동, 그레이스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQzIyQ4MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 광진구 자양로 294-1 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQxMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 광진구 자양로 48 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQyIyQ3IyQwMCQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "성원약국",
    "Address": "서울특별시 광진구 광나루로37길 8 1층 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "예일약국",
    "Address": "서울특별시 광진구 구의로 23 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "미소온누리약국",
    "Address": "서울특별시 광진구 아차산로 373 원이빌딩 1층 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ5MiQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "온누리건강약국",
    "Address": "서울특별시 광진구 뚝섬로56길 46 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ3OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "진주약국",
    "Address": "서울특별시 광진구 자양로15길 9 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "햇님약국",
    "Address": "서울특별시 광진구 천호대로111길 19 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ2MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "치료의빛예은약국",
    "Address": "서울특별시 광진구 동일로 74 1층 102호 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "세종약국",
    "Address": "서울특별시 광진구 능동로 209 세종대학교 대양 AI센터 1층 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ1IyQ3OSQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "세명약국",
    "Address": "서울특별시 광진구 천호대로 575 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQxMyQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "웰빙서울온누리약국",
    "Address": "서울특별시 광진구 뚝섬로 499 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ4OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "신세계약국",
    "Address": "서울특별시 광진구 뚝섬로 511 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "중곡종로약국",
    "Address": "서울특별시 광진구 용마산로 46 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQ5OSQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "착한약국",
    "Address": "서울특별시 광진구 자양로 43 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "디딤온누리약국",
    "Address": "서울특별시 광진구 천호대로 653 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ3MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "나라약국",
    "Address": "서울특별시 광진구 능동로 110 스타시티 영존빌딩 지2층 B201호 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQyNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "더나은약국",
    "Address": "서울특별시 광진구 천호대로 570 1층 101호 (능동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "치료의빛선약국",
    "Address": "서울특별시 광진구 아차산로 484 1층 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4OSQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "명성약국",
    "Address": "서울특별시 광진구 광나루로 538 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ2MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "정문대학약국",
    "Address": "서울특별시 광진구 능동로 110 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "해정약국",
    "Address": "서울특별시 광진구 군자로 93 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3MiQzNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 광진구 자양로 113 4층 401-1호 (자양동, 구의 현대 하이엘)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ4MiQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 광진구 뚝섬로 596 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 광진구 뚝섬로 503 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ2MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "누리온누리약국",
    "Address": "서울특별시 광진구 자양로15길 18 1층 (자양동, 혜성빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQxMyQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "한길약국",
    "Address": "서울특별시 광진구 동일로 262 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "건대가온약국",
    "Address": "서울특별시 광진구 광나루로 410 105호 (화양동, KCC파크타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ4OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "금와약국",
    "Address": "서울특별시 광진구 뚝섬로 585 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ2MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "조은우리약국",
    "Address": "서울특별시 광진구 자양로 109 104호 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "워커힐약국",
    "Address": "서울특별시 광진구 워커힐로 177 워커힐호텔 컨벤션동 지하1층 (광장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ5MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "기호약국",
    "Address": "서울특별시 광진구 군자로 25 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ4MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "메디파워약국",
    "Address": "서울특별시 광진구 뚝섬로 552 (자양동, 삼희빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQ4OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "중곡메디칼약국",
    "Address": "서울특별시 광진구 용마산로 45 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 광진구 동일로60길 14 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "새수정온누리약국",
    "Address": "서울특별시 광진구 용마산로 5 명클리닉 1층 101호 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQzNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "화양종로약국",
    "Address": "서울특별시 광진구 군자로 73 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQwMyQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "연진약국",
    "Address": "서울특별시 광진구 아차산로29길 12 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ4OSQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "진명약국",
    "Address": "서울특별시 광진구 군자로 144 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "광해약국",
    "Address": "서울특별시 광진구 능동로 298 (능동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQyIyQxIyQwMCQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "용마약국",
    "Address": "서울특별시 광진구 자양로 201 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ2MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "제중약국",
    "Address": "서울특별시 광진구 면목로 169 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ3MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "성진약국",
    "Address": "서울특별시 광진구 면목로 203 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 광진구 영화사로 30 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "온누리선명약국",
    "Address": "서울특별시 광진구 용마산로 58 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQwMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "금성당약국",
    "Address": "서울특별시 광진구 긴고랑로 115 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "보은약국",
    "Address": "서울특별시 광진구 영화사로 64-1 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQyIyQ1IyQwMCQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "성동약국",
    "Address": "서울특별시 광진구 자양번영로 11 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "건강한약국",
    "Address": "서울특별시 광진구 천호대로 655 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "세영약국",
    "Address": "서울특별시 광진구 뚝섬로27길 65 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "뉴우리약국",
    "Address": "서울특별시 광진구 아차산로 237 삼진빌딩 5층 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQyIyQ1IyQwMCQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "군자세계로약국",
    "Address": "서울특별시 광진구 천호대로 548 (군자동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ4MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "소라약국",
    "Address": "서울특별시 광진구 면목로 117 1층 102호 (중곡동, 바론채)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQyIyQ1IyQwMCQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "더샾스타시티약국",
    "Address": "서울특별시 광진구 아차산로 272 (자양동, 스타시티쇼핑몰)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQwMyQyNjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "백향목약국",
    "Address": "서울특별시 광진구 광나루로56길 34 구의동현대2단지 종합상가 1층 112호 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "이층약국",
    "Address": "서울특별시 광진구 능동로 18 205호 (자양동, 자양동 이튼타워리버3차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ3OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "스타온누리약국",
    "Address": "서울특별시 광진구 동일로 178 광진캠퍼스시티 1층 104호 (화양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQwMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "애플약국",
    "Address": "서울특별시 광진구 아차산로 244 1층 나-1호 일부 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "무지개약국",
    "Address": "서울특별시 광진구 뚝섬로 498-1 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4MiQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "새서울약국",
    "Address": "서울특별시 광진구 자양로 288 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "새한빛약국",
    "Address": "서울특별시 광진구 뚝섬로 558 (자양동, 대양빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQxMyQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "신승보약국",
    "Address": "서울특별시 광진구 뚝섬로24길 11 1층 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ5MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "군자종로약국",
    "Address": "서울특별시 광진구 천호대로 561 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQxMyQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 광진구 용마산로 53 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4OSQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "해동온누리약국",
    "Address": "서울특별시 광진구 용마산로 57 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQxMyQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "강변그랜드약국",
    "Address": "서울특별시 광진구 광나루로56길 63 123호,135호,136호 (구의동, 프라임프라자상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQxMyQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "뉴메디칼약국",
    "Address": "서울특별시 광진구 뚝섬로 496 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQxMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "중부고속약국",
    "Address": "서울특별시 광진구 강변역로 50 (구의동, 동서울터미널빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ3MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "명약국",
    "Address": "서울특별시 광진구 아차산로 532 101호 (광장동, 진넥스빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "성안약국",
    "Address": "서울특별시 광진구 자양로 311-1 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "온누리메디칼약국",
    "Address": "서울특별시 광진구 아차산로 220 (자양동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "군자한마음약국",
    "Address": "서울특별시 광진구 천호대로 557 풍국빌딩 1층 (중곡동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ3MiQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 광진구 광나루로 542 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQyIyQ3IyQwMCQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "초원약국",
    "Address": "서울특별시 광진구 강변역로4길 10 (구의동, 강변역지너스타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "한솔약국",
    "Address": "서울특별시 광진구 아차산로 621 1층 (광장동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ5OSQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "정약국",
    "Address": "서울특별시 광진구 자양로26길 8 (구의동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQwMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "오수약국",
    "Address": "서울특별시 강북구 도봉로53길 32 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ4OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "다나약국",
    "Address": "서울특별시 강북구 덕릉로 75 석우빌딩 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQyIyQ5IyQwMCQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "새봄약국",
    "Address": "서울특별시 강북구 노해로 87 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "누가약국",
    "Address": "서울특별시 강북구 솔샘로 254 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzExIyQxIyQzIyQ2MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "늘푸른평강약국",
    "Address": "서울특별시 강북구 한천로 1043 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "라라온누리약국",
    "Address": "서울특별시 강북구 도봉로 295 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQwMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "강북메디칼약국",
    "Address": "서울특별시 강북구 도봉로 190 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "송천약국",
    "Address": "서울특별시 강북구 솔샘로 291-1 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ4OSQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "혜민약국",
    "Address": "서울특별시 강북구 솔샘로67길 118 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQyIyQ3IyQwMCQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "사랑온누리약국",
    "Address": "서울특별시 강북구 도봉로 40 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzQxIyQxIyQ3IyQ2MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "고전약국",
    "Address": "서울특별시 강북구 도봉로 167 2층 (미아동, 아름빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQxMyQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "행복가득약국",
    "Address": "서울특별시 강북구 노해로 81 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "단골약국",
    "Address": "서울특별시 강북구 삼양로27길 35-21 미아프라자 1층 105호 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQwMyQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "우리대한약국",
    "Address": "서울특별시 강북구 도봉로81길 3 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ3MiQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "그린팜약국",
    "Address": "서울특별시 강북구 도봉로 329 5층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "화신약국",
    "Address": "서울특별시 강북구 삼양로 424 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ2MiQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "임온누리약국",
    "Address": "서울특별시 강북구 오현로34길 12 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "솔샘약국",
    "Address": "서울특별시 강북구 솔샘로 295-1 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ4OSQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "우림약국",
    "Address": "서울특별시 강북구 삼양로 466 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ2MiQ0NjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "승약국",
    "Address": "서울특별시 강북구 솔매로 38 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ2MiQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "노약국",
    "Address": "서울특별시 강북구 도봉로 174 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "건강비타민약국",
    "Address": "서울특별시 강북구 솔매로 59 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "세계로약국",
    "Address": "서울특별시 강북구 도봉로 253 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ3OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "이층약국",
    "Address": "서울특별시 강북구 도봉로 53 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQ5OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 강북구 도봉로 34 (미아동, 트레지오상가 1층)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ5MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "옵티마네오프라자약국",
    "Address": "서울특별시 강북구 도봉로 352 102호 (번동, 효성네오인텔리안)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "친절한약국",
    "Address": "서울특별시 강북구 도봉로 325 4층 (수유동, 수성타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQxMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "운산약국",
    "Address": "서울특별시 강북구 도봉로 260 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "수유대학약국",
    "Address": "서울특별시 강북구 삼양로 431-1 (수유동, 수유대학약국)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ3MiQyNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "동양당한약국",
    "Address": "서울특별시 강북구 노해로17길 21 1층 8호 (수유동, 수유중앙시장)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ5OSQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "우리들약국",
    "Address": "서울특별시 강북구 오현로 190 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ4MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "햇살약국",
    "Address": "서울특별시 강북구 한천로 1038 천지빌딩,유료주차장 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ4OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 강북구 덕릉로40길 79 대명빌딩 1층 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ2MiQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "수종로약국",
    "Address": "서울특별시 강북구 도봉로 61 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ2MiQ0NjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "SK온누리약국",
    "Address": "서울특별시 강북구 솔샘로 184 에스케이북한산시티 112~113호(미아동) (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzQxIyQxIyQ3IyQxMyQyNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "번동약국",
    "Address": "서울특별시 강북구 오현로32길 4-3 1층 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQxIyQwMyQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "선영약국",
    "Address": "서울특별시 강북구 노해로23길 73 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQxIyQwMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "엔젤팜약국",
    "Address": "서울특별시 강북구 삼양로19길 59 대선빌딩 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzMxIyQxIyQ3IyQ4OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "삼양약국",
    "Address": "서울특별시 강북구 솔매로 80 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQxIyQ3IyQ5MiQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "상아약국",
    "Address": "서울특별시 강북구 도봉로 143 광명빌딩 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ4MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "어약국",
    "Address": "서울특별시 강북구 삼각산로 132 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ3OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "북부약국",
    "Address": "서울특별시 강북구 도봉로 150 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "요나약국",
    "Address": "서울특별시 강북구 솔샘로 254 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "영약국",
    "Address": "서울특별시 강북구 한천로170길 5 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQyIyQxIyQwMCQyNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "대명약국",
    "Address": "서울특별시 강북구 삼양로 429 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ4MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "수유태평양약국",
    "Address": "서울특별시 강북구 도봉로67길 34 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzMxIyQxIyQ3IyQxMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "수온누리약국",
    "Address": "서울특별시 강북구 삼양로19길 25 107동 2호 (미아동, 삼성래미안트리베라1차아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "미양온누리약국",
    "Address": "서울특별시 강북구 솔샘로 229-1 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ5MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "직영약국",
    "Address": "서울특별시 강북구 도봉로67길 13 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "청백약국",
    "Address": "서울특별시 강북구 삼양로 623 1층 (우이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQwMyQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "엄마약국",
    "Address": "서울특별시 강북구 도봉로14길 7-8 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "수유대한약국",
    "Address": "서울특별시 강북구 도봉로81길 12 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "선경약국",
    "Address": "서울특별시 강북구 도봉로77길 9 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQ5IyQ3OSQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "새한약국",
    "Address": "서울특별시 강북구 도봉로 67 새한빌딩 1층 102호 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ5IyQwMCQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "화원약국",
    "Address": "서울특별시 강북구 삼양로 469 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ5MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "중앙약국",
    "Address": "서울특별시 강북구 오현로 191 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ5MiQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "올리브약국",
    "Address": "서울특별시 강북구 노해로 76 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQwMyQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "온누리대성약국",
    "Address": "서울특별시 강북구 수유로 9 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzIxIyQxIyQ1IyQ3OSQzNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "참바로약국",
    "Address": "서울특별시 강북구 한천로105길 7 207호 (번동, 주공아파트1단지상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQ2MiQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "푸른약국",
    "Address": "서울특별시 강북구 삼양로 309 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQwMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "동북약국",
    "Address": "서울특별시 강북구 솔샘로 233 305호 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ2MiQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "다나을약국",
    "Address": "서울특별시 강북구 도봉로 333 6층 (수유동, 정우빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQyIyQxIyQwMCQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "솔밭약국",
    "Address": "서울특별시 강북구 삼양로 579 화성빌딩 1층 (우이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "수유온누리약국",
    "Address": "서울특별시 강북구 도봉로 324 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "연주약국",
    "Address": "서울특별시 강북구 한천로105길 7 1층 101호 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQxMyQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "오렌지약국",
    "Address": "서울특별시 강북구 솔샘로 184 SK아파트주상가 115~116호(미아동) (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQxMyQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "뉴타운약국",
    "Address": "서울특별시 강북구 삼양로27길 43 2층 201,202호 (미아동, 위브 테라스 파크)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "강북우리약국",
    "Address": "서울특별시 강북구 한천로 1081 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzIxIyQxIyQ1IyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "하나약국",
    "Address": "서울특별시 강북구 삼양로 613 우암빌딩 1층 (우이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ3MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "민들레약국",
    "Address": "서울특별시 강북구 솔샘로 254 2층 2호 (미아동, 삼양아케이트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQ1IyQ4MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "조아약국",
    "Address": "서울특별시 강북구 도봉로13길 13 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQ3IyQ4MiQzNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "밝은온누리약국",
    "Address": "서울특별시 강북구 삼양로 191 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ3OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "바이엘약국",
    "Address": "서울특별시 강북구 삼양로 420 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQyIyQzIyQwMCQyNjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "솔약국",
    "Address": "서울특별시 강북구 솔샘로 167 지하층 312호 (미아동, 상가동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQxMyQzNjE4MzIjNjEjJDEjJDgjJDgz",
    "Name": "삼우약국",
    "Address": "서울특별시 강북구 삼양로 581 (우이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQzNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "호림프라자약국",
    "Address": "서울특별시 강북구 덕릉로 17 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQwMyQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "꿈이있는 온누리약국",
    "Address": "서울특별시 강북구 삼양로 462 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ3MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "메디팜미소약국",
    "Address": "서울특별시 강북구 도봉로 34 1층 (미아동, 트레지오빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQyIyQ3IyQwMCQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "동아약국",
    "Address": "서울특별시 강북구 도봉로 118 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ2MiQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "매일약국",
    "Address": "서울특별시 강북구 도봉로 389 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQwMyQyNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "은행나무약국",
    "Address": "서울특별시 강북구 삼양로 161 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQxMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "우정약국",
    "Address": "서울특별시 강북구 삼양로77길 25 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQwMyQ0NjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "수유동약국",
    "Address": "서울특별시 강북구 수유로 83 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3MiQyNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "백십자약국",
    "Address": "서울특별시 강북구 인수봉로 192 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQxMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "길약국",
    "Address": "서울특별시 강북구 도봉로67길 21 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzIxIyQxIyQxIyQ4OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "에버그린약국",
    "Address": "서울특별시 강북구 한천로 1000 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQwMyQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "소원약국",
    "Address": "서울특별시 강북구 도봉로 205 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ5OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "바우약국",
    "Address": "서울특별시 강북구 삼양로 509 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQxMyQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 강북구 도봉로67길 18 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ4MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "세일약국",
    "Address": "서울특별시 강북구 도봉로71길 34 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQyIyQ1IyQwMCQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "밀알약국",
    "Address": "서울특별시 강북구 덕릉로 79 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ5OSQ0NjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "바른약국",
    "Address": "서울특별시 강북구 노해로 95-1 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQzIyQwMyQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "수유상록수약국",
    "Address": "서울특별시 강북구 도봉로 328 301호 (번동, 가든타워빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQ4OSQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 강북구 도봉로 317 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ5MiQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "삼일약국",
    "Address": "서울특별시 강북구 삼양로 241 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQxIyQ4OSQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "삼화온누리약국",
    "Address": "서울특별시 강북구 도봉로 196 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQxMyQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "제일약국",
    "Address": "서울특별시 강북구 도봉로 376 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ4OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "타워온누리약국",
    "Address": "서울특별시 강북구 도봉로 358 2층 201호 (번동, 코스타타워)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ5MiQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "열린대학약국",
    "Address": "서울특별시 강북구 숭인로 63-1 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQyIyQzIyQwMCQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 강북구 도봉로 213 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "종로태평양약국",
    "Address": "서울특별시 강북구 오패산로 130 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ4MiQyNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "필약국",
    "Address": "서울특별시 강북구 오현로 193 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ3MiQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "인수약국",
    "Address": "서울특별시 강북구 삼각산로 71 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQxIyQ3MiQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "번동종로약국",
    "Address": "서울특별시 강북구 오현로34길 23-4 104호 (번동, 현대하니타운)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzUxIyQxIyQ1IyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "메디팜한마음약국",
    "Address": "서울특별시 강북구 오현로32길 3 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQxMyQzNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "대우약국",
    "Address": "서울특별시 강북구 삼양로 348 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ4OSQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "윤약국",
    "Address": "서울특별시 강북구 한천로 1071 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ2MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "이원약국",
    "Address": "서울특별시 강북구 삼양로 244 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ2MiQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "새현대약국",
    "Address": "서울특별시 강북구 인수봉로55길 13 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "생수당약국",
    "Address": "서울특별시 강북구 오패산로52길 51 지층 1호 (미아동, 화랑빌라)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ2MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "행복이가득한수약국",
    "Address": "서울특별시 강북구 도봉로 245 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQ3IyQ2MiQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "서울진약국",
    "Address": "서울특별시 강북구 삼양로 319 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ1IyQ5OSQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "하은약국",
    "Address": "서울특별시 강북구 노해로 118 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQxIyQxIyQ5OSQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "미아팜약국",
    "Address": "서울특별시 강북구 도봉로 65 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "수유프라자약국",
    "Address": "서울특별시 강북구 덕릉로 42 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "바로나한약국",
    "Address": "서울특별시 강북구 삼각산로 140 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ3OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "백화점약국",
    "Address": "서울특별시 강북구 도봉로96길 11 1층 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzExIyQxIyQzIyQ5MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "보건약국",
    "Address": "서울특별시 강북구 오현로31길 147 201호 (번동, 주공5단지복합상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQxIyQwMCQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "숭인약국",
    "Address": "서울특별시 강북구 도봉로 59 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzQxIyQxIyQ3IyQ3MiQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "녹십자약국",
    "Address": "서울특별시 강북구 도봉로 255 1층 (수유동, 나라빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzQxIyQxIyQ3IyQ5MiQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "수유파랑새약국",
    "Address": "서울특별시 강북구 삼양로123길 6-8 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQwMyQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 강북구 한천로 1088 1층 (수유동, 현진빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "가족사랑약국",
    "Address": "서울특별시 강북구 오패산로52길 39 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3MiQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "다정약국",
    "Address": "서울특별시 강북구 월계로 19 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQ2MiQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "복지약국",
    "Address": "서울특별시 강북구 한천로115길 15 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQwMyQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "드림약국",
    "Address": "서울특별시 강북구 덕릉로 136 2층 (번동, 삼양빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQxIyQzIyQ4OSQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "재원약국",
    "Address": "서울특별시 강북구 오패산로30길 30 상가동 1층 120호 (미아동, 경남아너스빌)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ3OSQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "솔샘우리약국",
    "Address": "서울특별시 강북구 솔샘로 203 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQ5MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "송일약국",
    "Address": "서울특별시 강북구 도봉로18길 46 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQyIyQ1IyQwMCQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "강북김약국",
    "Address": "서울특별시 강북구 도봉로49길 8 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQxMyQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "미아역온누리약국",
    "Address": "서울특별시 강북구 도봉로 217 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQwMyQzNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "7번약국",
    "Address": "서울특별시 강북구 도봉로 339 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ2MiQzNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "대동약국",
    "Address": "서울특별시 강북구 삼양로 207 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ5MiQyNjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "민정약국",
    "Address": "서울특별시 강북구 오패산로30길 41 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ2MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "신통일약국",
    "Address": "서울특별시 강북구 한천로123길 14 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ2MiQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "한양약국",
    "Address": "서울특별시 강북구 삼양로87길 35 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "수유참사랑약국",
    "Address": "서울특별시 강북구 삼양로 497 1층 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3MiQ0NjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "지영약국",
    "Address": "서울특별시 강북구 삼양로 423 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQyIyQ1IyQwMCQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "고려약국",
    "Address": "서울특별시 강북구 삼양로 337 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ4MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "송도약국",
    "Address": "서울특별시 강북구 도봉로 343 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ2MiQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "번동프라자약국",
    "Address": "서울특별시 강북구 한천로 940 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQ1IyQ3OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "세화온누리약국",
    "Address": "서울특별시 강북구 도봉로77길 6 1층 101,102호 (수유동, 수유동 이테크밸리 오피스텔)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ2MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "부부약국",
    "Address": "서울특별시 강북구 오패산로 112 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "강북제일약국",
    "Address": "서울특별시 강북구 도봉로37길 7 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "한독약국",
    "Address": "서울특별시 강북구 수유로23길 57 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ4MiQzNjE4MzIjNjEjJDEjJDAjJDgz",
    "Name": "정수약국",
    "Address": "서울특별시 강북구 솔샘로 239 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQwMyQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "진약국",
    "Address": "서울특별시 강북구 한천로 1148 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQxMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "삼천약국",
    "Address": "서울특별시 강북구 삼양로 293 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3MiQzNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "새서울약국",
    "Address": "서울특별시 강북구 삼양로 184 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ4OSQzNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "한사랑온누리약국",
    "Address": "서울특별시 강북구 인수봉로 142 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzUxIyQxIyQ1IyQ5MiQyNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "청구약국",
    "Address": "서울특별시 강북구 삼양로 255 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQ5MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "한빛약국",
    "Address": "서울특별시 강북구 도봉로 52 7층 (미아동, 연이빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzMxIyQxIyQ3IyQxMyQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "대지약국",
    "Address": "서울특별시 강북구 삼양로 247 3층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ5MiQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "사랑약국",
    "Address": "서울특별시 강북구 도봉로 186 1층 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzIxIyQxIyQ5IyQ2MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "늘푸른약국",
    "Address": "서울특별시 강북구 월계로7나길 9 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQwMyQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "웰빙메디칼약국",
    "Address": "서울특별시 강북구 도봉로 187 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQzIyQ5MiQ0NjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "참사랑약국",
    "Address": "서울특별시 강북구 도봉로 197 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ2MiQzNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "시대약국",
    "Address": "서울특별시 강북구 솔샘로 227 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQ3IyQwMyQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "정해약국",
    "Address": "서울특별시 강북구 삼양로 516 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQ3MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "시원약국",
    "Address": "서울특별시 강북구 오패산로 413 1층 (번동, 미니스톱)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzQxIyQxIyQ3IyQ3OSQ0NjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "강북다모아약국",
    "Address": "서울특별시 강북구 도봉로 79 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ1IyQ5MiQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "만남온누리약국",
    "Address": "서울특별시 강북구 삼양로 675 (우이동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ4MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "대창약국",
    "Address": "서울특별시 강북구 월계로 53 (미아동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQwMyQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "안국온누리약국",
    "Address": "서울특별시 강북구 한천로 1058 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ5OSQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "삼성약국",
    "Address": "서울특별시 강북구 한천로 1120 (수유동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ3MiQzNjE0ODEjNTEjJDEjJDIjJDgz",
    "Name": "새암온누리약국",
    "Address": "서울특별시 강북구 도봉로 308 1층 (번동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQxIyQ5MiQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "예닮약국",
    "Address": "서울특별시 금천구 시흥대로 403 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzUxIyQxIyQxIyQ3OSQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "늘사랑온누리약국",
    "Address": "서울특별시 금천구 금하로 816 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ2MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "미래팜약국",
    "Address": "서울특별시 금천구 독산로 290 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQwMyQyNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "천수온누리약국",
    "Address": "서울특별시 금천구 가산로 111 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQxMyQzNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "문성당약국",
    "Address": "서울특별시 금천구 독산로64길 39 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQzIyQxMyQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "늘푸른건강약국",
    "Address": "서울특별시 금천구 범안로 1183 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQ1IyQwMyQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "새우리약국",
    "Address": "서울특별시 금천구 디지털로 200 우리은행 가산IT타워 3층 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQyNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "라임약국",
    "Address": "서울특별시 금천구 디지털로9길 56 코오롱테크노밸리 109호 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3MiQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "도영약국",
    "Address": "서울특별시 금천구 독산로50길 90 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "굿모닝약국",
    "Address": "서울특별시 금천구 독산로 366 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQyIyQ3IyQwMCQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "시민약국",
    "Address": "서울특별시 금천구 독산로 139 1층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQ1IyQ3MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "성가약국",
    "Address": "서울특별시 금천구 독산로106길 32 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ4MiQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "한중약국",
    "Address": "서울특별시 금천구 독산로 136 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "건강플러스약국",
    "Address": "서울특별시 금천구 시흥대로 391 3층 (독산동, 홈플러스금천점)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQxIyQ4OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "현대온누리약국",
    "Address": "서울특별시 금천구 독산로 142 (시흥동, 덕산빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQ5MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "천세약국",
    "Address": "서울특별시 금천구 시흥대로 274 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4OSQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "고원약국",
    "Address": "서울특별시 금천구 시흥대로153길 68 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzExIyQxIyQ3IyQ4OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "강남약국",
    "Address": "서울특별시 금천구 남부순환로 1372 (독산동, 현경빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ5IyQ5OSQyNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "온누리건강약국",
    "Address": "서울특별시 금천구 시흥대로 232 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ4OSQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "금약국",
    "Address": "서울특별시 금천구 독산로 174 1층 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQxIyQ5OSQyNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "전진상약국",
    "Address": "서울특별시 금천구 탑골로3가길 22 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQzNjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "가산소중한약국",
    "Address": "서울특별시 금천구 디지털로9길 68 대륭포스트타워 5차 1층 106호 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ3MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "성문약국",
    "Address": "서울특별시 금천구 한내로 69-15 1317-107호 (독산동, 주공아파트)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQ3IyQ5MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "정암산약국",
    "Address": "서울특별시 금천구 시흥대로 192 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzExIyQxIyQzIyQ2MiQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "유아약국",
    "Address": "서울특별시 금천구 시흥대로104길 14 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQ3OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "하얀약국",
    "Address": "서울특별시 금천구 남부순환로 1290 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "광장온누리약국",
    "Address": "서울특별시 금천구 금하로 710 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQyIyQ3IyQwMCQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "정명약국",
    "Address": "서울특별시 금천구 시흥대로 399 410호 (독산동, 시티렉스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4OSQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "메디팜대안약국",
    "Address": "서울특별시 금천구 시흥대로 352 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "무림약국",
    "Address": "서울특별시 금천구 시흥대로 406 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQ3IyQ3MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "박애약국",
    "Address": "서울특별시 금천구 시흥대로141길 66 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "독산메디칼약국",
    "Address": "서울특별시 금천구 독산로 210 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQwMyQzNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "정진약국",
    "Address": "서울특별시 금천구 독산로64길 19 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ2MiQ0NjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "신보생약국",
    "Address": "서울특별시 금천구 시흥대로148길 37 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQyIyQ5IyQwMCQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "대지약국",
    "Address": "서울특별시 금천구 독산로 252 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzExIyQxIyQzIyQ5MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "건강한약국",
    "Address": "서울특별시 금천구 남부순환로 1384 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "대우당약국",
    "Address": "서울특별시 금천구 은행나무로 34 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ5MiQzNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "세종약국",
    "Address": "서울특별시 금천구 독산로 199 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ3MiQyNjE0ODEjNDEjJDEjJDQjJDgz",
    "Name": "명약국",
    "Address": "서울특별시 금천구 시흥대로 473 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3OSQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "태평양약국",
    "Address": "서울특별시 금천구 금하로25길 1 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ3MiQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "하이온누리약국",
    "Address": "서울특별시 금천구 가산디지털1로 145 에이스하이엔드타워3차 105호 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQ4MiQyNjEwMDIjNTEjJDEjJDYjJDgz",
    "Name": "우리캐슬약국",
    "Address": "서울특별시 금천구 시흥대로 291 (독산동, 금천롯데캐슬골드파크3차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ4OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "그린약국",
    "Address": "서울특별시 금천구 독산로93길 11 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzExIyQxIyQzIyQxMyQyNjEyMjIjNjEjJDEjJDgjJDgz",
    "Name": "현대약국",
    "Address": "서울특별시 금천구 두산로 70 T-113호 (독산동, 현대지식산업센터)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQ3IyQ3MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "가산약국",
    "Address": "서울특별시 금천구 가산로 116 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQxIyQ4MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "프라자약국",
    "Address": "서울특별시 금천구 가산디지털1로 168 A/115호 (가산동, 우림라이온스밸리)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ4MiQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "조은약국",
    "Address": "서울특별시 금천구 시흥대로 421 1층 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzQxIyQxIyQ3IyQ4MiQyNjEwMDIjODEjJDEjJDYjJDgz",
    "Name": "녹십자약국",
    "Address": "서울특별시 금천구 시흥대로 96 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "한울약국",
    "Address": "서울특별시 금천구 독산로 133 1층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ3MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "가디온누리약국",
    "Address": "서울특별시 금천구 가산디지털1로 171 가산 에스케이 브이원 센터 1층 117호 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQ3IyQ5MiQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "봄빛약국",
    "Address": "서울특별시 금천구 가산디지털1로 171 가산 에스케이 브이원 센터 2층 202-1호 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQ1IyQwMCQzNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "비타민약국",
    "Address": "서울특별시 금천구 독산로50길 84 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQyIyQ1IyQwMCQ0NjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "참약국",
    "Address": "서울특별시 금천구 남부순환로 1390 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "별장약국",
    "Address": "서울특별시 금천구 금하로24길 40 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzMxIyQxIyQzIyQ5OSQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "윤경약국",
    "Address": "서울특별시 금천구 남부순환로 1426 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3OSQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "한마음약국",
    "Address": "서울특별시 금천구 독산로6가길 22 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ3MiQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "삼화약국",
    "Address": "서울특별시 금천구 은행나무로 12-1 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzMxIyQxIyQzIyQxMyQyNjE0ODEjNzEjJDEjJDgjJDgz",
    "Name": "동행약국",
    "Address": "서울특별시 금천구 시흥대로 291 2층 280호 (독산동, 금천롯데캐슬골드파크3차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxMzUxIzExIyQxIyQzIyQ3OSQzNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "장수약국",
    "Address": "서울특별시 금천구 시흥대로 153 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQ1IyQ5MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "독산종로약국",
    "Address": "서울특별시 금천구 독산로 360 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzQxIyQyIyQ3IyQwMCQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "비즈메드약국",
    "Address": "서울특별시 금천구 시흥대로 214 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzIxIyQxIyQ1IyQ5MiQyNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "한사랑약국",
    "Address": "서울특별시 금천구 시흥대로63길 64 1층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ4MiQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "레아약국",
    "Address": "서울특별시 금천구 가산디지털1로 131 117-1호 (가산동, BYC하이시티)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ5MiQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "토마스약국",
    "Address": "서울특별시 금천구 시흥대로112길 6 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3OSQyNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "다보약국",
    "Address": "서울특별시 금천구 시흥대로26길 9 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ5OSQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "수도약국",
    "Address": "서울특별시 금천구 가산로3길 93 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ5MiQ0NjEwMDIjNjEjJDEjJDgjJDgz",
    "Name": "명보약국",
    "Address": "서울특별시 금천구 시흥대로 92 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMzUxIzMxIyQxIyQ3IyQ3OSQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "벽산프라자약국",
    "Address": "서울특별시 금천구 금하로 763 213,214호 (시흥동, 벽산중심상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxMTkxIzMxIyQxIyQ3IyQxMyQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "아이사랑약국",
    "Address": "서울특별시 금천구 시흥대로 214 401호 (시흥동, 비즈메드빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzIxIyQxIyQ5IyQ3OSQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "현약국",
    "Address": "서울특별시 금천구 가산디지털1로 149 1층 103호 (가산동, 신한이노플렉스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzExIyQyIyQ3IyQwMCQ0NjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "대제일약국",
    "Address": "서울특별시 금천구 독산로85길 13 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ3OSQzNjEyMjIjNTEjJDEjJDIjJDgz",
    "Name": "중앙메디칼약국",
    "Address": "서울특별시 금천구 가산디지털1로 186 109-1호 (가산동, JEI플라츠)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzMxIyQxIyQzIyQxMyQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "하늘약국",
    "Address": "서울특별시 금천구 금하로 720 306호 (시흥동, 에벤에셀프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "새연세약국",
    "Address": "서울특별시 금천구 독산로 87 1층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ4MiQ0NjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "경일약국",
    "Address": "서울특별시 금천구 시흥대로72길 32 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzUxIyQxIyQxIyQ3MiQzNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "나래약국",
    "Address": "서울특별시 금천구 독산로 137 (시흥동, 시흥음악학원)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzIxIyQxIyQ5IyQ2MiQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "녹수프라자약국",
    "Address": "서울특별시 금천구 독산로 213 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzExIyQxIyQzIyQ2MiQ0NjEwMDIjNjEjJDEjJDQjJDgz",
    "Name": "진한약국",
    "Address": "서울특별시 금천구 벚꽃로38길 5 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzQxIyQyIyQ3IyQwMCQzNjE4MzIjODEjJDEjJDIjJDgz",
    "Name": "중앙사약국",
    "Address": "서울특별시 금천구 시흥대로 202 (시흥동, 대의빌딩)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzIxIyQxIyQ1IyQ4MiQyNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "동아온누리약국",
    "Address": "서울특별시 금천구 시흥대로 371 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxOTYxIzUxIyQxIyQxIyQ4MiQzNjEwMDIjODEjJDEjJDIjJDgz",
    "Name": "시흥프라자약국",
    "Address": "서울특별시 금천구 독산로 135-1 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzIxIyQyIyQ1IyQwMCQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "봄약국",
    "Address": "서울특별시 금천구 가산디지털1로 1 더루벤스밸리 208-1호 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNTgxMzUxIzUxIyQxIyQ1IyQ5OSQyNjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "대명약국",
    "Address": "서울특별시 금천구 벚꽃로 298 104호 (가산동, 대륭포스트타워6차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQ0NjEwMDIjNDEjJDEjJDQjJDgz",
    "Name": "대인당온누리약국",
    "Address": "서울특별시 금천구 시흥대로 237 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzExIyQyIyQzIyQwMCQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "백산온누리약국",
    "Address": "서울특별시 금천구 금하로 763 313,314호 (시흥동, 벽산중심상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4MiQyNjE4MzIjNDEjJDEjJDQjJDgz",
    "Name": "형제약국",
    "Address": "서울특별시 금천구 금하로 707 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQzNjEyMjIjODEjJDEjJDIjJDgz",
    "Name": "수약국",
    "Address": "서울특별시 금천구 시흥대로 201 삼성홈플러스 지하1층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxNzAyIzExIyQxIyQzIyQ5OSQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "다원약국",
    "Address": "서울특별시 금천구 독산로93길 41 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQ5IyQ3OSQzNjEyMjIjODEjJDEjJDYjJDgz",
    "Name": "가람약국",
    "Address": "서울특별시 금천구 가산디지털1로 5 대륭테크노타운 20차 107호 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ5OSQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "명수약국",
    "Address": "서울특별시 금천구 시흥대로138길 13 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQxIyQ1IyQ4OSQzNjEyMjIjNDEjJDEjJDgjJDgz",
    "Name": "대한약국",
    "Address": "서울특별시 금천구 금하로 711 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQxMyQyNjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "이화약국",
    "Address": "서울특별시 금천구 독산로85길 7 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ2MiQ0NjEwMDIjNzEjJDEjJDgjJDgz",
    "Name": "코끼리약국",
    "Address": "서울특별시 금천구 금하로 720 에벤에셀프라자 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ5OSQyNjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "남대문약국",
    "Address": "서울특별시 금천구 독산로40길 25 1층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzQxIyQxIyQ3IyQ3MiQzNjEyMjIjNDEjJDEjJDQjJDgz",
    "Name": "튼튼온누리약국",
    "Address": "서울특별시 금천구 시흥대로 291 310동 279호 (독산동, 금천롯데캐슬골드파크3차)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQ5IyQ3MiQzNjEyMjIjNTEjJDEjJDYjJDgz",
    "Name": "에벤에셀온누리약국",
    "Address": "서울특별시 금천구 금하로 720 202호 (시흥동, 에벤에셀프라자)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzUxIyQxIyQ1IyQ2MiQyNjE4MzIjODEjJDEjJDYjJDgz",
    "Name": "행복한우리약국",
    "Address": "서울특별시 금천구 금하로 717 1층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzExIyQxIyQ3IyQ4OSQyNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "한신코아약국",
    "Address": "서울특별시 금천구 한내로 62 1160호 (독산동, 한신아파트상가)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ2MiQyNjE0ODEjNjEjJDEjJDAjJDgz",
    "Name": "남문프라자약국",
    "Address": "서울특별시 금천구 시흥대로 436 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQyIyQ5IyQwMCQ0NjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "새남부약국",
    "Address": "서울특별시 금천구 남부순환로 1394 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQwMyQ0NjEwMDIjNTEjJDEjJDIjJDgz",
    "Name": "드림플러스약국",
    "Address": "서울특별시 금천구 디지털로9길 46 이앤씨드림타워7차 201-1호 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMTkxIzUxIyQxIyQxIyQxMyQyNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "마미약국",
    "Address": "서울특별시 금천구 금하로 720 에벤에셀프라자 2층 206호 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzMxIyQxIyQzIyQ3OSQ0NjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "정약국",
    "Address": "서울특별시 금천구 두산로 81 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzUxIyQyIyQxIyQwMCQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "소망약국",
    "Address": "서울특별시 금천구 독산로75길 16 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxNzAyIzIxIyQxIyQ5IyQwMyQzNjEyMjIjNjEjJDEjJDAjJDgz",
    "Name": "우리약국",
    "Address": "서울특별시 금천구 시흥대로 211 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ3OSQzNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "정운약국",
    "Address": "서울특별시 금천구 금하로 763-12 벽산중심상가 2층 210호 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkNDgxOTYxIzExIyQxIyQ3IyQ2MiQzNjE4MzIjNTEjJDEjJDYjJDgz",
    "Name": "삼층약국",
    "Address": "서울특별시 금천구 시흥대로 198 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzUxIyQxIyQxIyQwMyQyNjE4MzIjNzEjJDEjJDgjJDgz",
    "Name": "은행나무약국",
    "Address": "서울특별시 금천구 금하로 705 2층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQ1IyQ4OSQzNjE4MzIjNTEjJDEjJDIjJDgz",
    "Name": "새보은약국",
    "Address": "서울특별시 금천구 독산로 138 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMTkxIzMxIyQyIyQ3IyQwMCQzNjE4MzIjNjEjJDEjJDQjJDgz",
    "Name": "은약국",
    "Address": "서울특별시 금천구 시흥대로 224 금천리메인시티 102호 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxMzUxIzExIyQxIyQ3IyQxMyQyNjEyMjIjNjEjJDEjJDQjJDgz",
    "Name": "리더스약국",
    "Address": "서울특별시 금천구 벚꽃로 286 삼성리더스타워 1층 110-1호 (가산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxOTYxIzQxIyQxIyQ3IyQ4MiQyNjE0ODEjNDEjJDEjJDgjJDgz",
    "Name": "약나라약국",
    "Address": "서울특별시 금천구 시흥대로 104 1층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzExIyQxIyQ3IyQwMyQ0NjE0ODEjODEjJDEjJDYjJDgz",
    "Name": "은혜약국",
    "Address": "서울특별시 금천구 시흥대로 242 반석빌딩 1층 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxMzUxIzUxIyQxIyQxIyQwMyQyNjE0ODEjODEjJDEjJDIjJDgz",
    "Name": "이든약국",
    "Address": "서울특별시 금천구 서부샛길 606 125호 (가산동, 대성디폴리스)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ2MiQzNjE0ODEjNTEjJDEjJDYjJDgz",
    "Name": "삼명약국",
    "Address": "서울특별시 금천구 독산로 88 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ2MiQzNjEwMDIjNDEjJDEjJDgjJDgz",
    "Name": "세명당약국",
    "Address": "서울특별시 금천구 시흥대로58길 5 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ4MiQyNjE0ODEjNjEjJDEjJDQjJDgz",
    "Name": "고성희약국",
    "Address": "서울특별시 금천구 금하로24길 57 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzIxIyQxIyQxIyQ2MiQ0NjEwMDIjNjEjJDEjJDAjJDgz",
    "Name": "명문당약국",
    "Address": "서울특별시 금천구 시흥대로 240 (시흥동, 장안의원)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkMCMkMDMkMzgxOTYxIzMxIyQxIyQzIyQ3OSQyNjEyMjIjNzEjJDEjJDgjJDgz",
    "Name": "영광약국",
    "Address": "서울특별시 금천구 시흥대로149길 7 (독산동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkMzgxNzAyIzExIyQxIyQzIyQ4MiQyNjE4MzIjNDEjJDEjJDgjJDgz",
    "Name": "신양온누리약국",
    "Address": "서울특별시 금천구 시흥대로58길 38 (시흥동)"
  },
  {
    "ID": "JDQ4MTg4MSM1MSMkMSMkNCMkMDMkNDgxOTYxIzIxIyQxIyQxIyQ3MiQzNjE0ODEjNjEjJDEjJDgjJDgz",
    "Name": "기분좋은약국",
    "Address": "서울특별시 금천구 시흥대로139길 15 (독산동)"
  }])
#all_items = list(db.project.find({}))
#print(all_items[0])

#ID 값 0부터 부여하는 코드
#for index, item in enumerate(all_items):
#    print(index, item)
#    db.project.update_one({'ID': item['ID']}, {'$set': {'ID': str(index)}})