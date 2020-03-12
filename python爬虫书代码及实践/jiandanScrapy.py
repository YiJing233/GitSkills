# -*- coding:utf-8 -*-
'''
爬取煎蛋图片
主要用到了requests BeautifulSoup os文件/目录方法 time计时 以及 css选择器
'''
#导入需要的库
import os
import time
import requests
from  bs4 import BeautifulSoup
 
#获取url的函数
def get_html(url):
    #万变不离其宗的找到headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    #代理 如果不让访问就用代理进行访问
    proxies = {'http': '111.23.10.27:8080'}
    #try和except必定运行一个 python的语法基础
    try:
        resp = requests.get(url,headers=headers)
    except:
        resp = requests.get(url,headers=headers,proxies=proxies)
    return  resp
 
#创建文件的函数
def mkdir(path):
    isExists = os.path.exists(os.path.join("D:\jiandan", path)) #os.path.exists()判断文件是否存在
    if not isExists:
        print('makedir', path)
        os.makedirs(os.path.join("D:\jiandan", path))  #os.makedirs()如果不存在就创建文件
        os.chdir(os.path.join("D:\jiandan", path))  #改变路径，切换到这个路径
        return  True              #添加一个判断条件 避免重复添加
    else:
        print("already exists")
        return  False
 
#获取图片的函数
def get_imgs():
    for url in all_page(): #遍历的方式获取
        path = url.split('-')[-1]  #以'-'划分，保留最后一段 就是jiandan文件里面的各个文件名 分析网页所得规律
        mkdir(path)
        soup = BeautifulSoup(get_html(url).text, 'lxml') #lxml可以改成html.parser(python标准库)，但是没有lxml好
        allimgs = soup.select("div.text > p > img") #CSS选择器 只要子节点就行了 find的方法也能实现 但是CSS方便
        download(allimgs)
 
    print('ok')
#对页面进行分析，获取所有的url
def all_page():
    base_url = 'http://jandan.net/ooxx/' #基本的url格式
    soup = BeautifulSoup(get_html(base_url).text, 'lxml') #先用BeautifulSoup转成文本
    #找到页码的标签，标签中有[]，不是数组，是字符串，去掉最后第一个和最后一个可以得到
    allpage = soup.find('span', class_="current-comment-page").get_text()[1:-1]
    urllist = []
    for page in range(1, int(allpage) + 1): #开始遍历每一页
        allurl = base_url + 'page-' + str(page) #每一页的格式就是这样的
        urllist.append(allurl) #添加进去
    return urllist #返回这个列表
 
#下载函数
def download(list):
    for img in list:
        urls = img['src']
        if urls[0:5] == 'http:': #判断urls前面五个字符是否为http:
            img_url = urls
        else:
            img_url = 'http:' + urls #缺少http: 就添加补充完整
        filename = img_url.split('/')[-1] #以'/'划分，保留最后一段
 
        with open(filename,'wb') as f: #witn语句处理文件存储发生异常 以二进制方式写入文件
            try:
                f.write(get_html(img_url).content) #img的解码方式为.content
                print("Successfule:",filename)
            except:
                print("Failed:",filename)
 
 
if __name__ == '__main__': #时间函数
 
    t1 = time.time()  #计时
 
    get_imgs()  #运行函数
    print(time.time() - t1)