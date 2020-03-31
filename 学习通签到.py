from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
browser = webdriver.Chrome()
WAIT = WebDriverWait(browser, 4)
browser.set_window_size(1400,900)
initial_URL = "https://passport2.chaoxing.com/login?fid=&newversion=true&refer=http://erya.mooc.chaoxing.com"
phone_number = '17339814729'
password = 'huanmiezhiyu'
def login():
    try:
        browser.get(initial_URL)
        WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, " html > body > div > div > div > div > form > div > button ")))
        input_phone = browser.find_element_by_id('phone')
        input_password = browser.find_element_by_id('pwd')
        input_phone.send_keys(phone_number)
        input_password.send_keys(password)
        submit_login = WAIT.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, " html > body > div > div > div > div > form > div > button ")))
        submit_login.click()
        url = browser.current_url
        return url
    except TimeoutException:
        return login()
def into():
    try:
        url = login()
        body = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, " html > body ")))
        body.send_keys(Keys.CONTROL + 't')
        browser.get(url)
        browser.get("http://i.mooc.chaoxing.com")
        mainURL = browser.current_url
        return mainURL
    except TimeoutException:
        return login()
def main():
    login()
    into()
if __name__ == '__main__':
    main()