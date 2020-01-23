# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> login_page
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/15 0015 14:53
@Desc   ：
=================================================='''
from common.base_page import BasePage
from pagelocators.login_page_loc import LoginPageLoc as lpc
from pagelocators.home_page_loc import HomePageLoc as hpc,WriteLetterRegionLoc as wlrc,ReceiveLetterRegionLoc as rlrc
import time

class SendMailPage(BasePage):
    """
    发送email页面对象层
    """
    # 业务区域
    """
    def send_mail(self, receiver, subject, body):

        # 输入正文
        self.switch_frame(wlrc.Loc_Main_Frame, "写邮件页面_主frame")
        self.switch_frame(wlrc.Loc_Body_Frame, "写邮件页面_正文frame")
        self.input_text(wlrc.Loc_Body_TextBox, "写邮件页面_正文输入框", body)

        # 输入主题和收件人
        time.sleep(3)
        self.switch_default_frame(wlrc.Loc_Main_Frame, "写邮件页面_主frame")
        self.switch_frame(wlrc.Loc_Main_Frame, "写邮件页面_主frame")

        self.click_element(wlrc.Loc_Receiver_TextBox, "写邮件页面_收件人文本框")
        self.driver.switch_to.active_element.send_keys(receiver)
        self.input_text(wlrc.Loc_Subject_TextBox, "写邮件页面_主题文本框", subject)
        self.click_element(wlrc.Loc_Send_Button, "写邮件页面_发送按钮")

    def send_mail(self, receiver, subject, body):
        
        # 输入正文
        self.switch_frame(wlrc.Loc_Main_Frame, "写邮件页面_主frame")
        self.switch_frame(wlrc.Loc_Body_Frame, "写邮件页面_正文frame")
        self.input_text(wlrc.Loc_Body_TextBox, "写邮件页面_正文输入框", body)

        # 输入主题和收件人
        self.switch_default_frame("写邮件页面_主frame", wait_time=2)
        self.switch_frame(wlrc.Loc_Main_Frame, "写邮件页面_主frame")

        self.click_element(wlrc.Loc_Receiver_TextBox, "写邮件页面_收件人文本框")
        self.input_text_in_active_ele("写邮件页面_收件人文本框", receiver, wait_time=1)
        self.input_text(wlrc.Loc_Subject_TextBox, "写邮件页面_主题文本框", subject)
        self.click_element(wlrc.Loc_Send_Button, "写邮件页面_发送按钮")
    """
    def input_receiver_text(self, receiver, wait_time=1):
        self.click_element(wlrc.Loc_Receiver_TextBox, "写邮件页面_收件人文本框")
        self.input_text_in_active_ele("写邮件页面_收件人文本框", receiver, wait_time)

    def input_subject_text(self, subject):
        self.input_text(wlrc.Loc_Subject_TextBox, "写邮件页面_主题文本框", subject)

    def input_body_text(self, body):
        self.input_text(wlrc.Loc_Body_TextBox, "写邮件页面_正文输入框", body)

    def switch_main_frame(self):
        self.switch_frame_by_webelement(wlrc.Loc_Main_Frame, "写邮件页面_主frame")

    def switch_mail_top_frame(self, wait_time=1):
        self.switch_default_frame("写邮件页面_顶级frame", wait_time)

    def click_send_button(self):
        self.click_element(wlrc.Loc_Send_Button, "写邮件页面_发送按钮")

    def switch_body_frame(self):
        self.switch_frame_by_webelement(wlrc.Loc_Body_Frame, "写邮件页面_正文frame")

    def send_mail(self, receiver, subject, body):
        # 输入正文
        self.switch_main_frame()
        self.switch_body_frame()
        self.input_body_text(body)

        # 输入主题和收件人
        self.switch_mail_top_frame()
        self.switch_main_frame()
        self.input_receiver_text(receiver)
        self.input_subject_text(subject)
        self.click_send_button()

    def upload_attachment_in_mail(self, file_path, wait_time=3):
        self.move_to_ele_with_click(wlrc.Loc_Attachment_Move_TextButton, "写邮件页面_上传附件悬浮按钮")
        time.sleep(wait_time)
        self.upload(file_path, "写邮件页面_上传附件", wait_time=5)
        # self.winUpLoadFile(file_path, "打开")

    def send_mail_with_attachment(self, receiver, subject, body, attachment_file_path):
        # 输入正文
        self.switch_main_frame()
        self.switch_body_frame()
        self.input_body_text(body)
        self.switch_mail_top_frame()
        self.switch_main_frame()
        self.input_receiver_text(receiver)                  # 输入主题和收件人
        self.input_subject_text(subject)

        time.sleep(3)
        self.upload_attachment_in_mail(attachment_file_path)  # 上传附件
        time.sleep(3)
        self.click_send_button()


    # 断言区域

    def verify_whether_send_mail_success(self):
        try:
            self.wait_ele_visible(wlrc.Loc_MailSendSuccess_Text, "写邮件页面_发送成功的文本提示")
            return True
        except:
            return False


