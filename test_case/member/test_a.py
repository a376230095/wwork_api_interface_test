import os

import pytest

from api.base_api import BaseApi
from common.get_log import log

a=BaseApi()
data=a.load_yaml("data/member/member_para_data.yml")["add"]
log.info(data)
@pytest.mark.parametrize(("a,b,c,d,e"),data)
def test(a,b,c,d,e):
    print(a,b,c,d,e)

def test_b():
    assert 4 !=3