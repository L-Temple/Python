#我的世界courseforge爬取整合包
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import xlwt
import pymysql
browser = webdriver.Chrome()
mainURL = 'https://www.curseforge.com/minecraft/modpacks'
WAIT = WebDriverWait(browser, 15)
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('1',cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
def search():
    try:
        browser.get(mainURL)
        input = WAIT.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, " html > body > div > main > div > div > section > div > div > div >"
                              " div > div > div > form > div > div > input")))
        #submit = WAIT.until(EC.element_to_be_clickable(
            #(By.CSS_SELECTOR, "#internationalHeader > div > div > div > div > #nav_searchform> div > button")))
        input.send_keys('greg')
        input.send_keys(Keys.ENTER)
        WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "html > body > div > main > div > div > ul > div ")))
        get_source()
    except TimeoutException:
        return search()
def get_source():
    WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "html > body > div > main > div > div > ul > div ")))
    html = browser.page_source
    soup = BeautifulSoup(html,'lxml')
    print_source(soup)
def print_source(soup):
    list = soup.find('div', class_='my-2')
    #for item in list:
        #item_title = item.find('div', class_='project-listing-row box py-3 px-4 flex flex-col lg:flex-row lg:items-center').text
        #print('爬取：' + item_title)
    content = list.text.replace("\n", "")
    print(content.replace(" ", ""))
def main():
    search()
if __name__ == '__main__':
    main()
    browser.close()