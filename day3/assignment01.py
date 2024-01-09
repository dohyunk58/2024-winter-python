from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('http://capszzang.gq/')
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[1]/a').click() #ABOUT 창 클릭
time.sleep(0.1)
driver.find_element(
    By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[1]/div/ul/li[4]/a').click() # 집행부 소개 클릭

name = driver.find_elements(
    By.XPATH, '/html/body/section[2]/div') # div/ul로 하면 기수 이름 부장여부만 출력

# name = driver.find_elements(
#     By.XPATH, '/html/body/section[2]/div/ul')

for i in name:
    print(i.text)

time.sleep(10)