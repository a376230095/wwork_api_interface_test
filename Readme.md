# 通通的企业微信简易接口测试框架

##### 作者的吐槽
###### 从一开始的无从下手，到现在写出点简单的东西了，感谢AD小姐姐和了然大佬给的建议和支持

<br>

## 简介+优点
- 使用的技术：pytest+requests+allure+yaml+Template+jsonpath+PyMySQL
- Log日志可以获取每个测试用例的请求参数、响应参数、数据库操作成功与失败的信息
- 利用Template技术，实现API请求+参数化断言+参数化用例标题的yaml数据驱动
- 解决api请求非必填参数的数据驱动，一个yml文件覆盖全部api参数
- 运用conftest+fixture，实现每一个用例不同的前置和后置需求，做到每个用例数据不冲突，实现并行运行
- 利用数据库封装的类，对企业微信无法通过接口获取的id，进行增删改查。解决用例间简单的数据关联
  - 比如增加日历api，会生成cal_id，但这个id无法通过接口获取，其他删除、修改、查询需要通过这个id
  - 保存在yml文件，担心操作失误，导致数据清空
  - 使用数据库保存这类数据，安全可靠方便，效率还高
- 配置文件分离企业微信id、秘钥、测试环境、正式环境
- 封装requests的方法，测试用例中，只需一行代码即可完成输入的请求参数，获得响应内容
- allure demo报告查看的地址：http://129.204.62.26/interface_report/

<br>

<br>


## 使用指南 
- 安装的包在根目录的requirement,pip install -r requriements.txt即可安装
- config.ini的配置，在根目录下
  - 企业微信的ID和各个应用秘钥在wwork的section
  - 数据库，数据库涉及到的类在mysql的section
- 数据库的使用
  - 在api/schedule的两个wcalendar和wschedule文件
  - 简单新建两张表，涉及三个参数，id，userid，cal_id（或者是schedule_id）
  - 请自己新建数据库，搜索所有的sql.select、sql.insert、sql.delete语句，并自行修改
- 有一些用例的数据和我本身的企业微信数据相关联，所以会出现运行失败的情况，数据最好都是自己造
- allure的使用
  - 在项目根目录下，输入：pytest --alluredir=./report/result即可生成结果
  - 输入：allure serve ./report/result可临时查看结果
  - 输入：allure generate ./report/result -o report/result/html 生成永久报告，放到nginx服务器可查看
  - 设置了两种allure用例等级，冒烟blocker，完整测试critical
- 推荐观看代码的顺序，都是一步一步完善的过程
  - 先看common的三个公共类的实现
  - api的文件夹：tag.py到member.py到department到sign到schedule
  - test_case文件夹的顺序和api的顺序差不多
- 一共完成33个接口，129条用例
  - 通讯录的联系人管理、部门管理、标签管理的api
  - 会议室的api
  - 日程的日程和日历api

<br>

<br>


# 目录结构
#### api
- 作用：把所有发送请求和返回响应的api汇集在此
- base_api：所有api类的父类，实现了各种有用的方法
- 其他api类，比如member.py，表示通讯录的联系人api集合，每个方法表示每个api
#### log 
- 存放日志的文件夹
#### common
- 作用：汇集api和test_case需要用到的类和方法
- get_log:获取log的封装类，导入log变量，即可通过log.info(msg)获取文件和屏幕的日志
- config.py：读取配置文件的封装类，导入cf变量，即可通过cf.get(section,option)获取value
- mysql.py，连接和操作数据库，导入sql变量，
  - 即可通过sql.select(query)、sql.insert(query)、sql.delete(query)，对数据库进行增删查
#### test_case
- 作用：作为pytest架构的测试类
- 每个文件夹的文件
  - conftest.py：为每个用例添加不同的前后置步骤，并获取对应的token值，供用例使用
  - test_xxxx.py：测试用例
#### data
- 作用：存放api请求的数据和参数化的数据
- 每个文件夹的文件
  - xxxx_api.yml：存放每一个类中的api请求数据，比如member的增删改查的api数据
  - xxx_para.yml：包含请求参数+断言+ids标题的参数化数据
#### config.ini文件：保存配置文件的数据
#### pytest.ini文件：pytest的配置文件

