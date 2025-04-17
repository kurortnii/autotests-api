from pydantic import BaseModel, ConfigDict, Field, EmailStr, HttpUrl, ValidationError
from pydantic.alias_generators import to_camel
import uuid


class FileSchema(BaseModel):
    id: str
    # используем HttpUrl вместо str
    url: HttpUrl
    filename: str
    directory: str


class UserSchema(BaseModel):
    id: str
    # используем EmailStr вместо str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CourseSchema(BaseModel):
    # автоматическое преобразование snake_case -> camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = 'playwright'
    max_score: int = Field(alias='maxScore', default=15)
    min_score: int = Field(default=0)
    # вложенный объект файла-превью
    preview_file: FileSchema = Field(alias='previewFile')
    description: str = 'playwright course'
    estimated_time: str = '3 weeks'
    # вложенный объект для пользователя, создавшего курс
    created_by_user: UserSchema = Field(alias='createdByUser')


try:
    file = FileSchema(
        id="file-id",
        url="localhost",
        filename="file.png",
        directory="courses"
    )
except ValidationError as error:
    print(error)
    print(error.errors())


# Инициализируем модель CourseSchema через передачу аргументов
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    # Добавили инициализацию вложенной модели FileSchema
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="file.png",
        directory="courses",
    ),
    estimatedTime="1 week",
    # добавили инициализацию вложенной модели UserSchema
    createdByUser=UserSchema(
        id="user-id",
        email="user@gmail.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise"
    )
)
print('Course default model:', course_default_model)


# инициализируем модель CourseSchema через передачу аргументов
# course_default_model = CourseSchema(
#     id='course_id',
#     title='Playwright',
#     maxScore=100,
#     minScore=10,
#     description='Playwright',
#     estimatedTime='1 week'
# )
# print('Course default model:', course_default_model)
#
# course_dict = {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
# course_dict_model = CourseSchema(**course_dict)
# print('Course dict model:', course_dict_model)
#
# course_json = """
# {
#     "id": "course-id",
#     "title": "Playwright",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "Playwright",
#     "estimatedTime": "1 week"
# }
# """
# course_json_model = CourseSchema.model_validate_json(course_json)
# print('Course JSON model:', course_json_model)
#
# print(course_dict_model.model_dump(by_alias=True))