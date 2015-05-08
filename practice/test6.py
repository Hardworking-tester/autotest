#encoding:utf-8
import cx_Oracle
def oracle(q):

    con = cx_Oracle.connect( "yydscs01", "cs_123","192.168.2.102/chinapay")
    cr = con.cursor()
    sql="select dd.* from yydscs.ims_news dd where dd.title='自动发布产品测试2'"
    cr.execute(sql)
    rs=cr.fetchall()
# a=cr.rowcount
# print a
# rs=cr.fetchall()

    for x in rs:
        print x
    con.close()