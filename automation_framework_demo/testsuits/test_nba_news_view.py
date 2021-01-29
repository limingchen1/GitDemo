import unittest
from time import sleep

from automation_framework_demo.framework.browser_engine import BrowserEngine
from automation_framework_demo.pageobjects.baidu_homepage import HomePage
from automation_framework_demo.pageobjects.baidu_news_home import NewsHomePage
from automation_framework_demo.pageobjects.new_sport_home import SportsNewsHomePage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    # def test_view_nba_views(self):
        # 初始化百度首页，并点击新闻链接


        # baiduhome = HomePage(self.driver)
        # baiduhome.click_news()
        # 初始化一个百度新闻主页
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        newshome = NewsHomePage(self.driver)
        newshome.click_sports()
        # 初始化一个体育新闻主页，点击NBA
        sportnewhome = SportsNewsHomePage(self.driver)
        sportnewhome.click_nba_link()
        sportnewhome.get_windows_img()

    def test_view_nba_views1(self):
        # 初始化百度首页，并点击新闻链接
        # baiduhome = HomePage(self.driver)
        # baiduhome.click_news()

        self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()
        print('1')
        sleep(3)
        # 初始化一个百度新闻主页对象，点击体育
        # newshome = NewsHomePage(self.driver)
        # newshome.click_sports()

        # 获取当前句柄
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="channel-all"]/div/ul/li[7]/a').click()
        # // *[ @ id = "channel-all"] / div / ul / li[7]

        print('2')
        # 初始化一个体育新闻主页，点击NBA
        sportnewhome = SportsNewsHomePage(self.driver)
        # sportnewhome.click_nba_link()
        self.driver.find_element_by_xpath("//*[@id='col_nba']/div[1]/div[2]/ul[1]/li[1]/a").click()
        print('3')
        sportnewhome.get_windows_img()

if __name__ == '__main__':
    unittest.main()








