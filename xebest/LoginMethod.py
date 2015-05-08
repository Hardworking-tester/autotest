# encoding:utf-8

from selenium import webdriver
import unittest
import Login,time,ResultLog

class LoginMethod(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.baseurl="http://www.xebest.com:8000"

    def testLogin(self):
        br=Login.login(self.driver,self.baseurl)
        log=ResultLog.resultLog()
        time.sleep(10)
        result=br.find_element_by_css_selector("a.red").is_displayed()
        print result
        if result:
            log.info("用户已登录2")
        else:
            log.info(u"用户登录失败")

    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LoginMethod("testLogin"))
    runner = unittest.TextTestRunner()
    runner.run(suite)