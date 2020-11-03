import pytest

from api.department import Department
depart=Department()

@pytest.fixture(scope="session")
def depart_smoke(token):
    depart.delete_depart(token,5)
    depart.delete_depart(token,6)
    depart.delete_depart(token,7)
    depart.add_depart(token,1,"smoke1")
    yield
    depart.delete_depart(token,5)
    depart.delete_depart(token,6)


@pytest.fixture(scope="session")
def add_depart(token):
    depart.delete_depart(token,5)
    depart.delete_depart(token,6)
    yield
    depart.delete_depart(token,5)


@pytest.fixture(scope="session")
def edit_depart(token):
    depart.add_depart(token, 1, "smoke2")
    yield
    depart.delete_depart(token,5)



@pytest.fixture(scope="session")
def delete_depart(token):
    depart.add_depart(token, 1, "delete")

