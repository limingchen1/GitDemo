import configparser
import os.path
from selenium import webdriver
from automation_framework_demo.framework.logger import Logger

logger = Logger(logger='BrowserEngine').getlog()


class BrowserEngine(object):

    # 获取当前路径
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'

    # def __init__(self, driver):
    #     self.driver = driver

    # 从config.ini文件中读取浏览器类型，返回驱动程序
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        # 获取浏览器类型、名称
        browser = config.get('browserType', 'browserName')
        logger.info('你使用的是 %s 浏览器.' % browser)
        # 获取url
        url = config.get('testServer', 'URL')
        logger.info('你使用的url是：%s' % url)

        # 判断你使用的那个浏览器
        if browser == 'Firefox':
            driver = webdriver.Firefox()
            driver.current_url()
            logger.info("开始使用火狐浏览器")
        elif browser == 'Chrome':
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("开始使用谷歌浏览器")
        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info("开始使用IE浏览器")

        # 访问url
        driver.get(url)
        logger.info('正在打开url：%s' % url)
        driver.maximize_window()
        logger.info("窗口放大")
        driver.implicitly_wait(10)
        logger.info("隐式等待10秒")
        return driver

    # 关闭浏览器
    def quit_browser(self):
        logger.info('现在，关闭并退出浏览器')
        self.driver.quit()





