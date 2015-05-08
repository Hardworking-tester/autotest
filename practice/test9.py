# encoding:utf-8
from selenium import webdriver
import xlrd


excel_path='E:\\data\\username_password_data.xls'
data=xlrd.open_workbook(excel_path)
table=data.sheets()[0]
rows=table.nrows
cols=table.ncols
for i in range(rows):
    list1=table.row_values(i)
    print ("第%d次输出" %(i+1))
    for i in list1:

        # if eval(i).get('username'):
            print eval(i)['username']
        # elif eval(i).get('password'):
            print eval(i)['password']
        # print dic
        # if dic.get('username'):
        #     print dic['username']
# br.find_element_by_id("userName").clear()
# br.find_element_by_id("userName").send_keys(k)
# br.find_element_by_id("password").clear()
# br.find_element_by_id("password").send_keys(v)
# br.find_element_by_id("imgLogin").click()
# print br.switch_to_alert().text

# br.switch_to_alert().accept()