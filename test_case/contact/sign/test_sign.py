# @Author : TongTong

import os
import allure
import pytest
from api.sign import Sign
from common.get_log import log
from test_case.contact.common_data import contact_token

class TestSign():
    base_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

    sign=Sign()
    data_path=os.path.join(base_path,"data/sign/sign_para.yml")

    # 参数化的数据
    sign_data=sign.template(data_path,{"token":contact_token})

    add_data=sign_data["add"]["data"]
    add_ids=sign_data["add"]["ids"]

    edit_data=sign_data["edit"]["data"]
    edit_ids=sign_data["edit"]["ids"]

    get_data=sign_data["get"]["data"]
    get_ids=sign_data["get"]["ids"]

    get_all_sign_data=sign_data["get_all_sign"]["data"]
    get_all_sign_ids=sign_data["get_all_sign"]["ids"]

    add_sign_to_member_data=sign_data["add_sign_to_member"]["data"]
    add_sign_to_member_ids=sign_data["add_sign_to_member"]["ids"]

    delete_data=sign_data["delete"]["data"]
    delete_member_ids=sign_data["delete"]["ids"]

    delete_sign_to_member_data=sign_data["delete_sign_to_member"]["data"]
    delete_sign_to_member_ids=sign_data["delete_sign_to_member"]["ids"]


    @pytest.mark.parametrize(("token1,tagid,tagname,errcode,errmsg"),add_data,ids=add_ids)
    @allure.story("增加标签测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add(self,token1,tagid,tagname,errcode,errmsg,add_sign):
        log.info("--------开始增加标签测试")
        res= self.sign.add_sign(token1,tagname,tagid)
        log.info("--------结束测试")
        assert errcode ==res["errcode"]
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("token1,errcode,errmsg"),get_all_sign_data,ids=get_all_sign_ids)
    @allure.story("查看所有的标签")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_sign(self,token1,errcode,errmsg):
        log.info("--------开始测试冒烟")
        res= self.sign.get_all_sign(token1)
        log.info("--------开始结束测试")
        assert errcode ==res["errcode"]
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("token1,tagid,tagname,errcode,errmsg"),edit_data,ids=edit_ids)
    @allure.story("编辑标签")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit(self,token1,tagid,tagname,errcode,errmsg,edit_sign):
        log.info("--------开始测试冒烟")
        res= self.sign.edit_sign(token1,tagname,tagid)
        log.info("--------开始结束测试")
        assert errcode ==res["errcode"]
        assert errmsg in res["errmsg"]


    @pytest.mark.parametrize(("token1,tagid,errcode,errmsg"),get_data,ids=get_ids)
    @allure.story("获取标签。通过tagid")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get(self,token1,tagid,errcode,errmsg,get_sign):
        log.info("--------开始测试冒烟")
        res= self.sign.get_member_sign(token1,tagid)
        log.info("--------开始结束测试")
        assert errcode ==res["errcode"]
        assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("token1,tagid,userlist,errcode,errmsg"),add_sign_to_member_data,ids=add_sign_to_member_ids)
    @allure.story("把标签添加到用户上")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_sign_to_member(self,token1,tagid,userlist,errcode,errmsg,add_sign_to_member):
        log.info("--------开始测试冒烟")
        res= self.sign.add_sign_to_member(token1,tagid,userlist)
        log.info("--------开始结束测试")
        assert errcode ==res["errcode"]
        assert errmsg in res["errmsg"]

    # @pytest.mark.parametrize(("token1,tagid,userlist,errcode,errmsg"),delete_sign_to_member_data,ids=delete_sign_to_member_ids)
    # @allure.story("删除用户的标签")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_delete_sign_to_member(self,token1,tagid,userlist,errcode,errmsg,delete_sign_to_member):
    #     log.info("--------开始删除用户的标签测试")
    #     res= self.sign.delete_sign_to_member(token1,tagid,userlist)
    #     log.info("--------开始结束测试")
    #     assert errcode ==res["errcode"]
    #     assert errmsg in res["errmsg"]

    @pytest.mark.parametrize(("token1,tagid,userlist,errcode,errmsg,invalidlist"),delete_sign_to_member_data,ids=delete_sign_to_member_ids)
    @allure.story("删除用户的标签")
    @allure.severity(allure.severity_level.CRITICAL)
    def test(self,token1,tagid,userlist,errcode,errmsg,delete_sign_to_member,invalidlist):
        log.info("--------开始删除用户的标签测试")
        res= self.sign.delete_sign_to_member(token1,tagid,userlist)
        log.info("--------开始结束测试")
        assert errcode ==res["errcode"]
        assert errmsg in res["errmsg"]
        if self.sign.jsonpath(res,"$.invalidlist"):
            assert invalidlist in self.sign.jsonpath(res,"$.invalidlist")


    #
    # @pytest.mark.parametrize(("token,errcode,errmsg"),,ids=)
    # @allure.story("")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test(self,):
    #     log.info("--------开始测试冒烟")
    #     res= self.sign
    #     log.info("--------开始结束测试")
    #     assert errcode ==res["errcode"]
    #     assert errmsg in res["errmsg"]



    @allure.story("增加标签的冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_smoke(self,smoke):
        log.info("--------开始增加标签的冒烟测试")
        res= self.sign.add_sign(contact_token,"add1",13)
        log.info("--------开始结束测试")
        assert 0==res["errcode"]
        assert "created" in res["errmsg"]

    @allure.story("获取所有标签信息冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_get_all_sign_smoke(self):
        log.info("--------开始测试冒烟获取所有标签信息")
        res= self.sign.get_all_sign(contact_token)
        log.info("--------开始结束测试")
        assert 0==res["errcode"]
        assert "ok" in res["errmsg"]

    @allure.story("编辑标签名字冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_edit_smoke(self,smoke):
        log.info("--------开始测试冒烟编辑标签名字")
        res= self.sign.edit_sign(contact_token,"add20",10)
        log.info("--------开始结束测试")
        assert 0 == res["errcode"]
        assert "updated" in res["errmsg"]

    @allure.story("删除标签冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_smoke(self):
        log.info("--------开始测试冒烟删除标签")
        res= self.sign.delete_sign(contact_token,11)
        log.info("--------结束测试")
        assert 0==res["errcode"]
        assert "deleted" in res["errmsg"]

    @allure.story("标签加入到用户上的冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_sign_to_member_smoke(self,smoke):
        log.info("--------开始标签加入到用户上的冒烟测试")
        res= self.sign.add_sign_to_member(contact_token,10,["sign"])
        log.info("--------开始结束测试")
        assert 0==res["errcode"]
        assert "ok" in res["errmsg"]

    @allure.story("删除用户名的标签的冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_sign_to_smoke(self,smoke):
        log.info("--------开始测试删除用户名的标签冒烟测试")
        res= self.sign.delete_sign_to_member(contact_token,10,["sign"])
        log.info("--------开始结束测试")
        assert 0==res["errcode"]
        assert "deleted" in res["errmsg"]

    @allure.story("获取标签信息冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_get_smoke(self,smoke):
        log.info("--------开始测试冒烟")
        res= self.sign.get_member_sign(contact_token,10)
        log.info("--------开始结束测试")
        assert 0==res["errcode"]
        assert "ok" in res["errmsg"]

