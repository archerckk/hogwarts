from page_object_appium.pages.base_page import BasePage
from page_object_appium.pages.market_page import Market


class Main(BasePage):
    _path = '../pages/main.yml'

    def goto_market(self):
        self._steps(self._step['market'])
        return Market(self._driver)

    def goto_me(self):
        self._steps(self._step['me'])
        return Market(self._driver)
