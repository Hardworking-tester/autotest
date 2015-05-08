# encoding:utf-8

from selenium import webdriver
import time

class DengLuLei:
    def dengLu(self,driver):
        browser=driver
        browser.get("http://localhost:8000/phpwind85")
        browser.find_element_by_link_text(u"登录").click()
        browser.find_element_by_id("J_u_login_username").send_keys('admin')
        browser.find_element_by_id("J_u_login_password").send_keys('admin')
        browser.find_element_by_xpath("//*[@id='J_u_login_form']/div/dl[4]/dd/button").click()
        time.sleep(5)

