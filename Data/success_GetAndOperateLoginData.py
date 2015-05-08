# encoding:utf-8
from selenium import webdriver
import xlrd,time
from object import LocateLoginObject
from Action import Login,Browser
from Data import ReadExcel
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
class GetAndOperateLoginData(unittest.TestCase):

    def instance_List(self):
        locate_login_object_class=LocateLoginObject.LocateLoginObject()#实例化定位登录模块所有元素的类
        login_class1=Login.Login()#实例化登录操作的类
        browser=Browser.Browser().init_browser()#获取webdriver对象
        instance_list=[locate_login_object_class,login_class1,browser]
        return  instance_list



    def testGetAndOperateData(self):
        u"""登录功能测试"""

        """
        此方法作用：
            1、获得excel中存储的用户名和密码，每一行对应的用户名和密码作为一个小列表，所有的小列表组成一个大列表
            2、将用户名和密码作为外层for循环，将需要定位的元素的名称的列表作为内层循环，拿到一个需要定位的元素的名称就去定位并进行sendkey或者click操作
        """
        class_list=self.instance_List()

        #拿到登录功能中需要定位的对象名称列表
        object_name_list=self.getObjList()
        #拿到存储在excel中存储的用户名和密码列表对
        username_password_list=self.getUsernameAndPasswordList()
        for username,password in username_password_list:
            for m in range(object_name_list.__len__()):
                class_list[0].locateObject(class_list[2],username,password,object_name_list[m])
            class_list[1].operate_alert(class_list[2])

    def getObjList(self):
        readexcel_class1=ReadExcel.ReadExcel()#实例化读取excel的类
        object_excelpath="F:\\pytest\\testauto\\Data\\objectname_locatemethod_locatedata.xls"
        object_sheet=readexcel_class1.getTable(object_excelpath)
        object_sheet_rows=object_sheet.nrows
        object_name_list=[]#得到需要定位的元素的名称的列表
        for i in range(object_sheet_rows):#拿到登录功能中需要定位的对象名称列表
            object_name_list.append(object_sheet.cell(i,0).value)
        object_name_list.pop(0)#去掉对象名excel中的第一行的标签项名称
        return object_name_list


    def getUsernameAndPasswordList(self):
        readexcel_class1=ReadExcel.ReadExcel()#实例化读取excel的类
        senddata_excelpath="F:\\pytest\\testauto\\Data\\username_password.xls"
        senddata_sheet=readexcel_class1.getTable(senddata_excelpath)
        senddata_sheet_rows=senddata_sheet.nrows
        username_password_list=[]
        for i in range(1,senddata_sheet_rows):
            username_password_list.append(senddata_sheet.row_values(i))#拿到存储在excel中存储的用户名和密码列表对
        return username_password_list



# pp=GetAndOperateLoginData()
# pp.getAndOperateData()