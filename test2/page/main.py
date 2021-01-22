'''
首页-进入行情页-点击搜索
'''


from test2.page.base_page import BasePage
from test2.page.market import Market


class Main(BasePage):
    def goto_market(self):
        #..目录代表上一层目录
        self.steps("../page/main.yaml")
        #返回行情页面
        #传参，传self._driver,因为在APP中已经给出定义，app中如果第一次运行driver是空，则app中给出定义，
        return Market(self._driver)
