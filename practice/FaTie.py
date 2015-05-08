# encoding:utf-8
"""
此功能主要实现发帖的自动化
"""
import unittest
import time

from win32com.client import Dispatch
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from practice import DengLuLei


class FaTie(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()

    def testFaTie(self):
        DengLuLei.DengLuLei().dengLu(self.browser)#调用登录方法，并把webdriver作为参数传递，在函数调用完成后此webdriver已被改变
        br=self.browser
        autoit = Dispatch("AutoItX3.Control")#调用au3
        str_filepath ="C:\\Users\\Administrator\\Desktop\\ces\\1.zip"#设置需要上传的附件的路径
        br.find_element_by_css_selector("dt.J_sidebar_forum_toggle").click()
        br.find_element_by_link_text("python").click()
        ActionChains(br).move_to_element(br.find_element_by_xpath("//div[@class=\"main_content\"]/div[3]/a")).perform()#使用achionchains的perform方法进行点击下拉列表中的值得操作
        time.sleep(2)
        br.find_element_by_link_text(u"普通帖").click()#使用achionchains的perform方法进行点击下拉列表中的值得操作
        br.find_element_by_id("J_atc_title").send_keys(u"autoit方式上传文件附件33")
        br.find_element_by_name()
        br.find_element_by_xpath("//ul[@class='wind_editor_icons']/li[3]/div[3]/span").click()
        br.find_element_by_id("SWFUpload_0").click()
        autoit.WinWait(u"打开", "", 5)
        autoit.WinActivate(u"打开")
        autoit.ControlSetText(u"打开","","[CLASS:Edit; INSTANCE:1]",str_filepath)
        autoit.ControlClick(u"打开","",1) #附件上传动作
        time.sleep(4)
        br.find_element_by_css_selector("button.edit_menu_btn").click()
        cotent=u"这是我使用js处理的富文本编辑器33"
        js="document.getElementsByClassName(\"wind_editor_iframe\")[0].contentWindow.document.body.innerHTML=\"%s\"" %(cotent)#此js可以解决富文本框编辑的问题，document.getElementsByClassName(\"wind_editor_iframe\")[0].contentWindow.document.body.innerHTML此段代码先通过classname获取iframe，随后通过获取当前的iframe的对象往body里写数据
        br.execute_script(js)
        br.find_element_by_id("J_post_sub").click()
        time.sleep(5)
        br.find_element_by_link_text(u"首页").click()





    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(FaTie("testFaTie"))
    runner = unittest.TextTestRunner()
    runner.run(suite)