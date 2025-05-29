from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.users.public_users_client import PublicUsersClient
from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeatures
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from fixtures.users import UserFixture
from tools.fakers import fake


emails = {
    "mail.ru": "user with domain mail.ru",
    "gmail.com": "user with domain gmail.com",
    "example.com": "user with domain example.com"

}


@pytest.mark.regression
@pytest.mark.users
@allure.tag(AllureTags.USERS, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.USERS)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.USERS)
class TestUsers:
    @pytest.mark.parametrize("email",
                             emails.keys(),
                             ids=lambda email: f"{email}: {emails[email]}")
    @allure.title("Create user")
    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        # формируем тело запроса на создание пользователя
        request = CreateUserRequestSchema(email=fake.email(email))
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

    @allure.title("Get user me")
    @allure.tag(AllureTags.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_get_user_me(self, private_users_client: PrivateUsersClient, function_user: UserFixture):
        # отправляем запрос на получение пользователя
        response = private_users_client.get_user_me_api()
        # инициализируем модель ответа на основе полученного json в ответе
        # также благодаря встроенной валидации в pydantic дополнительно убеждаемся, что ответ коректный
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        # проверяем статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        # # проверяем, что данные при создании и запросе совпадают
        assert_get_user_response(response_data, function_user.response)
        # проверяем, что тело ответа соответствует ожидаемой json-схеме
        validate_json_schema(response.json(), response_data.model_json_schema())
