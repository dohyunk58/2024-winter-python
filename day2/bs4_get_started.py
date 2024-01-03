import requests
from bs4 import BeautifulSoup
# 1. 직접 입력해서 보내기
# url에 보내고자 하는 데이터를 입력해서 전송한다.
URL_get = "https://search.naver.com/search.naver?query=%EA%B9%80%EC%9E%A5%ED%9B%88"
response = requests.get(URL_get)
soup = BeautifulSoup(response.text,'html.parser') #string 집어넣기

for i in soup.select('.news_contents > a'): #css selector 사용
    print(i.text) #글 출력
    print(i['href']) #a 태그 내 href 속성 출력
