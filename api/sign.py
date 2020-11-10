# @Author : TongTong

from api.base_api import BaseApi


class Sign(BaseApi):
    """
    联系人和部门标签的api类
    """

    # 获取所有标签
    def get_all_sign(self, token):
        # Template模板二次修改的值，p_data
        p_data = {"ip": self.ip, "token": token}
        res = self.send_api_data("data/sign/sign_api.yml", p_data, "get_all_sign")
        return res

    # 获取用户标签
    def get_member_sign(self, token, tagid):
        p_data = {"ip": self.ip, "token": token, "tagid": tagid}
        res = self.send_api_data("data/sign/sign_api.yml", p_data, "get_member_sign")
        return res

    # 增加标签
    def add_sign(self, token, tagname, tagid):
        p_data = {"ip": self.ip, "token": token, "tagname": tagname, "tagid": tagid}
        res = self.send_api_data("data/sign/sign_api.yml", p_data, "add_sign")
        return res

    # 删除标签
    def delete_sign(self, token, tagid):
        p_data = {"ip": self.ip, "token": token, "tagid": tagid}
        res = self.send_api_data("data/sign/sign_api.yml", p_data, "delete_sign")
        return res

    # 用户增加标签信息
    def add_sign_to_member(self, token, tagid, userlist):
        p_data = {"ip": self.ip, "token": token, "tagid": tagid, "userlist": userlist}
        res = self.send_api_data("data/sign/sign_api.yml", p_data, "add_sign_to_member")
        return res

    # 编辑标签
    def edit_sign(self, token, tagname, tagid):
        p_data = {"ip": self.ip, "token": token, "tagname": tagname, "tagid": tagid}
        res = self.send_api_data("data/sign/sign_api.yml", p_data, "edit_sign")
        return res

    # 用户删除标签
    def delete_sign_to_member(self, token, tagid, userlist):
        p_data = {"ip": self.ip, "token": token, "tagid": tagid, "userlist": userlist}
        res = self.send_api_data("data/sign/sign_api.yml", p_data, "delete_sign_to_member")
        return res


if __name__ == "__main__":
    a = Sign()
    print(a.get_all_sign("None"))
    # print(a.add_sign(a.token,"add1",1))
    # print(a.edit_sign(a.token,"add2",1))
    # print(a.add_sign_to_member(a.token,1,["tong"]))
    # print(a.get_member_sign(a.token,1))
    # print(a.delete_sign_to_member(a.token,1,["tong"]))
    # print(a.delete_sign(a.token,1))
