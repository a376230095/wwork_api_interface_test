from api.base_api import BaseApi


class Sign(BaseApi):
    token="xiUKRjd9wEErUgXifL-n7B9rLhuo11HsY-TU2vsKYw7cBzK8DxDuAfQOu3Pp_0vdqTDVuHJPUfWcV4IZ0uHvgHZe7O2W7hWbb1rnLLqkSUha1dHdhCWImGkPUBchEjI4qJ6_aTjt9n8IOu_S8mvBda-PcqVGswo3VeJRvxL7avV4YsWuz79UWErfEg18s-2azh7drPbvgBVV5QyVyEqkUA"

    def get_all_sign(self,token):
        p_data={"ip":self.ip,"token":token}
        res=self.send_api_data("data/sign/sign_api.yml",p_data,"get_all_sign")
        return res

    def get_member_sign(self,token,tagid):
        p_data={"ip":self.ip,"token":token,"tagid":tagid}
        res=self.send_api_data("data/sign/sign_api.yml",p_data,"get_member_sign")
        return res

    def add_sign(self,token,tagname,tagid):
        p_data={"ip":self.ip,"token":token,"tagname":tagname,"tagid":tagid}
        res=self.send_api_data("data/sign/sign_api.yml",p_data,"add_sign")
        return res

    def delete_sign(self,token,tagid):
        p_data={"ip":self.ip,"token":token,"tagid":tagid}
        res=self.send_api_data("data/sign/sign_api.yml",p_data,"delete_sign")
        return res

    def add_sign_to_member(self,token,tagid,userlist):
        p_data={"ip":self.ip,"token":token,"tagid":tagid,"userlist":userlist}
        res=self.send_api_data("data/sign/sign_api.yml",p_data,"add_sign_to_member")
        return res

    def edit_sign(self,token,tagname,tagid):
        p_data={"ip":self.ip,"token":token,"tagname":tagname,"tagid":tagid}
        res=self.send_api_data("data/sign/sign_api.yml",p_data,"edit_sign")
        return res

    def delete_sign_to_member(self,token,tagid,userlist):
        p_data={"ip":self.ip,"token":token,"tagid":tagid,"userlist":userlist}
        res=self.send_api_data("data/sign/sign_api.yml",p_data,"delete_sign_to_member")
        return res


if __name__ == "__main__":
    a=Sign()
    print(a.get_all_sign(a.token))
    # print(a.add_sign(a.token,"add1",1))
    # print(a.edit_sign(a.token,"add2",1))
    # print(a.add_sign_to_member(a.token,1,["tong"]))
    # print(a.get_member_sign(a.token,1))
    # print(a.delete_sign_to_member(a.token,1,["tong"]))
    # print(a.delete_sign(a.token,1))