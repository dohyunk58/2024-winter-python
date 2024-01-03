import requests

naver = requests.get('https://www.naver.com') # https://www.naver.com 요청
weather = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=37.5582018&lon=126.9979742&appid=4ada87268facd87550e6a5126401fda4&units=metric') #openweathermap api 호출
weather_json = weather.json() #response json를 파이썬 딕셔너리로 변환
print(naver.text) #text로 되어있는 페이지 소스
print('---------------------이하 weather-------------------------')
print(weather_json['current']) #딕셔너리 current 접근
