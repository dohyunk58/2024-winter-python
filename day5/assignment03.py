# iframe 내의 이미지 저장
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from urllib import request
path = ".\\image\\" # 저장 경로

driver = webdriver.Chrome()
driver.get('https://cafe.naver.com/joonggonara/994948311')
time.sleep(3)

iframe = driver.find_element(By.XPATH, '//*[@id="cafe_main"]')
driver.switch_to.frame(iframe)
# 이미지
img = driver.find_elements(By.TAG_NAME, 'img')
for i, j in enumerate(img):
    src_url = j.get_attribute("src")
    request.urlretrieve(src_url, f"{path}_{i}.jpg")
    