#encoding=utf-8
from  selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://www.youdao.com")
#获得cookie信息
cookie=driver.get_cookies()
print (cookie)
