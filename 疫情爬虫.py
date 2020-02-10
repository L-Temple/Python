#爬取全国疫情实施情况
import requests
from bs4 import BeautifulSoup
import re
import pymysql
mainURL = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
req = requests.get(url=mainURL)
#req.encoding = 'utf-8'
html = req.text
soup = BeautifulSoup(html, 'lxml')
db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='pytest', port=3306, charset='utf8')
cursor = db.cursor()
zhcn = """alter table content convert to character set utf8;"""
cursor.execute(zhcn)
def main():
    soup1 = soup.text.replace('{', '')
    soup2 = soup1.replace('"', '')
    soup3 = soup2.replace('\\', '')
    soup4 = soup3.replace('[', '')
    soup5 = soup4.replace(']', '')
    soup6 = soup5.replace('}', '')
    soup7 = re.search('\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}', soup6).group() #时间
    soup8 = soup6.replace(soup7, '')
    soup9 = re.search('\d{3,10}',soup8).group() #全国确诊
    soup10 = soup8.replace(soup9, '')
    soup11 = re.search('\d{3,10}',soup10).group() #疑似病例
    soup12 = soup10.replace(soup11, '')
    soup13 = re.search('\d{3,10}',soup12).group() #死亡人数
    soup14 = soup12.replace(soup13, '')
    soup15 = re.search('\d{3,10}',soup14).group() #治愈人数
    AllPeople = int(soup9)+int(soup11)
    DeadRate = (int(soup13)/AllPeople)*100
    HealRate = (int(soup15)/AllPeople)*100
    print('全国确诊:'+soup9)
    print('疑似病例:'+soup11)
    print('死亡人数:'+soup13)
    print('治愈人数:'+soup15)
    print('截至:'+soup7)
    print("死亡率:%.2f%%" % DeadRate)
    print("治愈率:%.2f%%" % HealRate)
    #sql = "INSERT INTO content(id,全国确诊,疑似病例,治愈人数,死亡人数,时间) " \
    #      "VALUES(null,'{}','{}','{}','{}','{}')"
    #sql2 = sql.format((soup9), (soup11), (soup15), (soup13),('截至 '+soup7))
    #cursor.execute(sql2)
    #db.commit()
    t = soup.text
    lasts = re.search('[a-zA-z]{.*?}[a-zA-z]', t).group()
    last = lasts[::-1].replace('{', '')
    last1 =last.replace('"', '')
    last2 =last1.replace('\\', '')
    last3 = last2.replace('[', '')
    last4 = last3.replace(']', '')
    last5 = last4.replace('}', '')
    l_Date = re.search('\d{2}.\d{2}', last5).group() #时间
    l_Dates = last5.replace(l_Date, '')
    l_HealRate = re.search('\d{1,2}.\d{1,2}', l_Dates).group()
    l_HealsRate = l_Dates.replace(l_HealRate, '')
    l_DeadRate = re.search('\d{1,2}.\d{1,2}', l_HealsRate).group()
    l_DeadRates = l_HealsRate.replace(l_DeadRate, '')
    last6 = re.search('\d{2,7}',l_DeadRates).group() #治愈人数
    last7 = l_DeadRates.replace(last6, '')
    last8 = re.search('\d{2,7}',last7).group() #死亡人数
    last9 = last7.replace(last8, '')
    last10 = re.search('\d{2,7}',last9).group() #疑似病例
    last11 = last9.replace(last10, '')
    last12 = re.search('\d{2,7}',last11).group() #全国确诊
    lastss = last11.replace(last12, '')
    lDate = re.search('\d{2}.\d{2}', lastss).group() #时间
    lDates = last11.replace(lDate, '')
    lHealsRate = re.search('\d{1,2}.\d{1,2}', lDates).group()
    lHealsRates = lDates.replace(lHealsRate, '')
    lDeadRate = re.search('\d{1,2}.\d{1,2}', lHealsRates).group()
    lDeadRates = lHealsRates.replace(lDeadRate, '')
    last13 = re.search('\d{2,7}',lDeadRates).group() #治愈人数
    last14 = lDeadRates.replace(last13, '')
    last15 = re.search('\d{2,7}',last14).group() #死亡人数
    last16 = last14.replace(last15, '')
    last17 = re.search('\d{2,7}',last16).group() #疑似病例
    last18 = last16.replace(last17, '')
    last19 = re.search('\d{2,7}',last18).group() #全国确诊
    print('昨天全国确诊:' + last19[::-1])
    print('昨天疑似病例:' + last17[::-1])
    print('昨天死亡人数:' + last15[::-1])
    print('昨天治愈人数:'+last13[::-1])
    print('昨天时间:'+l_Date[::-1])
if __name__ == '__main__':
    main()