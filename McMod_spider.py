from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import xlwt
import re
browser = webdriver.Chrome()
mainURL = 'https://www.mcbbs.net/forum-mod-1.html'
WAIT = WebDriverWait(browser, 15)
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('1',cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
def search():
    try:
        browser.get(mainURL)
        get_source()
        submit = WAIT.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, " html > body > div > div > div > div > div > div > div > div > span > div > a.nxt ")))
        submit.click()
        total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR," html > body > div > div > div > div > div > div > div > div > span > div > a.last ")))
        return int(total.text.replace('... ', ''))
    except TimeoutException:
        return search()
def get_source():
    WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, " html > body > div > div > div > div > div > div > div > div > div > form > table ")))
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    print_source(soup)
def print_source(html):
    #list = soup.find('table', summary='forum_45')
    item = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, " html > body > div > div > div > div > div > div > div > div > div > form > table  ")))
    items = item.text
    print(items)
    #url = html.select(" html > body > div > div > div > div > div > div > div > div > div > form > table > tbody > tr > th > a.s.xst")
    #print(url.text)
    #title = item.find('a', class_='s xst')
    #print(title)
    #print(item.text)
    #content = list.text.replace('\n', '')
    #for soup in list:
    #    title = soup.find()
    #    print(title)
    #print(content)
def main():
        total = search()
        print(total)
        for i in range(1, int(total + 1)):
            search()
if __name__ == '__main__':
    main()
    browser.close()