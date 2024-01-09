from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('https://finance.naver.com/sise/lastsearch2.naver')
time.sleep(1)


text = driver.find_elements(
    By.XPATH, '//*[@id="contentarea"]/div[3]/table/tbody/tr')

for i in text:
    if i.text != '':
        split1 = i.text.split(' ')
        print(split1[0],split1[1],split1[3],split1[5],split1[-2])