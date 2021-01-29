from automation_framework_demo1.framework.base_page import BasePage

class SportsNewsHomePage(BasePage):
    #NBA入口
    nba_link = "xpath=>.//*[@id='col_focus']/div[1]/div[2]/div/div[2]/div/ul/li[1]/a"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)