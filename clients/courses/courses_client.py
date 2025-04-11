from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetCoursesQueryDict(TypedDict):
    """
    описание структуры запроса на получение списка курсов
    """
    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    описание структуры запроса на создание курса
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict):
    """
    описание структуры запроса на обновление курса
    """
    title: str | None
    maxScore: str | None
    minScore: str | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    клиент для работы с /api/v1/courses
    """

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        метод для получения списка курсов
        :param query: словарь с UserId
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        метод получения курса
        :param course_id: идентификатор курса
        :return: ответ сервера в виде объекта htppx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        метод создания курса
        :param request: словарь с title, maxScore, minScore, description, estimatedTime, previewFileId, createdByUserId
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses/", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        метод обновления курса

        :param course_id: идентификатор курса
        :param request: словарь с title, maxScore, minScore, description, estimatedTime
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        метод удаления курса
        :param course_id: идентификатор курса
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")



