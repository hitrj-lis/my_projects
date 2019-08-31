# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import re

headers ={'accept': '*/*',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

base_url = 'https://meduza.io'

def parse(base_url, headers):
    news = []
    session = requests.session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'Section-root'})
        for div in divs:
            section_root = div.find_all('span')
            for blocktitle in div:
                bt = blocktitle.find('span', attrs={'class': 'BlockTitle-first BlockTitle-isFeatured'})
                if bt:
                    a = r'span class="BlockTitle-first BlockTitle-isFeatured">'
                    bt_split = re.split(pattern=a, string=bt, maxsplit=1)
                    print(bt)
            # section_root = div.find_all('span', attrs={'class': 'BlockTitle-first'})
            # print(section_root)
#             href = tr.find('a', attrs={'data-test': 'rating-bank-name'})['href'].strip()
#             div = tr.find('div', attrs='font-size-small color-gray-burn').text.strip()
#             license = re.findall(r'[\d]+', div)
#             registration = re.findall(r'\D+$', div)
#             news.append({
#                 'bank-name': td,
#                 'link ': href,
#                 'license': license[0],
#                 'registration': registration[0]
#             })
#         return news
    else:
        print('error')
parse(base_url, headers)
# for element in parse(base_url, headers):
#     print(element)
