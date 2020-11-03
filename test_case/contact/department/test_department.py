import os
import allure
import pytest

from api.department import Department
from common.get_log import log


class TestDepartment():
    depart = Department()
    base_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    base_path=os.path.dirname(base_path)
    para_path=os.path.join(base_path,"data/department/para_department.yml")
    para_data=depart.load_yaml(para_path)


    add_data=para_data["add"]["data"]
    add_ids=para_data["add"]["ids"]

    get_data=para_data["get"]["data"]
    get_ids=para_data["get"]["ids"]

    delete_data=para_data["delete"]["data"]
    delete_ids=para_data["delete"]["ids"]

    edit_data=para_data["edit"]["data"]
    edit_ids=para_data["edit"]["ids"]



    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(("parentid,name,errcode,errmsg"),add_data,ids=add_ids)
    def test_add_depart(self, token,parentid,name,errcode,errmsg,add_depart):
        log.info("-------------开始增加部门测试---------")
        res = self.depart.add_depart(token,parentid ,name)
        log.info("-------------测试结束---------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("id,errcode,errmsg"), get_data,ids=get_ids)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_depart(self, token, id,errcode,errmsg):
        log.info("-------------开始获取部门测试---------")
        res = self.depart.get_depart(token, id)
        log.info("-------------测试结束---------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("id,name,errcode,errmsg"), edit_data,ids=edit_ids)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_depart(self, token,id,name,errcode,errmsg,edit_depart):
        log.info("-------------开始编辑部门测试---------")
        res = self.depart.edit_depart(token, id, name)
        log.info("-------------测试结束---------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("id,errcode,errmsg"),delete_data,ids=delete_ids)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_depart(self, token, id,errcode,errmsg,delete_depart):
        log.info("-------------开始删除部门测试---------")
        res = self.depart.delete_depart(token, id)
        log.info("-------------测试结束---------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]


    @allure.severity(allure.severity_level.BLOCKER)
    def testa_add_depart(self,token,depart_smoke):
        log.info("-------------开始冒烟增加部门测试---------")
        res=self.depart.add_depart(token,1,"smoke")
        log.info("-------------测试结束---------")
        assert res["errcode"] == 0
        assert "created" in res["errmsg"]

    @allure.severity(allure.severity_level.BLOCKER)
    def testb_get_depart(self,token,depart_smoke):
        log.info("-------------开始冒烟获得部门测试---------")
        res=self.depart.get_depart(token,3)
        log.info("-------------测试结束---------")
        assert res["errcode"] == 0
        assert "" in res["errmsg"]

    @allure.severity(allure.severity_level.BLOCKER)
    def testc_edit_depart(self,token,depart_smoke):
        log.info("-------------开始冒烟编辑部门测试---------")
        res=self.depart.edit_depart(token,4,"edit")
        log.info("-------------测试结束---------")
        assert res["errcode"] == 0
        assert "updated" in res["errmsg"]

    @allure.severity(allure.severity_level.BLOCKER)
    def testd_delete_depart(self,token,depart_smoke):
        log.info("-------------开始删除部门冒烟测试---------")
        res=self.depart.delete_depart(token,5)
        log.info("-------------测试结束---------")
        assert res["errcode"] == 0
        assert "deleted" in res["errmsg"]




