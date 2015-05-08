#encoding:utf-8
import unittest

listdir="F:\\test\\testauto\\qqq"
def createsuit():
    testunit=unittest.TestSuite()
    disvover=unittest.defaultTestLoader.discover(listdir,pattern='start_*.py',top_level_dir=None)
    for test_suite in disvover:
        print test_suite
        print "上面是第一次打印--------------------------------"
        for test_case in test_suite:
            print test_case
            print "上面是第二次打印----------------------------"
            testunit.addTest(test_case)
            print testunit
            print "上面是第三次打印"
    return testunit

alltestnames=createsuit()
# now=time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
# filename="F:\\pytest\\"+now+'result.html'
# fp=file(filename,'wb')
# runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"用例执行情况：")
# runner.run(alltestnames)