# encoding:utf-8

import cx_Oracle,ResultLog
def ora(q):
    log=ResultLog.resultLog()
    con = cx_Oracle.connect( "yydscs01", "cs_123","192.168.2.102/chinapay")
    cr = con.cursor()
    q=q
    sql="select dd.* from yydscs.ims_news dd where dd.title="+"\'"+q+"\'"
    # print sql
    cr.execute(sql)
    cr.fetchall()
    count=cr.rowcount
    if count>0:
        log.info("通过数据库验证产品发布成功,一共有%d条数据" %count)
    con.close()