from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


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

