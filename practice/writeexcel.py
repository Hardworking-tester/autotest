#encoding:utf-8
import xlwt
book=xlwt.Workbook()
sheet1=book.add_sheet('hello')
# sheet2=book.add_sheet('word')
# sheet1.write(0,0,'hello')
# sheet1.write(0,1,'world')
sheet1.write(0,1,'woca')



book.save('E:\\wwg\\write.xls')