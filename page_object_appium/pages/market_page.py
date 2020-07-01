from page_object_appium.pages.base_page import BasePage
from page_object_appium.pages.search_page import Search


class Market(BasePage):

    def goto_search(self):
        self._steps("../pages/market.yml")
        return Search(self._driver)
