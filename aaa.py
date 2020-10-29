from string import Template

# 假设yaml的文件格式如下
import yaml

"""
"method": "post"
"url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?"
"params": "access_token=$token"
"json":
  "group_id": "etMCs1DwAAg_jBNAuvGR3B21cwl4o0jg"
  "tag":
    - "name": "$name"
"""
# 可以把yml文件的两个变量都改变，无须管是什么数据类型
# 写法："${name}" 这样写是最好的
with open("data/tag_add.yml") as f:
  name=1
  token=2
  # Template接收一个字符串，然后通过substitute改变值
  # substitute需要包含全部的$变量的值，用字典来接收，不包含全部会报错的
  # 最终返回的类型是字符串的类型
  data=Template(f.read()).substitute({"name":name,"token":token})
  print(data)
"""
结果如下，的确改变了token和name的值
"method": "post"
"url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag?"
"params": "access_token=2"
"json":
  "group_id": "etMCs1DwAAg_jBNAuvGR3B21cwl4o0jg"
  "tag":
    - "name": "1"
"""