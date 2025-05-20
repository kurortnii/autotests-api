from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExerciseClient
from clients.exercises.exercises_schema import (CreateExerciseRequestSchema, CreateExerciseResponseSchema,
                                                GetExerciseResponseSchema, UpdateExerciseRequestSchema,
                                                UpdateExerciseResponseSchema)
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (assert_create_exercise_response, assert_get_exercise_response,
                                        assert_update_exercise_response)
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
class TestExercises:
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