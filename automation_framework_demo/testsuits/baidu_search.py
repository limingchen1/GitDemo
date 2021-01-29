import time
import unittest

from automation_framework_demo.framework.browser_engine import BrowserEngine
from automation_framework_demo.pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        准备驱动，打开页面
        :return:
        '''
        browser = BrowserEngine()
        self.driver = browser.open_browser(self)

    @classmethod
    def tearDownClass(self):
        '''
        测试完成，关闭浏览器
        :return:
        '''
        self.driver.quit()

    def test_baidu_search(self):

        homepage = HomePage(self.driver)
        homepage.type_search('hao123')
        homepage.send_submit_btn()
        homepage.get_windows_img()
        try:
            assert 'sel1enium' in self.driver.title
            print('测试通过')
        except Exception as e:
            print('测试不通过', format(e))

    def test_baidu_search1(self):

        homepage = HomePage(self.driver)
        homepage.type_search('selenium')
        homepage.send_submit_btn()
        homepage.get_windows_img()
        time.sleep(2)
        try:
            assert 'selenium' in HomePage.get_page_title(self)
            print('测试通过')
        except Exception as e:
            print('测试不通过', format(e))

    def test_baidu_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')
        homepage.send_submit_btn()
        homepage.get_windows_img()
        time.sleep(2)
        try:
            assert "python" in HomePage.get_page_title(self)
            print('测试通过')
        except Exception as e:
            print('测试不通过')




if __name__ == '__main__':
    unittest.main()











