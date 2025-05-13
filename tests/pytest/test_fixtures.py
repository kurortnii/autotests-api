import pytest


# фикстура, которая будет автоматически вызываться для каждого теста
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")


# фикстура для инициализации настроек автотестов на уровнее сессии
@pytest.fixture(scope='session')
def settings():
    print("[SESSION] Инициализируем настройки автотестов")


# фикстура для создания данных пользователя, которая будет выполняться один раз на класс
@pytest.fixture(scope='class')
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")


# фикстура для инициализации API клиента, которая выполняется для каждого теста
@pytest.fixture(scope='function')
def users_client():
    print("[FUNCTION] Создаем API клиент на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        pass

    def test_user_can_create_course(self, settings, user, users_client):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        pass