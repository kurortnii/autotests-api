import allure

from clients.courses.courses_schema import (UpdateCourseRequestSchema, UpdateCourseResponseSchema,
                                            CreateCourseResponseSchema, GetCoursesResponseSchema,
                                            CourseSchema, CreateCourseRequestSchema)
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.files import assert_file
from tools.assertions.users import assert_user


@allure.step("Check update course response")
def assert_update_course_response(
        request: UpdateCourseRequestSchema,
        response: UpdateCourseResponseSchema
):
    """
    проверяет, что ответ на обновление курса соответствует данным из запроса

    :param request: исходный запрос на обновление курса
    :param response: ответ API с обновлением данными курса
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    if request.title is not None:
        assert_equal(response.course.title, request.title, "title")

    if request.max_score is not None:
        assert_equal(response.course.max_score, request.max_score, "max_score")

    if request.min_score is not None:
        assert_equal(response.course.min_score, request.min_score, "min_score")

    if request.description is not None:
        assert_equal(response.course.description, request.description, "description")

    if request.estimated_time is not None:
        assert_equal(response.course.estimated_time, request.estimated_time, "estimated_time")


@allure.step("Check course")
def assert_course(actual: CourseSchema, expected: CourseSchema):
    """
    проверяет, что фактические данные курса соответствует ожидаемым

    :param actual: фактические данные курса
    :param expected: ожидаемые данные курса
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")

    # проверяем вложенные сущности
    assert_file(actual.preview_file, expected.preview_file)
    assert_user(actual.created_by_user, expected.created_by_user)


@allure.step("Check get course response")
def assert_get_courses_response(
        get_courses_response: GetCoursesResponseSchema,
        create_course_responses: list[CreateCourseResponseSchema]
):
    """
    проверяет, что ответ на получение списка курсов соответствует ответам на их создание

    :param get_courses_response: ответ API при запросе списка курсов
    :param create_course_responses: список API ответов при создании курсов
    :raises AsserionError: если данные курсов не совпадают
    """
    assert_length(get_courses_response.courses, create_course_responses, "courses")

    for index, create_course_response in enumerate(create_course_responses):
        assert_course(get_courses_response.courses[index], create_course_response.course)


@allure.step("Check create course response")
def assert_create_course_response(request: CreateCourseRequestSchema, response: CreateCourseResponseSchema):
    """
    проверяет, что ответ на создание курса соответствует ожидаемому ответу

    :param request: исходный запрос на создание курса
    :param response: ответ API с данными курса
    :raises AssertionError: если хотя бы одно поле не совпадает
    """
    assert_equal(request.title, response.course.title, "title")
    assert_equal(request.max_score, response.course.max_score, "max_score")
    assert_equal(request.min_score, response.course.min_score, "min_score")
    assert_equal(request.description, response.course.description, "description")
    assert_equal(request.estimated_time, response.course.estimated_time, "estimated_time")

    # проверяем идентификаторы вложенных сущностей
    assert_equal(request.preview_file_id, response.course.preview_file.id, "preview_file_id")
    assert_equal(request.created_by_user_id, response.course.created_by_user.id, "created_by_user_id")
