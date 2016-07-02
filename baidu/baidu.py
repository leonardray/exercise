#encoding=utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#设置窗口大小
driver.set_window_size(600,600)
#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)

js="window.scrollTo(100,600);"
driver.execute_script(js)
