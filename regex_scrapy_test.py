from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "http://www.pythonscraping.com/pages/page3.html"
# url = originurl.encode("utf-8")
print(url)

html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img',
    {'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
#打印出图片的相对路径，以 ../img/gifts/img 开头，以.jpg结尾
for image in images:
    print(image['src'])