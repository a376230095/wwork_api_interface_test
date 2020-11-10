# @Author : TongTong

from api.base_api import BaseApi
from common.config import cf


class Wework(BaseApi):
    """
    获取企业微信的access_token，后续应该得写在BaseApi的父类，这个类没啥必要了

    CORP_ID:企业微信的企业id
    """
    # 通过配置文件获取企业微信的id
    CORP_ID = cf.get_key("wwork", "corp_id")


    def get_token(self, secret):
        """
        获取access_token，不同的应用的秘钥，会产生不同的access_token，所以就封装起来了
        :param secret: 企业微信不同也应用的密码
        :return: access_token的值
        """
        data = {
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": f"corpid={self.CORP_ID}&corpsecret={secret}"
        }
        # 使用send_api，传入data，相当于使用了requests了
        res = self.send_api(data)
        # 获取access_token
        token = res["access_token"]
        return token


if __name__ == "__main__":
    a = Wework()
    print(a.get_token("YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"))