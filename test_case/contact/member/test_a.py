import allure


@allure.feature("happy")
def test_b(token):
    print(token)