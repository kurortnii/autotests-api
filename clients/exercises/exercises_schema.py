from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    описание структуры упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class GetExercisesQuerySchema(BaseModel):
    """
    описание структуры запроса на получение списка заданий определенного курса
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')


class CreateExerciseRequestSchema(BaseModel):
    """
    описание структуры запроса на создание упражнения определенного курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


class CreateExerciseResponseSchema(BaseModel):
    """
    описание структуры ответа создания упражнения
    """
    exercise: ExerciseSchema


class GetExerciseResponseSchema:
    """
    структура ответа на получения упражнения
    """
    exercise: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """
    структура ответа на получения списка упражнений
    """
    exercises: list[ExerciseSchema]


class UpdateExerciseRequestSchema(BaseModel):
     """
     описание структуры запроса обновления данных задания
     """
     model_config = ConfigDict(populate_by_name=True)

     title: str | None
     max_score: int | None = Field(alias='maxScore')
     min_score: int | None = Field(alias='minScore')
     order_index: int | None = Field(alias='orderIndex')
     description: str | None
     estimated_time: str | None = Field(alias='estimatedTime')


class UpdateExerciseResponseSchema(BaseModel):
    """
    описание структуры ответа обновления данных задания
    """
    exercise: ExerciseSchema

