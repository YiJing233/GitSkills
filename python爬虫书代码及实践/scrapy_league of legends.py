from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import URLError
from urllib.error import HTTPError
import requests

def getitle(url):

    session = requests.Session()
    headers ={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
       'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
       'Accept':'text/html,application/xhtml+xml,application/xml;'
       'q=0.9,image/webp,*/*;q=0.8'
    }
    req = session.get(url, headers=headers)

    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body
    except AttributeError as e:
        return None
    return title

title = getitle('http://lol.qq.com/act/a20190114story/index.html?ccid=32000336259641151&clickId=1')
if title == None:
    print('Error')
else:
    print(title)
    