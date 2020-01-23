# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：qq_web__mail -> handle_context
@IDE    ：PyCharm
@Author ：Mr. wang
@Date   ：2019/12/17 0017 21:47
@Desc   ：
=================================================='''
import re
import random
class HandleContext():

    pattern = "\*\*\*\*"

    @classmethod
    def replace_context(cls, replace_str, data):
        if re.search(HandleContext.pattern, data, re.M|re.I):
            data = re.sub(HandleContext.pattern, replace_str, data)
        return data

    @classmethod
    def generate_number(self, digit):
        """
        生成指定长度的随机数
        :param digit: 随机数位数，不能大于10
        :return: 返回生成的随机数
        """
        random_number = ''.join(random.sample("1234567890", digit))
        return random_number

if __name__=="__main__":
    hc = HandleContext()
    data = hc.replace_context("wang", "lageg e****t ian")
    print(data)
    print(hc.generate_number(5))
