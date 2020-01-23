# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> home_page
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/15 0015 22:42
@Desc   ：
=================================================='''
from common.base_page import BasePage
from pagelocators.home_page_loc import HomePageLoc as hpc

class HomePage(BasePage):
    """
    首页页面对象层
    """

    def enter_write_letter(self):
        self.click_element(hpc.Loc_WriteLetter_Button, "首页_写邮件按钮")

    def enter_reveive_letter(self):
        self.click_element(hpc.Loc_ReceiveLetter_Button, "首页_收信按钮")