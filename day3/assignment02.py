from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('http://capszzang.gq/')
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[6]/a').click() #로그인 창 클릭
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="user_id"]').send_keys('test1234') #아이디 입력
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('12345678') #패스워드 입력
driver.find_element(
    By.XPATH, '/html/body/section[2]/div/div/div/form/div[3]/button').click()  # 로그인 버튼 클릭
time.sleep(0.5)

try: #예외처리
    result = driver.switch_to.alert #alert창으로 전환
    result.accept() #alert 확인 버튼 클릭
except:
    pass

time.sleep(1)

driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[5]/a').click() # UTIL
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[5]/div/ul/li[3]/a').click() # WIKI
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="search"]').send_keys('신효환') # 검색
driver.find_element(
    By.XPATH, '/html/body/section[2]/div[1]/form/button').click()


time.sleep(1)

text = driver.find_elements(
    By.XPATH, '/html/body/section[3]/div')

for i in text:
    print(i.text)

with open("./2024-winter-python/day3/wiki_text.txt", 'w') as f:
    for i in text:
        f.write(i.text)