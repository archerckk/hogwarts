from page_object_appium.pages.base_page import BasePage
from page_object_appium.pages.market_page import Market


class Main(BasePage):

    def goto_market(self):
        self._steps('../pages/main.yml')
        return Market(self._driver)
