'''个人信息页面'''
from time import sleep

from appzhiboer.page.base_page import BasePage
from appzhiboer.page.personal_info_edit import PersonalInfoEdit


class PersonalInfo(BasePage):
    def clickmore(self):
        '''
        个人信息详细页面，点击编辑成员，进入编辑成员页面
        :return:
        '''
        #点三个点
        self.driver.find_element_by_id("ie0").click()
        sleep(3)
        self.driver.find_element_by_id("bcc").click()
        return PersonalInfoEdit(self.driver)