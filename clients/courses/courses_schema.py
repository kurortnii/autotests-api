from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    """
    описание структуры курса
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    # вложенная структура файла
    preview_file: FileSchema = Field(alias='previewFile')
    estimated_time: str = Field(alias='estimatedTime')
    # вложенная структура пользователя
    created_by_user: UserSchema = Field(alias='createdByUser')


class GetCoursesQuerySchema(BaseModel):
    """
    описание структуры запроса на получение списка курсов
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')


class CreateCourseRequestSchema(BaseModel):
    """
    описание структуры запроса на создание курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int = Field(alias='minScore', default_factory=fake.min_score)
    description: str = Field(default_factory=fake.text)
    preview_file_id: str = Field(alias='previewFileId', default_factory=fake.uuid4)
    estimated_time: str = Field(alias='estimatedTime', default_factory=fake.estimated_time)
    created_by_user_id: str = Field(alias='createdByUserId', default_factory=fake.uuid4)


class CreateCourseResponseSchema(BaseModel):
    """
    описание структуры ответа на создание курса
    """
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    описание структуры запроса на обновление курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: str | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: str | None = Field(alias='minScore', default_factory=fake.min_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class UpdateCourseResponseSchema(BaseModel):
    """
    описание структуры ответа обновления курса
    """
    course: CourseSchema


class GetCoursesResponseSchema(BaseModel):
    """
    описание структуры ответа на получение списка курсов
    """
    courses: list[CourseSchema]
