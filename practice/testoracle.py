#encoding:utf-8
import cx_Oracle
con = cx_Oracle.connect( "yydscs01", "cs_123","192.168.2.102/chinapay")
cr = con.cursor()
m="自动化2014-09-6".decode('utf-8').encode('gbk')
sql="select dd.* from yydscs.ims_news dd where dd.title like"+"'"+m+"'"
cr.execute(sql)
rs=cr.fetchall()
# a=cr.rowcount
# print a
for x in rs:
    print x
cr.close()
con.close()






