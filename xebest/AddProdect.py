# encoding:utf-8

from selenium import webdriver
import unittest,time
import Login,cx_Oracle
import ResultLog,oracle
import ResultLog

class AddProdect(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.baseurl="http://www.xebest.com:8000"
        self.tit='自动化'

    def testAddProdect(self):
        br=Login.login(self.driver,self.baseurl)
        log=ResultLog.resultLog()
        br.maximize_window()
        time.sleep(5)
        # m="我的会员中心".decode("utf-8")
        #br.find_element_by_xpath("//div[@class='mod-login']/div[3]/div[2]/a[contains(text(),m)]").click()
        #br.find_element_by_link_text(u"我的会员中心").click()
        br.find_element_by_css_selector("a.red").click()
        time.sleep(5)
        br.switch_to_window(br.window_handles[1])
        br.find_element_by_link_text(u"我是供应商").click()
        time.sleep(3)
        br.find_element_by_link_text(u"产品管理").click()
        br.find_element_by_link_text(u"发布信息").click()
        br.find_element_by_id("userItem").click()#网站栏目选择
        br.find_element_by_link_text(u"供应信息").click()
        br.find_element_by_css_selector("button.btn.selectOk").click()
        br.find_element_by_id("newsItem").click()#产品类别选择
        time.sleep(5)
        br.find_element_by_css_selector("a[Data-id='1000001008']").click()
        time.sleep(2)
        br.find_element_by_css_selector("a[Data-id='1000001008001']").click()
        time.sleep(2)
        br.find_element_by_css_selector("a[Data-id='1000001008001001']").click()
        time.sleep(2)
        br.find_element_by_xpath("//*[@id='seeNewsItemsBody']/div[3]/button").click()#产品类别选择对话框的确定按钮
        br.find_element_by_id("infoTitle").send_keys(self.tit.decode("utf-8"))#产品标题
        br.find_element_by_id("infoFlag").send_keys("wwg")#关键词
        br.find_element_by_id("proBrandName").find_element_by_css_selector("option[value=\"生鸡蛋\"]").click()#品牌名称
        br.find_element_by_id("proStandard").send_keys("wwg")#规格
        br.find_element_by_id("proCompany").send_keys("wwg")#生产厂家
        js1="$(\"input[Data-provide='datetimepicker'    ]\").removeAttr('readonly');$(\"input[Data-provide='datetimepicker']\").attr('value','2014-08-09')"
        br.execute_script(js1)#生产日期
        br.find_element_by_id("infoPrice").send_keys("1")#批发价
        br.find_element_by_id("pricelast").send_keys("1")#零售价
        br.find_element_by_id("infoCon").send_keys("2222")#供应量
        br.find_element_by_id("proMinNum").send_keys("1")#最小起订量
        br.find_element_by_id("province").find_element_by_css_selector("option[value=\"10008\"]").click()
        br.find_element_by_id("city").find_element_by_css_selector("option[value=\"10009\"]").click()#发货地
        br.find_element_by_id("proDaysLimit").send_keys("1")#发货期限
        br.find_element_by_xpath("//*[@id='img_list']/p[1]/a/img").click()
        time.sleep(3)
        br.find_element_by_xpath("//*[@id='tabNavi']/ul/li[2]").click()
        br.find_element_by_id("imgFile").send_keys("E:\\wwg\\xampp\\php\\php.gif")
        time.sleep(2)
        br.find_element_by_id("upToServer").click()#图片
        br.find_element_by_id("infoBrief").send_keys("wwg")#产品简介
        content="wwg"
        #js2="document.getElementsByClassName(\"ke-iframe\")[0].contentWindow.document.body.innerHTML=\"%s\" " %(u"是打发士大夫士大夫是地方")
        js2="KE.text('infoContent','123wwg')"
        br.execute_script(js2)#产品详情
        js3="document.getElementsByClassName(\"ke-iframe\")[1].contentWindow.document.body.innerHTML=\"%s\"" %(content)
        br.execute_script(js3)#配送说明
        time.sleep(10)
        br.find_element_by_id("saveBtn").click()
        time.sleep(8)
        br.find_element_by_link_text(u"身份认证").click()
        br.find_element_by_link_text(u"产品管理").click()
        br.find_element_by_link_text(u"信息管理").click()
        time.sleep(5)
        #调用数据库查询验证产品发布是否成功
        oracle.ora(self.tit.decode("utf-8").encode("gbk"))
        #通过页面元素判断产品发布是否成功
        try:
            product=br.find_element_by_link_text("safdfsdfsdfsdfsdfdsf").is_displayed()
            if product:
                log.info("通过界面验证产品:%s发布成功" %self.tit)
            else:
                log.info("通过界面验证产品:%s没有发布成功" %self.tit)
        except:
            log.info("没有找到此元素")











    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(AddProdect("testAddProdect"))
    runner = unittest.TextTestRunner()
    runner.run(suite)