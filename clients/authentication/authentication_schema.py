from pydantic import BaseModel, Field
from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    описание структуры аутентификационных токенов
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginRequestSchema(BaseModel):
    """
    описание структуры запроса на аутентификацию
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):
    """
    описание структуры ответа аутентификации
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    описание структуры запроса для обновления токена
    """
    refresh_token: str = Field(alias='refreshToken', default_factory=fake.sentence)

