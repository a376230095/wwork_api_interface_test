import allure
import pytest
from api.member import Member
from api.wework import Wework
from common.config import cf
from common.get_log import log

@allure.feature("通讯录人员的增删改查等接口测试")
class TestMember():
    # 通过配置文件获取联系人的secret
    contact_secret=cf.get_key("wwork","contact_secret")
    # 获取access_token
    token = Wework().get_token(contact_secret)
    # 初始化member的api对象
    member = Member()

    '''
    这样获取数据的方法，要读取两次文件，速度太慢了
    add_data = member.load_yaml("data/member/member_para_data.yml")['add']['data']
    add_ids = member.load_yaml("data/member/member_para_data.yml")['add']['ids']
    '''
    # 参数化的数据
    para_data = member.load_yaml("data/member/member_para_data.yml")

    # 删除用例的参数化数据和ids标题数据
    delete_data = para_data['delete']['data']
    delete_ids = para_data['delete']['ids']
    # 删除用例的参数化数据和ids标题数据
    multi_delete_data = para_data['multi_delete']['data']
    multi_delete_ids = para_data['multi_delete']['ids']
    # 删除用例的参数化数据和ids标题数据
    add_data = para_data['add']['data']
    add_ids = para_data['add']['ids']
    # 删除用例的参数化数据和ids标题数据
    edit_data = para_data['edit']['data']
    edit_ids = para_data['edit']['ids']
    # 删除用例的参数化数据和ids标题数据
    get_data = para_data['get']['data']
    get_ids = para_data['get']['ids']
    # 删除用例的参数化数据和ids标题数据
    active_data = para_data['active']['data']
    active_ids = para_data['active']['ids']
    # 删除用例的参数化数据和ids标题数据
    qr_data = para_data['qr']['data']
    qr_ids = para_data['qr']['ids']
    # 删除用例的参数化数据和ids标题数据
    depart_simple_data = para_data['depart_simple']['data']
    depart_simple_ids = para_data['depart_simple']['ids']
    # 删除用例的参数化数据和ids标题数据
    depart_explicit_data = para_data['depart_explicit']['data']
    depart_explicit_ids = para_data['depart_explicit']['ids']

    #
    # def setup_class(self,):
    #     print("abc")

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("增加联系人")
    @pytest.mark.parametrize(("userid,name,mobile,errcode,errmsg"),add_data,ids=add_ids)
    def test01_add_member(self,userid,name,mobile,errcode,errmsg,add):
        log.info(f"-------开始测试增加成员-------")
        res=self.member.add_member(self.token,userid,name,mobile)
        log.info(f"打印响应结果:{res}")
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("获得联系人信息")
    @pytest.mark.parametrize(("userid,errcode,errmsg"),get_data , ids=get_ids)
    def test02_get_member(self,userid,errcode,errmsg,get):
        log.info("-------开始测试获取成员-------")
        res=self.member.get_member_info(self.token,userid)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("删除联系人")
    @pytest.mark.parametrize(("userid,errcode,errmsg"),delete_data,ids=delete_ids)
    def test04_delete_member(self,userid,errcode,errmsg,delete):
        log.info("-------开始测试获取成员-------")
        res=self.member.delete_member(self.token,userid)
        log.info(f"打印响应结果:{res}")
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("批量删除联系人")
    @pytest.mark.parametrize(("userid_list,errcode,errmsg"), multi_delete_data, ids=multi_delete_ids)
    def test05_multi_delete_member(self,userid_list,errcode,errmsg,multi_delete):
        log.info("-------开始批量删除获取成员-------")
        res=self.member.multi_delete_member(self.token,userid_list)
        log.info(f"打印响应结果:{res}")
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("编辑联系人")
    @pytest.mark.parametrize(("userid,name,mobile,errcode,errmsg"),edit_data,ids=edit_ids)
    def test03_edit_member(self,userid,name,mobile,errcode,errmsg,edit):
        log.info("-------开始修改获取成员-------")
        res=self.member.edit_member(self.token,userid,name,mobile)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("查看企业微信活跃度")
    @pytest.mark.parametrize(("date,errcode,errmsg"), active_data, ids=active_ids)
    def test_active_stat(self,date,errcode,errmsg):
        log.info("-------开始查看企业微信活跃度-------")
        res=self.member.get_active_stat(self.token,date)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("增加联系人")
    @pytest.mark.parametrize(("size,errcode,errmsg"), qr_data, ids=qr_ids)
    def test_get_invite_qr(self,size,errcode,errmsg):
        log.info("-------开始获取企业微信二维码-------")
        res=self.member.get_invite_qr(self.token,size)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("查看部门联系人的简单信息")
    @pytest.mark.parametrize(("department_id,fetch_child,errcode,errmsg"),depart_simple_data,ids=depart_simple_ids)
    def test_get_depart_member(self,department_id,fetch_child,errcode,errmsg):
        log.info("-------开始获取部门成员简单的信息-------")
        res=self.member.get_depart_member(self.token,department_id,fetch_child)
        log.info(f"打印响应结果:{res}" )
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("查看部门联系人的复杂信息")
    @pytest.mark.parametrize(("department_id,fetch_child,errcode,errmsg"), depart_explicit_data, ids=depart_explicit_ids)
    def test_get_depart_member_explict(self,department_id,fetch_child,errcode,errmsg):
        log.info("-------开始部门成员详细信息-------")
        res = self.member.get_depart_member_explicit(self.token,department_id,fetch_child)
        log.info(f"打印响应结果:{res}")
        log.info("-------测试结束-------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("增加联系人")
    @pytest.mark.smoke
    def test_all_smoke_member(self,test_all_pre_data):
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




