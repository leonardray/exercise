#encoding=utf-8

from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://www.youdao.com")

driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbb'})
cookies = driver.get_cookies()

#遍历cookies中的name和value信息并打印
for cookie in cookies:
    print("%s -> %s" % (cookie['name'],cookie['value']))
