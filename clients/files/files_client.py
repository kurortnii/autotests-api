from typing import TypedDict

from httpx import Response, URL

from clients.api_client import APIClient
from clients.private_http_builder import AutheticationUserDict, get_private_http_client

class File(TypedDict):
    """
    описание структуры файла
    """
    id: str
    url: str
    filename: str
    directory: str


class CreateFileRequestDict(TypedDict):
    """
    описание структуры запроса на создание файла
    """
    filename: str
    directory: str
    upload_file: str

class CreateFileResponseDict(TypedDict):
    """
    описание структуры ответа создания файла
    """
    file: File


class FilesClient(APIClient):
    """
    клиент для работы с /api/v1/files
    """

    def get_file_api(self, file_id: str) -> Response:
        """
        метод получения файла

        :param file_id: идентификатор файла
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
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

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        response = self.create_file_api(request)
        return response.json()


# добавляем builder для FilesClient
def get_files_client(user: AutheticationUserDict) -> FilesClient:
    """
    функция создает экземпляр FilesClient с уже настроенным HTTP-клиентом

    :param user: словарь с данными пользователя для аутентификации
    :return: готовый к использованию FilesClient
    """
    return FilesClient(client=get_private_http_client(user))