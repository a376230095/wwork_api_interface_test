# @Author : TongTong

import pytest
from api.wework import Wework
from common.config import cf

# 获取token值
@pytest.fixture(scope="session")
def schedule_token():
    schedule_secret=cf.get_key("wwork","schedule_secret")
    token= Wework().get_token(schedule_secret)
    return token

