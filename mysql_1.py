import pymysql

# 链接数据库，通过connect函数链接，生成对象
# 定义游标cursor，通过游标执行脚本获取结果
# 关闭连接
conn=pymysql.connect(host='129.204.62.26',port=3308,user='root',password='1234',
                     database='wework',charset="utf8")
'''
常用方法：
1.cursor()：使用当前连接创建并返回游标
2.commit()：提交当前事务，做了数据修改，需要commit，比如update，delete，insert
3.rollback()：回滚当前事务
4.close()：关闭当前连接
'''
# 第二步建立游标
cur=conn.cursor()
'''
游标操作方法：
1.execute()：执行数据库查询或命令，将结果从数据库返回给客户端
2.fetchone()：获取结果集的下一行
3.fetchall()：获取结果集的所有行
4.fetchmany()：获取结果集的几行
'''
# 执行脚本
cur.execute('select * from cal_id')
# print(cur.fetchall()) #获取所有的信息((1, '123', '123124'), (2, '1123', '324234'))
# print(cur.fetchone()) # 获取第一行的数据(1, '123', '123124')
print(cur.fetchmany(3)) # 获取两行数据((1, '123', '123124'), (2, '1123', '324234'))

# 提交数据
# cur.execute('insert into cal_id values (3,"ffef","sfsf")')
# cur.execute('commit')

# 关闭数据库
conn.close()

# mysql的封装