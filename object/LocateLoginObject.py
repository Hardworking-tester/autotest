#encoding:utf-8
import os
import sys,xlrd
from Action import Browser
from Action import Login
from Data import ReadExcel
# from Action import DataOperate
from Action import Browser
from selenium.webdriver.common.by import By
class LocateLoginObject():
    def locateObject(self,browser,object_username,object_password,object_name):
        br=browser
        username=object_username
        password=object_password
        locate_element=object_name

        login_class2=Login.Login()#实例化Login类
        readexcel_class2=ReadExcel.ReadExcel()
        objectname_locatemethod_locatedata_excelpath="F:\\pytest\\testauto\\Data\\objectname_locatemethod_locatedata.xls"
        objectname_locatemethod_locatedata_sheet=readexcel_class2.getTable(objectname_locatemethod_locatedata_excelpath)#得到excel操作实体
        objectname_locatemethod_locatedata_sheet_rows=readexcel_class2.getExcelRows(objectname_locatemethod_locatedata_excelpath)#得到excel总行数
        #定义一个字典去映射excel表中的元素定位方式
        dic1={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        #循环excel中的每一行，判断定位方式是id、css、xpath，每一行是一个界面元素
        for i in range(objectname_locatemethod_locatedata_sheet_rows):
            list3=objectname_locatemethod_locatedata_sheet.row_values(i)
            if list3[0]==locate_element:
                #在该行中，如果定位方式是id，就使用id定位方式
                if list3[1]=='id':
                    element=br.find_element(by=dic1['id'],value=list3[2])
                    login_class2.operate_element(br,username,password,locate_element,element)
                #在该行中，如果定位方式是css，就使用css定位方式
                elif list3[1]=='css':
                    element=br.find_element(by=dic1['css'],value=list3[2])
                    login_class2.operate_element(br,username,password,locate_element,element)
                #在该行中，如果定位方式是xpath，就使用xpath定位方式
                elif list3[1]=='xpath':
                    element=br.find_element(by=dic1['xpath'],value=list3[2])
                    login_class2.operate_element(br,username,password,locate_element,element)
                elif list3[1]=='linktext':
                    element=br.find_element(by=dic1['linktext'],value=list3[2])
                    login_class2.operate_element(br,username,password,locate_element,element)
