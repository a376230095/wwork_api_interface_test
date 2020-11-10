# @Author : TongTong

# 解决pytest参数化的标题
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid= item.nodeid.encode("utf-8").decode("unicode_escape")