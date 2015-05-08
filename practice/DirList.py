#encoding:utf-8
import os
import time
for pp in os.listdir("E:\\wwg"):
    #print pp.decode('gbk')
    if pp.decode('gbk')==u"软件性能测试从这里开始.pdf":
        print "文件已找到"
        print "文件大小为:",os.stat(u"E:\\wwg\\51CTO下载-精通qtp+自动化测试技术领航.pdf").st_size
        break
    else:
        print("文件未找到")
# qq=os.stat("E:\\wwg\\ZenTaoPMS.5.2.1.exe")
# print qq.st_size/1024
# print time.strftime("%c",time.localtime(qq.st_ctime))
# print time.time()
# now=time.localtime(time.time())
# print time.strftime("%y/%m/%d %H:%M",now)
# print time.strftime("%a %b %d",now)
# print time.strftime("%c",now)