from api.base_api import BaseApi

# 封装企业微信公共的api类，继承BaseApi的公共类
from common.config import cf


class Wework(BaseApi):
    # 通过配置文件获取企业微信的id
    corpid=cf.get_key("wwork","corp_id")
    # 获取access_token，不同的应用的秘钥，会产生不同的access_token，所以就封装起来了
    def get_token(self,secret):
        data={
            "method":"GET",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?",
            "params":f"corpid={self.corpid}&corpsecret={secret}"
        }
        # 使用send_api，传入data，相当于使用了requests了
        res= self.send_api(data)
        # 获取access_token
        token=res["access_token"]
        return token

if __name__=="__main__":
    a=Wework()
    print(a.get_token("YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"))