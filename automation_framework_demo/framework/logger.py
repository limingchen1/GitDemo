import logging
import logging.handlers
import os.path
import time


class Logger(object):

    # 指定保存日志的文件路径，日志级别，以及调用文件
    # 讲日志存入到指定的文件中
    def __init__(self, logger):

        # 创建一个日志器logger，并设置日志级别为DEBUG
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件，路径 + 时间 + .log = 日志名称
        # 当前日期
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # os.path.dirname(__file__) -->去掉文件名，返回当前目录
        # os.path.abspath('.') -->当前目录绝对路径
        # os.path.abspath('..') -->上一级目录绝对路径
        # 保存日志路径
        log_path = os.path.abspath('..') + '/logs/'
        # 日志名称
        log_name = log_path + rq + '.log'

        # 日志格式，RotatingFileHandler写入文件，如果文件超过1024*1024个Bytes，仅保留5个文件，为utf-8格式
        fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')

        # 设置该日志等级为INFO
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 创建一个格式器formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给日志处理器logger添加上面创建的handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger




