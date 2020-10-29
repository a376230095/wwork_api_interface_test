import pytest

from api.member import Member
from api.wework import Wework

from common.get_log import log

class TestMember():
    secret="YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
    token = Wework().get_token(secret)
    member = Member()
    add_data = member.load_yaml("data/member/member_para_data.yml")['add']


    def setup_class(self):
        # add的数据准备
        self.member.delete_member(self.token,"tong")
        pass



    @pytest.mark.parametrize(("userid,name,mobile,errcode,errmsg"),add_data)
    def test01_add_member(self,userid,name,mobile,errcode,errmsg):
        log.info("-------开始测试增加成员-------")

        res=self.member.add_member(self.token,userid,name,mobile)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert res["errmsg"] == errmsg

    def test02_get_member(self):
        log.info("-------开始测试获取成员-------")
        userid="tong1234"
        res=self.member.get_member_info(self.token,userid)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == 0

    def test04_delete_member(self):
        log.info("-------开始测试获取成员-------")
        userid="tong12345"
        res=self.member.delete_member(self.token,userid)
        log.info(f"打印响应结果:{res}")
        log.info("-------测试结束-------")
        assert res["errcode"] == 0

    def test05_multi_delete_member(self):
        log.info("-------开始批量删除获取成员-------")
        user_list=["tongtong1","tongtong2","tongtong3"]
        res=self.member.multi_delete_member(self.token,user_list)
        log.info("打印响应结果:res")
        log.info("-------测试结束-------")
        assert res["errcode"] == 0

    def test03_edit_member(self):
        log.info("-------开始批量删除获取成员-------")
        userid="tong1234"
        name="tong1234"
        mobile="13172771165"
        res=self.member.edit_member(self.token,userid,name,mobile)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == 0

    def test_active_stat(self):
        log.info("-------开始查看企业微信活跃度-------")
        date="2020-10-10"
        res=self.member.get_active_stat(self.token,date)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == 0

    def test_get_invite_qr(self):
        log.info("-------开始获取企业微信二维码-------")
        size_type=1
        res=self.member.get_invite_qr(self.token,size_type)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == 0

    def test_get_depart_member(self):
        log.info("-------开始获取部门成员简单的信息-------")
        department_id="1"
        fetch_child="1"
        res=self.member.get_depart_member(self.token,department_id,fetch_child)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == 0

    def test_get_depart_member_explict(self):
        log.info("-------开始部门成员详细信息-------")
        department_id="1"
        fetch_child="1"
        res = self.member.get_depart_member_explicit(self.token,department_id,fetch_child)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == 0

    @pytest.mark.smoke
    def test_all_smoke_member(self,pre_data):
        add_res=self.member.add_member(self.token,"tong1234","tong1234","13172771165")
        edit_res=self.member.edit_member(self.token,"tong1234","tong1234","13172771165")
        del_res=self.member.delete_member(self.token,"tong1234")
        multi_del_res=self.member.multi_delete_member(self.token,["tongtong1","tongtong2","tongtong3"])
        qr_res=self.member.get_invite_qr(self.token,1)
        active_res=self.member.get_active_stat(self.token,"2020-10-10")
        depart_res=self.member.get_depart_member(self.token,"1","1")
        depart_res_e = self.member.get_depart_member_explicit(self.token,"1", "1")
        assert add_res["errcode"] == 0
        assert edit_res["errcode"] == 0
        assert del_res["errcode"] == 0
        assert multi_del_res["errcode"] == 0
        assert qr_res["errcode"] == 0
        assert active_res["errcode"] == 0
        assert depart_res["errcode"] == 0
        assert depart_res_e["errcode"] == 0
        log.info("finish")




    def tear_down(self):
        pass




