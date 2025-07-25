import allure

from clients.errors_schema import (ValidationErrorSchema, ValidationErrorResponseSchema,
                                   InternalErrorResponseSchema)
from tools.assertions.base import assert_equal, assert_length
from tools.logger import get_logger

logger = get_logger("ERRORS_ASSERTIONS")


@allure.step("Check validation error")
def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    проверяется, что объект ошибки валидации соответствует ожидаемому значению

    :param actual: фактическая ошибка
    :param expected: ожидаемая ошибка
    :raises AssertionError: если значения полей не совпадают
    """
    logger.info("Check validation error")

    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.input, expected.input, "input")
    assert_equal(actual.context, expected.context, "context")
    assert_equal(actual.message, expected.message, "message")
    assert_equal(actual.location, expected.location, "location")


@allure.step("Check validation error response")
def assert_validation_error_response(
        actual: ValidationErrorResponseSchema,
        expected: ValidationErrorResponseSchema
):
    """
    проверяет, что объект ответа API с ошибками валидации соответствует ожидаемому значению
    :param actual: фактический ответ API
    :param expected: ожидаемый ответ API
    :raises AssertionError: если значения полей не совпадают
    """
    logger.info("Check validation error response")

    assert_length(actual.details, expected.details, "details")

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)


@allure.step("Check internal error response")
def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    """
    функция для проверки внутренней ошибки. например, ошибки 404 (File not found)
    :param actual: фактический ответ API
    :param expected: ожидаемый ответ API
    :raises AssertionError: если значения полей не совпадают
    """
    logger.info("Check internal error response")

    assert_equal(actual.details, expected.details, "details")