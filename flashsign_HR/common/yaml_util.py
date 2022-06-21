import os
import yaml


class YamlUtil:

    # 读取extract.yml文件
    def read_extract_yaml(self,path):
        with open(path, mode="r", encoding='utf-8')as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

        # 写入save.yml文件

    def write_save_yaml(self, data):
        with open(os.getcwd() + "/data/save.yml", mode="a", encoding='utf-8')as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除yaml文件
    def clear_save_yaml(self):
        with open(os.getcwd() + "/data/save.yml", mode="w", encoding='utf-8')as f:
            f.truncate()