# @Author : TongTong

import os
from api.base_api import BaseApi
from common.config import cf
from common.get_log import log


# 没用的装饰器部分
# def log_test(text=None):
#     def decorate(func):
#         def wrapper(*args,**kargs):
#             logs.info(f"-----------------开始测试{text}用例")
#             res=func(*args,**kargs)
#             logs.info(f"响应结果是：{res}")
#             logs.info(f"-----------------结束测试{text}用例")
#             return res
#         return wrapper
#     return decorate

# 通讯录联系人的公共api类
class Member(BaseApi):
    """
    通讯录的api类，比较low的代码展示，其他api类在不断完善中

    env_ip：测试环境的ip，都可以放到父类
    BASE_PATH：根路径，都可以放到父类
    """
    # 定义不同测试、生产环境的ip，通过配置文件获取
    # 但是这里并没有用到，是比较老的api代码了
    env_ip = cf.get_key("env", "formal_ip")
    # 定义项目的绝对根路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    #
    def send_api_data(self, p_data, path):
        """
        封装从yml拿数据，并改变替换yml原本的$变量的数据
        :param p_data: Template二次转化的变量数据
        :param path: yml_api的路径
        :return:
        """
        # 打印传入template要改变的$变量值
        log.info(f"template传入的p_data：{p_data}")
        # 读取yml文件的路径
        data_path = os.path.join(self.BASE_PATH, path)
        # 改变yml文件的$变量值
        data = self.template(data_path, p_data)
        log.info(f"请求的所有参数：{data}")
        # 获取响应体
        res = self.send_api(data)
        return res

    def add_member(self, token, userid, name, mobile):
        """
        增加联系人，这里代码没有封装，看起来很乱
        :param token: token值
        :param userid: 请求参数的值
        :param name: 请求参数的值
        :param mobile: 请求参数的值
        :return: 返回响应体
        """
        # Template模板二次修改的值，p_data
        p_data = {"token": token, "name": name, "userid": userid, "mobile": mobile}
        # 合并yml_api的文件路径
        data_path = os.path.join(self.BASE_PATH, "data/member/add_member.yml")
        # 通过模板技术获取更改后的请求数据
        data = self.template(data_path, p_data)
        # log日志打印请求体
        log.info(data)
        # 发送封装requests的请求，获取响应值
        res = self.send_api(data)
        return res

    def get_invite_qr(self, token, size_type):
        """
        获取企业微信邀请二维码，代码进行了优化缩减，使用了send_api_data进一个封装代码
        :param token: token值
        :param size_type: 二维码尺寸大小
        :return: 返回响应体
        """
        p_data = {"token": token, "size_type": size_type}
        res = self.send_api_data(p_data, "data/member/get_invite_qr.yml")
        """
        这四行代码用上面的两行代码搞定了
        p_data = {"token": token, "size_type": size_type}
        data_path = os.path.join(self.BASE_PATH, "data/member/get_invite_qr.yml")
        data = self.base.template(data_path, p_data)
        res = self.send_api(data)
        """
        return res

    # 获取企业微信活跃数
    def get_active_stat(self, token, date):
        p_data = {"ip": self.env_ip, "token": token, "date": date}
        res = self.send_api_data(p_data, "data/member/get_active_stat.yml")
        return res

    # 获取企业微信用户数
    def get_member_info(self, token, userid):
        p_data = {"token": token, "userid": userid}
        data_path = os.path.join(self.BASE_PATH, "data/member/get_member.yml")
        data = self.template(data_path, p_data)
        res = self.send_api(data)
        return res

    # 编辑联系人
    def edit_member(self, token, userid, name, mobile):
        p_data = {"token": token, "name": name, "userid": userid, "mobile": mobile}
        data_path = os.path.join(self.BASE_PATH, "data/member/edit_member.yml")
        data = self.template(data_path, p_data)
        res = self.send_api(data)
        return res

    # 删除联系人
    def delete_member(self, token, userid):
        p_data = {"token": token, "userid": userid}
        data_path = os.path.join(self.BASE_PATH, "data/member/delete_member.yml")
        data = self.template(data_path, p_data)
        log.info(f"请求的参数：{data}")
        res = self.send_api(data)
        return res

    # 批量删除联系人
    def multi_delete_member(self, token, uesrid_list):
        p_data = {"token": token, "userid_list": uesrid_list}
        data_path = os.path.join(self.BASE_PATH, "data/member/multi_delete_member.yml")
        data = self.template(data_path, p_data)
        res = self.send_api(data)
        return res

    # 获取部门的联系人信息
    def get_depart_member(self, token, department_id, fetch_child):
        p_data = {"token": token, "department_id": department_id, "fetch_child": fetch_child}
        log.info(p_data)
        data_path = os.path.join(self.BASE_PATH, "data/member/get_depart_member.yml")
        data = self.template(data_path, p_data)
        log.info(data)
        res = self.send_api(data)
        return res

    # 获取部门详细的联系人信息
    def get_depart_member_explicit(self, token, department_id, fetch_child):
        p_data = {"token": token, "department_id": department_id, "fetch_child": fetch_child}
        log.info(p_data)
        data_path = os.path.join(self.BASE_PATH, "data/member/get_depart_member_explicit.yml")
        data = self.template(data_path, p_data)
        log.info(data)
        res = self.send_api(data)
        return res


if __name__ == "__main__":
    a = Member()
    # print(a.get_depart_member_explicit(1,""))
    # print(a.get_invite_qr(1))
    print(a.get_active_stat("1"))
