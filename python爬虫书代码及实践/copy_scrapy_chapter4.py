'''
整个思路其实很清楚
将各个类分得清清楚楚明明白白，有些是基类，有些是描述内容位置的类，各个类分工都很明确
'''

from bs4 import BeautifulSoup
import requests

class Content():
    #所有文章、网页的基类
    def __init__(self,url,title,body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        #打印所有信息
        print("URL: {}".format(self.url))
        print("Title: {}".format(self.title))
        print("Body: \n{}".format(self.body))

class Website():
    
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler():

    def getPage(self,url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:#确保不是异常字符串
            return None
        return BeautifulSoup(req.text,'hetml.parser')

    def safeGet(self, pageObj, selector):
        """
        用于从一个BeautifulSoup对象和一个选择器获取内容的辅助函数。
        如果选择器没有找到对象，就返回空字符串
        """
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join(
            [elem.get_text() for elem in selectedElems])#这段代码写的也贼鸡儿漂亮，尤其是join函数
        return ''
    
    def parse(self,site,url):
        """
        从指定URL提取内容
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
        


crawler = Crawler() #创建一个对象

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com',
    'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'h1',
    'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu',
    'h1', 'div.post-body'],
    ['New York Times', 'http://nytimes.com',
    'h1', 'p.story-content']
]#网站们，清楚明白

#后面就没写了
