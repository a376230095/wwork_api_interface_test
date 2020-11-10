# @Author : TongTong

from api.base_api import BaseApi
from api.wework import Wework
from common.config import cf
from common.get_log import log
from common.mysql import sql


class WCalendar(BaseApi):
    """
    企业微信日程中的日历模块的API类

    secret：日历的秘钥
    token：日历的token
    yml_api_path: yml api数据的相对路径
    """

    # 通过配置文件获取日历的secret，token只是为了测试方法，其实不应该存在的
    secret = cf.get_key("wwork", "schedule_secret")
    token = Wework().get_token(secret)
    # yml api数据的相对路径
    yml_api_path = "data/schedule/calendar/calendar_api.yml"

    # 不用yml文件保存cal_id的数据了，放在数据库好啦
    # cal_id_path="data/schedule/calendar/cal_id.yml"

    def get_cal_id_list(self):
        """
        通过数据库，获取日历id的值，日历id的值无法通过接口获取，所以就保存在数据库中
        :return: 返回全部的日历id的列表
        """
        # 执行sql语句获取日历id的元祖
        cal_id_tuple = sql.select("select cal_id from cal_id")
        # 把元祖转化成列表
        cal_id_list = [i[0] for i in cal_id_tuple]
        return cal_id_list

    def add_calendar(self, token, organizer, readonly, set_as_default, summary, color, description):
        """
        添加日历
        :param token: access_token的值
        :param organizer: 请求参数的值
        :param readonly: 请求参数的值
        :param set_as_default: 请求参数的值
        :param summary: 请求参数的值
        :param color: 请求参数的值
        :param description: 请求参数的值
        :return: 返回响应体
        """
        # Template模板需要二次改变的值
        p_data = {"ip": self.ip, "token": token, "organizer": organizer, "readonly": readonly,
                  "set_as_default": set_as_default, "summary": summary, "color": color, "description": description}
        res = self.send_api_data(self.yml_api_path, p_data, "add")
        try:
            cal_id = res["cal_id"]
            # 当cal_id获取到了，就把cal_id放到数据库中
            sql.insert(f"insert into cal_id(userid,cal_id) values('{organizer}','{cal_id}')")
        except KeyError:
            log.error(f"响应不正确，无法插入数据")

        # 用yml文件保存数据的方法不要了
        # try:
        #     cal_id=res["cal_id"]
        #     cal_id_list=self.load_yaml(self.cal_id_path)
        #     cal_id_list.append(cal_id)
        #     cal_id_list=list(filter(None,cal_id_list))
        #     self.save_yaml(self.cal_id_path,cal_id_list)
        # except:
        #     log.info(f"无法获取到cal_id")
        return res

    def get_calendar(self, token, index=None):
        """
        获取日历信息
        :param token: 日历的token值
        :param index: 在数据库获取第几个id值
        :return: 返回响应体
        """
        # 解决index存在的时候，传的cal_id_list是一个列表
        cal_id_list = []
        # 从数据库获取cal_id_list，才能查询日历
        if index is None:
            cal_id_list = self.get_cal_id_list()
        else:
            cal_id_list.append(self.get_cal_id_list()[index])
        p_data = {"ip": self.ip, "token": token, "cal_id_list": cal_id_list}
        res = self.send_api_data(self.yml_api_path, p_data, "get")
        return res

    def delete_calendar(self, token, index):
        """
        删除日历
        :param token: 日历的token值
        :param index: 在数据库获取第几个id值
        :return: 返回响应体
        """
        # 从数据库获取cal_id_list
        cal_id = self.get_cal_id_list()[index]
        p_data = {"ip": self.ip, "token": token, "cal_id": cal_id}
        res = self.send_api_data(self.yml_api_path, p_data, "delete")
        # 当删除api成功时，同步从数据库中删除cal_id
        if res["errcode"] == 0:
            sql.delete(f"delete from cal_id where cal_id='{cal_id}'")
        else:
            log.info("日历删除请求有误，数据库没有删除cal_id")
        return res

    def edit_calendar(self, token, index, readonly, summary, color, description):
        """
        编辑日历
        :param token: 日历的token值
        :param index: 请求参数的值
        :param readonly: 请求参数的值
        :param summary: 请求参数的值
        :param color: 请求参数的值
        :param description: 请求参数的值
        :return: 返回响应体
        """
        # 从数据库获取cal_id_list
        cal_id = self.get_cal_id_list()[index]
        p_data = {"ip": self.ip, "token": token, "cal_id": cal_id, "readonly": readonly, "summary": summary,
                  "color": color, "description": description}
        res = self.send_api_data(self.yml_api_path, p_data, "edit")
        return res


if __name__ == "__main__":
    a = WCalendar()
    # print(a.add_calendar(a.token,"calendar",0,0,"help","FF3030","abc"))
    # print(a.get_calendar(a.token,0))
    # print(a.delete_calendar(a.token,0))
    # print(a.edit_calendar(a.token, 0, None, "ddd", "0000FF", "cccc"))
