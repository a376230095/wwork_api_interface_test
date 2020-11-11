# @Author : TongTong

import os
import allure
from api.meeting_room import MeetingRoom
from common.get_log import log


class TestMeetingRoom():
    """
    会议室的测试类
    1.没有做参数化
    """

    # 初始化会议室对象
    meeting = MeetingRoom()

    @allure.story("增加会议室的冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_metting_room_smoke(self, meeting_smoke, token):
        log.info(f"token:{token}")
        log.info("--------开始增加会议室的冒烟测试")
        res = self.meeting.add_meeting_room(token, "smoke1", 30, None, None, None, None)
        log.info("--------开始结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]

    @allure.story("编辑会议室的冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_edit_metting_room_smoke(self, meeting_smoke, token):
        log.info("--------开始编辑会议室的冒烟测试")
        res = self.meeting.edit_meeting_room(token, 2, "edit", None, None, None, None, None)
        log.info("--------开始结束测试")
        assert 0 == res["errcode"]
        assert "updated" in res["errmsg"]

    @allure.story("删除会议室的冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_metting_room_smoke(self, meeting_smoke, token):
        log.info("--------开始删除会议室的冒烟测试")
        res = self.meeting.delete_meeting_room(token, 1)
        log.info("--------开始结束测试")
        assert 0 == res["errcode"]
        assert "deleted" in res["errmsg"]

    @allure.story("获取会议室的冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_get_metting_room_smoke(self, meeting_smoke, token):
        log.info("--------开始获取会议室的冒烟测试")
        res = self.meeting.get_meeting_room(token, None, None, None, None)
        log.info("--------开始结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]
