import yaml
from api.base_api import BaseApi
a=BaseApi()

def save_yml(path,data):
    with open("test.yml","w") as f:
        yaml.safe_dump(data,f)


def test_b():
    c=a.load_yaml("test.yml")
    c.append("d")
    save_yml("test.yml",c)
    # with open("test.yml","w") as f:
    #     yaml.safe_dump(c,f)

def test_c():
    a="#1"
    print(a)
