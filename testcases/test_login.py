# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> test_login
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/15 0015 15:12
@Desc   ：
=================================================='''
import unittest
from selenium import webdriver
from pageobjects.login_page import LoginPage
from common.handle_log import do_log
from common.handle_config import do_config
from ddt import ddt,data
from testdatas.test_data import LoginData as ld
from testdatas.common_data import login_data
import time

@ddt
class TestLogin(unittest.TestCase):
    """
    测试登录
    """

    def setUp(self):
        do_log.info("开始执行登录的用例".center(40, "#"))
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(do_config.get_value("project_url", "url"))
        self.lg = LoginPage(self.driver)


    def tearDown(self):
        self.driver.close()
        do_log.info("结束执行登录的用例".center(40,"#"))

    def test_01_login_success(self):
        self.lg.login_in(login_data["username"], login_data["password"])
        self.assertTrue(self.lg.verify_login_whether_success(), msg="用例执行失败")

    @data(*ld.login_exception_data)
    def test_02_login_failed(self, data):
        self.lg.login_in(data["username"], data["password"])
        text = self.lg.get_except_msg()
        self.assertIn(data["verify_msg"], str(text), msg="用例执行失败")


if __name__ == "__main__":
    unittest.main()
