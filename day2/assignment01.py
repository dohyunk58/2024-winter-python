import requests
from bs4 import BeautifulSoup

find = input("검색어를 입력해주세요: ")
URL_get = f"https://search.naver.com/search.naver?query={find}"
response = requests.get(URL_get)
soup = BeautifulSoup(response.text,'html.parser') #string 집어넣기

for i in soup.select('.news_contents > a'): #css selector 사용
    print(i.text) #글 출력
    print(i['href']) #a 태그 내 href 속성 출력
