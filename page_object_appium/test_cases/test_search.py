from page_object_appium.pages.app import App


class TestSearch:
    def setup(self):
        self.app = App().start()

    def teardown(self):
        self.app.close()

    def test_search_input(self):
        self.app.main().goto_market().goto_search().search('jd')
