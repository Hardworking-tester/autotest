#encoding:utf-8
from selenium import webdriver
class Browser():
    def init_browser(self):

        """
        该函数主要是初始化浏览器对象并返回一个webdriver对象
        """
        br=webdriver.Firefox()
        br.get("http://www.xebest.com:8000")
        return br

