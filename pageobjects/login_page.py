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
from pagelocators.home_page_loc import HomePageLoc as hpc

class LoginPage(BasePage):
    """
    登录页面对象层
    """
    # def __init__(self):
    #     pass
    # 业务区域
    def login_in(self, email, password):
        self.switch_frame_by_webelement(lpc.Loc_Login_Frame,"登录页面_登录表单frame")
        self.input_text(lpc.Loc_Email_InputBox,"登录页面_email输入框", email)
        self.input_text(lpc.Loc_Password_InputBox, "登录页面_password输入框", password)
        self.click_element(lpc.Loc_Login_Button, "登录页面_登录按钮")

    # 断言区域
    def verify_login_whether_success(self):
        try:
            self.wait_ele_visible(hpc.Loc_EmailAddr_Text, "首页_顶部邮箱地址")
            return True
        except:
            return False

    def get_except_msg(self):
        return self.get_ele_text(lpc.Loc_Exception_Text, "登录页面_异常信息")
