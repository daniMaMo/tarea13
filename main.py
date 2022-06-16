"""
Course: Programación avanzada
Date: 2022/06/14
Name: Daniela Martínez Madrid
Description: Download exchange rate of USD/MXN.
See https://mx.investing.com/

"""

import csv
import datetime
import time
from bs4 import BeautifulSoup
import requests

URL = "https://mx.investing.com/"
PAGE = requests.get(URL)
print(PAGE)

if 7 <= datetime.datetime.today().hour < 16:
    while True:
        with open('exchange_rate.csv', mode='a') as csv_file:
            soup = BeautifulSoup(PAGE.content, 'html.parser')
            content_stocks = soup.find(id='qb_pair_last_39')
            item = content_stocks.find_all(class_='pid-39-last')

            csv_writer = csv.writer(csv_file, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([content_stocks.text, datetime.datetime.today().time()])
        print(content_stocks.text, datetime.datetime.today().time())
        time.sleep(3600)
