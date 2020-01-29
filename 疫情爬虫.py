import requests
from bs4 import BeautifulSoup
import re
import pymysql
mainURL = 'https://123.sogou.com/zhuanti/pneumonia.html?fr=sgnews'
req = requests.get(url=mainURL)
req.encoding = 'utf-8'
html = req.text
soup = BeautifulSoup(html, 'lxml')
db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='pytest', port=3306, charset='utf8')
cursor = db.cursor()
zhcn = """alter table content convert to character set utf8;"""
cursor.execute(zhcn)
def main():
    intime(soup)
    icbar(soup)
    suspect(soup)
    cure(soup)
    dead(soup)
    #info()
    sql = "INSERT INTO content(id,全国确诊,疑似病例,治愈人数,死亡人数,时间) " \
          "VALUES(null,'{}','{}','{}','{}','{}')"
    sql2 = sql.format(((icbar(soup))), (suspect(soup)), (cure(soup)), (dead(soup)),(intime(soup)))
    cursor.execute(sql2)
    db.commit()
def icbar(soup):
    list = soup.find('div', class_='icbar confirm')
    content = list.find('div',class_='number').text
    print('全国确诊:'+content)
    return content
def suspect(soup):
    list = soup.find('div', class_='icbar suspect')
    content = list.find('div',class_='number').text
    print('疑似病例:'+content)
    return content
def cure(soup):
    list = soup.find('div', class_='icbar cure')
    content = list.find('div',class_='number').text
    print('治愈人数:'+content)
    return content
def dead(soup):
    list = soup.find('div', class_='icbar dead')
    content = list.find('div',class_='number').text
    print('死亡人数:'+content)
    return content
def intime(soup):
    list = soup.find('p', class_='time-num')
    content = list.text
    print(content)
    return content
#def info():
#    list = soup.find_all('p')
#    content = re.compile(r'[\u4e00-\u9fa5]+')
#    result = content.findall(list)
#    print(result)
def get():
    sql = 'select * from content order by id desc limit 1'
    cursor.execute(sql)
    result = cursor.fetchall()
    ic = icbar(soup)
    su = suspect(soup)
    cu = cure(soup)
    de = dead(soup)
    ti = intime(soup)
    for row in result:
        icbars = row[0]
        suspects = row[1]
        cures = row[2]
        deads = row[3]
        intimes = row[4]
        print(int(ic)-icbars)
        print(int(su)-suspects)
        print(int(cu)-cures)
        print(int(de)-deads)
        print(intimes)
if __name__ == '__main__':
    sql = 'select 时间 from content'
    cursor.execute(sql)
    result = cursor.fetchall()
    if result == intime(soup):
        main()
    else:
        get()
        main()