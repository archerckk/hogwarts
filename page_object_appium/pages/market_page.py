from page_object_appium.pages.base_page import BasePage
from page_object_appium.pages.search_page import Search


class Market(BasePage):
    _path = "../pages/market.yml"

    def goto_search(self):
        self._steps(self._step['search'])
        return Search(self._driver)
