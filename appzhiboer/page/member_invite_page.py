from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from appzhiboer.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):


    def add_member_manul(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from appzhiboer.page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)


    '''获取toast，添加成功'''
    def verify_toast(self):
        result = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

        return result