#是一个范例版的py程序，每一个类和函数都分工明确且紧密结合，观赏性很强，也很漂亮

#不过还是有不足之处的，
# 每个网站必须具有一定的结构，即特定的字段必须存在，
# 从字段取出的数据必须干净，并且每个目标字段必须有唯一且可靠的 CSS 选择器。
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


'''
#同样有点问题，运行不动

class content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find("h1").text
    lines = bs.find_all("p", {"class":"story-content"})
    body = '\n'.join([line.text for line in lines])
    return content(url, title, body)

def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find("h1").text
    body = bs.find("div",{"class","post-body"}).text
    return content(url, title, body)

url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
content = scrapeBrookings(url)

print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)

url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'

content = scrapeNYTimes(url)

print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)
'''

#以下是对上述代码的优化

class Content:
    """
    所有文章/网页的共同基类
    """

    def __init__(self,topic, url, title, body):
        self.url = url
        self.topic = topic
        self.title = title
        self.body = body

    def print(self):
        """
        用灵活的打印函数控制结果
        """
        print("New article found for topic: {}".format(self.topic))
        print("URL: {}".format(self.url))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))

class Website:  #"工具人（类）"，服务于crawler

    """
    描述网站结构的信息
    这里 Website 类并不存储任何从页面本身抓取的信息，而是存储关于如何抓取数据的指令。
    它也不存储“My Page Title”这样的标题。它只会存储字符串标签 h1，
    表明了在哪里可以找到标题。这就是这个类被命名为 Website（它包含适用于整个网站的信息）
    而不是 Content（它包含来自单个网页的信息）的原因
    """

    def __init__(self, name, url, searchUrl,resultListing,resultUrl,absoluteUrl,titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl=absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:#确保不是异常字符串
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        用于从一个BeautifulSoup对象和一个选择器获取内容的辅助函数。
        如果选择器没有找到对象，就返回空字符串
        """
        childObj = pageObj.select(selector)

        if childObj is not None and len(childObj) > 0:
            return '\n'.join(
            [elem.get_text() for elem in childObj])
        return ''

    def search(self,topic,site):
        """
        根据主题搜索网站并记录所有找到的页面
        """
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs["href"]
            # 检查一下是相对URL还是绝对URL
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print("Something was wrong with that page or URL. Skipping!")
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, title, body, url)
                content.print()

'''
#更新更加完善之后这段就没有用了
    def parse(self, site, url):
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
'''
crawler = Crawler()

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com',
        'https://ssearch.oreilly.com/?q=','article.product-result',
        'p.title a', True, 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com',
        'http://www.reuters.com/search/news?blob=',
        'div.search-result-content','h3.search-result-title a',
        False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu',
        'https://www.brookings.edu/search/?s=',
        'div.list-content article', 'h4.title a', True, 'h1',
        'div.post-body']
]

sites = []

for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

topics = ['python','data sicence']

for topic in topics:
    print("GETTING INFO ABOUT:" + topic)
    for targetSite in sites:
        crawler.search(topic,targetSite)
