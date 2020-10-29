# 装饰器


def checkLogin(func):
     def inner(*args, **kwargs):
          print("登录操作")
          func(*args, **kwargs)
     return inner

@checkLogin
def ftp(name, pwd, yzm):
     print(name,pwd, yzm["abc"])
     print("发说说操作")

# fss("lbtest", '123')

# ftp("root", '123', {"abc"="tongtong"})
# @checkLogin
# def fss(name, pwd):
#      print(name,pwd)
#      print("发说说操作")

def a(**kwargs):
    print(kwargs)