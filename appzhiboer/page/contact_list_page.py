'''
通讯录页面
'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from appzhiboer.page.base_page import BasePage
from appzhiboer.page.member_invite_page import MemberInviteMenuPage
from appzhiboer.page.searchresult import SearchResult


class ContactListPage(BasePage):

    def addmember(self):
        '''
        添加成员
        :return:
        '''
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return MemberInviteMenuPage(self.driver)

    def search_button(self):
        '''
        点击搜索按钮,进入搜索页面
        :return:
        '''
        self.driver.find_element_by_id("ie_").click()
        return SearchResult(self.driver)

