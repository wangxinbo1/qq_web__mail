# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> base_page
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/14 0014 19:38
@Desc   ：
=================================================='''
import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handle_log import do_log
from common.dir_path import SCREENSHOT_DIR
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import win32gui
import win32con

class BasePage():
    """
    基本页面对象
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver

    ##################################################基本元素操作方法区域#############################################

    def wait_ele_visible(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("等待 '{}' 元素值为 '{}' 可见".format(img_desc, loc))
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except:
            do_log.error("查找 '{}' 元素出现失败".format(img_desc))
            raise
        else:
            end_time = time.time()
            wait_time = time.strftime("%H:%M:%S", time.localtime(end_time - start_time))
            do_log.info("等待 '{}' 元素出现成功，等待时间为 {}s".format(img_desc, wait_time))

    def wait_page_contains_ele(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("等待 '{}' 元素值为 '{}' 出现在页面".format(img_desc, loc))
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
            do_log.info("等待 '{}' 元素出现成功".format(img_desc))
        except:
            do_log.error("等待 '{}' 元素出现失败".format(img_desc))
            raise
        else:
            end_time = time.time()
            wait_time = time.strftime("%H:%M:%S", time.localtime(end_time - start_time))
            do_log.info("等待 '{}' 元素出现成功，等待时间为 {}s".format(img_desc, wait_time))

    def find_element(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("查找 '{}' 元素值为 '{}' ".format(img_desc, loc))
        self.wait_ele_visible(loc, img_desc, timeout, frequency)
        try:
            ele = self.driver.find_element(*loc)
            do_log.info("找到 '{}' 元素".format(img_desc))
            return ele
        except:
            do_log.error("未找到 '{}' 元素".format(img_desc))
            raise

    def get_active_ele(self, img_desc):
        """
        return 一个活动的元素对象，适用于光标所在处的元素
        :param img_desc:
        :return: Webelement对象
        """
        do_log.info("查找 '{}' 的活动元素".format(img_desc))
        try:
            ele = self.driver.switch_to.active_element
            do_log.info("找到 '{}' 活动的元素".format(img_desc))
            return ele
        except:
            do_log.error("未找到 '{}' 活动的元素".format(img_desc))
            raise

    def input_text(self, loc, img_desc, text_value, timeout=30, frequency=0.5):
        do_log.info("在 '{}' 的 '{}' 元素处输入 '{}' ".format(img_desc, loc, text_value))
        try:
            self.find_element(loc, img_desc, timeout, frequency).send_keys(text_value)
            do_log.info("在 '{}' 输入文本值成功".format(img_desc))
        except:
            do_log.error("在 '{}' 输入文本值失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def input_text_in_active_ele(self, img_desc, text_value, wait_time=0):
        do_log.info("在 '{}' 活动元素处输入 '{}' ".format(img_desc, text_value))
        time.sleep(wait_time)
        try:
            self.get_active_ele(img_desc).send_keys(text_value)
            do_log.info("在 '{}' 输入文本值成功".format(img_desc))
        except:
            do_log.error("在 '{}' 输入文本值失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def input_text_use_js(self, loc, img_desc, text_value, timeout=30, frequency=0.5):
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            self.driver.execute_script("arguments[0].value=arguments[1]", ele, text_value)
            do_log.info("在 '{}' 输入文本值成功".format(img_desc))
        except:
            do_log.error("在 '{}' 输入文本值失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def click_element(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("在 '{}' 点击 ' {}' 元素".format(img_desc, loc))
        try:
            self.find_element(loc, img_desc, timeout, frequency).click()
            do_log.info("在 '{}' 点击元素成功".format(img_desc))
        except:
            do_log.error("在 '{}' 点击元素失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def click_element_use_js(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("在 '{}' 点击 ' {}' 元素".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            self.driver.execute_script("arguments[0].click()", ele)
            do_log.info("在 '{}' 点击元素成功".format(img_desc))
        except:
            do_log.error("在 '{}' 点击元素失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def get_ele_text(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("获取 '{}' 元素的 '{}' 文本值".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            text = ele.text
            do_log.info("获取 '{}' 文本为 '{}'  成功".format(img_desc, text))
            return text
        except:
            do_log.error("获取 '{}' 文本失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def get_ele_attribute(self, loc, attribute_name, img_desc, timeout=30, frequency=0.5):
        do_log.info("获取 '{}' 元素的属性值，元素值为 '{}'".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            attribute_value = ele.get_attribute(attribute_name)
            do_log.info("获取 '{}' 属性名为 '{}' 的值 '{}' 成功".format(img_desc, attribute_name, attribute_value))
            return attribute_value
        except:
            do_log.error("获取 '{}' 属性名为 '{}' 的属性值失败".format(img_desc, attribute_name))
            self.save_error_screenshot(img_desc)
            raise

    ##################################################滚动条操作方法区域#############################################

    # 移动到元素element对象的“底端”与当前窗口的“底部”对齐
    def slide_scoll_bar_to_ele_bottom(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("开始滑动页面滚动条到 '{}' 底部对齐，元素值为 '{}'".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
            do_log.info("滑动页面滚动条到 '{}' 底部对齐成功".format(img_desc))
        except:
            do_log.error("滑动页面滚动条到 '{}' 底部对齐失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    # 移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
    def slide_scoll_bar_to_ele_top(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("开始滑动页面滚动条到 '{}' 顶部对齐，元素值为 '{}'".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            do_log.info("滑动页面滚动条到 '{}' 顶部对齐成功".format(img_desc))
        except:
            do_log.error("滑动页面滚动条到 '{}' 顶部对齐失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    # 移动到页面底部
    def slide_scoll_bar_to_bottom(self, img_desc, wait_time=0):
        do_log.info("开始滑动 '{}' 到底部".format(img_desc))
        time.sleep(wait_time)
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            do_log.info("滑动 '{}' 到底部成功".format(img_desc))
        except:
            do_log.error("滑动 '{}' 到底部部失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    # 移动到页面顶部
    def slide_scoll_bar_to_top(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("开始滑动 '{}' 到顶部".format(img_desc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
            do_log.info("滑动 '{}' 到顶部成功".format(img_desc))
        except:
            do_log.error("滑动 '{}' 到顶部失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    ##################################################frame切换方法区域#############################################

    def switch_frame_by_webelement(self, loc, img_desc, timeout=30, frequency=0.5):
        do_log.info("在 '{}' 切换到 '{}' frame".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            self.driver.switch_to.frame(ele)
            do_log.info("切换 '{}' frame成功".format(img_desc))
        except:
            do_log.error("切换 '{}' frame失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def switch_frame_by_index(self, index, img_desc, wait_time=0):
        do_log.info("在 '{}' 切换到索引为  '{}' 的frame".format(img_desc, index))
        time.sleep(wait_time)
        try:
            self.driver.switch_to.frame(index)
            do_log.info("切换索引为 '{}' frame成功".format(img_desc))
        except:
            do_log.error("切换 '{}'索引为 frame失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def switch_frame_by_name(self, name, img_desc, wait_time=0):
        do_log.info("在 '{}' 切换到名称为  '{}' 的frame".format(img_desc, name))
        time.sleep(wait_time)
        try:
            self.driver.switch_to.frame(name)
            do_log.info("切换到名称为 '{}' frame成功".format(img_desc))
        except:
            do_log.error("切换到名称为 '{}' frame失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def switch_parent_frame(self, img_desc, wait_time=0):
        do_log.info("切换到父 '{}' frame".format(img_desc, wait_time))
        time.sleep(wait_time)
        try:
            self.driver.switch_to.parent_frame()
            do_log.info("切换到 '{}' 的frame成功".format(img_desc))
        except:
            do_log.info("切换到 '{}' 的frame失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def switch_default_frame(self, img_desc, wait_time=0):
        do_log.info("切换到 '{}' frame前，强制等待 {}s".format(img_desc, wait_time))
        time.sleep(wait_time)
        try:
            self.driver.switch_to.default_content()
            do_log.info("切换到 '{}' 的frame成功".format(img_desc))
        except:
            do_log.info("切换到 '{}' 的frame失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise


    ##################################################鼠标操作方法区域#############################################

    def move_to_ele(self, loc, img_desc, timeout=30, frequency=5):
        do_log.info("鼠标悬浮到 '{}' ,元素值为 '{}'' 中间".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
            do_log.info("悬浮到 '{}' 元素成功".format(img_desc))
        except:
            do_log.error("悬浮到 '{}' 元素失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def move_to_ele_with_click(self, loc, img_desc, timeout=30, frequency=5):
        do_log.info("鼠标悬浮并点击 '{}' ,元素值为 '{}'".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            ActionChains(self.driver).move_to_element(ele).click(ele).perform()
            do_log.info("悬浮到 '{}' 元素成功".format(img_desc))
        except:
            do_log.error("悬浮到 '{}' 元素失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def double_click_ele(self, loc, img_desc, timeout=30, frequency=5):
        do_log.info("双击 '{}' ,元素值为 '{}' ".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            ActionChains(self.driver).double_click(ele).perform()
            do_log.info("双击 '{}' 元素成功".format(img_desc))
        except:
            do_log.error("双击 '{}' 元素失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def right_click_ele(self, loc, img_desc, timeout=30, frequency=5):
        do_log.info("右击 '{}' ,元素值为 '{}' ".format(img_desc, loc))
        ele = self.find_element(loc, img_desc, timeout, frequency)
        try:
            ActionChains(self.driver).context_click(ele).perform()
            do_log.info("右击 '{}' 元素成功".format(img_desc))
        except:
            do_log.error("右击 '{}' 元素失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    def drag_to_ele(self, loc_source, loc_target, img_desc, timeout=30, frequency=5):
        do_log.info("拖拽 '{}' ,source元素值为 '{}'，target元素值为 '{}' ".format(img_desc, loc_source))
        ele_source = self.find_element(loc_source, img_desc, timeout, frequency)
        ele_terget = self.find_element(loc_target, img_desc, timeout, frequency)
        try:
            ActionChains(self.driver).drag_and_drop(ele_source, ele_terget).perform()
            do_log.info("拖拽 '{}' 成功".format(img_desc))
        except:
            do_log.error("拖拽 '{}' 失败".format(img_desc))
            self.save_error_screenshot(img_desc)
            raise

    ##################################################上传文件方法区域#############################################

    def upload(self, filePath, img_desc, browser_type="chrome", wait_time=5):
        do_log.info("'{}' 开始上传文件 '{}'".format(img_desc, filePath))
        try:
            if browser_type == "chrome":
                title = "打开"
            else:
                title = ""
            # 找元素
            # 一级窗口"#32770","打开"
            dialog = win32gui.FindWindow("#32770", title)
            #
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
            comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
            # 编辑按钮
            edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
            # 打开按钮
            # button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(O)")  # 二级
            button = win32gui.FindWindowEx(dialog, 0, 'Button', None)

            # 往编辑当中，输入文件路径 。
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)  # 发送文件路径
            time.sleep(wait_time)
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
            do_log.info("{}上传 '{}' 成功".format(img_desc, filePath))
            time.sleep(wait_time)
        except:
            do_log.error("{}上传 '{}' 失败".format(img_desc, filePath))
            raise

    def winUpLoadFile(self, file_path, title):
        # 一级顶层窗口，此处title为上传窗口名称，浏览器不一样上传窗口名称不一样
        dialog = win32gui.FindWindow("#32770", title)
        # 二级窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级窗口
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
        # 四级窗口
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        # 执行操作 输入文件路径
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
        # 点击打开上传文件
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    ##################################################截图方法区域#############################################

    def save_error_screenshot(self, img_desc):
        screenshot_name = SCREENSHOT_DIR + os.sep + str(
            time.strftime("%Y%m%d%H%M%S", time.localtime())) + img_desc + ".jpg"
        self.driver.save_screenshot(screenshot_name)
        do_log.info("页面截图文件保存在 {}".format(screenshot_name))

if __name__ == "__main__":
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.add_argument("lang=en_US")


    driver = webdriver.Chrome(chrome_options=options)
    ob = BasePage(driver)
    driver.get("https://mail.qq.com/")
    driver.switch_to.frame("login_frame")
    loc_mail_text = (By.ID, "u")
    Loc_Login_Frame = (By.ID, "login_frame")  # 登录表单处的frame
    Loc_Email_InputBox = (By.ID, "u")  # Email输入框
    Loc_Password_InputBox = (By.ID, "p")  # 密码输入框
    Loc_Login_Button = (By.ID, "login_button")  # 登录按钮
    Loc_Exception_Text = (By.ID, "err_m")  # 提示信息：您没有输入密码
    # loc_baidu_button = (By.XPATH, "//input[@class='g-cp submitInput button-hook']")

    ob.input_text_use_js(loc_mail_text, "邮箱首页_用户名输入框", "1020487224@qq.com")
    # ob.click_element(loc_baidu_button, "百度首页_百度按钮")
    ob.input_text_use_js(Loc_Password_InputBox, "邮箱首页_密码输入框", "wxb112112!")
    ob.click_element_use_js(Loc_Login_Button,"登陆按钮")
