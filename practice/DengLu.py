# encoding:utf-8
"""
该类主要作为测试登录功能的类，通过从excel中读取登录数据，再通过判断把测试结果写入excel中
"""
import time
import unittest

from selenium import webdriver
import xlrd
from xlutils.copy import copy


class Denglu(unittest.TestCase):


    testid=001

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.baseurl="http://localhost:8000/phpwind85"
    def getExcel(self,excelfile):
        """
        该函数主要是获取需要读取数据的excel，如果找到就返回该excel，如果找不到给出提示信息
        """
        try:
            data=xlrd.open_workbook(excelfile)#获取通过excel路径工作表
            table=data.sheets()[0]#制定需要操作的excel的sheet
            return table#返回需要操作的excel的sheet
        except:
            return False
    def getRows(self):
        """
        该方法主要是得到要读取数据的excel的行
        """
        table=self.getExcel("E:\\wwg\\dengludata.xls")
        if table:
            rows=table.nrows
            print "该文档的有%i行" %rows
            return rows
        else:
            print("该excel文档不存在")
    def getCols(self):
        """
        该方法主要是得到要读取数据的excel的列
        """
        table=self.getExcel("E:\\wwg\\dengludata.xls")
        if table:
            cols=table.ncols
            return cols
        else:
            print("该excel文档不存在")
    def getLoginDict(self):
        """
        该方法主要是得到从excel读取的数据并整合成列表
        """
        table=self.getExcel("E:\\wwg\\dengludata.xls")#向getExcel方法传递一个excel的路径的参数
        logindict={}#定义一个字典
        rows=self.getRows()#获取该excel一共有多少行
        cols=self.getCols()#获取该excel一共有多少列
        for i in range(1,rows):
            for m in range(cols-1):
                logindict[table.cell(i,m).value]=table.cell(i,i).value#使用字典的赋值方法，把用户名和密码作为key和value对应赋值
        return list(logindict.items())#把得到的有用户名和密码的字典转换为列表并返回
    def testLoginin(self):
        """
        该方法主要是进行登录操作
        """
        resultlist=[]#定义一个测试结果的列表
        ppp=u"登录成功"
        faile=u"登录失败"
        br=self.driver
        br.get(self.baseurl)
        loginlist=self.getLoginDict()#通过调用方法，得到用户名和密码的列表
        br.find_element_by_link_text(u"登录").click()
        for k,v in loginlist:#遍历上面步骤得到的用户名和密码的列表
            br.find_element_by_id("J_u_login_username").send_keys(k)#传递用户名
            br.find_element_by_id("J_u_login_password").send_keys(v)#传递密码
        br.find_element_by_xpath("//*[@id='J_u_login_form']/div/dl[4]/dd/button").click()
        time.sleep(10)
        if br.current_url=="http://localhost:8000/phpwind85/":
            resultlist.append(self.testid)
            resultlist.append(ppp)#向测试结果列表中增加值
            resultlist.append(br.current_url)
            self.writeData(resultlist)#调用writeData方法往excel中输入测试结果
        else:
            print(faile)
            resultlist.append(faile)
            self.writeData(resultlist)
    def writeData(self,result):
        rb=xlrd.open_workbook("E:\\wwg\\qqq.xls")
        wb=copy(rb)
        wbk=wb.get_sheet(0)
        for i in range(len(result)):
            wbk.write(1,i,result[i])
        wb.save("E:\\wwg\\qqq.xls")

    def tearDown(self):
        br=self.driver
        br.quit()

if __name__=="__main__":
    unittest.main()