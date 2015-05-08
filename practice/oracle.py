#encoding:utf-8
import cx_Oracle
con = cx_Oracle.connect( "yydscs01", "cs_123","192.168.2.102/chinapay")
cr = con.cursor()
c=10
m=str(c)
print m
sql="update yydscs.PSM_CUST_FUND set FUNDMONEY="+"'"+m+"'"+"where CUSTEMAIL='wwg874562@163.com'"
cr.execute(sql)
con.commit()
# rs=cr.fetchall()
# a=cr.rowcount
# print a
cr.close()
con.close()