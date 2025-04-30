from typing import Any


def assert_status_code(actual: int, expected: int):
    """
    проверяет, что фактический статус-код ответа соответствует ожидаемому

    :param actual: фактический статус-код ответа
    :param expected: ожидаемый статус-код ответа
    :raises AssertionError: если статус-коды не совпадают
    """
    assert actual == expected, (
        f'Incorrect response status code'
        f'Expected status code: {expected}'
        f'Actual status code: {actual}'
    )


def assert_equal(actual: Any, expected: Any, name: str):
    """
    проверяет, что фактическое значение равно ожидаемому

    :param actual: фактическое значение
    :param expected: ожидаемое значение
    :param name: название проверяемого значения
    :raises AssertionError: если фактическое значение не равно ожидаемому
    """
    assert actual == expected, (
        f'Incorrect value: {name}'
        f'Expected value: {expected}'
        f'Actual value: {actual}'
    )


def assert_is_true(actual: Any, name: str):
    """
    проверяет, что фактическое значение является истинным

    :param actual: фактическое значение
    :param name: название проверяемого значения
    :raises AssertionError: если фактическое значение ложно
    """
    assert actual, (
        f'Incorrect value: {name}'
        f'Expected true value but got: {actual}'
    )