# encoding:utf-8

import unittest
import time
import os

from win32com.client import Dispatch
from selenium import webdriver

from practice import DengLuLei


class DownLoadZip(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Ie()

    def testDownLoad(self):
        Denglu= DengLuLei.DengLuLei()
        Denglu.dengLu(self.driver)
        br=self.driver

        file_path="E:\\testtools\\1.zip"
        br.find_element_by_link_text(u"selenium").click()
        br.find_element_by_link_text(u"python").click()
        br.find_element_by_link_text(u"autoit方式上传文件附件1").click()
        time.sleep(3)
        br.find_element_by_css_selector("a.J_attach_post_buy").click()
        br.switch_to_alert()
        time.sleep(2)
        br.find_element_by_xpath("//*[@id='J_buy_pop']/div/div/div[3]/button[1]").click()
        self.autoIt(browser=br,filepath=file_path)

    def autoIt(self,browser,filepath):
        """
        该方法主要是实现au3的调用，需要传递两个变量，一个是webdriver，一个是文件下载存放的路径
        :param browser: 是传的webdriver
        :param filepath: 是文件下载存放的路径
        """
        file_path=filepath
        autoit = Dispatch("AutoItX3.Control")
        autoit.WinWait(u"文件下载", "", 5)
        autoit.WinActivate(u"文件下载")
        autoit.ControlClick(u"文件下载","",4427)
        autoit.WinWait(u"另存为","",5)
        autoit.WinActivate(u"另存为")
        autoit.ControlSetText(u"另存为","","[CLASS:Edit; INSTANCE:1]",file_path)
        autoit.ControlClick(u"另存为","",1)
        autoit.WinWait(u"下载完毕","",5)
        autoit.WinActivate(u"下载完毕")
        autoit.ControlClick(u"下载完毕","",2)
        time.sleep(4)
        br=browser
        br.find_element_by_link_text(u"« 返回列表").click()
        self.isExist(path=file_path)

    def isExist(self,path):
        """
        判断下载后的文件是否存在以及文件大小
        :param path:
        """
        for pp in os.listdir(u"E:\\wwg"):
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
    suite.addTest(DownLoadZip("testDownLoad"))
    runner = unittest.TextTestRunner()
    runner.run(suite)