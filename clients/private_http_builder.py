# импортируем функцию для кеширования
from functools import lru_cache

from httpx import Client
from pydantic import BaseModel

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings


class AuthenticationUserSchema(BaseModel, frozen=True):
    """
    структура данных пользователя для авторизации
    """
    email: str
    password: str


# создаем private builder и кешируем возвращаемое значение
@lru_cache(maxsize=None)
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
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={
            "request": [curl_event_hook, log_request_event_hook],
            "response": [log_response_event_hook]
        }
    )