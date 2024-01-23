# 네이버 사전 영어 발음 엑셀에 저장
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from openpyxl import Workbook

search = input("저장할 영단어: ")

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
driver.get(f'https://en.dict.naver.com/#/search?query={search}')
time.sleep(5)
# 첫 번쨰 발음 //*[@id="searchPage_entry"]/div/div[1]/div[3]/div/div/span[2]
pronounce = driver.find_element(By.XPATH, '//*[@id="searchPage_entry"]/div/div[1]/div[3]/div/div/span[2]')
print(pronounce.text)
time.sleep(1)

xlsx = Workbook()
xlsx_sheet = xlsx.create_sheet('sheet1')
xlsx_sheet = xlsx.active
xlsx_sheet['A1'] = '단어'
xlsx_sheet['B1'] = '발음'
xlsx_sheet['A2'] = search
xlsx_sheet['B2'] = pronounce.text
xlsx.save('./2024-winter-python/day6/assignment01.xlsx')