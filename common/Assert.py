# -*- encoding=utf8 -*-
import allure
from airtest.core.api import assert_exists
from airtest.core.cv import Template

from common.Screenshots_operation import Screenshots
from common.operate import poco


class AssertOperate:
    def assert_exists_syf(self, param=None, text0=None):
            assert bool(poco(param, text=text0)) is True
            Screenshots().execute_screenshot()
            print("截图成功")
            with allure.step("断言"):
                allure.attach("断言成功", "断言", allure.attachment_type.TEXT)
                allure.attach(Screenshots().flie_jt(), "截图", allure.attachment_type.PNG)
