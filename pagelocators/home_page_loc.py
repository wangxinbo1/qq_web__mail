# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> login_page_loc
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/15 0015 14:42
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By


class HomePageLoc():
    """
    首页页面元素
    """
    # 首页区域元素
    Loc_EmailAddr_Text = (By.ID, "useraddr")  # 首页_顶部email文本地址
    Loc_WriteLetter_Button = (By.ID, "composebtn")   # 首页_写邮件按钮
    Loc_ReceiveLetter_Button = (By.XPATH, "//a[@id='readmailbtn_link']")  # 首页_收信按钮

class WriteLetterRegionLoc():
    """
    写信界面元素
    """
    Loc_Receiver_TextBox = (By.XPATH, "//div[@id='toAreaCtrl']//div[@class='addr_text']")   # 写邮件页面_收件人文本框
    Loc_Subject_TextBox = (By.ID, "subject")  # 写邮件页面_主题文本框
    Loc_Body_TextBox = (By.XPATH, "//body[@accesskey='q']")  # 写邮件页面_正文输入框
    Loc_Body_Frame = (By.XPATH, "//div[@id='QMEditorArea']//iframe[@class='qmEditorIfrmEditArea']")  # 写邮件页面_正文frame
    Loc_Send_Button = (By.XPATH, "//div[@style]/a[text()='发送']")  # 写邮件页面_发送按钮
    Loc_Main_Frame = (By.XPATH, "//iframe[@id='mainFrame']")  # 写邮件页面_主frame
    Loc_MailSendSuccess_Text = (By.ID, "sendinfomsg")  # 写邮件页面_发送成功的文本提示
    Loc_Attachment_Move_TextButton = (By.XPATH, "//*[@id='AttachFrame']/a") # 写邮件页面_上传附件悬浮按钮
    Loc_Attachment_TextButton = (By.ID, "sAddAtt1")  # 写邮件页面_上传附件按钮

class ReceiveLetterRegionLoc():
    """
    收信界面元素
    """
    Loc_ReceiveEmailSubject_Text = (By.XPATH, "//u[contains(text(),'****')]")  # 收信界面_邮件主题
    Loc_Main_Frame = (By.XPATH, "//iframe[@id='mainFrame']")  # 收信界面_主frame
