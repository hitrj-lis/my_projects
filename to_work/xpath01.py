# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import re

headers ={'accept': '*/*',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

base_url = 'https://www.banki.ru/banks/ratings/'

def parse(base_url, headers):
    arrey = []
    session = requests.session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        trs = soup.find_all('tr', attrs={'data-test': 'rating-table-item'})
        for tr in trs:
            td = tr.find('a', attrs={'data-test': 'rating-bank-name'}).text.strip()
            href = tr.find('a', attrs={'data-test': 'rating-bank-name'})['href'].strip()
            div = tr.find('div', attrs='font-size-small color-gray-burn').text.strip()
            license = re.findall(r'[\d]+', div)
            registration = re.findall(r'\D+$', div)
            arrey.append({
                'bank-name': td,
                'link ': href,
                'license': license[0],
                'registration': registration[0]
            })
        return arrey
    else:
        print('error')

for element in parse(base_url, headers):
    print(element)
