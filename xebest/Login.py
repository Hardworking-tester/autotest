# encoding:utf-8

from selenium import webdriver
import time
import ResultLog
def login(driver,url):
    log=ResultLog.resultLog()
    br=driver
    br=webdriver.Firefox()
    br.get(url)
    br.find_element_by_link_text(u"请登录").click()
    time.sleep(5)
    br.find_element_by_id("userName").send_keys("wwg771512@163.com")
    br.find_element_by_id("password").send_keys("wwg123456")
    br.find_element_by_id("imgLogin").click()
    log.info(br.switch_to_alert().text.encode('utf-8'))
    br.switch_to_alert().accept()
    return br


