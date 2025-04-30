from http import HTTPStatus

from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response


def test_create_user():
    # инициализируем api-клиент для работы с пользователем
    public_users_client = get_public_users_client()

    # формируем тело запроса на создание пользователя
    request = CreateUserRequestSchema()
    # отправляем запрос на создание пользователя
    response = public_users_client.create_user_api(request)
    # инициализируем модель ответа на основе полученного json в ответе
    # также благодаря встроенной валидации в pydantic дополнительно убеждаемся, что ответ коректный
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    # проверяем статус-код
    assert_status_code(response.status_code, HTTPStatus.OK)
    # используем функцию для проверки ответа создания юзера
    assert_create_user_response(request, response_data)
    # проверяем, что тело ответа соответствует ожидаемой json-схеме
    validate_json_schema(response.json(), response_data.model_json_schema())