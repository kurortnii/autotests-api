from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import (UpdateCourseRequestSchema, UpdateCourseResponseSchema,
                                            GetCoursesResponseSchema, GetCoursesQuerySchema,
                                            CreateCourseRequestSchema, CreateCourseResponseSchema)
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from fixtures.files import FileFixture
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeatures
from tools.assertions.base import assert_status_code
from tools.assertions.courses import (assert_update_course_response, assert_get_courses_response,
                                      assert_create_course_response)
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTags.COURSES, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.COURSES)
class TestCourses:
    @allure.tag(AllureTags.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update course")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        # формируем данные для обновления
        request = UpdateCourseRequestSchema()
        # отправляем запрос на обновление курса
        response = courses_client.update_course_api(function_course.response.course.id, request)
        # преобразуем JSON-объект в объект схемы
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        # проверяем статус-код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем, что данные в ответе соответствуют запросу
        assert_update_course_response(request, response_data)

        # валидируем JSON-схему ответа
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTags.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get courses")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    def test_get_courses(
            self,
            courses_client: CoursesClient,
            function_user: UserFixture,
            function_course: CourseFixture):
        # формируем параметры запроса, передавая user_id
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        # отправляем GET-запрос на получение списка курсов
        response = courses_client.get_courses_api(query)
        # десериализуем JSON-ответ в Pydantic-модель
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)

        # проверяем, что код ответа 200
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем, что список курсов соответствует раннее созданным курсам
        assert_get_courses_response(response_data, [function_course.response])

        # проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create course")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_course(
            self,
            courses_client: CoursesClient,
            function_course: CourseFixture,
            function_file: FileFixture,
            function_user: UserFixture):
        # формируем данные для создания курса
        request = CreateCourseRequestSchema(preview_file_id=function_file.response.file.id,
                                            created_by_user_id=function_user.response.user.id)
        # отправляем POST-запрос на создание курса
        response = courses_client.create_course_api(request)
        # десериализуем JSON-ответ в Pydantic-модель
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        # проверяем, что код ответа 200
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем, что данные запроса на создание курса соответствуют данными ответа
        assert_create_course_response(request, response_data)

        # проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())