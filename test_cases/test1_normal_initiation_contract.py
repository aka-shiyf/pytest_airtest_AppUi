# -*- encoding=utf8 -*-
import os
import allure
import pytest

from common.Unpack import unpack
from common.operate import Operate_More
from common.yaml_util import YamlUtil

from common.Screenshots_operation import Screenshots

TestCaseData = YamlUtil().read_extract_yaml(os.getcwd() + "/case_data/AContract/contract_case.yml")


@allure.feature((unpack(TestCaseData))[0])  # 一级菜单
class TestContract:
    # @allure.epic()  # 最顶级描述
    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级 用例等级：blocker\critical\normal\minor\trivial
    @allure.story((unpack(TestCaseData))[1])  # 二级菜单
    # @allure.description((unpack(TestCaseData))[2])  # 用例描述
    # @allure.testcase()  #
    # @allure.issue()     # 缺陷管理系统链接
    # @allure.link()  # 定义一个链接在测试报告展现
    # @allure.step()  # 操作步骤
    # @allure.attachment()  # 附件
    @allure.title("测试用例标题")  # 测试用例标题
    @pytest.mark.parametrize('args', TestCaseData)
    def test_a_contract(self, args):
        try:
            Operate_More().implement(text0=args["text"])
            Screenshots().execute_screenshot()
        except BaseException as e:
            print(type(e))
            print(e)
