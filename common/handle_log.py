# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> handle_log
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/14 0014 19:12
@Desc   ：
=================================================='''
import logging
from common.dir_path import LOG_FILE_PATH
from common.handle_config import do_config
import time

log_file_name = LOG_FILE_PATH + "/" + str(time.strftime("%Y%m%d", time.localtime())) + "log.log"

class HandleLog():
    """
    封装日志处理
    """

    def __init__(self):
        # 定义收集器对象
        self.logger = logging.getLogger(do_config.get_value("log", "log_name"))
        # 定义收集器日志等级
        self.logger.setLevel(do_config.get_value("log", "log_collector_level"))

        # 定义控制台日志对象
        console_log = logging.StreamHandler()
        # 控制台日志等级
        console_log.setLevel(do_config.get_value("log", "log_console_level"))
        # 控制台日志的格式
        console_format = logging.Formatter(do_config.get_value("log", "log_console_format"))
        console_log.setFormatter(console_format)

        # 输出文件日志对象

        file_log = logging.FileHandler(log_file_name, encoding="utf-8")
        # 输出文件日志等级
        file_log.setLevel(do_config.get_value("log", "log_file_level"))
        # 输出日志格式
        file_format = logging.Formatter(do_config.get_value("log", "log_file_format"))
        file_log.setFormatter(file_format)

        # 对接日志收集器
        self.logger.addHandler(console_log)
        self.logger.addHandler(file_log)

    def get_logger(self):
        return self.logger


do_log = HandleLog().get_logger()

if __name__ == "__main__":
    do_log.info("我是info信息")
    do_log.error("我是error信息")
    do_log.debug("我是debug信息")
