# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> run_script
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/14 0014 19:12
@Desc   ：
=================================================='''
import unittest
from lib.HTMLTestRunnerNew import HTMLTestRunner
from common.dir_path import REPORT_FILE_DIR
import os
import time
# suite = unittest.TestSuite()

suite = unittest.defaultTestLoader.discover(".", "test_*.py")
current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
print(type(current_time))
report_file_name = os.path.join(REPORT_FILE_DIR,str(current_time)+"report.html" )

with open(report_file_name, "wb") as fs:
    runner = HTMLTestRunner(stream=fs,
                            verbosity=3,
                            title="qq邮箱的测试报告",
                            description="本人第一份测试",
                            tester="老王"
                            )
    runner.run(suite)
