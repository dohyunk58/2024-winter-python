import requests
from bs4 import BeautifulSoup
import re

URL_get = "https://www.melon.com/chart/index.htm"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
hdr = {'User-Agent':user_agent}

response = requests.get(URL_get, headers=hdr)

print(response)

#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a # 제목
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a # 가수

soup = BeautifulSoup(response.text,'html.parser') #string 집어넣기

p = re.compile('아이.')


rank = []
title = []
singer = []

for i in soup.select('#lst50 > td:nth-child(2) > div > span.rank'): #css selector 사용
    rank.append(i.text)
for i in soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'): #css selector 사용
    title.append(i.text)
for i in soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a'): #css selector 사용
    singer.append(i.text)

for i in range(len(title)):
    print(f"{rank[i]}위 {singer[i]} - {title[i]}")

print("\'아이\'가 들어가는 가수")
for i in range(len(singer)):
    if p.search(singer[i]):
        print(f"{rank[i]}위 ", end='')
        print(p.search(singer[i]).group(), end='')
        print(f" - {title[i]}")
# print(filter_list)
# for i in singer:
    