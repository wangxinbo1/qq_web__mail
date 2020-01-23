# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> handle_config
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/14 0014 19:12
@Desc   ：
=================================================='''
import configparser
from common.dir_path import CONFIG_FILE_PATH
import os

class HandleConfig():
    """
    封装配置文件
    """

    def __init__(self, filename):
        self.config  = configparser.ConfigParser()
        self.config.read(filename,encoding="utf-8")

    def get_value(self, section, option):
        return self.config.get(section,option)

    @staticmethod
    def write(data,filename):
        config_write = configparser.ConfigParser()
        for i in data:
            config_write[i] = data[i]
        with open(filename,"w", encoding="utf-8") as fs:
            config_write.write(fs)

do_config = HandleConfig(CONFIG_FILE_PATH)

if __name__=="__main__":
    do_config = HandleConfig(CONFIG_FILE_PATH)
    print(do_config.get_value("log", "log_name"))
    print(do_config.get_value("log", "log_file_level"))
    data = {
        "log":{"log_name": "jiabao", "log_level": "DEBUG"},
        "filename":{"级别":"老王哥"}
            }
    HandleConfig.write(data,"test.conf")


