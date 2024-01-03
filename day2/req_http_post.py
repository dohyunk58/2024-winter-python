import requests
datas = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('https://httpbin.org/post', data=datas)
print(r.text)