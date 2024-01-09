 # 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# 실행경로와 드라이버 객체 생성
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
time.sleep(0.5)
nickname = driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[6]/a').text #닉네임 정보 알아오기
print(nickname)