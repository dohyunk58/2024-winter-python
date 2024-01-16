# 본인이 검색한 키워드의 이미지들을 저장해 보세요.(모든 이미지)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from urllib import request
path = ".\\image\\" # 저장 경로

driver = webdriver.Chrome()
search = input("이미지 검색: ")

driver.get('https://www.naver.com/')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="query"]').send_keys(search) #검색어 입력
driver.find_element(By.XPATH, '//*[@id="query"]').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[2]/a').click() # 이미지 선택
time.sleep(1)
imagediv = driver.find_elements(By.CLASS_NAME, '_fe_image_tab_content_thumbnail_image')
for i, j in enumerate(imagediv):
    src_url = j.get_attribute('src') #img src 주소값을 변수에 저장
    request.urlretrieve(src_url, f"{path}{search}_{i}.jpg")





