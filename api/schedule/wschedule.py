# @Author : TongTong

from api.base_api import BaseApi
from api.wework import Wework
from common.config import cf
from common.get_log import log
from common.mysql import sql


class WSchedule(BaseApi):
    """
    企业微信日程中的日程模块的API类

    secret：日历的秘钥
    token：日历的token
    yml_api_path: yml api数据的相对路径
    """

    # 通过配置文件获取日历的secret，token只是为了测试方法，其实不应该存在的
    secret = cf.get_key("wwork", "schedule_secret")
    token = Wework().get_token(secret)
    # yml api数据的相对路径
    data_path = "data/schedule/schedule/schedule_api.yml"

    def get_schedule_id_list(self):
        """
        通过数据库，获取日程id的值，日程id的值无法通过接口获取，所以就保存在数据库中
        :return: 返回全部的日历程id的列表
        """
        # 执行sql语句获取日历id的元祖
        schedule_id_list = sql.select("select schedule_id from schedule_id")
        # 把元祖转化成列表
        schedule_id_list = [i[0] for i in schedule_id_list]
        return schedule_id_list

    def add_schedule(self, token, organizer, start_time, end_time, userid, summary, description, location):
        """
        增加日程
        :param token: access_token的值
        :param organizer: 请求参数的值
        :param start_time: 请求参数的值
        :param end_time: 请求参数的值
        :param userid: 请求参数的值
        :param summary: 请求参数的值
        :param description: 请求参数的值
        :param location: 请求参数的值
        :return: 返回响应体
        """
        # 时间传入时间戳，get_time可以将时间字符串转化成时间戳，自己封装的
        start_time = self.get_time(start_time)
        end_time = self.get_time(end_time)
        # Template模板需要二次改变的值
        p_data = {"ip": self.ip, "token": token, "organizer": organizer, "start_time": start_time, "end_time": end_time,
                  "userid": userid, "summary": summary, "description": description, "location": location}
        res = self.send_api_data(self.data_path, p_data, "add")
        try:
            schedule_id = res["schedule_id"]
            # 当cal_id获取到了，就把schedule_id放到数据库中
            sql.insert(f"insert into schedule_id(userid,schedule_id) values('{organizer}','{schedule_id}')")
        except KeyError as e:
            log.error("响应不正确，无法插入数据")
        return res

    def delete_schedule(self, token, index):
        """
        删除日程
        :param token: 日历的token值
        :param index: 在数据库获取第几个id值
        :return: 返回响应体
        """
        # 从数据库获取schedule_id
        schedule_id = self.get_schedule_id_list()[index]
        p_data = {"ip": self.ip, "token": token, "schedule_id": schedule_id}
        res = self.send_api_data(self.data_path, p_data, "delete")
        # 当删除api成功时，同步从数据库中删除schedule_id
        if res["errcode"] == 0:
            sql.delete(f"delete from schedule_id where schedule_id='{schedule_id}'")
        else:
            log.info("删除请求失败，无法删除schedule_id")
        return res

    def get_schedule(self, token, index=None):
        """
        获取日程信息
        :param token: 日程的token值
        :param index: 在数据库获取第几个id值
        :return: 返回响应体
        """
        # 解决index存在的时候，传的schedule_id_list不是一个列表
        schedule_id_list = []
        # 从数据库获取schedule_id_list，才能查询日历
        if index is None:
            schedule_id_list = self.get_schedule_id_list()
        else:
            schedule_id_list.append(self.get_schedule_id_list()[index])
        p_data = {"ip": self.ip, "token": token, "schedule_id_list": schedule_id_list}
        res = self.send_api_data(self.data_path, p_data, "get")
        return res

    def edit_schedule(self, token, organizer, index, start_time, end_time, userid, summary, description, location):
        """

        :param token: 日程的token值
        :param organizer: 请求参数的值
        :param index: 请求参数的值
        :param start_time: 请求参数的值
        :param end_time: 请求参数的值
        :param userid: 请求参数的值
        :param summary: 请求参数的值
        :param description: 请求参数的值
        :param location: 请求参数的值
        :return:
        """
        # 从数据库获取schedule_id
        schedule_id = self.get_schedule_id_list()[index]
        start_time = self.get_time(start_time)
        end_time = self.get_time(end_time)
        p_data = {"ip": self.ip, "token": token, "organizer": organizer, "schedule_id": schedule_id,
                  "start_time": start_time, "end_time": end_time,
                  "userid": userid, "summary": summary, "description": description, "location": location}
        res = self.send_api_data(self.data_path, p_data, "edit")
        return res


if __name__ == "__main__":
    a = WSchedule()
    # a.delete_schedule(a.token,0)
    # print(a.get_schedule_id_list())
    a.add_schedule(a.token,"schedule","2020-10-01 00:00:00","2020-10-02 00:00:00","calendar","abc",None,None)
    # a.edit_schedule(a.token,"schedule",1,"2020-10-01 00:00:00","2020-10-02 00:00:00","calendar","abc",None,None)
    print(a.get_schedule(a.token, 0))
