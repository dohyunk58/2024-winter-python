# 스크롤하기
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('http://capszzang.gq/')
time.sleep(1)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 최하단까지 스크롤/

element = driver.find_element(By.XPATH, '//*[@id="call-to-action"]') # 원하는 요소 XPATH
driver.execute_script("window.scrollTo(0, arguments[0].scrollHeight)", element) # 원하는 요소 y값까지 스크롤
time.sleep(5)