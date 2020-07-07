from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, *locator):
        return WebDriverWait(self._driver, 15).until(expected_conditions.element_to_be_clickable(
            self._driver.find_element(*locator)))

    def back(self, num=1):
        for i in range(num):
            self._driver.back()

    def scroll_find(self, text):
        element = self._driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).'
            f'instance(0)).scrollIntoView(new UiSelector().text("{text}").'
            f'instance(0));')
        return element

    def find_and_click(self, *locator):
        self.find(*locator).click()

    def get_toast(self):
        return self.find(By.XPATH, '//*[@class="android.widget.Toast"]').text
