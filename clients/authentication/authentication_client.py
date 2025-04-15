from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
# импортируем билдер
from clients.public_http_builder import get_public_http_client


class Token(TypedDict):
    """
    описание структуры аутентификационных токенов
    """
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginRequestDict(TypedDict):
    """
    описание структуры запроса на аутентификацию
    """
    email: str
    password: str


class LoginResponseDict(TypedDict):
    """
    описание структуры ответа аутентификации
    """
    token: str


class RefreshRequestDict(TypedDict):
    """
    описание структуры запроса для обновления токена
    """
    refreshToken: str


class AuthenticationClient(APIClient):
    """
    клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        метод выполняет аутентификацию пользователя
        :param request: словарь с email и password
        :return: ответ от сервера с виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        метод обновляет токен авторизации

        :param request: словарь с refreshToken
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        # отправляем запрос на аутентификацию
        response = self.login_api(request)
        # извлекаем JSON из ответа
        return response.json()


def get_authentication_client() -> AuthenticationClient:
    """
     функция создает экземпляр AuthenticationClient с уже настроенным HTTP-клиентом
     :return: готовый к использованию AuthenticationClient
     """
    return AuthenticationClient(client=get_public_http_client())
