import os
from api.base_api import BaseApi
from api.wework import Wework
from common.config import cf

secret=cf.get_key("wwork","contact_secret")
token=Wework().get_token(secret)

class Department(BaseApi):
    base_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ip=cf.get_key("env","formal_ip")

    def get_depart(self,token,id):
        p_data={"ip":self.ip,"token":token,"id":id}
        res=self.send_api_data("data/department/department_api.yml",p_data,"get")
        return res

    def add_depart(self,token,parentid,name):
        p_data={"ip":self.ip,"token":token,"parentid":parentid,"name":name}
        res=self.send_api_data("data/department/department_api.yml",p_data,"add")
        return res

    def delete_depart(self,token,id):
        p_data={"ip":self.ip,"token":token,"id":id}
        res=self.send_api_data("data/department/department_api.yml",p_data,"delete")
        return res

    def edit_depart(self,token,id,name):
        p_data={"ip":self.ip,"token":token,"id":id,"name":name}
        res=self.send_api_data("data/department/department_api.yml",p_data,"edit")
        return res


if __name__ == "__main__":
    a=Department()
    # print(a.get_depart())
    # print(a.add_depart(1, "tong"))
    # print(a.edit_depart(3,"aaa"))