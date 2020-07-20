from time import sleep
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote
import os


class TestSeleniumGridDemo:

    def setup(self):
        self.hub_url = 'http://192.168.163.1:4444/wd/hub'
        self.web_browser = os.getenv('browser', None)
        if self.web_browser == 'chrome':
            capbilities = DesiredCapabilities.CHROME.copy()
            self.driver = Remote(command_executor=self.hub_url, desired_capabilities=capbilities)
        elif self.web_browser == 'ie':
            capbilities = DesiredCapabilities.INTERNETEXPLORER.copy()
            self.driver = Remote(command_executor=self.hub_url, desired_capabilities=capbilities)
        elif self.web_browser == 'edge':
            capbilities = DesiredCapabilities.EDGE.copy()
            # capbilities['platform']='WIN10'
            capbilities['browser-version']='84'
            capbilities['executable_path']='msedgedriver.exe'
            # capbilities['visual']='true'
            self.driver = Remote(
                command_executor=self.hub_url, desired_capabilities=capbilities)

    def teardown(self):
        self.driver.quit()


    def test_demo(self):
        self.driver.get('http://www.baidu.com')
        sleep(2)
