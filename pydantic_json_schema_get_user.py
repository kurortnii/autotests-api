from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

# инициализируем клиент для создания пользователя
public_client_user = get_public_users_client()

# подготавливаем данные для создания пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="password",
    last_name="Potapov",
    first_name="Roman",
    middle_name="AQA"
)

# создаем пользователя
create_user_response = public_client_user.create_user(create_user_request)

# инициализируем приватный клиент, чтобы получить данные по пользователю
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_client_user = get_private_users_client(authentication_user)

# получаем пользователя по его идентификатору
get_user_response = private_client_user.get_user_api(create_user_response.user.id)
# инициализируем json-схему для валидации ответа эндпоинта GET /api/v1/users/{user_id}
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# валидируем ответ с json-схемой
validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)


