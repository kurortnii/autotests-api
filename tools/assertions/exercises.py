from clients.exercises.exercises_schema import (CreateExerciseResponseSchema, CreateExerciseRequestSchema,
                                                ExerciseSchema, GetExerciseResponseSchema)

from tools.assertions.base import assert_equal


def assert_create_exercise_response(request: CreateExerciseRequestSchema,
                                    response: CreateExerciseResponseSchema):
    """
    проверяет, что данные запроса на создание упражнения курса совпадают с данными ответа

    :param request: запрос с данными для создания упражнения курса
    :param response: ответ API при создании упражнения курса
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    проверяет, что фактические данные упражнения курса соответствуют ожидаемым

    :param actual: фактические данные упражнения курса
    :param expected: ожидаемые данные упражнения курса
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(get_exercise_request: GetExerciseResponseSchema,
                                 create_exercise_response: CreateExerciseResponseSchema):
    assert_exercise(get_exercise_request.exercise, create_exercise_response.exercise)

