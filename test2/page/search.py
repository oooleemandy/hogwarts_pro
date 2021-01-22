from test2.page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        #定义命中规则，value在basepage中的value，命中yaml里的value
        self._params["value"] = value
        self.steps("../page/search.yaml")
