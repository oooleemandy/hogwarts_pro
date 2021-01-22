from appium import webdriver

from test2.page.base_page import BasePage
from test2.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        #判断self.driver是否等于none
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:5555"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrantPerissions"] = True
            #webdriver初始化
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        #如果driver有就不重启，简单打印一下
        else:
            self._driver.start_activity(_package, _activity)

        return self


    def main(self):
        #main中传入self._driver是命中start方法中的复用规则，不用每次从0创建selfdriver
        return Main(self._driver)
