from typing import Any

import allure
from httpx import Client, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles


class APIClient:
    def __init__(self, client: Client):
        """
        базовый API клиент, принимающий httpx.Client.

        :param client: экземпляр httpx.Client для выполнения http-запросов
        """
        self.client = client

    @allure.step("Make GET request to {url}")
    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        выполняет GET-запрос

        :param url: URL-адрес эндпоинта
        :param params: GET-параметры запроса (например, ?key=value)
        :return: объект Response с данными ответа
        """
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(self,
             url: URL | str,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None
             ) -> Response:
        """
        выполняет POST-запрос

        :param url: URL-адрес эндпоинта
        :param json: данные в формате JSON
        :param data: форматированные данные формы (например, application/x-www-form-urlencoded)
        :param files: файлы для загрузки на сервер
        :return: объект Response c данными ответа
        """
        return self.client.post(url, json=json, data=data, files=files)

    @allure.step("Make PATCH request to {url}")
    def patch(self, url: URL | str, json: Any | None = None) -> Response:
        """
        выполняет PATCH-запрос (частичное обновление данных)

        :param url: URL-адрес эндпоинта
        :param json: данные для обновления в формате JSON
        :return: объект Response c данными ответа
        """
        return self.client.patch(url, json=json)

    @allure.step("Make DELETE request to {url}")
    def delete(self, url: URL | str) -> Response:
        """
        выполняет DELETE-запрос (удаление данных)

        :param url: URL-адрес эндпоинта
        :return: объект Response с данными ответа
        """
        return self.client.delete(url)
