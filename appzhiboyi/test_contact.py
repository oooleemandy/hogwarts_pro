from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:5555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_addcontact(self):
        name = "EE"
        gender = "男"
        phonenum = "13055555555"

        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        #滚动查找方式
        # 滚动查找
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        #按照姓名找必填那栏，是兄弟节点
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        #编辑性别一栏
        self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@text='男']").click()
        if gender =="男":
            sleep(3)
            self.driver.find_element_by_xpath("//*[@text='男']").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='女']").click()

        #填写手机号
        self.driver.find_element_by_xpath("//*[@text='手机号']").send_keys(phonenum)
        #点击保存
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        #判断是否添加成功
        result = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert result == "添加成功"


        '''删除用户'''
    def test_delcontact(self):
        name="EE"
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.driver.find_element_by_id("ie_").click()
        self.driver.find_element_by_id("gwt").send_keys(name)
        sleep(2)
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        beforenum = len(eles)
        print(beforenum)
        if beforenum < 2:
            print("没有可删除成员")
            return
        #eles[1].click()
        self.driver.find_element_by_id("dsm").click()
        self.driver.find_element_by_id("ie0").click()
        self.driver.find_element_by_id("bcc").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("删除成员").instance(0));').click()
        sleep(2)
        self.driver.find_element_by_id("bom").click()
        sleep(2)
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        afternum = len(eles1)
        print(afternum)
        assert afternum == beforenum - 1





