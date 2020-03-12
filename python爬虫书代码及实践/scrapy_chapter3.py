#用来爬取juejin网站的一部分url

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://juejin.im')
bs = BeautifulSoup(html, 'html.parser')

for link in bs.find('div', {'id':'juejin'}).find_all(#实际操作中发现大多url在以id=juejin的div里
    'a', href=re.compile('^((https|http)?:\/\/)[^\s]+')):#正则表达式，筛出以http或https打头的url

    if 'href' in link.attrs:
        print(link.attrs['href'])