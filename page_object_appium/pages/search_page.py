from page_object_appium.pages.base_page import BasePage


class Search(BasePage):

    def search(self, value):
        self._parames['value'] = value
        self._steps('../pages/search.yml')
