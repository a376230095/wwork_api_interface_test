# @Author : TongTong

import os
import allure
import pytest
from api.department import Department
from common.get_log import log


class TestDepartment():
    """
    部门的测试类
    1.参数化存放在特定的yml文件中，用三级目录管理用例、参数数据和ids的数据
    2.token值是获取conftest的fixture
    3.并未对token的值做参数化
    4.获取路径的方式有点蠢
    5.critical的用例等级为完整测试，blocker等级为冒烟测试
    6.每个用例都配合fixture，完成了不同的前置和后置，实现了不同用例互不干扰的状态
    """

    # 新建部门的类的对象
    depart = Department()
    # 下面三行代码都是无谓的写法，第五行就可以替代4行代码了
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    base_path = os.path.dirname(base_path)
    para_path = os.path.join(base_path, "data/department/para_department.yml")
    # para_data=depart.load_yaml(para_path)
    # 获取参数化的数据
    para_data = depart.load_yaml("data/department/para_department.yml")

    # 获取不同用例需要的参数化数据以及ids标题数据
    add_data = para_data["add"]["data"]
    add_ids = para_data["add"]["ids"]

    get_data = para_data["get"]["data"]
    get_ids = para_data["get"]["ids"]

    delete_data = para_data["delete"]["data"]
    delete_ids = para_data["delete"]["ids"]

    edit_data = para_data["edit"]["data"]
    edit_ids = para_data["edit"]["ids"]

    #
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(("parentid,name,errcode,errmsg"), add_data, ids=add_ids)
    def test_add_depart(self, token, parentid, name, errcode, errmsg, add_depart):
        log.info("-------------开始增加部门测试---------")
        res = self.depart.add_depart(token, parentid, name)
        log.info("-------------测试结束---------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("id,errcode,errmsg"), get_data, ids=get_ids)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_depart(self, token, id, errcode, errmsg):
        log.info("-------------开始获取部门测试---------")
        res = self.depart.get_depart(token, id)
        log.info("-------------测试结束---------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("id,name,errcode,errmsg"), edit_data, ids=edit_ids)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_depart(self, token, id, name, errcode, errmsg, edit_depart):
        log.info("-------------开始编辑部门测试---------")
        res = self.depart.edit_depart(token, id, name)
        log.info("-------------测试结束---------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("id,errcode,errmsg"), delete_data, ids=delete_ids)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_depart(self, token, id, errcode, errmsg, delete_depart):
        log.info("-------------开始删除部门测试---------")
        res = self.depart.delete_depart(token, id)
        log.info("-------------测试结束---------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.BLOCKER)
    def testa_add_depart(self, token, depart_smoke):
        log.info("-------------开始冒烟增加部门测试---------")
        res = self.depart.add_depart(token, 1, "smoke")
        log.info("-------------测试结束---------")
        assert res["errcode"] == 0
        assert "created" in res["errmsg"]

    @allure.severity(allure.severity_level.BLOCKER)
    def testb_get_depart(self, token, depart_smoke):
        log.info("-------------开始冒烟获得部门测试---------")
        res = self.depart.get_depart(token, 3)
        log.info("-------------测试结束---------")
        assert res["errcode"] == 0
        assert "" in res["errmsg"]

    @allure.severity(allure.severity_level.BLOCKER)
    def testc_edit_depart(self, token, depart_smoke):
        log.info("-------------开始冒烟编辑部门测试---------")
        res = self.depart.edit_depart(token, 4, "edit")
        log.info("-------------测试结束---------")
        assert res["errcode"] == 0
        assert "updated" in res["errmsg"]

    @allure.severity(allure.severity_level.BLOCKER)
    def testd_delete_depart(self, token, depart_smoke):
        log.info("-------------开始删除部门冒烟测试---------")
        res = self.depart.delete_depart(token, 5)
        log.info("-------------测试结束---------")
        assert res["errcode"] == 0
        assert "deleted" in res["errmsg"]
