import os.path
from selenium import webdriver
from selenium.common.exceptions import TimeoutException #界面加载超时相关
from selenium.webdriver.common.by import By   #模拟人工操作
from selenium.webdriver.support.ui import WebDriverWait   #等待加载相关
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import json
import yaml
import chardet
import selenium
import xlwt
import pymysql
driver = r"C:\...."
browser = webdriver.Chrome(executable_path=driver)  #driver
browser.implicitly_wait(10)
WAIT = WebDriverWait(browser, 10) #定义等待默认超时时间
browser.set_window_size(1280, 720)  #定义窗口长宽
planID = '0'
url = "https://xxxxxx" #网站主页面
log_url = "https://xxx" #网站你要通过cookie绕过登录后的页面，一般为固定地址
def main():
    browser.get(url)
    close_ad = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'css标签')))    #如果有弹出界面影响登录，获取关闭按钮的css标签
    webdriver.ActionChains(browser).move_to_element(close_ad).click(close_ad).perform() #通过鼠标点击事件关闭弹窗
    # 关闭公告弹窗
    login = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '')))  #选择登录按钮的标签
    webdriver.ActionChains(browser).move_to_element(login).click(login).perform()  #移动鼠标指针到登录按钮标签，点击
    # 点击登录按钮
    input_user = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'')))
    input_passwd = WAIT.until(EC.presence_of_element_located(By.XPATH, ''))
    input_user.sent_keys('')
    input_passwd.send_keys("")
    print('跳转到新窗口')
def get_cookies_login():
    browser.get(url)
    if not os.path.exists('resource'):
        os.mkdir('resource') #创建resource文件夹用于存储cookies文件
    if os.path.exists('resource/cookie.yaml'): #判断cookie是否存在，如果存在则使用cookie跳过登录
        cookie = yaml.safe_load(open('resource/cookie.yaml'))
        for i in cookie:
            browser.add_cookie(i)
        browser.get(log_url)
    else:
        WebDriverWait(browser, 60).until(EC.url_contains(log_url)) #判断登录状态，获取cookies
        cookie = browser.get_cookies()
        with open('resource/cookie.yaml', 'w') as f:
            yaml.safe_dump(cookie, f)
def get_session():
    browser.get(log_url) # 浏览器地址已经更换到目标，但还是需要通过此命令重新get一次网页
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    all_plan = soup.find(class_='as-list').find_all(class_='s-list')
    for item in all_plan:
        item_title = item.find(class_ = 'fl as-name').text
        item_session = item.find(class_='i_link').text
        item_link = item.find(class_='lm_wordA').get('herf')
        item_progress_rate = item.find(class_='jdBar').text
        item_complate = item.find(class_='fl as-name-o otherP').text
        print(item_title)
        print(item_session)
        print(item_link)
        print(item_progress_rate)
        print(item_complate)
if __name__ == '__main__':
    get_cookies_login() #获取cookie冰使用cookie登录
    browser.get(log_url)
    get_session()