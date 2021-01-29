from automation_framework_demo1.testsuits import HTMLTestRunner
import os
import unittest
import time
from automation_framework_demo1.framework.SendEmail import SendMail

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

print('report_path'+ report_path)
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
#fp = file(HtmlFile, "wb")
fp = open(HtmlFile, "wb")

#用例路径
case_path = os.path.join(os.getcwd(), '')
print('case_path',case_path)


# 构建suite
# suite = unittest.TestLoader().discover(case_path, "test_baidu_search.py", top_level_dir=None)
suite = unittest.TestLoader().discover(case_path, "baidu_search.py", top_level_dir=None)

if __name__ == '__main__':
    #初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"Python+Selenium自动化测试框架实战篇7项目演示测试报告", description=u"用例测试情况")
    #开始执行测试套件
    runner.run(suite)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    fp.close()