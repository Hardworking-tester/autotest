# encoding:utf-8

from selenium import webdriver
import unittest,xlrd
import HTMLTestRunner

class LoginAction(unittest.TestCase):

    def setUp(self):

        self.driver=webdriver.Firefox()
        self.baseurl="http://www.xebest.com:8000"

    def testLogin(self):
        list=self.getExcelRowData()
        br=self.driver
        br.get(self.baseurl)
        br.find_element_by_link_text(u"请登录").click()
        for k,v,m in list:
            br.find_element_by_id("userName").clear()
            br.find_element_by_id("userName").send_keys(k)
            br.find_element_by_id("password").clear()
            br.find_element_by_id("password").send_keys(v)
            br.find_element_by_id("imgLogin").click()
            # print br.switch_to_alert().text
            self.assertEqual(m,br.switch_to_alert().text)
            br.switch_to_alert().accept()


    def getExcel(self):
        """
        读取一个excel文件并返回该表格对象
        """
        data=xlrd.open_workbook("E:\\wwg\\dengludata.xls")
        table=data.sheets()[0]
        return table

    def getExcelRows(self):
        """
        通过获取到的表格对象得到总行数
        """
        table=self.getExcel()
        rows=table.nrows
        return rows

    def getListId(self):
        """
        此方法主要是用于获取一个list标记，比如：list1，list2用于存储excel中每一行的数据
        """
        rows=self.getExcelRows()
        list_count=[]

        for i in range(1,rows):
            list="list"+str(i)
            list_count.append(list)
        # print list_count
        return list_count

    def getExcelRowData(self):
        """
        此方法主要是通过为【list1，list2，list3，list4】这个列表中的每一项赋值,并得到一个嵌套列表
        :return:
        """
        list=self.getListId()
        table=self.getExcel()
        rows=self.getExcelRows()
        for i in range(list.__len__()):
            list[i]=table.row_values(i+1)
        print list
        return list



    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(LoginAction("testLogin"))
    runner = unittest.TextTestRunner()
    runner.run(suite)