import requests
# 1. 직접 입력해서 보내기
# url에 보내고자 하는 데이터를 입력해서 전송한다.
URL_get = "https://search.naver.com/search.naver?query=%EA%B9%80%EC%9E%A5%ED%9B%88"
response = requests.get(URL_get)
print(response.status_code)

print("--------이하 dict---------")
# 2. dict 이용하기
URL_dict = "https://search.naver.com/search.naver"

param = { "query" : "김장훈"}
response = requests.get(URL_dict, params=param)
print(response.text)