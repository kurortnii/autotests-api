import allure
from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.courses.courses_schema import (GetCoursesQuerySchema, CreateCourseRequestSchema,
                                            UpdateCourseRequestSchema, CreateCourseResponseSchema)


class CoursesClient(APIClient):
    """
    клиент для работы с /api/v1/courses
    """

    @allure.step("Get courses")
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        метод для получения списка курсов
        :param query: словарь с UserId
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params=query.model_dump(by_alias=True))

    @allure.step("Get course by id {course_id}")
    def get_course_api(self, course_id: str) -> Response:
        """
        метод получения курса
        :param course_id: идентификатор курса
        :return: ответ сервера в виде объекта htppx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    @allure.step("Create course")
    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        метод создания курса
        :param request: словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request.model_dump(by_alias=True))

    @allure.step("Update course by id {course_id}")
    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        метод обновления курса

        :param course_id: идентификатор курса
        :param request: словарь с title, maxScore, minScore, description, estimatedTime
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete course by id {course_id}")
    def delete_course_api(self, course_id: str) -> Response:
        """
        метод удаления курса
        :param course_id: идентификатор курса
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

    @allure.step("Create course")
    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


# добавляем builder для CoursesClient
def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    функция создает экземпляр CourseClient с уже настроенным HTTP-клиентом
    :param user: словарь с данными пользователя для аутентификациии

    :return: готовый к использованию CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))

