import allure
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema
from tools.routes import APIRoutes


class PrivateUsersClient(APIClient):
    """
    клиент для работы с /api/v1/users
    """

    @allure.step("Get user me")
    def get_user_me_api(self) -> Response:
        """
        метод для получения текущего пользователя

        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.USERS}/me")

    @allure.step("Get user by {user_id}")
    def get_user_api(self, user_id: str) -> Response:
        """
        метод получения пользователя по идентификатору
        :param user_id: индентификатор пользователя
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.get(f"{APIRoutes.USERS}/{user_id}")

    @allure.step("Update user by id {user_id}")
    def update_user_api(self,
                        user_id: str,
                        request: UpdateUserRequestSchema) -> Response:
        """
        метод обновления пользователя по идентификатору

        :param user_id: идентификатор пользователя
        :param request: словарь с email, lastName, firstname, middleName
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"{APIRoutes.USERS}/{user_id}",
                          json=request.model_dump(by_alias=True))

    @allure.step("Delete user by id {user_id}")
    def delete_user_api(self, user_id: str) -> Response:
        """
        метод удаления пользователя по идентификатору
        :param user_id: идентификатор пользователя
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.delete(f"{APIRoutes.USERS}/{user_id}")

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


# добавляем builder для PrivateUsersClient
def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    функция создает экземпляр PrivateUsersClient c уже настроенным HTTP-клиентом

    :return: готовый к использованию PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user))