from selenium import webdriver

# a=webdriver.Chrome()
# a.implicitly_wait(5)

a={"a":"b"}
b={'ip': 'qyapi.weixin.qq.com', 'token': 'V5vhBQE-gcRRz5BBC4FpmEhVbut6bauTD1PAJU-KEMZrlBhyoDp6pZNt-sWjnbeezDZfwG3qBBG24SxSVJ872svHjJPfhFVtIyXJRrK-U3LoaEBWQarmSqiT_aUnKqcc9hRwwIe8wLQupkzbNb0CcaQOGG4FPUzwqmeuZWu-1c-mNavk7AC20Zru_WYocPgq-IvUoUhUU0NjYI3efPUrBw', 'name': 'ab', 'capacity': 11, 'city': None, 'building': None, 'floor': None, 'equipment': None}

c={'city': None, 'building': None, 'floor': 123, 'equipment': None}

str(c)
print(dict(str(c).replace("None","123")))