import requests
from bs4 import BeautifulSoup
import re
import datetime
import time
import xlwt
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('1',cell_overwrite_ok=True)
sheet.write(0, 0, '标题')
sheet.write(0, 1, '地址')
n = 1
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
def video_url(day): #获取当日的所有链接并返回
    mainURL = 'http://tv.cctv.com/lm/wjxw/day/{}.shtml'
    URL = mainURL.format(days)
    req = requests.get(url=URL, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    url = re.findall('[a-zA-z]+://[^\s]*.shtml',str(soup))
    return url
def get_video_uid(listURL): # 获取所提供链接的视频uid并返回
    #listURL = 'http://tv.cctv.com/2019/01/01/VIDE2HsA8GVwiT4lz7HPyNPu190101.shtml?'
    req = requests.get(url=listURL, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'lxml').text
    uids = re.search('guid = +"[^\s]+"', soup).group().replace('"', '')
    uid = uids.replace('guid = ', '')
    return uid
def video(uid): #通过获取的uid取得下载链接并返回
    videoURL = 'http://vdn.apps.cntv.cn/api/getHttpVideoInfo.do?pid={}'
    URL = videoURL.format(uid)
    req = requests.get(url=URL, headers=headers)
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'lxml').text
    soup1 = re.search('[a-zA-z]+://[^\s]*', soup).group()
    soup2 = soup1.replace('}', '\n')
    soup3 = re.search('"url":"[a-zA-z]+://[^\s]*', soup2).group()
    title = soup.replace(',', '\n')
    tirtle = re.search('"title":"\[视频\][\u4e00-\u9fa5]*[^\s]*', title).group()
    tirtles = tirtle.replace('"title":"', '')
    global n
    sheet.write(n, 0, tirtles)
    sheet.write(n, 1, soup3)
    n = n + 1
    return soup3, tirtles
def main(i,days):
    video_url(day=days)
    uid = get_video_uid(i) # 将遍历的列表赋给获取uid的函数
    print(video(uid))
if __name__ == '__main__':
    begin = datetime.date(2019, 1, 1)
    end = datetime.date(2019, 1, 5)
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        days = str(day).replace('-', '')
        list = video_url(day=days)
        for i in list: # 将所提供的的链接列表进行遍历
            main(i, days)
    book.save(u'央视新闻.xls')