import pytest
from api.member import Member
from api.wework import Wework

secret = "YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
token = Wework().get_token(secret)

@pytest.fixture(scope="session")
def pre_data():
    member = Member()
    pre_add_list = [
        ["tongtong1", "tongtong1", "13112661165"],
        ["tongtong2", "tongtong2", "13122661165"],
        ["tongtong3", "tongtong3", "13132661165"],
        ["tong1234"]
    ]

    for i in range(len(pre_add_list)):
        if i <= 2:
            member.add_member(token, pre_add_list[i][0], pre_add_list[i][1], pre_add_list[i][2])
        else:
            member.delete_member(token, pre_add_list[i][0])
