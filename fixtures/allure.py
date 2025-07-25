import pytest

from tools.allure.environment import create_allure_environment


@pytest.fixture(scope='session', autouse=True)
def save_allure_environment_file():
    # до начала автотестов ничего не делаем
    # запускаются автотесты
    yield
    # после завершения автотестов создаем файл environment.properties
    create_allure_environment()