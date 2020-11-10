# @Author : TongTong

import pytest
from api.member import Member
from api.sign import Sign

sign=Sign()
member=Member()

@pytest.fixture(scope="session")
def smoke(token):
    # 先执行删除操作
    sign.delete_sign(token, 13)
    sign.delete_sign(token,1)
    sign.add_sign(token,"add10",10)
    sign.add_sign(token, "add11", 11)
    yield
    sign.delete_sign(token,10)
    sign.delete_sign(token, 13)

@pytest.fixture(scope="session")
def add_sign(token):
    sign.delete_sign(token,1)
    sign.delete_sign(token,2)
    sign.delete_sign(token,10)
    sign.delete_sign(token,11)
    sign.delete_sign(token,12)
    sign.delete_sign(token,13)
    sign.delete_sign(token,14)
    yield
    sign.delete_sign(token,1)
    sign.delete_sign(token,2)
    sign.delete_sign(token,10)
    sign.delete_sign(token,11)
    sign.delete_sign(token,12)
    sign.delete_sign(token,13)
    sign.delete_sign(token,14)


@pytest.fixture(scope="session")
def edit_sign(token):
    sign.add_sign(token,"add10",1)
    sign.add_sign(token,"addd",20)
    yield
    sign.delete_sign(token,1)
    sign.delete_sign(token,20)

@pytest.fixture(scope="session")
def get_sign(token):
    sign.add_sign(token,"add10",1)
    yield
    sign.delete_sign(token,1)

@pytest.fixture(scope="session")
def add_sign_to_member(token):
    member.add_member(token,"sign1","sign1","13999999909")
    member.add_member(token,"sign2","sign2","13999999919")
    member.add_member(token,"sign3","sign3","13999999929")
    member.add_member(token,"sign4","sign4","13999999939")
    member.add_member(token,"sign5","sign5","13999999949")
    member.add_member(token,"sign6","sign6","13999999959")
    member.add_member(token,"sign7","sign7","13999999969")
    member.add_member(token,"sign8","sign8","13999999979")
    member.add_member(token,"sign9","sign9","13999999989")
    sign.add_sign(token,"sign1",1)
    yield
    sign.delete_sign(token,1)
    sign.delete_sign_to_member(token,1,["sign1","sign2","sign7","sign8"])

@pytest.fixture(scope="session")
def delete_sign_to_member(token):
    sign.add_sign(token,"delete1",1)
    sign.add_sign_to_member(token,1,["sign1","sign2","sign3","sign4"])
    yield
    sign.delete_sign(token,1)
    sign.delete_sign_to_member(token,1,["sign1","sign2","sign3","sign4"])




# @pytest.fixture(scope="session")
# def add_sign(token):
#     sign.delete_sign(token,1)
#
# @pytest.fixture(scope="session")
# def add_sign(token):
#     sign.delete_sign(token,1)
#
