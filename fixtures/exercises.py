import pytest
from pydantic import BaseModel

from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from clients.exercises.exercises_client import get_exercises_client, ExerciseClient
from fixtures.users import UserFixture
from fixtures.courses import CourseFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercise_client(function_user: UserFixture) -> ExerciseClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(exercise_client: ExerciseClient,
                      function_course: CourseFixture) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
    response = exercise_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)