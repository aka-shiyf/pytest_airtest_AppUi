# -*- encoding=utf8 -*-
__author__ = "syf"

import allure
from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

from common.Screenshots_operation import Screenshots

from common.Assert import AssertOperate


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

    def cace_describe(self, Title, CaseDescription3, file_type):
        with allure.step(Title):
            allure.attach(CaseDescription3, file_type)

    # 运行主方法
    def implement(self, text0):
        for texts in text0:
            # BACK返回，operational为0时执行。
            if texts["operational"] == 0:
                Operate_More().back_syf()
            # HOME返回，operational为1时执行。
            elif texts["operational"] == 1:
                Operate_More().home_syf()
            # 输入操作，operational为2时执行，需要参数enter。
            elif texts["operational"] == 2:
                Operate_More().input_text(enter=texts["enter"])
            # 点击操作，operational为3时执行，jd_path为ui绝对路径，text为组件中的文本。
            elif texts["operational"] == 3:
                Operate_More().click_syf(param=texts["jd_path"], text0=texts["text"])
            # 左右滑动操作，operational为4时执行，abscissax0>abscissax1为从左往右滑动屏幕，例：(0.8，0.2),反之相反。
            elif texts["operational"] == 4:
                Operate_More().swipe_LR(X0=texts["abscissax0"], X1=texts["abscissax1"])
            # 上下滑动操作，operational为5时执行，Y_axis0>Y_axis1时从上往下滑动，例：(0.8,0.2),反之相反。
            elif texts["operational"] == 5:
                Operate_More().swipe_UL(texts["Y_axis0"], texts["Y_axis1"])
            elif texts["operational"] == 6:
                Screenshots().execute_screenshot()
                with allure.step("截图"):
                    allure.attach(Screenshots().flie_jt(), "截图", allure.attachment_type.PNG)
            elif texts["operational"] == 7:
                AssertOperate().assert_exists_syf(param=texts["jd_path"], text0=texts["text"])
            elif texts["operational"] == 8:
                Operate_More().cace_describe(Title=texts["Title"], CaseDescription3=texts["CaseDescription3"],
                                             file_type=texts["file_type"])
