import pytest
import requests

class TestMember():

    add_tuple=(
        # 都ok的，断言也ok
        [""],
        # userid存在，断言失败
        [],
        []
    )

    def setup(self):
        pass


    def teardown(self):
        pass


    @pytest.mark.parametrize(("userid,name,mobile,errcode,errmsg"),add_tuple)
    def test_add_member(self,userid,name,mobile,errcode,errmsg):
        corpid = "ww4a8d8403cb338c65"
        corpsecret = "y5-95rLakHkBz3b69WqbcUXGPMfgn5k-2WFI1WOs4gM"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        res = requests.get(url=url, params=f"corpid={corpid}&corpsecret={corpsecret}")
        access_token = res.json()["access_token"]
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"
        data = {
            "userid": "tong",
            "name": "tong",
            "mobile": "13172661165",
            "department": [1, 1]
        }
        res = requests.post(url=url, json=data).json()
        print(res)
        assert res["errcode"] == errcode
        assert res["errmsg"] == errmsg