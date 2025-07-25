import allure

from clients.exercises.exercises_schema import (CreateExerciseResponseSchema, CreateExerciseRequestSchema,
                                                ExerciseSchema, GetExerciseResponseSchema,
                                                UpdateExerciseRequestSchema, UpdateExerciseResponseSchema,
                                                GetExercisesResponseSchema)
from clients.errors_schema import InternalErrorResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("EXERCISES_ASSERTIONS")


@allure.step("Check create exercise response")
def assert_create_exercise_response(request: CreateExerciseRequestSchema,
                                    response: CreateExerciseResponseSchema):
    """
    проверяет, что данные запроса на создание упражнения курса совпадают с данными ответа

    :param request: запрос с данными для создания упражнения курса
    :param response: ответ API при создании упражнения курса
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    logger.info("Check create exercise response")

    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")


@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    проверяет, что фактические данные упражнения курса соответствуют ожидаемым

    :param actual: фактические данные упражнения курса
    :param expected: ожидаемые данные упражнения курса
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    logger.info("Check exercise")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


@allure.step("Check get exercise response")
def assert_get_exercise_response(get_exercise_request: GetExerciseResponseSchema,
                                 create_exercise_response: CreateExerciseResponseSchema):
    """
    проверяет, что запрос на получение упражнения соответствует созданному упражнению

    :param get_exercise_request: запрос на получение упражнения
    :param create_exercise_response: ответ при создании упражнения
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    logger.info("Check get exercise response")

    assert_exercise(get_exercise_request.exercise, create_exercise_response.exercise)


@allure.step("Check update exercise response")
def assert_update_exercise_response(
        request: UpdateExerciseRequestSchema,
        response: UpdateExerciseResponseSchema
):
    """
    проверяет, что запрос на обновление упражнения курса соответствует ответу

    :param request: исходный запрос на обновление упражнения курса
    :param response: ответ API на обновление упражнения курса
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    logger.info("Check update exercise response")

    if request.title is not None:
        assert_equal(response.exercise.title, request.title, "title")

    if request.max_score is not None:
        assert_equal(response.exercise.max_score, request.max_score, "max_score")

    if request.min_score is not None:
        assert_equal(response.exercise.min_score, request.min_score, "min_score")

    if request.order_index is not None:
        assert_equal(response.exercise.order_index, request.order_index, "order_index")

    if request.description is not None:
        assert_equal(response.exercise.description, request.description, "description")

    if request.estimated_time is not None:
        assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")


@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    проверяет, что возвращается корректный текст ошибки, если упражнение для курса отсутствует

    :param actual: фактический ответ
    :raises AssertionError: если фактический ответ не соответствует ошибке "Exercise not found"
    """
    logger.info("Check exercise not found response")

    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual, expected)


@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    проверяет, что ответ на получение списка упражнений соответствует ответам на их создание

    :param get_exercises_response:
    :param get_exercises_response: ответ API на получение списка упражнений
    :param create_exercise_responses: список ответов API на создание упражнения
    :raises AssertionsError: если данные упражнений не совпадают
    """
    logger.info("Check get exercises response")

    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")

    for index, create_exercise_response in enumerate(create_exercise_responses):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)