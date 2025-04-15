from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.files.files_client import File
from clients.private_http_builder import AutheticationUserDict, get_private_http_client
from clients.users.private_users_client import User


class Course(TypedDict):
    """
    описание структуры курса
    """
    id: str
    title: str
    maxScore: str
    minScore: str
    description: str
    # вложенная структура файла
    previewFile: File
    estimatedTime: str
    # вложенная структура пользователя
    createdByUser: User


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


class CreateCourseResponseDict(TypedDict):
    """
    описание структуры ответа создания курса
    """
    course: Course


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
        return self.post("/api/v1/courses", json=request)

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

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        response = self.create_course_api(request)
        return response.json()


# добавляем builder для CoursesClient
def get_courses_client(user: AutheticationUserDict) -> CoursesClient:
    """
    функция создает экземпляр CourseClient с уже настроенным HTTP-клиентом
    :param user: словарь с данными пользователя для аутентификациии

    :return: готовый к использованию CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))

