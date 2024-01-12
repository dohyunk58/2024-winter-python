# innerHTML로 내용 변경
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('http://capszzang.gq/')
time.sleep(1)

notice = driver.find_element(By.XPATH, '//*[@id="feature"]/div/div[2]/div[1]/div/div/h4/a')
driver.execute_script("arguments[0].innerHTML = '<h1>꽁치사랑</h1>';", notice)
time.sleep(10)