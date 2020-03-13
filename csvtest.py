import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('https://www.runoob.com/tags/tag-table.html')
# bs = BeautifulSoup(html, 'html.parser')
# # 主对比表格是当前页面上的第一个表格
# table = bs.findAll('table',{'class':'reference notranslate'})[0]
# rows = table.findAll('tr')

# csvFile = open('editors.csv', 'wt+',encoding='utf-8')
# print('CSV open')
# writer = csv.writer(csvFile)
# try:
#     for row in rows:
#         csvRow = []
#         for cell in row.findAll(['td', 'th']):
#             csvRow.append(cell.get_text())
#         writer.writerow(csvRow)
# finally:
#     csvFile.close()

csvFile = open('editors.csv','r',encoding='utf-8')
reader = csv.reader(csvFile)

datalist = [i for i in reader]

for i in datalist:
    if i == []:
        datalist.remove(i)

for line in datalist:
    if '\n' in line:
        line = line.remove('\n')
    

print(datalist)


import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.runoob.com/tags/tag-table.html')
bs = BeautifulSoup(html,'html.parser')

table = bs.findAll('table',{'class':'reference notranslate'})[0]
rows = table.findAll('tr')

csvfile = open('editors.csv','w+',encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()