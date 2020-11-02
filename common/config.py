import configparser
import os
import sys


class ConfigIni:
    # 获得当前项目的绝对路径
    # root_dir = os.path.dirname(os.path.abspath("."))
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # 获取当前配置文件的路径，相当于根路径
    config_file_path = os.path.join(BASE_PATH, "config.ini")

    # 定义一个配置文件的对象，默认一个文件路径，可自己补充其他路径
    def __init__(self, file_path=config_file_path):
        # 为了让写入文件的路径是唯一值，所以这样定义下来
        self.config_file_path = file_path
        # 定义配置文件对象
        self.cf = configparser.ConfigParser()
        # 读取配置文件
        self.cf.read(file_path)

    # 获取配置文件的value值，配置文件有section，option，value
    def get_key(self, section, option):
        # 获取value的值
        value = self.cf.get(section, option)
        return value

    # 修改value的值
    def set_value(self, section, option, value):
        # python内存先修改值
        self.cf.set(section, option, value)
        # 需要通过文件的方式写入才行，不然实体文件的值不会改变
        with open(self.config_file_path, "w+") as f:
            self.cf.write(f)

cf=ConfigIni()


if __name__ == "__main__":
    # 测试内容，不要随便运行
    a = ConfigIni()
    print(a.root_dir)
    print(a.config_file_path)
    print(a.get_key("test", "name"))
    a.set_value("test", "name", "tongtong")
    print(a.get_key("logs", "name"))
