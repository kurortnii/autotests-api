from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class UpdateUserRequestDict(TypedDict):
    """
    описание структуры запроса на обновление данных
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    """
    клиент для работы с /api/v1/users
    """

    def get_user_me_api(self) -> Response:
        """
        метод для получения текущего пользователя

        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        """
        метод получения пользователя по идентификатору
        :param user_id: индентификатор пользователя
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        метод обновления пользователя по идентификатору

        :param user_id: идентификатор пользователя
        :param request: словарь с email, lastName, firstname, middleName
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        метод удаления пользователя по идентификатору
        :param user_id: идентификатор пользователя
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/users/{user_id}")