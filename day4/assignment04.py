# Date 출력
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('http://capszzang.gq/')
time.sleep(1)

Date = driver.execute_script("return Date();") # Date()
print(Date)
iframe = driver.find_element(By.XPATH, '//*[@id="feature"]/div/div[2]/div[2]/div/div/p') # 주저리 
driver.execute_script(f"arguments[0].innerText = '{Date}';", iframe)
time.sleep(10)
