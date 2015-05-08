#encoding:utf-8
from selenium import webdriver
import xlrd
data=xlrd.open_workbook("E:\\wwg\\dengludata.xls")
table=data.sheet_by_name('first')
rows=table.nrows
cols=table.ncols
print rows,cols