# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> login_page_loc
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/15 0015 14:42
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By
class LoginPageLoc():
    """
    登录页面元素
    """
    # 用户名密码区域
    Loc_Login_Frame = (By.ID, "login_frame") # 登录表单处的frame
    Loc_Email_InputBox = (By.ID, "u")  # Email输入框
    Loc_Password_InputBox = (By.ID, "p")  # 密码输入框
    Loc_Login_Button = (By.ID, "login_button")  # 登录按钮
    Loc_Exception_Text = (By.ID, "err_m") # 提示信息：您没有输入密码


