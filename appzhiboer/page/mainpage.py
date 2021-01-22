'''
主页
'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from appzhiboer.page.base_page import BasePage
from appzhiboer.page.contact_list_page import ContactListPage


class MainPage(BasePage):



    def goto_contactlist(self):
        '''
        进入到通讯录
        :return:
        '''
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()

        return ContactListPage(self.driver)