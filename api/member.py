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
    # 定义不同测试、生产环境的ip，通过配置文件获取
    env_ip=cf.get_key("env","formal_ip")
    # 定义项目的绝对根路径
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # 封装从yml拿数据，并改变替换yml原本的$变量的数据
    def send_api_data(self,p_data,path):
        # 打印传入template要改变的$变量值
        log.info(f"template传入的p_data：{p_data}")
        # 读取yml文件的路径
        data_path = os.path.join(self.BASE_PATH, path)


        # 改变yml文件的$变量值
        data = self.template(data_path, p_data)
        log.info(f"请求的所有参数：{data}")
        res = self.send_api(data)
        return res

    def add_member(self,token,userid,name,mobile):
        p_data={"token":token,"name":name,"userid":userid,"mobile":mobile}

        data_path = os.path.join(self.BASE_PATH, "data/member/add_member.yml")
        data=self.template(data_path,p_data)
        log.info(data)
        res=self.send_api(data)
        return res

    def get_member_info(self,token,userid):
        p_data={"token":token,"userid":userid}
        data_path = os.path.join(self.BASE_PATH, "data/member/get_member.yml")
        data = self.template(data_path,p_data)
        res = self.send_api(data)
        return res

    def edit_member(self,token,userid,name,mobile):
        p_data={"token":token,"name":name,"userid":userid,"mobile":mobile}
        data_path = os.path.join(self.BASE_PATH, "data/member/edit_member.yml")
        data=self.template(data_path,p_data)
        res=self.send_api(data)
        return res

    def delete_member(self,token,userid):
        p_data={"token":token,"userid":userid}
        data_path = os.path.join(self.BASE_PATH, "data/member/delete_member.yml")
        data = self.template(data_path,p_data)
        log.info(f"请求的参数：{data}")
        res = self.send_api(data)
        return res

    def multi_delete_member(self,token,uesrid_list):
        p_data = {"token": token, "userid_list": uesrid_list}
        data_path = os.path.join(self.BASE_PATH, "data/member/multi_delete_member.yml")
        data = self.template(data_path, p_data)
        res = self.send_api(data)
        return res

    def get_depart_member(self,token,department_id,fetch_child):
        p_data = {"token": token, "department_id": department_id,"fetch_child":fetch_child}
        log.info(p_data)
        data_path = os.path.join(self.BASE_PATH, "data/member/get_depart_member.yml")
        data = self.template(data_path, p_data)
        log.info(data)
        res = self.send_api(data)
        return res

    def get_depart_member_explicit(self,token,department_id,fetch_child):
        p_data = {"token": token, "department_id": department_id,"fetch_child":fetch_child}
        log.info(p_data)
        data_path = os.path.join(self.BASE_PATH, "data/member/get_depart_member_explicit.yml")
        data = self.template(data_path, p_data)
        log.info(data)
        res = self.send_api(data)
        return res

    def get_invite_qr(self,token,size_type):
        p_data = {"token": token,"size_type":size_type}
        res=self.send_api_data(p_data,"data/member/get_invite_qr.yml")
        # p_data = {"token": token, "size_type": size_type}
        # data_path = os.path.join(self.BASE_PATH, "data/member/get_invite_qr.yml")
        # data = self.base.template(data_path, p_data)
        # res = self.send_api(data)
        return res

    def get_active_stat(self,token,date):
        p_data = {"ip":self.env_ip,"token": token, "date": date}
        res=self.send_api_data(p_data,"data/member/get_active_stat.yml")
        return res



if __name__=="__main__":
    a=Member()
    # print(a.get_depart_member_explicit(1,""))
    # print(a.get_invite_qr(1))
    print(a.get_active_stat("1"))


