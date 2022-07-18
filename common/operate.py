# -*- encoding=utf8 -*-
__author__ = "syf"

import allure

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

from common.Screenshots_operation import Screenshots


class Operate_More:
    # 点击事件

    def click_syf(self, param=None, text0=None, pos=None):
        """
        点击操作，operational为3时执行.当param和text0为列表时可以循环执行点击操作，pos，不能是列表
        :param param: 直接输入的定位方式
        :param text0: text定位方式
        :param pos: 坐标定位方式
        :return:
        """
        if pos is not None:
            poco.click(pos)
        elif text0 is not None:
            if type(text0) == list:
                for text0s in text0:
                    poco(text=text0s).click()
            else:
                poco(text=text0).click()
        elif param is not None:
            if type(param) == list:
                for paramS in param:
                    poco(paramS).click()
            else:
                poco(param).click()

    # 输入事件
    def input_text(self, enter, param=None, text0=None, pos=None):
        """
         输入操作，operational为2时执行，需要参数enter和定位方式，输入文本和定位方式。
        由定位元素和输入文本组成点击输入，text0和param可以是列表，如果是列表则循环执行点击输入。
        :param enter: 需要输入的文本
        :param param: 直接输入的定位方式
        :param text0: text定位方式
        :param pos: 坐标定位方式
        :return:
        """
        if type(param) == list:
            index = 0
            for params in param:
                self.click_syf(param=params, text0=text0, pos=pos)
                text(enter[index])
                index += 1
        elif type(text0) == list:
            index = 0
            for text0s in text0:
                self.click_syf(param=param, text0=text0s, pos=pos)
                text(enter[index])
                index += 1
        elif pos is not None:
            self.click_syf(param=param, text0=text0, pos=pos)
            text(enter)

        else:
            self.click_syf(param, text0, pos)
            text(enter)

    # 左右滑动事件
    def swipe_LR(self, X0, X1):
        """
        左右滑动操作，operational为4时执行，abscissax0>abscissax1为从左往右滑动屏幕，例：(0.8，0.2),反之相反。
        :param X0: 滑动起点坐标
        :param X1: 滑动终点坐标
        :return:
        """
        poco.swipe([X1, 0.5], [X0, 0.5])

    # 上下滑动事件
    def swipe_UL(self, Y0, Y1):
        """
        上下滑动操作，operational为5时执行，Y_axis0>Y_axis1时从上往下滑动，例：(0.8,0.2),反之相反。
        :param Y0: 起点坐标
        :param Y1: 终点坐标
        :return:
        """
        poco.swipe([0.5, Y1], [0.5, Y0])

    # 返回事件
    def back_syf(self):
        """
        # BACK返回，operational为0时执行。
        :return:
        """
        keyevent("BACK")

    # 返回首页事件
    def home_syf(self):
        """
        HOME返回，operational为1时执行。
        :return:
        """
        keyevent("HOME")

    # 用例描述操作
    def cace_describe(self, Title, CaseDescription3, file_type):
        """
        增加用例描述，在当前页面截图，生成到测试报告中。 operational: 8 时执行。
        :param Title: 用例标题
        :param CaseDescription3: 用例描述
        :param file_type: 用例文件类型
        :return:
        """
        with allure.step(Title):
            # 增加描述
            allure.attach(CaseDescription3, file_type)
            # 截图上传到测试报告
            Screenshots().execute_screenshot()
            allure.attach(Screenshots().flie_jt(), "截图", allure.attachment_type.PNG)

    # 长按操作
    def changan(self, duration, pos=None, texts=None, param=None):
        """
        长按操作：通过三种参数去定位
        :param param: 接受参数为ui结构树中的绝对路径
        :param pos: pos坐标，接受参数类型为列表 例如: [0.1638888888888889, 0.17863247863247864]
        :param texts:接受参数为ui结构树中的文本
        :param duration:长按时间
        :return:
        """
        if pos is not None:
            poco.long_click(pos, duration)
        elif texts is not None:
            poco(text=texts).long_click(duration)
        elif param is not None:
            poco(param).long_click(duration)

    # 查找元素等待或断言
    def chazhao(self, WaitTime, assert_txt, param=None, text0=None, ):
        """
        12查找等待，text0、param必传，其中必须有一个不为空。
        :param WaitTime: 等待时间,必传不能为空；
        :param assert_txt: 断言字段，必传，可为空。
        :param param: 直接定位
        :param text0: text定位
        :return:
        """
        if assert_txt is not None:
            if param is not None:
                if poco(param).wait(WaitTime).exists():
                    print("断言查找通过")
                    Screenshots().execute_screenshot()
                    with allure.step(assert_txt):
                        allure.attach("断言成功", "断言详情", allure.attachment_type.TEXT)
                        allure.attach(Screenshots().flie_jt(), "截图", allure.attachment_type.PNG)

                else:
                    print("断言查找超时")
                    Screenshots().execute_screenshot()
                    with allure.step(assert_txt):
                        allure.attach("断言不通过", "断言详情", allure.attachment_type.TEXT)
                        allure.attach(Screenshots().flie_jt(), "截图", allure.attachment_type.PNG)

            elif text0 is not None:
                if poco(text=text0).wait(WaitTime).exists():
                    print("断言查找通过")
                    Screenshots().execute_screenshot()
                    with allure.step(assert_txt):
                        allure.attach("断言成功", "断言详情", allure.attachment_type.TEXT)
                        allure.attach(Screenshots().flie_jt(), "截图", allure.attachment_type.PNG)

                else:
                    Screenshots().execute_screenshot()
                    with allure.step(assert_txt):
                        allure.attach("断言不通过", "断言详情", allure.attachment_type.TEXT)
                        allure.attach(Screenshots().flie_jt(), "截图", allure.attachment_type.PNG)
                    print("断言查找超时")

        else:
            if param is not None:
                if poco(param).wait(WaitTime).exists():
                    print("查找通过")
                else:
                    print("查找超时")

            elif text0 is not None:
                if poco(text=text0).wait(WaitTime).exists():
                    print("查找通过")
                else:
                    print("查找超时")

    # 归一化坐标定位点击方法

    # 运行主方法
    def implement(self, args):
        for texts in args:
            if texts["operational"] == 0:
                self.back_syf()
            elif texts["operational"] == 1:
                self.home_syf()
            elif texts["operational"] == 2:
                self.input_text(enter=texts["enter"], param=texts["jd_path"], text0=texts["text"],
                                          pos=texts["coordinate"])
            elif texts["operational"] == 3:
                self.click_syf(param=texts["jd_path"], text0=texts["text"], pos=texts["coordinate"])
            elif texts["operational"] == 4:
                self.swipe_LR(X0=texts["abscissax0"], X1=texts["abscissax1"])
            elif texts["operational"] == 5:
                self.swipe_UL(texts["Y_axis0"], texts["Y_axis1"])
            # 截图操作，operational为6时执行截图操作，截图后会生成在当前用例测试报告中。
            elif texts["operational"] == 6:
                Screenshots().execute_screenshot()
                with allure.step("截图"):
                    allure.attach(Screenshots().flie_jt(), "截图", allure.attachment_type.PNG)
            elif texts["operational"] == 8:
                self.cace_describe(Title=texts["Title"], CaseDescription3=texts["CaseDescription3"],
                                   file_type=texts["file_type"])
            # 不运行
            elif texts["operational"] == 9:
                pass
            # 10休眠操作
            elif texts["operational"] == 10:
                sleep(texts["sleep"])
            elif texts["operational"] == 11:
                self.changan(texts["duration"], pos=texts["coordinate"], texts=texts["text"],
                                       param=texts["jd_path"])
            elif texts["operational"] == 12:
                self.chazhao(WaitTime=texts["WaitTime"], assert_txt=texts["assert_txt"], text0=texts["text"],
                                       param=texts["jd_path"])
