from typing import TypedDict

from httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict


class AutheticationUserDict(TypedDict):
    """
    структура данных пользователя для авторизации
    """
    email: str
    password: str


# создаем private builder
def get_private_http_client(user: AutheticationUserDict) -> Client:
    """
    функция создает экземпляр httpx.Client с аутентификацией пользователя
    :param user: объект AuthenticationUserSchema с email и паролем пользователя
    :return: готовый к использованию объект httpx.Client с установленным заголовком Authorization
    """
    # инициализируем AutheticationClient для аутентификации
    authentication_client = get_authentication_client()

    # инициализируем запрос на аутентификацию
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    # выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )