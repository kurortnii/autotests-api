from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
# импортиртируем билдер
from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """
    описание структуры пользователя
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """
    описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(APIClient):
    """
    описание структуры ответа создания пользователя
    """
    user: User


class PublicUsersClient(APIClient):
    """
    клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        метод создает пользователя
        :param request: словарь с данными для создания пользователя: email, password, firstName, middleName, lastName
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    функция создает экземпляр PublicUsersClient с уже настроенным HTTP-клиентом
    :return: готовый к использованию PublicUsersClient
    """
    return PublicUsersClient(client=get_public_http_client())
