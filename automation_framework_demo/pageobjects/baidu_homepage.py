from time import sleep

from selenium import webdriver

from automation_framework_demo.framework.base_page import BasePage


class HomePage(BasePage):
    input_box = 'id=>kw'
    search_submit_btn = "xpath=>//*[@id='su']"

    #百度新闻入口
    news_link = "xpath=>//*[@id='s-top-left']/a[1]"

    def type_search(self, text):
        self.type(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)

    def click_news(self):
        self.click(self.news_link)
        self.sleep(2)


