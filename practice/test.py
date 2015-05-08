# encoding:utf-8

import unittest
import time

from selenium import webdriver


class test(unittest.TestCase):
    def setUp(self):
        self.fp=webdriver.FirefoxProfile()
        downloadpath="F:\\resultlog"

        self.fp.set_preference("browser.download.folderList",2)#询问下载位置2，桌面0，“下载”目录1
        self.fp.set_preference("browser.download.manager.showWhenStarting",False)#当一个下载开始时显示下载管理器。true为显示，false为不显示，缺省我true
        self.fp.set_preference("browser.download.dir", downloadpath)#上次通过“如何处理这个文件”对话框保存一个文件时所指定的目录
        self.fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")#指定下载文件格式
        self.driver=webdriver.Firefox(firefox_profile=self.fp)
        self.baseurl="http://localhost:8000/phpwind85"

    def testDownLoad(self):



        br=self.driver
        br.get(self.baseurl)
        br.find_element_by_link_text(u"登录").click()
        br.find_element_by_id("J_u_login_username").send_keys("admin")#传递用户名
        br.find_element_by_id("J_u_login_password").send_keys("admin")#传递密码
        br.find_element_by_xpath("//*[@id='J_u_login_form']/div/dl[4]/dd/button").click()
        time.sleep(10)


        file_path="E:\\testtools\\1.zip"
        br.find_element_by_link_text(u"selenium").click()
        br.find_element_by_link_text(u"python").click()
        br.find_element_by_link_text(u"autoit方式上传文件附件1").click()
        time.sleep(3)
        br.find_element_by_css_selector("a.J_attach_post_buy").click()
        br.switch_to_alert()
        time.sleep(2)
        br.find_element_by_xpath("//*[@id='J_buy_pop']/div/div/div[3]/button[1]").click()








    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(test("testDownLoad"))
    runner = unittest.TextTestRunner()
    runner.run(suite)