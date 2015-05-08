# encoding:utf-8
"""
此功能主要实现发帖的自动化
"""
import unittest
import time

from selenium import webdriver

from practice import DengLuLei


class ShanTie(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()

    def testShanTie(self):
        login= DengLuLei.DengLuLei().dengLu(self.browser)
        br=self.browser
        time.sleep(5)
        br.find_element_by_css_selector("input.J_check[value='5']").click()
        br.find_element_by_link_text(u"删除").click()
        time.sleep(1)
        br.find_element_by_css_selector("input[name='deductCredit']").click()
        time.sleep(2)
        br.find_element_by_id("J_resson_input").clear()
        br.find_element_by_id("J_resson_input").send_keys(u"我真的什么都不想再说了")
        br.find_element_by_id("J_sub_topped").click()



    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ShanTie("testShanTie"))
    runner = unittest.TextTestRunner()
    runner.run(suite)