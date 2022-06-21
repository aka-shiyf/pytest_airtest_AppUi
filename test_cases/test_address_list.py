import os

import allure
import pytest

from common.Unpack import unpack
from common.operate import Operate_More
from common.yaml_util import YamlUtil

TestCaseData = YamlUtil().read_extract_yaml(os.getcwd() + "/case_data/Home/contract_data.yml")


@allure.feature((unpack(TestCaseData))[0])  # 一级菜单
class TestHome:
    # @allure.epic()  # 最顶级描述
    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级 用例等级：blocker\critical\normal\minor\trivial
    @allure.story((unpack(TestCaseData))[1])  # 二级菜单
    # @allure.description((unpack(TestCaseData))[2])  # 用例描述
    # @allure.testcase()  #
    # @allure.issue()     # 缺陷管理系统链接
    # @allure.link()  # 定义一个链接在测试报告展现
    # @allure.step()  # 操作步骤
    # @allure.attachment()  # 附件
    @allure.title("HR小程序测试demo")  # 测试用例标题
    @pytest.mark.parametrize('args', TestCaseData)
    def test_home_list(self, args):
        "测试"
        Operate_More().implement(text0=args["text"])
