from test2.testcase.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("alibaba")