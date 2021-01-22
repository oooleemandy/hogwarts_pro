from time import sleep


class EditMember:
    def clickdel(self):
        '''
        点击删除成员
        :return:
        '''
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("删除成员").instance(0));').click()
        sleep(2)
        self.driver.find_element_by_id("bom").click()
