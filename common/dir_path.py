# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> dir_path
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/14 0014 19:12
@Desc   ：
=================================================='''
import os

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件目录路径
CONFIG_FILE_DIR = BASE_DIR +  os.sep + "configfile"

# 配置文件路径
CONFIG_FILE_PATH = CONFIG_FILE_DIR + os.sep + "config.conf"

# 输出文件的目录
OUTPUT_DIR = BASE_DIR + os.sep + "output"

# 日志文件的路径
LOG_FILE_PATH = OUTPUT_DIR + os.sep + "log"

# 报告输出目录
REPORT_FILE_DIR  = OUTPUT_DIR + os.sep + "report"

# 截图目录
SCREENSHOT_DIR = BASE_DIR + os.sep + "output" + os.sep + "screenshot"

# 测试数据文件路径

TEST_DATAS_DIR = BASE_DIR + os.sep + "testdatas"


