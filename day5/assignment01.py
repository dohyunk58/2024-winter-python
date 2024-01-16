from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
original_window = driver.current_window_handle
driver.maximize_window() # 최대화
time.sleep(1)
driver.get('https://everytime.kr/')
time.sleep(1)
driver.switch_to.new_window('tab')
driver.get('https://mdrims.dongguk.edu/')
time.sleep(1)
driver.switch_to.window(window_name = original_window)
time.sleep(1)

