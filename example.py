import requests
from bs4 import BeautifulSoup

url = "https://www.lanacion.com.ar/"
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')

content_stocks = soup.find_all('h2', 'com-title')

for stock in content_stocks:
    sub = stock.find_all('a')
    print(sub)
    #print(sub[0].attrs.get('title'))