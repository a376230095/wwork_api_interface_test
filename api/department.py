import os
from api.base_api import BaseApi
from api.wework import Wework
from common.config import cf
from common.get_log import log

secret=cf.get_key("wwork","contact_secret")
token=Wework().get_token(secret)

class Department(BaseApi):
    base_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    ip=cf.get_key("env","formal_ip")


    def get_depart(self,id=None):
        p_data={"ip":self.ip,"token":token,"id":id}
        res=self.send_api_data("data/department/department_api.yml",p_data,"get")
        return res


if __name__ == "__main__":
    a=Department()
    print(a.get_depart())