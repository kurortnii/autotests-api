import pytest
from pydantic import BaseModel, EmailStr

# импортируем API клиенты
from clients.authentication.authentication_client import AuthenticationClient, get_authentication_client
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client, PrivateUsersClient


# модель для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(email=self.email,
                                        password=self.password)


# объявляем фикстуру, по умолчанию скоуп function
# аннотируем возращаемое фикстурой значение
@pytest.fixture
def authentication_client() -> AuthenticationClient:
    # создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    # создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()


@pytest.fixture
def private_users_client(function_user) -> PrivateUsersClient:
    # создаем новый API клиент для работы с приватными API пользователей
    return get_private_users_client(function_user.authentication_user)


# фикстура для создания пользователя
# + используем фикстуру public_users_client, которая создает нужный API клиент
@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


