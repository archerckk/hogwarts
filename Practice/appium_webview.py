from time import sleep

from appium import webdriver


class TestWebview():

    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'com.example.android.apis',
            'appActivity': 'com.example.android.apis.ApiDemos',
            'deviceName': 'emulator-5554',
            'noReset': 'true',
            'chromedriverExecutable': 'J:\Python\chromedriver_2.19.exe'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardwon(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_xpath('//*[@text="Views"]').click()
        webview = 'Webview'
        print(self.driver.contexts)
        scorll_text = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).' \
                      'scrollIntoView(new UiSelector().text("WebView").instance(0));'
        self.driver.find_element_by_android_uiautomator(scorll_text).click()
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        print('现在的上下文为：',self.driver.current_context)
        self.driver.find_element_by_xpath('//*[@href="x"]').click()
        print(self.driver.page_source)
        sleep(3)