import requests
from bs4 import BeautifulSoup
import time
#T_URL = 'http://www.shuxue9.com/pep/gzbixiu1/ebook/.html'
P_URL = 'http://www.shuxue9.com/pep/gzbixiu1/ebook/{}.jpg'
i = 1
n = 1000
p = 1
for p in range(1, n + 1):
    if p < 10:
        p = "00%d" % p
        t = p.replace('0', '', 2)
    elif p < 100:
        p = "0%d" % p
        t = p.replace('0', '', 1)
    elif p < 1000:
        p = "%d" % p
        t = p.replace('0', '', 0)
    else:
        p = str(p)
    T_URL = f'http://www.shuxue9.com/pep/gzbixiu1/ebook/{t.capitalize()}.html'
    T_req = requests.get(url=T_URL.format())
    T_req.encoding = 'gbk'
    html = T_req.text
    html1 = BeautifulSoup(html, 'lxml')
    soup = html1.find('h1', class_='title')
    content = soup.text.replace('/', '')
    P_req = requests.get(P_URL.format(p))
    f = open('D:\\电子课本\\{}.png'.format(content), 'wb')
    f.write(P_req.content)
    f.close()
    print(t)
    print(T_URL)
    print(P_URL.format(p))