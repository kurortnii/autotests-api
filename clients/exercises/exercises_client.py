from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class GetExerciseQueryRequest(TypedDict):
    """
    описание структуры запроса на получение списка заданий определенного курса
    """
    courseId: str


class CreateExerciseRequest(TypedDict):
    """
    описание структуры запроса на создание упражнения определенного курса
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequest(TypedDict):
    """
    описание структуры запроса обновления данных задания
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExerciseClient(APIClient):
    """
    клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExerciseQueryRequest) -> Response:
        """
        метод для получения списка заданий для определенного курса

        :param query: словарь с courseId
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        метод для получения информации о задании по exercise_id

        :param exercise_id: идентификатор задания
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequest) -> Response:
        """
        метод создания задания

        :param request: словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequest) -> Response:
        """
        метод обновления данных задания

        :param exercise_id: идентификатор задания
        :param request: словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        метод удаления задания

        :param exercise_id: идентификатор задания
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")