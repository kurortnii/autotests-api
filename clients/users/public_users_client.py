from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
# импортиртируем билдер
from clients.public_http_builder import get_public_http_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        метод создает пользователя
        :param request: словарь с данными для создания пользователя: email, password, firstName, middleName, lastName
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    функция создает экземпляр PublicUsersClient с уже настроенным HTTP-клиентом
    :return: готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
