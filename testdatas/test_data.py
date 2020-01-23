# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> common_data
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/15 0015 19:31
@Desc   ：
=================================================='''
class LoginData:
    # 登录的测试数据
    login_data = {"username": "1020487224@qq.com", "password": "wang13468610626"}
    login_exception_data = (
        {"username": "1020487224@qq.com", "password": "", "verify_msg": "没有输入密码"},
        {"username": "1020487224@qq.co", "password": "wang112", "verify_msg": "输入的帐号或密码不正确"}
    )

class SendEmailData:
    # 登录的测试数据
    email_subject = "我是主题"
    email_body = "我是 body体"
    email_receiver = "1020487224@qq.com"
