import requests

# 请求：
# 1.请求方法，请求的url，请求体，请求的头部
# 2.请求完之后有响应，有响应码，有响应头部，响应体
# 3.首先如果我们需要去创建企业微信的成员，需要有一个前提条件，获取access_token（权限）

corpid="ww630f49269e06f865"
corpsecret="YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"

url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
res=requests.get(url=url,params=f"corpid={corpid}&corpsecret={corpsecret}")
# res.text实质是一个字符串，res.json()把响应体转化成为字典,通过access_token这个key获取value
access_token=res.json()["access_token"]
# print(access_token)

# 创建联系人

create_member_url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"
# data是一个字典的格式
create_member_data={
    "userid": "zhangsan123",
    "name": "张三",
    "mobile": "+13800000000",
    "department": [1, 2]
}


# 我们的请求体不能传字典，需要传json
# requests库给我们一个很好的东西，json，json=create_member_data相当于帮我们把字典转化成json格式，作为请求体传给企业微信的服务器
res=requests.post(url=create_member_url,json=create_member_data)
result=res.json()
if result["errcode"]==0:
    print("第一步验证成功")
    if result["errmsg"]=="created":
        print("的确创建成功")


