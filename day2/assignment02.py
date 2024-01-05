import requests
from bs4 import BeautifulSoup

URL_get = "https://www.melon.com/chart/index.htm"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
hdr = {'User-Agent':user_agent}

response = requests.get(URL_get, headers=hdr)

print(response)
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a # 제목
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a # 가수

soup = BeautifulSoup(response.text,'html.parser') #string 집어넣기

find_rank = int(input("찾고 싶은 순위: "))

rank = []
title = []
singer = []

for i in soup.select(f'#lst50:nth-child({find_rank}) > td:nth-child(2) > div > span.rank'): #css selector 사용
    rank.append(i.text)
for i in soup.select(f'#lst50:nth-child({find_rank}) > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'): #css selector 사용
    title.append(i.text)
for i in soup.select(f'#lst50:nth-child({find_rank}) > td:nth-child(6) > div > div > div.ellipsis.rank02 > a'): #css selector 사용
    singer.append(i.text)

for i in range(len(title)):
    print(f"{rank[i]}위 {singer[i]} - {title[i]}")