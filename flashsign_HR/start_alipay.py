# -*- encoding=utf8 -*-
__author__ = "syf"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:///", ])
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def start():
    # start_app("com.eg.android.AlipayGphone")
    # poco("com.alipay.mobile.antui:id/search_bg").click()
    # text("闪链签企业HR")
    # poco(text="搜索").click()
    # poco(text="闪链签企业HR").click()
    start_app("com.eg.android.AlipayGphone")
    poco(text="我的小程序").click()
    poco(text="闪链签企业HR").click()