# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "127.0.0.1:5555"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["noReset"] = "True"
caps["ensureWebviewsHavePages"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[6]")
el1.click()

driver.quit()