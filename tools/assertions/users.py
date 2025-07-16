import allure

from clients.users.users_schema import (CreateUserRequestSchema, CreateUserResponseSchema,
                                        UserSchema, GetUserResponseSchema)
from tools.assertions.base import assert_equal


@allure.step("Check create users response")
def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    проверяет, что ответ на создание пользователя соответствует запросу

    :param request: исходный запрос на создание пользователя
    :param response: ответ API с данными пользователя
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    assert_equal(response.user.email, request.email, 'email')
    assert_equal(response.user.last_name, request.last_name, 'last_name')
    assert_equal(response.user.first_name, request.first_name, 'first_name')
    assert_equal(response.user.middle_name, request.middle_name, 'middle_name')


@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    """
    проверяет корректность данных пользователя
    :param actual: актуальная модель пользователя
    :param expected: ожидаемая модель пользователя
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    assert_equal(expected.id, actual.id, 'id')
    assert_equal(expected.email, actual.email, 'email')
    assert_equal(expected.last_name, actual.last_name, 'last_name')
    assert_equal(expected.first_name, actual.first_name, 'first_name')
    assert_equal(expected.middle_name, actual.middle_name, 'middle_name')


@allure.step("Check get user response")
def assert_get_user_response(get_user_response: GetUserResponseSchema,
                             create_user_response: CreateUserResponseSchema):
    """

    :param get_user_response: ответ API при запросе пользователя
    :param create_user_response: ответ API при создании пользователя
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    assert_user(get_user_response.user, create_user_response.user)
