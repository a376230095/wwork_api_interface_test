from common.get_log import log
from functools import wraps
from time import time
import requests

def log_more(text=None):
    def decorate(func):
        def wrapper(*args,**kargs):
            log.info(f"--------现在开始测试{text}用例------")

corpid="ww4a8d8403cb338c65"
corpsecret="y5-95rLakHkBz3b69WqbcUXGPMfgn5k-2WFI1WOs4gM"

url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
res=requests.get(url=url,params=f"corpid={corpid}&corpsecret={corpsecret}")
access_token=res.json()["access_token"]


url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"
data={
    "userid":"tong",
    "name":"tong",
    "mobile":"13172661165",
    "department":[1,1]
}
res=requests.post(url=url,json=data)
print(res.json())