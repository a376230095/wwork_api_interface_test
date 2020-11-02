import os

import pytest

from api.base_api import BaseApi
from common.get_log import log

a=BaseApi()
data=a.load_yaml("data/member/member_para_data.yml")["delete"]["data"]
ids=a.load_yaml("data/member/member_para_data.yml")["delete"]["ids"]
log.info(data)
# ids=[
#     "通通","通通","通通","通通","通通","通通","通通"
# ]
@pytest.mark.parametrize(("a,b,c,d,e"),data,ids=ids)
def test(a,b,c,d,e):
    print(a,b,c,d,e)
    assert False

def test_b():
    assert 4 !=3
