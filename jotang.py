from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re


url = ("https://d.jotang.party/t/2019-19/497")

html = urlopen(url)

bs = BeautifulSoup(html,'html.parser')

nameList = bs.find_all('span',class='first username staff admin')

bodyList = bs.find_all('div',class='cooked')

for name in nameList:
    for body in bodyList:
        print(name.get_text())
        print(body.get_text())
    