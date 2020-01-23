# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> test_send_mail
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/15 0015 21:18
@Desc   ：
=================================================='''
import unittest
from selenium import webdriver
from pageobjects.login_page import LoginPage
from common.handle_log import do_log
from common.handle_config import do_config
from ddt import ddt,data
from testdatas.common_data import login_data
from pageobjects.write_letter_page import SendMailPage
from pageobjects.home_page import HomePage
from common.dir_path import TEST_DATAS_DIR
import time
from pageobjects.receive_letter_page import ReceiveMailPage
from common.handle_context import HandleContext
from testdatas.test_data import SendEmailData
import os

email_subject = str(SendEmailData.email_subject) + str(HandleContext.generate_number(6))
email_body = str(SendEmailData.email_body) + str(HandleContext.generate_number(6))
email_receiver = SendEmailData.email_receiver
file_name = TEST_DATAS_DIR + os.sep + "test1.txt"

class SendMail(unittest.TestCase):
    """
    测试登录
    """

    def setUp(self):
        do_log.info("开始执行发送邮件的用例".center(100, "#"))
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(do_config.get_value("project_url", "url"))
        LoginPage(self.driver).login_in(login_data["username"], login_data["password"])
        self.sm = SendMailPage(self.driver)
        self.hp = HomePage(self.driver)
        self.rmp = ReceiveMailPage(self.driver)

    def tearDown(self):
        self.driver.close()
        do_log.info("{:#^20}".format("结束执行发送邮件的用例"))

    def test_01_send_mail_with_attachment(self):
        self.hp.enter_write_letter()
        self.sm.send_mail_with_attachment(email_receiver, email_subject, email_body, file_name)
        self.assertTrue(self.sm.verify_whether_send_mail_success(), msg="验证邮件发送成功失败")

        self.rmp.switch_mail_top_frame(wait_time=2)
        self.hp.enter_reveive_letter()
        self.rmp.switch_main_frame()
        self.assertTrue(self.rmp.verify_email_whether_exist("wo shi subject"), msg="邮件不在收件中")

if __name__ == "__main__":
    unittest.main()





