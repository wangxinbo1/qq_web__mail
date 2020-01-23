# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> receive_letter_page
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/16 0016 21:19
@Desc   ：
=================================================='''
from common.base_page import BasePage
from pagelocators.login_page_loc import LoginPageLoc as lpc
from pagelocators.home_page_loc import HomePageLoc as hpc, WriteLetterRegionLoc as wlrc, ReceiveLetterRegionLoc as rlrc
import time
from common.handle_context import HandleContext as hc

class ReceiveMailPage(BasePage):
    """
    发送email页面对象层
    """
    # 业务区域

    def switch_main_frame(self):
        self.switch_frame_by_webelement(rlrc.Loc_Main_Frame, "收件页面_主frame")

    def switch_mail_top_frame(self, wait_time=1):
        self.switch_default_frame("收件页面_顶级frame", wait_time)


    def verify_email_whether_exist(self, subject):
        Loc_ReceiveEmailSubject_Text = str(rlrc.Loc_ReceiveEmailSubject_Text)
        Loc_ReceiveEmailSubject_Text = eval(hc.replace_context(subject, Loc_ReceiveEmailSubject_Text))
        # print(Loc_ReceiveEmailSubject_Text)
        try:
            self.wait_ele_visible(Loc_ReceiveEmailSubject_Text, "收信界面_邮件主题")
            return True
        except:
            return False


if __name__=="__main__":
    data = str((1,2))

    print(type(data))
    data = eval(data)
    print(type(data))
