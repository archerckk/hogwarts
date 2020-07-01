from page_object_appium.pages.app import App


class TestSearch:

    def test_search_input(self):
        App().start().main().goto_market().goto_search().search('jd')
