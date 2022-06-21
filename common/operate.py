# -*- encoding=utf8 -*-
__author__ = "syf"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


class Operate_More:
    # 点击事件
    def click_syf(self, param=None, text0=None):
        poco(param, text=text0).click()

    # 输入事件
    def input_text(self, enter):
        text(enter)

    # 左右滑动事件
    def swipe_LR(self, X0, X1):
        poco.swipe([X1, 0.5], [X0, 0.5])

    # 上下滑动事件
    def swipe_UL(self, Y0, Y1):
        poco.swipe([0.5, Y1], [0.5, Y0])

    # 返回事件
    def back_syf(self):
        keyevent("BACK")

    # 返回首页事件
    def home_syf(self):
        keyevent("HOME")

    # def exists_syf(self,verify_param=None, verify_text=None,eq):
    #     if exists(poco(verify_param, verify_text)):
    #         Operate_More().click_syf(param=verify_param, text0=verify_text["text"])

    # 运行主方法
    def implement(self, text0):
        for texts in text0:
            if texts["operational"] == 0:
                Operate_More().back_syf()
            elif texts["operational"] == 1:
                Operate_More().home_syf()
            elif texts["operational"] == 2:
                Operate_More().input_text(enter=texts["enter"])
            elif texts["operational"] == 3:
                Operate_More().click_syf(param=texts["jd_path"], text0=texts["text"])
            elif texts["operational"] == 4:
                Operate_More().swipe_LR(X0=texts["abscissax0"], X1=texts["abscissax1"])
            elif texts["operational"] == 5:
                Operate_More().swipe_UL(texts["Y_axis0"], texts["Y_axis1"])
            # elif texts["operational"] == 6:
            #     print(texts["equals"])
            #     Operate_More().exists_syf(verify_param=texts["jd_path"],verify_text=texts["text"])
