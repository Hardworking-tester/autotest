#encoding:utf-8
from selenium import  webdriver
import  os,time
import requests
print requests.head("https://www.python.org").headers['content-type']
# fp=webdriver.FirefoxProfile()
# fp.set_preference("browser.download.folderList",2)#询问下载位置2，桌面0，“下载”目录1
# fp.set_preference("browser.download.manager.showWhenStarting",False)#当一个下载开始时显示下载管理器。true为显示，false为不显示，缺省我true
# fp.set_preference("browser.download.dir", os.getcwd())#上次通过“如何处理这个文件”对话框保存一个文件时所指定的目录
# fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")#指定下载文件格式
print os.getcwd()