# 使用Selenium获取cookie
#1. 导入必要的模块和库：
import os
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#1. 创建一个WebDriver对象，并设置Chrome浏览器的选项：
options = Options()
options.add_argument("--headless")  # 无界面模式
driver = webdriver.Chrome(options=options)
#1. 获取登录后的Cookie：
cookie = driver.get_cookies()
#1. 定义保存Cookie的文件路径和文件名：
file_path = "path_to_file.yaml"  # 替换为实际的文件路径
#1. 将Cookie保存到YAML文件中：
with open(file_path, "w") as file:
    yaml.dump(cookie, file)
#现在，你的Cookie已经保存到了指定的YAML文件中。
#请注意，使用`os`和`pyyaml`库需要事先安装，并且需要提供有效的文件路径来保存Cookie。另外，你也可以根据实际需求自定义保存Cookie的逻辑和文件格式。