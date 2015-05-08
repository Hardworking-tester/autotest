#encoding:utf-8
import xlrd
from selenium import webdriver
import os
from xlrd import open_workbook

a=xlrd.biffh
data=open_workbook("E:\\wwg\\test.xls")
table=data.sheets()[0]
rows=table.nrows
cols=table.ncols
# print(rows)
for p in range(rows):
    print(table.row_values(p))
# for m in range(cols):
#     print ((table.col_values(m))[0])



# for i in range(0,rows):
#     for m in range(0,cols):
#         if table.cell(0,1).value=="age":
#             print(table.cell(i,m).value)
#         i+=1


