'''搜索页面'''

from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from appzhiboer.page.base_page import BasePage


class SearchResult(BasePage):
    def searchmember(self, name):
        '''
        输入名字，搜索成员，点开成员，进入个人信息页面
        :return:
        '''
        self.driver.find_element_by_id("gwt").send_keys(name)
        sleep(2)
        eles = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        beforenum = len(eles)
        print(beforenum)
        if beforenum < 2:
            print("没有可删除成员")
            return
        # eles[1].click()
        self.driver.find_element_by_id("dsm").click()
        from appzhiboer.page.personal_info import PersonalInfo
        return PersonalInfo(self.driver)

    '''获取afternum'''
    def afternum(self, name):
        sleep(3)
        eles1 = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        afternum = len(eles1)
        return afternum