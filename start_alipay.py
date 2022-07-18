# -*- encoding=utf8 -*-
__author__ = "syf"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///", ])
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco

    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def start():
    start_app("com.eg.android.AlipayGphone")
    if poco("android:id/button2"):
        poco("android:id/button2").click()



    # 闪链签企业HR小程序
    # poco("com.alipay.mobile.antui:id/search_bg").click()
    # text("闪链签企业HR")
    # poco(text="搜索").click()
    # poco(text="闪链签企业HR").click()
    # stop_app("com.eg.android.AlipayGphone")

    # 闪链签电子单据小程序
    poco(text="").click()
    poco("com.alipay.mobile.antui:id/search_bg").click()
    text("闪链签电子单据")
    poco(text="搜索").click()
    poco(text="为组织、企业提供电子单据的发送和管理平").click()

