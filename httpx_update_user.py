import httpx

import pprint

from tools.fakers import get_random_email

# создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "password",
    "lastName": "Potapov",
    "firstName": "Roman",
    "middleName": "Junior AQA"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# получаем данные нашего пользователя
headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}

user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_response_data = user_response.json()

# обновляем пользователя, мечты-мечты...
update_user_payload = {
  "middleName": "Senior AQA + SDET"
}

update_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_response_data["user"]["id"]}", json=update_user_payload, headers=headers)
update_response_data = update_response.json()

pprint.pp(update_response_data)

