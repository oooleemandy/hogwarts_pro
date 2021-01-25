import pytest
import yaml

from app25.page.app import App
from app25.testcase.test_base import TestBase


class TestMain(TestBase):
    @pytest.mark.parametrize("value1,value2", yaml.safe_load(open("./test_case.yaml")))
    def test_main(self, value1, value2):
        self.app.start().main().goto_search()

    def test_windows(self):
        self.app.start().main().goto_search()
