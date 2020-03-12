import os
import time
import requests
from  bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re

'''
爬取worldcosplay图片
用到了requests BeautifulSoup os文件/目录方法 time计时 以及 css选择器等方法
'''

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    
    data = {
    'email':'747322623@qq.com',#为了登陆   
    'password':'huyuting',
    #'next_url': 'https://worldcosplay.net/member/Itsuki-chan/characters'
    }
    
    #代理 如果不让访问就用代理进行访问
    proxies = {'http': '111.23.10.27:8080'}
    try:
        resp = requests.get(url,headers=headers)
    except:
        resp = requests.get(url,headers=headers,proxies=proxies)
    return  resp

#创建文件的函数
def mkdir(path):
    isExists = os.path.exists(os.path.join("D:\worldcosplay", path)) #os.path.exists()判断文件是否存在
    if not isExists:
        print('makedir', path)
        os.makedirs(os.path.join("D:\worldcosplay", path))  #os.makedirs()如果不存在就创建文件
        os.chdir(os.path.join("D:\worldcosplay", path))  #改变路径，切换到这个路径
        return  True              #添加一个判断条件 避免重复添加
    else:
        print("already exists")
        return  False

# def geturls():
    html = urlopen('https://worldcosplay.net/member/Itsuki-chan/characters')
    bs = BeautifulSoup(html, 'html.parser')

    title = bs.body.get_text()
    print(title)

'''
    for link in bs.find('div', {'class':'preview'}).find_all(#实际操作中发现大多url在class=preview的div里
        'a', href=re.compile('^((https|http)?:\/\/)[^\s]+')):#正则表达式，筛出以http或https打头的url

        if 'href' in link.attrs:
            print(link.attrs['href'])
'''



