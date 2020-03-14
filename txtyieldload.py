from urllib.request import urlopen

textPage = urlopen('http://www.pythonscraping.com/'\
    'pages/warandpeace/chapter1.txt')

print(textPage.read())

def yeildGet(url):
    textpage = urlopen('http://www.pythonscraping.com/'\
    'pages/warandpeace/chapter1.txt')

    BLOCK_SIZE = 1024

    while True:
        block = textpage.read(BLOCK_SIZE)
        if block:
            yield block
        else:
            return