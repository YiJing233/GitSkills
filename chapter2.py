from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getHTML(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("HTTPError")
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        # for sibling in bs.find('table',{'border':'1'}).tr.next_siblings:
        #     print(sibling)
        # print(bs)
        return bs
    except AttributeError as e:
        print("AttributeError")
        return None

def findSpan(beautifulsoap):
    nameList = beautifulsoap.findAll('span',{'class':'green'})
    for name in nameList:
        print(name.get_text())

#findSpan(getHTML("http://www.pythonscraping.com/pages/warandpeace.html"))

def findChildren(beautifulsoap):
    for child in beautifulsoap.find('table',{'id':'giftList'}).children:
        print(child)
        print("\n")
#findChildren(getHTML("http://www.pythonscraping.com/pages/page3.html"))


def findSiblings(beautifulsoap):
    for sibling in beautifulsoap.find('table',{'id':'giftList'}).tr\
        .next_siblings:
        print(sibling)

def findParents(beautifulsoap):
    print(beautifulsoap.find('img',{'src':'../img/gifts/img1.jpg'})\
        .parent.previous_sibling.get_text())

findParents(getHTML("http://www.pythonscraping.com/pages/page3.html"))