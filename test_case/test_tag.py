import pytest
from api.tag import Tag

class TestTag():
    # 由于参数化的代码比classmethod更早执行，所以需要放到最外层去执行
    base_data=Tag().load_yaml("../data/test_tag.yml")

    @classmethod
    # 做测试的初始化，只需要初始化一次
    # 把tag标签都删除
    def setup_class(cls):
        # 定义好Tag()对象，cls.a，其他def test都可以用self.a使用
        cls.a=Tag()
        # 定义好要删除的的标签的名字
        name_data=["aaa","bbb","tongtong","tongtong1"]
        # 获取标签的数据
        data=cls.a.get_tag()
        # 对标签名字进行遍历
        for name in name_data:
            # 通过name去找到对应的tag_id
            tag_id=cls.a.jsonpath(data,f'$..tag[?(@.name=="{name}")].id')
            # 删除标签的api需要传tag_id
            cls.a.delete_tag(tag_id)

    # 测试获取标签的用例
    def test_get_tag(self):
        res=self.a.get_tag()
        assert res["errcode"] ==0
        # print(json.dumps(res,indent=2))

    # 使用参数化，数据都保存在yml文件，读取出来变成base_data
    @pytest.mark.parametrize(("oldname,newname"),base_data)
    # 测试一次增加标签，修改标签是否正常运行
    def test_all(self,oldname,newname):
        # 增加成功，errcode就是0
        assert self.a.add_tag(oldname)["errcode"] == 0
        tag_id=self.a.jsonpath(self.a.get_tag(),f"$..tag[?(@.name=='{oldname}')].id")[0]
        # edit_tag修改标签需要传tag_id，获取即可，修改成功后，errcode就是0
        assert self.a.edit_tag(tag_id,newname)["errcode"] == 0

    # 测试删除是否成功的用例
    def test_delete(self):
        name="zzz"
        # 当tag_id是一个可变的值，只要能够获取，弄成变量即可
        tag_id = self.a.jsonpath(self.a.get_tag(), f"$..tag[?(@.name=='{name}')].id")[0]
        assert self.a.delete_tag(tag_id)["errcode"] ==0