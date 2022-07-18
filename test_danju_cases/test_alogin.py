# -*- encoding=utf8 -*-
import os
import allure
import pytest

from common.Unpack import unpack
from common.operate import Operate_More
from common.yaml_util import YamlUtil

from common.Screenshots_operation import Screenshots

TestCaseData = YamlUtil().read_extract_yaml(os.getcwd() + "/case_data_danju/Login/login.yml")


@allure.feature((unpack(TestCaseData))[0])  # 一级菜单
class Testdenglu:
    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级 用例等级：blocker\critical\normal\minor\trivial
    @allure.story((unpack(TestCaseData))[1])  # 二级菜单
    # @allure.title("测试用例标题")  # 测试用例标题
    @pytest.mark.parametrize('args', TestCaseData)
    def test_denglu(self, args):
        try:
            Operate_More().implement(args["text"])
        except BaseException as e:
            print(type(e))
            print(e)


