from time import sleep
from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestDW():
  def setup(self):
    desire_cap = {
      "platformName": "android",
      "deviceName": "127.0.0.1:5555",
      "appPackage": "com.xueqiu.android",
      "appActivity": ".view.WelcomeActivityAlias",
      "noReset": True,
      "unicodeKeyBoard": True,
      "resetKeyBoard": True
    }
    self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
    self.driver.implicitly_wait(5)

  def teardown(self):
    '''增加取消操作'''
    self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
    self.driver.quit()

  def test_search(self):
    '''
    搜索中文阿里巴巴，点击第一个阿里巴巴,获取这只阿里巴巴的股价，判断这只股价价格大于200
    :return:
    '''
    self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")


  def test_attr(self):
    '''
    定位首页搜索框
    判断搜索框是否可用并且查看name属性并且打印左上角坐标 它的宽和高
    如果搜索框可用，则进行点击
    判断阿里巴巴是否可见
    :return:
    '''
    element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    search_enabled = element.is_enabled()
    print(element.text)
    print(element.location)
    print(element.size)

    if search_enabled ==True:
      element.click()
      self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
      alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text ='阿里巴巴']")
      print(alibaba_element.get_attribute("displayed"))



  def test_touchaction(self):
    '''定义touchaction，传入driver'''
    action = TouchAction(self.driver)
    '''获取当前屏幕尺寸'''
    window_rect = self.driver.get_window_rect()
    width = window_rect['width']
    height = window_rect['height']

    '''
    按下x的中心点坐标
    按下某个点并进行滑动,再调用release方法释放掉，并且调用perform方法执行
    '''
    x1 = int(width/2)
    y_start = int(height*4/5)
    y_end = int(height*1/5)
    action.press(x = x1, y = y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

  def test_getcurrentprice(self):
    self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
    self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text ='阿里巴巴']").click()
    current_price = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
    print(current_price)



  def test_wait(self):
    self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
    self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text ='阿里巴巴']").click()

    locator = (MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
    #判断元素是否是可点击的
    WebDriverWait(self.driver ,10).until(expected_conditions.element_to_be_clickable(locator))
    ele = self.driver.find_element(*locator)

  def test_get_attr(self):
    search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    print(search_ele.get_attribute("content-desc"))
    print(search_ele.get_attribute("resource-id"))
    print(search_ele.get_attribute("enabled"))
    print(search_ele.get_attribute("clickable"))
    print(search_ele.get_attribute("bounds"))



  '''
  打开雪球，搜索阿里巴巴，或小米，或搜索其他股票。点击第一个搜索结果，根据股票代号查看股票价格。
  希望实际价格比期望价格上下浮动0.1
  '''
  @pytest.mark.parametrize('searchkey,type,expect_price', [
    ('alibaba','BABA',243),
    ('xiaomi','01810',31)
  ])
  def test_search(self,searchkey, type, expect_price):
    self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
    self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
    element_price = self.driver.find_element_by_xpath(f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
    current_price = float(element_price.text)
    print(f"当前价格为{current_price}")
    assert_that(current_price,close_to(expect_price,expect_price*0.1))


