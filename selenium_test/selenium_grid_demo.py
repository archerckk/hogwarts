from time import sleep
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote
import os



class TestSeleniumGridDemo:
    _env = 'clould'

    def setup(self):

        if self._env == 'home':
            self.hub_url = 'http://192.168.163.1:4444/wd/hub'
        elif self._env == 'company':
            self.hub_url = 'http://10.8.8.186:4444/wd/hub'
        elif self._env=='clould':
            self.hub_url= 'http://192.168.24.128:5001/wd/hub'

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
            # capbilities['browser-version']='83'
            # capbilities['visual']='true'
            capbilities['executable_path'] = 'msedgedriver.exe'
            self.driver = Remote(
                command_executor=self.hub_url, desired_capabilities=capbilities)

        elif self.web_browser == 'firefox':
            capbilities = DesiredCapabilities.FIREFOX.copy()
            self.driver = Remote(command_executor=self.hub_url, desired_capabilities=capbilities)

    def teardown(self):
        self.driver.quit()


    def test_demo(self):
        self.driver.get('http://www.baidu.com')
        print(self.driver.title)
        sleep(2)
