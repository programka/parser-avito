from bs4 import BeautifulSoup
import requests

url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
response = requests.get(url)
print(response)

bs4 = BeautifulSoup(response.text,"lxml")
print(bs4)