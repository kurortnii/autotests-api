from pydantic import BaseModel, Field, EmailStr
from tools.fakers import get_random_email


class UserSchema(BaseModel):
    """
    описание базовой модели пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    описание модели запроса на создание пользователя
    в поле email добавлена генерация уникальной почты
    в поле password добавлены ограничения по количеству символов
    """
    email: EmailStr = Field(default_factory=lambda: str(get_random_email()))
    password: str = Field(min_length=5, max_length=10)
    last_name: str = Field(alias='lastName', default='Potapov')
    first_name: str = Field(alias='firstName', default='Roman')
    middle_name: str = Field(alias='middleName', default='AQA')


class CreateUserResponseSchema(BaseModel):
    """
    описание модели ответа на создание пользователя
    """
    user: UserSchema
