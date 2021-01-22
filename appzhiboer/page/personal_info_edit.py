'''编辑成员页面'''
from appzhiboer.page.base_page import BasePage


class PersonalInfoEdit(BasePage):
    def clickeditmem(self):
        '''
        编辑成员页面，下滑到删除成员按钮，点击删除成员，弹框，点确定，回到搜索页面
        :return:
        '''
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("删除成员").instance(0));').click()
        self.driver.find_element_by_id("bom").click()
        from appzhiboer.page.searchresult import SearchResult
        return SearchResult(self.driver)
