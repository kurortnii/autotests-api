import allure
from httpx import Response

from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema
# импортируем билдер
from clients.public_http_builder import get_public_http_client


class AuthenticationClient(APIClient):
    """
    клиент для работы с /api/v1/authentication
    """

    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        метод выполняет аутентификацию пользователя
        :param request: словарь с email и password
        :return: ответ от сервера с виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login",
                         json=request.model_dump(by_alias=True))

    @allure.step("Refresh authentication token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        метод обновляет токен авторизации

        :param request: словарь с refreshToken
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh",
                         json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        # отправляем запрос на аутентификацию
        response = self.login_api(request)
        # инициализируем модель через валидацию JSON строки
        return LoginResponseSchema.model_validate_json(response.text)


def get_authentication_client() -> AuthenticationClient:
    """
     функция создает экземпляр AuthenticationClient с уже настроенным HTTP-клиентом
     :return: готовый к использованию AuthenticationClient
     """
    return AuthenticationClient(client=get_public_http_client())
