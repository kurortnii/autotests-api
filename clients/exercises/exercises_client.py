from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AutheticationUserDict


class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryRequest(TypedDict):
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


class CreateExerciseResponse(TypedDict):
    exercise: Exercise


class GetExerciseResponseDict(TypedDict):
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]


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


class UpdateExerciseResponseDict(TypedDict):
    exercise: Exercise


class ExerciseClient(APIClient):
    """
    клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQueryRequest) -> Response:
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

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesResponseDict) -> GetExercisesResponseDict:
        response = self.get_exercise_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequest) -> CreateExerciseResponse:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, request: UpdateExerciseRequest) -> UpdateExerciseResponseDict:
        response = self.update_exercise_api(request)
        return response.json()


# добавляем builder для ExerciseClient
def get_exercises_client(user: AutheticationUserDict) -> ExerciseClient:
    """
    функция создает экземпляр ExerciseClient с уже настроенным HTTP-клиентом

    :param user: словарь с данными пользователя
    :return: готовый к использованию ExerciseClient
    """
    return ExerciseClient(client=get_private_http_client(user))