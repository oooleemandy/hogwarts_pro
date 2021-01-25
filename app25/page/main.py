import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from app25.page.base_page import BasePage


class Main(BasePage):
    '''搜索方法,点击搜索'''

    def goto_search(self):
        self.steps("../page/main.yaml")
        return

    '''编辑方法，点击笔的图标'''

    def goto_windows(self):
        self.find(By.ID, "post_status").click()
        self.find(By.ID, 'tv_search').click()
