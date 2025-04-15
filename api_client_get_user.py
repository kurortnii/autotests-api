from clients.private_http_builder import AutheticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# инициализируем клиент PublicUsersClient
public_user_client = get_public_users_client()

# инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="password",
    lastName="Joe",
    firstName='Doe',
    middleName='Jack'
)

# отправляем POST-запрос на создание пользователя
create_user_response = public_user_client.create_user(create_user_request)
print(f'Create user data: {create_user_response}')

# инициализируем пользовательские данные для аутентификации
authentication_user = AutheticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

# инициализируем клиент PrivateUserClient
private_users_client = get_private_users_client(authentication_user)

# отправляем GET-запрос на получение данных пользователя
get_user_response = private_users_client.get_user(create_user_response['user']['id'])
print(f'Get user data: {get_user_response}')