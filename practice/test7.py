#encoding:utf-8
import xlrd
data=xlrd.open_workbook("E:\\wwg\\dengludata.xls")
table=data.sheets()[0]
rows=table.nrows
cols=table.ncols
list_count=[]
for i in range (rows):
    list="list"+str(i+1)
    list_count.append(list)
# print list_count
for p in range(rows):
    list_count[p]=table.row_values(p)

print list_count[1]
# for m in range(list_count.__len__()):
#     print list_count[m]
   # print (("list"+str(i))=table.row_values(i))



