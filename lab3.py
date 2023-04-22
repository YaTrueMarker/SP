from bs4 import BeautifulSoup
import requests

url = 'http://biik.ru/rasp/cg109.htm'  
resp = requests.get(url) #получение с сайта всего
resp.encoding = 'windows-1251' 
print(resp.text) 