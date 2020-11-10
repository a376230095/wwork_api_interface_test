# @Author : TongTong

import pytest
from api.department import Department

# 新建部门api的类的对象
depart = Department()


# 冒烟测试的前置和后置步骤，token值是上一级conftest提供的fixture方法
@pytest.fixture(scope="session")
def depart_smoke(token):
    depart.delete_depart(token, 5)
    depart.delete_depart(token, 6)
    depart.delete_depart(token, 7)
    depart.add_depart(token, 1, "smoke1")
    yield
    depart.delete_depart(token, 5)
    depart.delete_depart(token, 6)

# 增加部门的前后置步骤
@pytest.fixture(scope="session")
def add_depart(token):
    depart.delete_depart(token, 5)
    depart.delete_depart(token, 6)
    yield
    depart.delete_depart(token, 5)

# 编辑部门的前后置步骤
@pytest.fixture(scope="session")
def edit_depart(token):
    depart.add_depart(token, 1, "smoke2")
    yield
    depart.delete_depart(token, 5)

# 删除部门的前后置步骤
@pytest.fixture(scope="session")
def delete_depart(token):
    depart.add_depart(token, 1, "delete")
