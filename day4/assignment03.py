# iframe 내의 내용 저장하기
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/joonggonara/994948311')
time.sleep(1)

iframe = driver.find_element(By.XPATH, '//*[@id="cafe_main"]')
driver.switch_to.frame(iframe)
# 텍스트
text = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]')
print(text.text)
# 이미지
img = driver.find_elements(By.TAG_NAME, 'img')
for i in img:
    i = i.get_attribute("src")
    print(i)

