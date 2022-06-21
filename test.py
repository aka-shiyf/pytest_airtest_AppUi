# -*- encoding=utf8 -*-
import os

from common.Unpack import unpack
from common.yaml_util import YamlUtil

TestCaseData=YamlUtil().read_extract_yaml(os.getcwd() + "/case_data/Home/contract_data.yml")

print((unpack(TestCaseData))[2])