from api.base_api import BaseApi
from api.wework import Wework
from common.config import cf
from common.get_log import log
from common.mysql import sql


class WCalendar(BaseApi):
    secret=cf.get_key("wwork","schedule_secret")
    token= Wework().get_token(secret)

    yml_api_path="data/schedule/calendar/calendar_api.yml"
    # 不用yml文件保存cal_id的数据了，放在数据库好啦
    # cal_id_path="data/schedule/calendar/cal_id.yml"


    def get_cal_id_list(self):
        cal_id_tuple=sql.select("select cal_id from cal_id")
        cal_id_list=[i[0] for i in cal_id_tuple]
        return cal_id_list

    def add_calendar(self,token,organizer,readonly,set_as_default,summary,color,description):
        p_data={"ip":self.ip,"token":token,"organizer":organizer,"readonly":readonly,
               "set_as_default":set_as_default,"summary":summary,"color":color,"description":description}
        res=self.send_api_data(self.yml_api_path,p_data,"add")
        try:
            cal_id = res["cal_id"]
            sql.insert(f"insert into cal_id(userid,cal_id) values('{organizer}','{cal_id}')")
        except Exception as e:
            log.error("错误原因：{e}")
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

    def get_calendar(self,token,index=None):
        cal_id_list=[]
        if index==None:
            cal_id_list=self.get_cal_id_list()
        else:
            cal_id_list.append(self.get_cal_id_list()[index])
        p_data = {"ip": self.ip, "token": token, "cal_id_list": cal_id_list}
        res = self.send_api_data(self.yml_api_path, p_data, "get")
        return res

    def delete_calendar(self,token,index):
        cal_id=self.get_cal_id_list()[index]
        p_data = {"ip": self.ip, "token": token, "cal_id":cal_id}
        res = self.send_api_data(self.yml_api_path, p_data, "delete")
        if res["errcode"] == 0:
            sql.delete(f"delete from cal_id where cal_id='{cal_id}'")
        else:
            log.info("日历删除请求有误，数据库没有删除cal_id")
        return res

    def edit_calendar(self,token,index,readonly,summary,color,description):
        cal_id = self.get_cal_id_list()[index]
        p_data = {"ip": self.ip, "token": token, "cal_id": cal_id,"readonly":readonly,"summary":summary,"color":color,"description":description}
        res= self.send_api_data(self.yml_api_path,p_data,"edit")
        return res




if __name__ == "__main__":
    a=WCalendar()
    # print(a.add_calendar(a.token,"calendar",0,0,"help","FF3030","abc"))
    # print(a.get_calendar(a.token,0))
    # print(a.delete_calendar(a.token,0))
    print(a.edit_calendar(a.token,0,None,"ddd","0000FF","cccc"))