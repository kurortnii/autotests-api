import allure

from clients.authentication.authentication_schema import LoginResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


@allure.step("Check login response")
def assert_login_response(response: LoginResponseSchema):
    """
    проверяет корректность ответа при успешной авторизации
    :param response: объект ответа с токенами авторизации
    :raises AssertionError: если какое-либо из условий не выполняется
    """
    assert_equal(response.token.token_type, 'bearer', 'token_type')
    assert_is_true(response.token.access_token, 'access_token')
    assert_is_true(response.token.refresh_token, 'refresh_token')