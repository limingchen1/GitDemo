import os.path
import time

from automation_framework_demo.framework.logger import Logger


logger = Logger(logger='BasePage').getlog()

class BasePage(object):
    '''
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    '''
    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("在当前页面点击前进")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("在当前页面进行后退")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("隐式等待 %d 秒", seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭并退出浏览器")
        except NameError as e:
            logger.info("关闭浏览器失败")

    # 保存图片
    def get_windows_img(self):

        # 图片保存路径
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'

        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'

        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("截屏保存到文件夹--screenshots")
        except NameError as e:
            logger.error("截屏失败 %s" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, selector):
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        print(selector_value)

        if selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        else:
            raise NameError('请输入有效的目标元素类型。')
        return element

    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("在输入框中输入 %s" % text)
        except NameError as e:
            logger.error("未能在输入框中输入 %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("输入前清空文本框")
        except NameError as e:
            logger.error("未能在输入框中清空 %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("这个元素 %s 被点击了一下" % el)
        except NameError as e:
            logger.error("无法点击该元素")

    # 网页标题
    def get_page_title(self):
        logger.info("当前网页标题为；%s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("休眠 %d 秒" % seconds)

























