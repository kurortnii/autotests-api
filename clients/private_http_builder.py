from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    """
    структура данных пользователя для авторизации
    """
    email: str
    password: str


# создаем private builder
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    функция создает экземпляр httpx.Client с аутентификацией пользователя
    :param user: объект AuthenticationUserSchema с email и паролем пользователя
    :return: готовый к использованию объект httpx.Client с установленным заголовком Authorization
    """
    # инициализируем AutheticationClient для аутентификации
    authentication_client = get_authentication_client()

    # инициализируем запрос на аутентификацию
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    # выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )