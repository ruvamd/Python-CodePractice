import requests
import os

url='https://apiok.ru/'
url1='https://api.github.com/'
response=requests.get(url)
response=response.status_code
# print(response)
if response==200:
    print('success')
elif response==404:
    print('not found')