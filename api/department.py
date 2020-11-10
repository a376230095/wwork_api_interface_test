# @Author : TongTong

import os
from api.base_api import BaseApi
from api.wework import Wework
from common.config import cf

secret = cf.get_key("wwork", "contact_secret")
token = Wework().get_token(secret)


class Department(BaseApi):
    """
    部门的API类
    """

    def get_depart(self, token, id):
        """
        获取部门信息
        :param token: token值
        :param id: 部门id
        :return: 返回响应体
        """
        # Template模板二次修改的值，p_data
        p_data = {"ip": self.ip, "token": token, "id": id}
        res = self.send_api_data("data/department/department_api.yml", p_data, "get")
        return res

    def add_depart(self, token, parentid, name):
        """
        增加部门
        :param token: token值
        :param parentid: 父部门id
        :param name: 部门名
        :return: 返回响应体
        """
        p_data = {"ip": self.ip, "token": token, "parentid": parentid, "name": name}
        res = self.send_api_data("data/department/department_api.yml", p_data, "add")
        return res

    def delete_depart(self, token, id):
        """
        删除部门信息
        :param token: token值
        :param id: 部门id
        :return: 返回响应体
        """
        p_data = {"ip": self.ip, "token": token, "id": id}
        res = self.send_api_data("data/department/department_api.yml", p_data, "delete")
        return res

    def edit_depart(self, token, id, name):
        """
        编辑部门部门
        :param token: token值
        :param parentid: 父部门id
        :param name: 部门名
        :return: 返回响应体
        """
        p_data = {"ip": self.ip, "token": token, "id": id, "name": name}
        res = self.send_api_data("data/department/department_api.yml", p_data, "edit")
        return res


if __name__ == "__main__":
    a = Department()
    print(a.get_depart(token,1))
    # print(a.add_depart(1, "tong"))
    # print(a.edit_depart(3,"aaa"))
