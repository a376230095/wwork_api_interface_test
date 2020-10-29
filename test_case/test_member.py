from api.member import Member
from common.get_log import log


class TestMember():

    def setup(self):
        self.member=Member()

    def test1_add_member(self):
        userid="tong1234"
        name="tong1234"
        mobile="13172771165"
        res=self.member.add_member(userid,name,mobile)
        log.info(res)
        assert res["errcode"] == 0
