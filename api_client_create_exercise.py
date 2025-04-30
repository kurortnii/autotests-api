from clients.exercises.exercises_client import get_exercises_client
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.users.private_users_client import AuthenticationUserSchema
from clients.courses.courses_client import get_courses_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema

# инициализируем публичный клиент для создания пользователя
public_user_client = get_public_users_client()

# создаем пользователя
create_user_request = CreateUserRequestSchema()
create_user_response = public_user_client.create_user(create_user_request)

# инициализируем pydentic-объект для аутентификации
# инициализируем приватные клиенты для создания файла, курса и задания курса
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

# загружаем файл
create_file_request = CreateFileRequestSchema(upload_file='./test.jpg')
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# создаем курс
create_course_request = CreateCourseRequestSchema(
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)
create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# создаем задание к курсу
create_exercise_request = CreateExerciseRequestSchema(courseId=create_course_response.course.id)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data', create_exercise_response)