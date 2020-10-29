from api.base_api import BaseApi
from api.wework import Wework

# 企业微信标签的api类
class Tag(BaseApi):
    # 这是标签的秘钥
    secret="MDe1km8BK3AZ05Dnfw4uILuKCZDStZ2NPaokf-UE6c8"
    # 通过get_token获取到标签的access_token
    token=Wework().get_token(secret)

    # 这是增加标签的api，传一个tag_name
    def add_tag(self,name):
        # data={
        #     "method":"post",
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?",
        #     "params":f"access_token={self.token}",
        #     "json":{
        #         "group_id": "etMCs1DwAAg_jBNAuvGR3B21cwl4o0jg",
        #         "tag":[{"name":name}]
        #    }
        # }

        # 现在要把add_tag的数据都放到yaml文件上去
        # 但这种写法比较low，也不好控制和管理
        # data=self.load_yaml("../data/tag_add.yml")
        # print(data["params"])
        # data["params"]=f"access_token={self.token}"
        # data["json"]["tag"][0]['name']=name

        # 把请求的数据都放到yml文件，通过template模板把yml文件特定的值改成变量
        data=self.template("../data/tag_add.yml",{"token":self.token,"name":name})
        # 返回响应的dict
        return self.send_api(data)

    # 这是获取tag相关信息的api
    def get_tag(self):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params":f"access_token={self.token}",
            "json":{
                "tag":[]
            }
        }
        return self.send_api(data)

    # 修改tag名字，需要传tag_id和修改后的名字
    def edit_tag(self,tag_id,edit_name):
        data={
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params":f"access_token={self.token}",
            "json":{
                "id":tag_id,
                "name":edit_name
            }
        }
        return self.send_api(data)

    # 这是删除标签的api，需要传tag_id
    def delete_tag(self,tag_id):
        # data={
        #     "method":"post",
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
        #     "params":f"access_token={self.token}",
        #     "json":{
        #         "tag_id":[tag_id]
        #     }
        # }
        data=self.template("../data/tag_all.yml",{"token":self.token,"tag_id":tag_id},"delete")
        return self.send_api(data)


if __name__=="__main__":
    pass
    # a=Tag().add_tag("zzz")

    # a=Tag()
    # print(a.add_tag("tongtong2"))