# @Author : TongTong

from api.wework import Wework
from common.config import cf


class Base:
    """
    用类的方式获取token，这样测试类就不用受到fixture中，只有test用例才能拿到token的困扰
    """

    # 获取token
    def get_token(self):
        secret = cf.get_key("wwork", "contact_secret")
        access_token = Wework().get_token(secret)
        return access_token

# 单例模式获取到的token值
contact_token = Base().get_token()

if __name__ == "__main__":
    pass
