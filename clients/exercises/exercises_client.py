from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.exercises.exercises_schema import (GetExercisesQuerySchema, CreateExerciseRequestSchema,
                                                UpdateExerciseRequestSchema, GetExerciseResponseSchema,
                                                GetExercisesResponseSchema, CreateExerciseResponseSchema,
                                                UpdateExerciseResponseSchema)


class ExerciseClient(APIClient):
    """
    клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        метод для получения списка заданий для определенного курса

        :param query: словарь с courseId
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        метод для получения информации о задании по exercise_id

        :param exercise_id: идентификатор задания
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        метод создания задания

        :param request: словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        метод обновления данных задания

        :param exercise_id: идентификатор задания
        :param request: словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        метод удаления задания

        :param exercise_id: идентификатор задания
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


# добавляем builder для ExerciseClient
def get_exercises_client(user: AuthenticationUserSchema) -> ExerciseClient:
    """
    функция создает экземпляр ExerciseClient с уже настроенным HTTP-клиентом

    :param user: словарь с данными пользователя
    :return: готовый к использованию ExerciseClient
    """
    return ExerciseClient(client=get_private_http_client(user))