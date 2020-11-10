# @Author : TongTong

import os
import time
from string import Template
import requests
import yaml
from jsonpath import jsonpath
from common.config import cf
from common.get_log import log


# BaseApi
class BaseApi:
    """
    实现了所有公共类API的需要的东西,是其他API的父类

    ip：测试环境的ip地址
    Base_Path：项目的根路径
    """

    # 通过配置文件获取测试的环境的ip地址
    ip = cf.get_key("env", "formal_ip")
    Base_Path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def send_api(self, req: dict):
        """
        封装requests代码，替代requests.request方法
        :param req: 传入请求的字典数据，包括method，url，params，json
        :return: 响应体
        """

        """
        req传入的数据类型如下
        req={
            "method":"GET",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?",
            "params":f"corpid={self.corpid}&corpsecret={secret}"
        }
        request的参数接收method，url，params，data，json
        把这些参数都写在一个字典里面，**req就可以解包
        变成method="get",url="http://xxx"，符合request传参的需求
        """

        res = requests.request(**req).json()
        return res

    @classmethod
    def get_time(cls, date):
        """
        时间字符串转化成时间戳，格式：2013-10-10 23:40:00，转化成1605021256的时间戳
        :param date: 2013-10-10 23:40:00的时间格式
        :return: 返回时间戳1605021256
        """
        # 先转换成时间格式对象，再转化成时间戳
        time_strp = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(time_strp))
        return time_stamp

    @classmethod
    def jsonpath(cls, json, expr):
        """
        优化jsonpath代码，其他类就不用from jsonpath improt jsonpath了
        :param json: 传入json格式，发现json或者字典都ok也
        :param expr: 要获取json内容的表达式
        :return: 返回想要的字符串
        """
        return jsonpath(json, expr)

    @classmethod
    def load_yaml(cls, path, sub=None):
        """
        封装yaml读取的代码，通过路径直接读取yml文件并转化成python数据类型
        :param path: yml文件的相对路径
        :param sub: 读取yml文件的二级数据目录，默认为None
        :return: 返回yml文件的python数据
        """
        # 链接根路径和yml文件的相对路径，简化文件路径
        path = os.path.join(cls.Base_Path, path)
        with open(path, encoding="utf-8") as f:
            # 不写sub就获取yml的所有内容，写就获取yml的二级数据目录
            if sub is None:
                return yaml.safe_load(f)
            else:
                return yaml.safe_load(f)[sub]

    @classmethod
    def save_yaml(cls, path, data):
        """
        封装yaml写入的代码
        :param path: yml文件的相对路径
        :param data: python的数据
        """
        # 链接根路径和yml文件的相对路径，简化文件路径
        path = os.path.join(cls.Base_Path, path)
        with open(path, "r+", encoding="utf-8", ) as f:
            yaml.safe_dump(data, f)

    @classmethod

    def template(cls, path, data, sub=None):
        """
        使用模板技术，把yml文件中的变量进行二次转化，是本框架的yml文件的技术基础
        :param path: 模板技术输入yml文件相对路径
        :param data: data是需要修改的模板变量的字典类型
        :param sub: sub是对yml的数据进行二次提取，等于是一个大字典，再提取下一层的小字典，为了让一个yml文件可以有多个接口数据
        :return:
        """
        with open(path, encoding="utf-8") as f:
            if sub is None:
                '''
                不需要对数据进行二次提取，Template(f.read()).substitute(data)先替换变量
                yaml.safe_load把yml格式的字符串变成dict类型返回
                '''
                return yaml.safe_load(Template(f.read()).substitute(data))
            else:
                '''
                由于Template需要替换全部的变量，有漏的就会报错，先写Template(f.read()).substitute(data)
                就会报错，data只对sub下一层的数据改，并没有改其他层的数据，肯定会报错
                需要先yaml.safe_load(f)[sub]提取到下一层的数据，但由于是dict
                要通过yaml.dump转化成yml格式的字符串，经过Template来改变变量，最后在yaml.safe_load转化成dict
                '''
                return yaml.safe_load(Template(yaml.dump(yaml.safe_load(f)[sub])).substitute(data))
                # 错误的写法：return yaml.safe_load(Template(f.read()).substitute(data))

    #
    def send_api_data(self, path, p_data, sub):
        """
        1.进一步优化封装请求，是本框架的第二个核心技术要点
        2.解决了如何非必填字段的问题，接口测试的非必填字段，只需要传入None值就好
        2.1 本方法就是解决如何传入None的问题
        :param path: 存放yml的api数据的相对路径
        :param p_data: Template模板里面，二次转化的数据
        :param sub: yml的二级数据目录，区别同一个api类中不同的api方法，比如add，delete
        :return: 返回请求体的字典类型
        """
        # 链接根路径和yml文件的相对路径，简化文件路径
        path = os.path.join(self.Base_Path, path)
        # 获取请求数据
        data: dict = self.template(path, p_data, sub)
        log.info(f"api模板改变的参数为：{p_data}")
        # 由于Template转化的数据都是字符串，None也会变成'None'，通过下面的方法解决这个问题
        # 防止有些请求没有请求体的，不然就报错了
        try:
            for i in data['json'].keys():
                if data['json'][i] == 'None':
                    data['json'][i] = None
        except:
            pass
        log.info(f"修改后的请求为：{data}")
        res = self.send_api(data)
        log.info((f"响应为：{res}"))
        return res


if __name__ == "__main__":
    pass
