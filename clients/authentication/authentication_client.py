from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class LoginRequestDict(TypedDict):
    """
    описание структуры запроса на аутентификацию
    """
    email: str
    password: str


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
