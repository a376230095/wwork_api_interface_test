
from api.wework import Wework
from common.config import cf

class Base():

    def get_token(self):
        secret = cf.get_key("wwork", "contact_secret")
        access_token = Wework().get_token(secret)
        return access_token

contact_token=Base().get_token()

if __name__=="__main__":
    print(a)
