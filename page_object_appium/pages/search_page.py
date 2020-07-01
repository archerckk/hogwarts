from page_object_appium.pages.base_page import BasePage


class Search(BasePage):
    _path = '../pages/search.yml'

    def search(self, value):
        self._parames['value'] = value
        self._steps(self._step['send_value'])
