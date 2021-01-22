import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    '''黑名单list'''
    _black_list = [(By.ID, "image_cancel")]

    '''记错误次数'''
    _error_count = 0

    '''记错误测试最大值'''
    _error_max = 10

    _params={}


    '''driver传进来的类型是WebDriver类型'''
    def __init__(self,driver:WebDriver = None):
        self._driver = driver


    '''find方法，by：用了什么方法定位，locator：具体定位内容'''
    def find(self,by,locator=None):
        '''解决弹窗问题'''
        try:
            '''*解元祖。三目表达式，如果是元祖就解元祖，不是元祖就是findelement方法'''
            element = self._driver.find_element(*by) if isinstance(by,tuple) else self._driver.find_element(by,locator)
            #错误次数：如果找到了element，错误次数记为0
            self._error_count=0
            return element
        except Exception as e:
            #错误次数：如果没找到元素，错误次数+1
            self._error_count += 1
            #判断:如果错误测试大于等于错误最大值,则抛出异常
            if self._error_count >= self._error_max:
                raise e
            #取出一个值判断black是否在页面中,在的话赋值给element
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                #如果elements长度大于0，则说明有黑名单中元素，则对第一个进行点击
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by,locator)
            raise e

    '''send方法'''
    def send(self, value, by, locator=None):
        try:
            self.find(by,locator).send_keys(value)
            # 错误次数：如果找到了element，错误次数记为0
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            # 判断:如果错误测试大于等于错误最大值,则抛出异常
            if self._error_count >= self._error_max:
                raise e
            # 取出一个值判断black是否在页面中,在的话赋值给element
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                # 如果elements长度大于0，则说明有黑名单中元素，则对第一个进行点击
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            raise e









    '''读取yaml文件'''
    def steps(self,path,):
        #读取yaml文件，并加中文编码
        with open(path, encoding='utf-8') as f:
            #定义steps是一个list，并且list里有好多字典
            steps : list[dict]= yaml.safe_load(f)
            #循环找step
            for step in steps:
                #如果在key值中找到了by，将by和locator传入
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                #找动作
                if "action" in step.keys():
                    #如果是click动作,则调用click方法
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        #取出value值,这个值如果有则替换成params
                        content:str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}"%param, self._params[param])
                        self.send(content, step["by"], step["locator"])