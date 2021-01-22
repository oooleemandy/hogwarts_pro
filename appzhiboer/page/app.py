'''
app.py 存放app相关操作
'''
from appium import webdriver

from appzhiboer.page.base_page import BasePage
from appzhiboer.page.mainpage import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:5555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "True"
            caps["ensureWebviewsHavePages"] = True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
            #return self：当前类的实例。return self可以继续调用这个类里的方法

        else:
            #复用driver。启动app，启动页面是desirecaps里面设置的activity
            self.driver.launch_app()

        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

        pass

    def goto_main(self):
        #进入到主页
        return MainPage(self.driver)