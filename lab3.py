from bs4 import BeautifulSoup
import requests

url = 'http://biik.ru/rasp/cg109.htm' #website 
resp = requests.get(url) #get all from site ()
resp.encoding = 'windows-1251' #because site biik.ru rasp use cp-1251 need do that 
print(resp.text) #write site answer code