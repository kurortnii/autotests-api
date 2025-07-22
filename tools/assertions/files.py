import httpx
import allure

from clients.files.files_schema import (CreateFileRequestSchema, CreateFileResponseSchema,
                                        FileSchema, GetFileResponseSchema)
from tools.assertions.base import assert_equal
from tools.assertions.errors import (ValidationErrorSchema, ValidationErrorResponseSchema,
                                     InternalErrorResponseSchema)
from tools.assertions.errors import assert_validation_error_response, assert_internal_error_response
from config import settings


@allure.step("Check create file response")
def assert_create_file_response(request: CreateFileRequestSchema,
                                response: CreateFileResponseSchema):
    """
    проверяет, что ответ на создание файла соответствует запросу

    :param request: исходный запрос на создание файла
    :param response: ответ API с данными ответа
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    # формируем ожидаемую ссылку на загруженный файл
    expected_url = f"{settings.http_client.client_url}static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url")
    assert_equal(response.file.filename, request.filename, "filename")
    assert_equal(response.file.directory, request.directory, "directory")


@allure.step("Check file is accessible")
def assert_file_is_accessible(url: str):
    """
    проверяет, что файл доступен по указанному URL
    :param url: ссылка на файл
    :raises AssertionError: если файл недоступен
    """
    response = httpx.get(url)
    assert response.status_code == 200, f"файл недоступен по URL: {url}"


@allure.step("Check file")
def assert_file(actual: FileSchema, expected: FileSchema):
    """
    проверяет, что фактические данные файла соответствуют ожидаемым

    :param actual: фактические данные файла
    :param expected: ожидаемые данные файла
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")


@allure.step("Check get file response")
def assert_get_file_response(
        get_file_response: GetFileResponseSchema,
        create_file_response: CreateFileResponseSchema
):
    """
    проверяет, что ответ на получение пользователя соответствует ответу на его создание
    :param get_file_response: ответ API при запросе данных файла
    :param create_file_response: ответ API при создании файла
    :raises AssertionError: если данные пользователя не совпадают
    """
    assert_file(get_file_response.file, create_file_response.file)


@allure.step("Check create file with empty filename response")
def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой
    валидационной ошибке

    :param actual: ответ API с ошибкой валидации, который необходимо проверить
    :raises AssertionError: если фактический ответ не соответствует ожидаемому
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "filename"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Create file with empty directory response")
def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    проверяет, что ответ на создание файла с пустым значением директории соответствует
    ожидаемой валидационной ошибке

    :param actual: ответ от API с ошибкой валидации, который необходимо проверить
    :raises AssertionError: если фактический ответ не соответствует ожидаемому
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="string_too_short",
                input="",
                context={"min_length": 1},
                message="String should have at least 1 character",
                location=["body", "directory"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)


@allure.step("Check file not found response")
def assert_file_not_found_response(actual: InternalErrorResponseSchema):
    """
    функция для проверки ошибки, если файл не найден на сервере

    :param actual: фактический ответ
    :raises AssertionError: если фактический ответ не соответствует ошибке "File not found"
    """
    expected = InternalErrorResponseSchema(details="File not found")
    assert_internal_error_response(actual, expected)


@allure.step("Check get file with incorrect file id")
def assert_get_file_with_incorrect_file_id(actual: ValidationErrorResponseSchema):
    """
    проверяет, что ответ при получении файла с некорректным id соответствует ожидаемой
    валидационной ошибке

    :param actual: фактический ответ
    :raises AssertionError: если фактический ответ не соответствует ожидаемому
    """
    expected = ValidationErrorResponseSchema(
        details=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=["path", "file_id"],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-file-id",
                context={"error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"}

            )
        ]
    )
    assert_validation_error_response(actual, expected)