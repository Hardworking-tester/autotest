# encoding:utf-8
from selenium import webdriver
br=webdriver.Firefox()
br.get("http://www.baidu.com")
br.find_element_by_link_text(u"新闻").click()
#
# br.find_element_by_id("userName").send_keys('wwg74581@163.com')
# br.find_element_by_id("password").send_keys('wwg123456')
# br.find_element_by_id("imgLogin").click()