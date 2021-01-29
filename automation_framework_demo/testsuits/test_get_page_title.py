import unittest


from automation_framework_demo.framework.browser_engine import BrowserEngine


class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserEngine(cls)
        cls.driver.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_page_title(self):
        home = Home