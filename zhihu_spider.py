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
mainURL = 'https://www.zhihu.com/hot'
WAIT = WebDriverWait(browser, 15)
def search():
    try:
        browser.get(mainURL)
        WAIT.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, " html > body > div > main > div > div > div > div > div > div >"
                              " div > div > section > div ")))
        get_source()
    except TimeoutException:
        return search()
def get_source():
    WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, " html > body > div > main > div > div > div > div > div"
                                                                " > div > div > div > section > div ")))
    html = browser.page_source
    soup = BeautifulSoup(html,'lxml')
    print_source(soup)
def print_source(soup):
    #list = soup.find('div', class_='my-2')
    list = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, " html > body > div > main > div > div > div > div > div"
                                                                " > div > div > div > section > div ")))
    print(list)
    #for item in list:
        #item_title = item.find('div', class_='project-listing-row box py-3 px-4 flex flex-col lg:flex-row lg:items-center').text
        #print('爬取：' + item_title)
    #content = list.text.replace("\n", "")
    #print(content.replace(" ", ""))
def main():
    search()
if __name__ == '__main__':
    main()
    browser.close()