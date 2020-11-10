# @Author : TongTong

from api.base_api import BaseApi
from api.wework import Wework
from common.config import cf


class MeetingRoom(BaseApi):
    """
    会议室的api类

    test_token： token值
    api_path： yml_api的相对路径
    """

    # 只是拿来测试用，可以不存在在这里
    test_token = Wework().get_token(cf.get_key("wwork", "meeting_room_secret"))
    # 简化send_api_data方法路径引用，不用写那么多路径了
    api_path = "data/meeting_room/meeting_room_api.yml"

    # 增加会议室
    def add_meeting_room(self, token, name, capacity, city, building, floor, equipment):
        # Template模板二次修改的值，p_data
        p_data = {"ip": self.ip, "token": token, "name": name, "capacity": capacity, "city": city, "building": building,
                  "floor": floor, "equipment": equipment}
        # 获取响应，进行了多次封装
        res = self.send_api_data(self.api_path, p_data, "add")
        return res

    # 编辑会议室
    def edit_meeting_room(self, token, meetingroom_id, name, capacity, city, building, floor, equipment):
        p_data = {"ip": self.ip, "token": token, "meetingroom_id": meetingroom_id, "name": name, "capacity": capacity,
                  "city": city, "building": building, "floor": floor, "equipment": equipment}
        res = self.send_api_data(self.api_path, p_data, "edit")
        return res

    # 删除会议室
    def delete_meeting_room(self, token, meetingroom_id):
        p_data = {"ip": self.ip, "token": token, "meetingroom_id": meetingroom_id}
        res = self.send_api_data(self.api_path, p_data, "delete")
        return res

    # 获取会议室
    def get_meeting_room(self, token, city, building, floor, equipment):
        p_data = {"ip": self.ip, "token": token, "city": city, "building": building, "floor": floor,
                  "equipment": equipment}
        res = self.send_api_data(self.api_path, p_data, "get")
        return res


if __name__ == "__main__":
    a = MeetingRoom()
    print(a.get_meeting_room(a.test_token, None, None, None, None))
    # print(a.test_token)
    # print(a.add_meeting_room(a.test_token,"a",20,"c","d","e",[1,2]))
    # print(a.edit_meeting_room(a.test_token,1,None,None,None,None,None,None))
    # print(a.delete_meeting_room(a.test_token,1))
    # print(a.add_meeting_room(a.test_token,"ab",11,None,None,None,None))
    # print(a.load_yaml("data/meeting_room/1meeting_room_api.yml")["add"])
