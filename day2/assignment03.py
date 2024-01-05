import requests
from bs4 import BeautifulSoup

URL_get = "https://finance.naver.com/sise/lastsearch2.naver"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
hdr = {'User-Agent':user_agent}

response = requests.get(URL_get, headers=hdr)

print(response)

soup = BeautifulSoup(response.text,'html.parser') #string 집어넣기

rank = []
title = []
price = []
perc = []
per = []
list1 = [rank, title, price, perc, per]

for i in soup.select('#contentarea > div.box_type_l > table > tr td.no'): #css selector 사용
    rank.append(i.text)
    print(i.text)
for i in soup.select('#contentarea > div.box_type_l > table > tr td a'): #css selector 사용
    title.append(i.text)
for i in soup.select('#contentarea > div.box_type_l > table > tr td:nth-child(4)'): #css selector 사용
    price.append(i.text)
for i in soup.select('#contentarea > div.box_type_l > table > tr td:nth-child(6) > span'): #css selector 사용
    perc.append(i.text.strip())
for i in soup.select('#contentarea > div.box_type_l > table > tr td:nth-child(11)'): #css selector 사용
    per.append(i.text)

for i in range(len(rank)):
    print(f"{list1[0][i]}위 {list1[1][i]} 현재가 {list1[2][i]} 등락률 {list1[3][i]} PER {list1[4][i]}")