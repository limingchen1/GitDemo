from automation_framework_demo.framework.base_page import BasePage


class SportsNewsHomePage(BasePage):
    # NBA入口
    nba_link = "xaph=>//*[@id='channel-all']/div/ul/li[7]"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)
