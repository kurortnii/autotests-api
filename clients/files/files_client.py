from typing import TypedDict

from httpx import Response, URL

from clients.api_client import APIClient

class CreateFileRequest(TypedDict):
    """
    описание структуры запроса на создание файла
    """
    filename: str
    directory: str
    upload_file: str


class FilesClient(APIClient):
    """
    клиент для работы с /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        метод получения файла

        :param user_id: идентификатор файла
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files{file_id}")

    def create_file_api(self, request: CreateFileRequest) -> Response:
        """
        метод создания файла

        :param request: словарь с filename, directory, upload_file
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/files",
                         data=request,
                         files={"upload_file": open(request["upload_file"], 'rb')})

    def delete_file_api(self, file_id: str) -> Response:
        """
        метод удаления файла

        :param file_id: идентификатор файла
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")
