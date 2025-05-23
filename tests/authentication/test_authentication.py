from http import HTTPStatus
import pytest

from clients.authentication.authentication_client import AuthenticationClient
from fixtures.users import UserFixture
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import PublicUsersClient
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:
    def test_login(self,
                   function_user: UserFixture,
                   public_users_client: PublicUsersClient,
                   authentication_client: AuthenticationClient):
        # создаем pydantic-объект с данными для аутентификации и выполняем аутентификацию
        request = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        )
        response = authentication_client.login_api(request)
        # десериализуем response
        response_data = LoginResponseSchema.model_validate_json(response.text)

        # проверяем статус-код ответа при аутентификации пользователя
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем корректность тела
        assert_login_response(response_data)
        # проверяем, что ответ соответствует LoginResponseSchema
        validate_json_schema(response.json(), response_data.model_json_schema())
