#内链遍历
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()#已经找过的页面
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))#第一个页面
    bs = BeautifulSoup(html, 'html.parser')

    try:#其实就是找内链并输出
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0])#查找id属性为‘mw-content-text’的标签里的‘p’
        print(bs.find(id='ca-edit').find('span')#查找id属性为‘ca-edit’的标签里的‘span’标签里的链接‘a’，属性为‘href’
            .find('a').attrs['href'])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")#如果属性出错就显示这个

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):#用了个正则，作为链接的筛选
        if 'href' in link.attrs:#link的属性里有href（表示它是个链接）
            if link.attrs['href'] not in pages:
                # 我们遇到了新页面
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')