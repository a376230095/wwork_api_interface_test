import pymysql
from common.config import cf
from common.get_log import log

class Mysql():

    def __init__(self):
        host=cf.get_key("mysql","host")
        # 从配置文件获取的值是str，需要转化成int
        port=int(cf.get_key("mysql","port"))
        user=cf.get_key("mysql","user")
        password=cf.get_key("mysql","password")
        charset=cf.get_key("mysql","charset")
        database=cf.get_key("mysql","database")
        try:
            self.conn=pymysql.connect(host=host,port=port,user=user,
                                      password=password,charset=charset,database=database)
        except Exception as e:
            log.error(f"无法登陆数据库，错误原因：{e}")

    def select(self,query):
        log.info(f"select语句为：{query}")
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            select_data=cur.fetchall()
            log.info("数据查询成功")
            return select_data
        except Exception as e:
            log.error(f"select语句错误，错误原因是：{e}")

    def insert(self,query):
        log.info(f"insert语句为：{query}")
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            cur.execute("commit")
            log.info(f"数据插入成功")
        except Exception as e:
            log.error(f"insert 语句错误，原因是{e}")
            cur.execute("rollback")

    def delete(self,query):
        log.info(f"delete语句为：{query}")
        try:
            cur=self.conn.cursor()
            cur.execute(query)
            cur.execute("commit")
            log.info("数据删除成功")
        except Exception as e:
            log.error(f"delete语句失败，原因：{e}")
            cur.execute("rollback")

sql=Mysql()

if __name__ == "__main__":
    a=Mysql()
    # a.insert(f"insert into cal_id(userid,cal_id) values('calendar','hehehda')")
    print(a.select("select cal_id from cal_id"))
    # b=a.select("select cal_id from cal_id")
    # b=[i[0] for i in b ]
    # print(b)

