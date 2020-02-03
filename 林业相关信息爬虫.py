import requests
from bs4 import BeautifulSoup
import re
mainURL = 'http://lycy.gansu.gov.cn'
def main():
    one()
    two()
    three()
    four()
    five()
    six()
def one():
    url = mainURL+'/content/2019-08/79231.html'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', class_='article').text
    print(content)
def two():
    url = mainURL+'/content/2019-07/75742.html'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', class_='article').text
    print(content)
def three():
    url = mainURL+'/content/2019-07/75732.html'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', class_='article').text
    print(content)
def four():
    url = mainURL+'/content/2019-07/75719.html'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', class_='article').text
    print(content)
def five():
    url = mainURL+'/content/2019-07/75718.html'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', class_='article').text
    print(content)
def six():
    url = mainURL+'/content/2019-07/75513.html'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div', class_='article').text
    print(content)
if __name__ == '__main__':
    main()