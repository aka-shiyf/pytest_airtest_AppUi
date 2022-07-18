# -*- encoding=utf8 -*-
import logging
import os
import time

from airtest.core.api import text
from poco.proxy import UIObjectProxy

from common.Unpack import unpack
from common.operate import poco, Operate_More
from common.yaml_util import YamlUtil
from common.Assert import AssertOperate

# TestCaseData=YamlUtil().read_extract_yaml(os.getcwd() + "/case_data/Home/contract_case.yml")
# print(TestCaseData)
# print(TestCaseData[1]["text"][0]["CaseDescription3"])
# print((unpack(TestCaseData))[2])
# print(len(TestCaseData))
# AssertOperate().assert_exists_syf
# assert bool(poco(text="我的")) is False
# print(1)
# assert poco(text="") in b
# Operate_More().swipe_LR(0.8, 0.2)
# poco.click([0.6314814814814815, 0.17])
# text("18812345678")


