# encoding:utf-8

from selenium import webdriver
import unittest
import time
br=webdriver.Firefox()
br.get("http://officeen.drakex2.com/default.aspx")
br.find_element_by_id("un_input").send_keys("test")
br.find_element_by_id("pw_input").send_keys("abc123")
br.find_element_by_id("login").click()
time.sleep(25)
br.find_element_by_id("arrow_down").click()











