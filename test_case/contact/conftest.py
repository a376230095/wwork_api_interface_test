# @Author : TongTong

import pytest
from api.wework import Wework
from common.config import cf

# 获取到token值，给其他下层目录的测试用例使用，优化代码
@pytest.fixture(scope="session")
def token():
    secret = cf.get_key("wwork", "contact_secret")
    access_token = Wework().get_token(secret)
    return access_token
