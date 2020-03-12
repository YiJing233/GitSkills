import os
import time
import requests
from  bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
  
data = {
    'email':'747322623@qq.com',#为了登陆
    'password':'huyuting',
    #'next_url': 'https://worldcosplay.net/member/Itsuki-chan/characters'
    }

url ='https://worldcosplay.net/'
session = requests.Session()
session.post(url,headers = headers,data = data)
# 登录后，我们需要获取另一个网页中的内容
response = session.get('https://worldcosplay.net/member/Itsuki-chan/characters',headers = headers)
print(response.status_code)#返回状态码

print(response.text)