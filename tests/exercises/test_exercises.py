from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExerciseClient
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema, CreateExerciseResponseSchema,
                                                GetExerciseResponseSchema, UpdateExerciseRequestSchema,
                                                UpdateExerciseResponseSchema, GetExercisesQuerySchema,
                                                GetExercisesResponseSchema)
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeatures
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (assert_create_exercise_response, assert_get_exercise_response,
                                        assert_update_exercise_response, assert_exercise_not_found_response,
                                        assert_get_exercises_response)
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
@allure.tag(AllureTags.EXERCISES, AllureTags.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeatures.EXERCISES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeatures.EXERCISES)
class TestExercises:
    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create exercise")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_exercise(
            self,
            exercise_client: ExerciseClient,
            function_course: CourseFixture):
        # формируем запрос для создания упражнения курса
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        # отправляем POST-запрос на создание упражнения курса
        response = exercise_client.create_exercise_api(request)
        # десериализуем JSON-ответ в Pydantic-модель
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        # проверяем, что данные при создании упраженения совпадают с данными ответа
        assert_create_exercise_response(request, response_data)
        # проверяем, что код ответа 200
        assert_status_code(response.status_code, HTTPStatus.OK)

        # проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTags.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get exercise")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_exercise(
            self,
            exercise_client: ExerciseClient,
            function_exercise: ExerciseFixture):
        # отправляем GET-запрос на получение упражнения курса по id
        response = exercise_client.get_exercise_api(function_exercise.response.exercise.id)
        # десериализуем JSON-ответ в Pydantic-модель
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        # проверяем, что код ответа 200
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем, что тело ответа на получение курса соответствует ответу на создание курса
        assert_get_exercise_response(response_data, function_exercise.response)

        # проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.tag(AllureTags.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    def test_update_exercise(
            self,
            exercise_client: ExerciseClient,
            function_exercise: ExerciseFixture):
        # формируем данные для обновления
        request = UpdateExerciseRequestSchema()
        # отправляем запрос на обновление курса
        response = exercise_client.update_exercise_api(function_exercise.response.exercise.id, request)
        # десериализуем JSON-ответ в Pydantic-модель
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        # проверяем, что код-статус ответа 200
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем, что данные запроса на обновление упражнения курса соответствуют ответу
        assert_update_exercise_response(request, response_data)

        # проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), GetExerciseResponseSchema.model_json_schema())

    @allure.tag(AllureTags.DELETE_ENTITY)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.title("Delete exercise")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    def test_delete_exercise(
            self,
            exercise_client: ExerciseClient,
            function_exercise: ExerciseFixture):
        # удаляем упражнение курса
        response = exercise_client.delete_exercise_api(function_exercise.response.exercise.id)

        # проверяем, что упражнение курса успешно удалено
        assert_status_code(response.status_code, HTTPStatus.OK)

        # пытаемся получить удаленный файл
        get_response = exercise_client.get_exercise_api(function_exercise.response.exercise.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        # проверяем, что сервер вернул 404
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        # проверяем, что в ответе содержится message "Exercise not Found"
        assert_exercise_not_found_response(get_response_data)

        # проверяем соответствие JSON-ответа схеме
        validate_json_schema(get_response.json(), InternalErrorResponseSchema.model_json_schema())

    @allure.tag(AllureTags.GET_ENTITIES)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.title("Get exercises")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    def test_get_exercises(
            self,
            exercise_client: ExerciseClient,
            function_exercise: ExerciseFixture,
            function_course: CourseFixture):
        # формируем параметры запроса, передавая course_id
        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        # отправляем GET-запрос на получение списка упражнений
        response = exercise_client.get_exercises_api(query)
        # десериализуем JSON-ответ в Pydantic-ответ
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        # проверяем, что статус-код на получение списка упражнений 200
        assert_status_code(response.status_code, HTTPStatus.OK)

        # проверяем, что ответ запроса на список упражнений соответствует
        # списку ранее созданых упражнений
        assert_get_exercises_response(response_data, [function_exercise.response])

        # проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), GetExercisesResponseSchema.model_json_schema())
