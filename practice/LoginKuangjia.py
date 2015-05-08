# encoding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import xlrd,time
class LoginUpdate():
    def getAndOperateData(self):
        browser=webdriver.Firefox()
        browser.get("http://www.xebest.com:8000")
        object_excel=xlrd.open_workbook(r"E:\data\objectname_locatemethod_locatedata.xls")
        object_sheet=object_excel.sheets()[0]
        object_sheet_rows=object_sheet.nrows
        object_sheet_cols=object_sheet.ncols
        object_name_list=[]#定义一个存放登录功能中需要定位的对象名称的空列表
        for i in range(object_sheet_rows):#拿到登录功能中需要定位的对象名称列表
            object_name_list.append(object_sheet.cell(i,0).value)
        object_name_list.pop(0)#去掉对象名excel中的第一行的标签项名称
        print object_name_list

        username_password_list=[]
        senddata_excel=xlrd.open_workbook(r"E:\data\username_password.xls")
        senddata_sheet=senddata_excel.sheets()[0]
        senddata_sheet_rows=senddata_sheet.nrows
        senddata_sheet_cols=senddata_sheet.ncols
        for i in range(1,senddata_sheet_rows):
            username_password_list.append(senddata_sheet.row_values(i))
        print username_password_list


        for username,password in username_password_list:
            for m in range(object_name_list.__len__()):
                self.locateObject(browser,username,password,object_name_list[m])
            browser.switch_to_alert().accept()


    def locateObject(self,browser,object_username,object_password,object_name):
        br=browser
        username=object_username
        password=object_password
        locate_element=object_name


        excel_path="E:\\data\\objectname_locatemethod_locatedata.xls"
        object_excel=xlrd.open_workbook(excel_path)
        objectname_locatemethod_locatedata_sheet=object_excel.sheets()[0]
        objectname_locatemethod_locatedata_sheet_rows=objectname_locatemethod_locatedata_sheet.nrows
        objectname_locatemethod_locatedata_sheet_cols=objectname_locatemethod_locatedata_sheet.ncols
        #定义一个字典去映射excel表中的元素定位方式
        dic1={'id':By.ID,'css':By.CSS_SELECTOR,'xpath':By.XPATH,'linktext':By.LINK_TEXT}
        #循环excel中的每一行，判断定位方式是id、css、xpath，每一行是一个界面元素
        for i in range(objectname_locatemethod_locatedata_sheet_rows):
            list3=objectname_locatemethod_locatedata_sheet.row_values(i)
            if list3[0]==locate_element:
                #在该行中，如果定位方式是id，就使用id定位方式
                if list3[1]=='id':
                    element1=br.find_element(by=dic1['id'],value=list3[2])
                    self.operateElement(br,username,password,locate_element,element1)
                #在该行中，如果定位方式是css，就使用css定位方式
                elif list3[1]=='css':
                    element1=br.find_element(by=dic1['css'],value=list3[2])
                    self.operateElement(br,username,password,locate_element,element1)
                #在该行中，如果定位方式是xpath，就使用xpath定位方式
                elif list3[1]=='xpath':
                    element1=br.find_element(by=dic1['xpath'],value=list3[2])
                    self.operateElement(br,username,password,locate_element,element1)
                elif list3[1]=='linktext':
                    element1=br.find_element(by=dic1['linktext'],value=list3[2])
                    self.operateElement(br,username,password,locate_element,element1)


    def operateElement(self,br,username,password,locate_element,element):
        obj=locate_element
        username_send=username
        password_send=password
        excel_path="E:\\data\\operate_method.xls"
        operate_method_excel=xlrd.open_workbook(excel_path)
        operate_method_sheet=operate_method_excel.sheets()[0]
        operate_method_sheet_rows=operate_method_sheet.nrows
        operate_method_sheet_cols=operate_method_sheet.ncols
        objectname_list=operate_method_sheet.col_values(0)
        if obj in objectname_list:
            for i in range(operate_method_sheet_rows):
                if objectname_list[i]==obj:
                    operatemethod_list=operate_method_sheet.row_values(i)
                    if operatemethod_list[1]=='sendkey' and obj=='username':
                        element.clear()
                        element.send_keys(username_send)
                        time.sleep(5)
                    elif operatemethod_list[1]=='sendkey' and obj=='password':
                        element.clear()
                        element.send_keys(password_send)
                        time.sleep(5)
                    elif operatemethod_list[1]=='click':
                        element.click()
                        time.sleep(10)
        else:
            print("该元素没有在caozuo.xls文件中")








pp=LoginUpdate()
pp.getAndOperateData()