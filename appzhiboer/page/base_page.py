'''
存放driver初始化；存放最基本方法
'''
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver=None):
        self.driver = driver

    def find(self,by,locator):
        return self.driver.find_element(by,locator)

