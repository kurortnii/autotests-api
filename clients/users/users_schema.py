from pydantic import BaseModel, EmailStr, ConfigDict, Field


class UserSchema(BaseModel):
    """
    описание структуры пользователя
    """
    # эта настройка позволит обращаться к полям по python-именам (snake_case)
    # при создании экземпляров моделей
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserRequestSchema(BaseModel):
    """
    описание структуры запроса на создание пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')


class CreateUserResponseSchema(BaseModel):
    """
    описание структуры ответа создания пользователя
    """
    user: UserSchema


class UpdateUserRequestSchema(BaseModel):
    """
    описание структуры запроса на обновление пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: str | None = Field(alias='lastName')
    first_name: str | None = Field(alias='firstName')
    middle_name: str | None = Field(alias='middleName')


class UpdateUserResponseSchema(BaseModel):
    """
    описание структуры ответа обновления пользователя
    """
    user: UserSchema


class GetUserResponseSchema(BaseModel):
    user: UserSchema
