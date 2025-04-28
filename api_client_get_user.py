from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema

# инициализируем клиент PublicUsersClient
public_user_client = get_public_users_client()

# инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema()

# отправляем POST-запрос на создание пользователя
create_user_response = public_user_client.create_user(create_user_request)
print(f'Create user data: {create_user_response}')

# инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# инициализируем клиент PrivateUserClient
private_users_client = get_private_users_client(authentication_user)

# отправляем GET-запрос на получение данных пользователя
get_user_response = private_users_client.get_user(create_user_response.user.id)
print(f'Get user data: {get_user_response}')