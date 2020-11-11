# @Author : TongTong

import allure
from api.schedule.wschedule import WSchedule
from common.get_log import log


class TestSchedule():
    """
    日程的测试类
    1.没有做参数化
    """

    # 初始化日程对象
    schedule = WSchedule()

    @allure.story("增加日程冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_calendar_smoke(self, schedule_token):
        log.info("--------开始增加日程冒烟测试")
        res = self.schedule.add_schedule(schedule_token, "schedule", "2020-10-01 00:00:00", "2020-10-02 00:00:00",
                                         "calendar", "abc", None, None)
        log.info("--------结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]

    @allure.story("编辑日程冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_edit_calendar_smoke(self, schedule_token):
        log.info("--------开始编辑日程冒烟测试")
        res = self.schedule.edit_schedule(schedule_token, "schedule", 1, "2020-10-01 00:00:00", "2020-10-02 00:00:00",
                                          "calendar", "abc", None, None)
        log.info("--------结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]

    @allure.story("获取日程冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_get_calendar_smoke(self, schedule_token):
        log.info("--------开始获取日程冒烟测试")
        res = self.schedule.get_schedule(schedule_token)
        log.info("--------结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]

    @allure.story("删除日程冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_calendar_smoke(self, schedule_token):
        log.info("--------开始删除日程冒烟测试")
        res = self.schedule.delete_schedule(schedule_token, 0)
        log.info("--------结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]
