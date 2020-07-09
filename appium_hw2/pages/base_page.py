from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def _find(self, by, locator=None):
        element = WebDriverWait(self._driver, 15).until(expected_conditions.presence_of_element_located(by)) if \
            isinstance(locator, tuple) else WebDriverWait(self._driver, 15).until(
            expected_conditions.presence_of_element_located((by, locator)))

        return element

    def _finds(self, by, locator=None):
        elements = WebDriverWait(self._driver, 15).until(expected_conditions.presence_of_all_elements_located(by)) if \
            isinstance(locator, tuple) else WebDriverWait(self._driver, 15).until(
            expected_conditions.presence_of_all_elements_located((by, locator)))

        return elements

    def confirm_element_disappear(self, by, locator=None):
        element = WebDriverWait(self._driver, 15).until_not(expected_conditions.presence_of_element_located(by)) if \
            isinstance(locator, tuple) else WebDriverWait(self._driver, 15).until_not(
            expected_conditions.presence_of_element_located((by, locator)))
        return element

    def back(self, num=1):
        for i in range(num):
            self._driver.back()

    def scroll_find(self, text):
        element = self._driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true).'
            f'instance(0)).scrollIntoView(new UiSelector().text("{text}").'
            f'instance(0));')
        return element

    def _find_and_click(self, *locator):
        self._find(*locator).click()

    def get_toast(self):
        return self._find(By.XPATH, '//*[@class="android.widget.Toast"]').text
