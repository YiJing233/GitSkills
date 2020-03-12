from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

originurl = "http://www.pythonscraping.com/pages/page3.html"
url = originurl.encode("utf-8")
print(url)

html = urlopen(url)

# html = urlopen('https://baike.baidu.com/item/八叉树/')
# bs = BeautifulSoup(html, 'html.parser')

# print(bs.text())