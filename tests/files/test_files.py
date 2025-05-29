from http import HTTPStatus

import pytest
import allure
from allure_commons.types import Severity

from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import (CreateFileRequestSchema, CreateFileResponseSchema,
                                        GetFileResponseSchema)
from fixtures.files import FileFixture
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeatures
from tools.assertions.base import assert_status_code
from tools.assertions.files import (assert_create_file_response, assert_file_is_accessible,
                                    assert_get_file_response, assert_create_file_with_empty_filename_response,
                                    assert_create_file_with_empty_directory_response, assert_file_not_found_response,
                                    assert_get_file_with_incorrect_file_id)
from tools.assertions.schema import validate_json_schema


@pytest.mark.files
@pytest.mark.regression
@allure.tag(AllureTags.FILES, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.FILES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.FILES)
class TestFiles:
    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create file")
    @allure.severity(Severity.BLOCKER)
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="./testdata/files/image.jpg")
        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)
        # проверяем, что файл доступен по ссылке после создания
        assert_file_is_accessible(str(response_data.file.url))

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTags.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get file")
    @allure.severity(Severity.BLOCKER)
    def test_get_file(self, files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTags.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Create file with empty filename")
    @allure.severity(Severity.NORMAL)
    def test_create_file_with_empty_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            filename="",
            upload_file="./testdata/files/image.jpg"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTags.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Create file with empty directory")
    @allure.severity(Severity.NORMAL)
    def test_create_file_with_empty_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(
            directory="",
            upload_file="./testdata/files/image.jpg"
        )
        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTags.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Delete file")
    @allure.severity(Severity.NORMAL)
    def test_delete_file(self, files_client: FilesClient, function_file: FileFixture):
        # удаляем файл
        delete_response = files_client.delete_file_api(function_file.response.file.id)
        # проверяем, что файл успешно удален (статус 200 OK)
        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        # пытаемся получить удаленный файл
        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        # проверяем, что сервер вернул 404
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        # проверяем, что в ответе содержится ошибка "File not found"
        assert_file_not_found_response(get_response_data)

        # проверяем, что ответ соответствует схеме
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    @allure.tag(AllureTags.VALIDATE_ENTITY)
    @allure.story(AllureStory.VALIDATE_ENTITY)
    @allure.title("Get file with incorrect id")
    @allure.severity(Severity.NORMAL)
    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient, function_file: FileFixture):
        # отправляем запрос на получение файла с некорреткный file_id
        response = files_client.get_file_api("incorrect-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        # проверяем, что API возвращает статус-код 422
        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        # проверяем, что приходит корректный ответ с ошибкой
        assert_get_file_with_incorrect_file_id(response_data)

        # проверяем, что ответ соответствует схеме
        validate_json_schema(response.json(), response_data.model_json_schema())