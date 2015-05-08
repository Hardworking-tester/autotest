# encoding:utf-8

import unittest
import time
import os

from selenium import webdriver


class DownloadByAu3(unittest.TestCase):
    def setUp(self):
        self.fp=webdriver.FirefoxProfile()
        self.driver=webdriver.Firefox(self.fp)
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
        downloadpath="F:\\resultlog"
        br.find_element_by_link_text(u"selenium").click()
        br.find_element_by_link_text(u"python").click()
        br.find_element_by_link_text(u"autoit方式上传文件附件1").click()
        time.sleep(3)
        br.find_element_by_css_selector("a.J_attach_post_buy").click()
        br.switch_to_alert()
        time.sleep(2)
        br.find_element_by_xpath("//*[@id='J_buy_pop']/div/div/div[3]/button[1]").click()
        fp=self.fp
        fp.set_preference("browser.download.folderList",0)#询问下载位置2，桌面0，“下载”目录1
        fp.set_preference("browser.download.manager.showWhenStarting",False)#当一个下载开始时显示下载管理器。true为显示，false为不显示，缺省我true
        # fp.set_preference("browser.download.dir", downloadpath)#上次通过“如何处理这个文件”对话框保存一个文件时所指定的目录
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/html")#指定下载文件格式
        # self.autoIt(browser=br,filepath=file_path)

    # def autoIt(self,browser,filepath):
    #     """
    #     该方法主要是实现au3的调用，需要传递两个变量，一个是webdriver，一个是文件下载存放的路径
    #     :param browser: 是传的webdriver
    #     :param filepath: 是文件下载存放的路径
    #     """
    #     file_path=filepath
    #     autoit = Dispatch("AutoItX3.Control")
    #     autoit.WinWait(u"正在打开 1.zip", "", 5)
    #     autoit.WinActivate(u"正在打开 1.zip")
    #     autoit.Send("{UP}")
    #     autoit.Send("{TAB 2}")
    #     time.sleep(10)
    #     autoit.Send("{ENTER}")
    #     time.sleep(4)
    #     br=browser
    #     br.find_element_by_link_text(u"« 返回列表").click()
    #     time.sleep(10)
    #     self.isExist(path=file_path)

    def isExist(self,path):
        """
        判断下载后的文件是否存在以及文件大小
        :param path:
        """
        for pp in os.listdir(u"C:\\Users\\Administrator\\Downloads"):
            if pp=="1.zip":
                print "文件已找到"
                print "文件大小为:",os.stat(path).st_size
                break
            else:
                print("文件未找到")



    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(DownloadByAu3("testDownLoad"))
    runner = unittest.TextTestRunner()
    runner.run(suite)