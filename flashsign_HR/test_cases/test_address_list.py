import os

import pytest

from common.operate import Operate_More
from common.yaml_util import YamlUtil


# @allure.feature("发起模板合同合同")  # 一级菜单
class TestHome:
    """
    人力小程序，使用首页发起模板合同
    """

    # @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    # @allure.story("不动产赠与合同（企业与个人）")  # 二级菜单
    @pytest.mark.parametrize('args', YamlUtil().read_extract_yaml(os.getcwd() + "/case_data/Home/contract_data.yml"))
    def test_home_list(self, args):
        Operate_More().implement(text0=args["text"])