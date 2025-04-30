from http import HTTPStatus
import pytest

from clients.users.public_users_client import get_public_users_client
from clients.authentication.authentication_client import get_authentication_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    # инициализируем клиент для создания пользователя
    public_users_client = get_public_users_client()
    authentication_client = get_authentication_client()

    # создаем нового пользователя
    create_user_request = CreateUserRequestSchema()
    public_users_client.create_user(create_user_request)

    # создаем pydantic-объект с данными для аутентификации и выполняем аутентификацию
    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    login_response = authentication_client.login_api(login_request)
    # десериализуем login_response
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    # проверяем статус-код ответа при аутентификации пользователя
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    # проверяем корректность тела
    assert_login_response(login_response_data)
    # проверяем, что ответ соответствует LoginResponseSchema
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())
