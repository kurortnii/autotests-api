from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequest
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.users.private_users_client import get_private_users_client, AutheticationUserDict
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# инициализируем публичный клиент для создания пользователя
public_user_client = get_public_users_client()

# создаем пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password='password',
    firstName='Roman',
    lastName='Potapov',
    middleName='AQA'
)
create_user_response = public_user_client.create_user(create_user_request)

# инициализируем словарь с данными для аутентификации
# инициализируем приватные клиенты для создания файла, курса и задания курса
authentication_user = AutheticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_files_client(authentication_user)
course_client = get_courses_client(authentication_user)
exercise_client = get_exercises_client(authentication_user)

# загружаем файл
create_file_request = CreateFileRequestDict(
    filename='image.png',
    directory='courses',
    upload_file='./test.jpg'
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# создаем курс
create_course_request = CreateCourseRequestDict(
    title='Python',
    minScore=5,
    maxScore=15,
    description='Python API Tests',
    estimatedTime='2 weeks',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = course_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# создаем задание к курсу
create_exercise_request = CreateExerciseRequest(
    title='Первое задание',
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=0,
    description='Описание первого задания',
    estimatedTime='30 минут',
    orderIndex=5
)
create_exercise_response = exercise_client.create_exercise(create_exercise_request)
print('Create exercise data', create_exercise_response)