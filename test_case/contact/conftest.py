import pytest

from api.wework import Wework
from common.config import cf


@pytest.fixture(scope="session")
def token():
    secret = cf.get_key("wwork", "contact_secret")
    access_token=Wework().get_token(secret)
    return access_token


