'''
编辑成员信息页面
'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver

from appzhiboer.page.base_page import BasePage


class ContactAddPage(BasePage):


    def edit_contact(self, name, gender, phonenum):
        '''
        编辑成员信息
        :return:
        '''
        self.find(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # 编辑性别一栏
        self.find(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        # 填写手机号
        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        # 点击保存
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from appzhiboer.page.member_invite_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)