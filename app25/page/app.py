from appium import webdriver

from app25.page.base_page import BasePage
from app25.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        # 判断self.driver是否等于none
        if self._driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:5555"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["autoGrantPerissions"] = True
            # webdriver初始化
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(5)
        # 如果driver有就不重启，简单打印一下
        else:
            self._driver.start_activity(self._package, self._activity)
        # 返回自身
        return self

    def main(self) -> Main:
        return Main(self._driver)
