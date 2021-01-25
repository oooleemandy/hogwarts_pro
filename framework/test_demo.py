import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def load_data(path):
    with open(path, encoding='utf-8') as f:
        return yaml.load(f)


class TestDemo:
    @pytest.mark.parametrize("'data'", load_data("test_data.yaml")['data'])
    def test_search(self, data):
        for step in load_data("test_data.yaml")['steps']:
            if 'webdriver' in step:
                browser = str(step.get("webdriver").get("browser", " chrome")).lower()
                if browser == 'chrome':
                    driver = webdriver.Chrome()
                elif browser == 'firefox':
                    driver = webdriver.Firefox()
                else:
                    print(f"{driver} 未知浏览器")

            if 'get' in step:
                url = step.get('get')
                driver.get(url)

            if 'find_element' in step:
                by = step.get("find_element")['by']
                locator = step.get("find_element")['value']
                current_element = driver.find_element(by, locator)

            if 'click' in step:
                current_element.click()

            if 'send_keys' in step:
                value = step.get("send_keys")
                current_element.send_keys(value)
