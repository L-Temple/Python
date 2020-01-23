import requests
from bs4 import BeautifulSoup
import sys
import threading
class download(object):
    def __init__(self):
        self.target = "https://read.qidian.com/hankread/1016414271/79945909"
        self.base_target = "https://read.qidian.com/chapter/_Q3cDZ7Pr5CLTMDvzUJZaQ2/"
        self.path = 'D:\\Python project\\爬虫\\爬取文字\\小说.txt'
        self.num = 151
    def get_tirtle(self,target,num):
        req = requests.get(url=target)
        html = req.text
        tirtle_bf = BeautifulSoup(html)
        tirtle1 = tirtle_bf.find_all('div',class_="text-head")
        tirtle = tirtle1[num].text
        return tirtle
    def get_content(self,target,num):
        req = requests.get(url=target)
        html = req.text
        text_bf = BeautifulSoup(html)
        text1 = text_bf.find_all('div', class_="read-content j_readContent")
        text = text1[num].text
        return text
    #def get_url(self):
        #return
    def write(self,tirtle,text,path):
        f = open(path,'a',encoding='utf-8')
        f.write(tirtle + '\n')
        f.writelines(text)
if __name__ == '__main__':
    spider = download()
    print('开始下载')
    for i in range(spider.num):
        spider.write(spider.get_tirtle(spider.target,i),spider.get_content(spider.target,i),spider.path)
        sys.stdout.write("  已下载:%.3f%%" % float(i / spider.num) + '\r')
        sys.stdout.flush()
    print('下载完成')