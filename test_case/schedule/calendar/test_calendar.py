import os
import allure
import pytest
from api.schedule.wcalendar import WCalendar
from common.get_log import log

class TestCalendar():
    base_path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    calendar=WCalendar()

    @allure.story("增加日历冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_calendar_smoke(self,schedule_token):
        log.info("--------增加日历开始冒烟测试")
        res = self.calendar.add_calendar(schedule_token,"calendar",1,0,"test1","0001FF","hehedada")
        log.info("--------结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]

    @allure.story("编辑日历冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_edit_calendar_smoke(self,schedule_token):
        log.info("--------开始编辑日历冒烟测试")
        res = self.calendar.edit_calendar(schedule_token,0,None,"gaigai","1000FF",None)
        log.info("--------结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]

    @allure.story("获取日历冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_get_calendar_smoke(self,schedule_token):
        log.info("--------开始获取日历冒烟测试")
        res = self.calendar.get_calendar(schedule_token)
        log.info("--------结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]

    @allure.story("删除日历冒烟测试")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_calendar_smoke(self,schedule_token):
        log.info("--------开始删除日历冒烟测试")
        res = self.calendar.delete_calendar(schedule_token,0)
        log.info("--------结束测试")
        assert 0 == res["errcode"]
        assert "ok" in res["errmsg"]
































