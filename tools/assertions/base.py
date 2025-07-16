from typing import Any, Sized

import allure


@allure.step("Check that response status code equals to {expected}")
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


@allure.step("Check that {name} equals to {expected}")
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


@allure.step("Check that {name} is true")
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


def assert_length(actual: Sized, expected: Sized, name: str):
    """
    проверяет, что длины двух объектов совпадают
    :param actual: фактический объект
    :param expected: ожидаемый объект
    :param name: название проверяемого объекта
    :raises AssertionError: если длины не совпадают
    """
    with allure.step(f"Check that length of {name} equals to {len(expected)}"):
        assert len(actual) == len(expected), (
            f'Incorrect object length: "{name}".'
            f'Expected length: {len(expected)}'
            f'Actual length: {len(actual)}'
        )