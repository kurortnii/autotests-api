from httpx import Response, URL

from clients.api_client import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


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

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        """
        метод создания файла

        :param request: словарь с filename, directory, upload_file
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/files",
                         data=request.model_dump(by_alias=True, exclude={'upload_file'}),
                         files={"upload_file": open(request.upload_file, 'rb')})

    def delete_file_api(self, file_id: str) -> Response:
        """
        метод удаления файла

        :param file_id: идентификатор файла
        :return: ответ сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


# добавляем builder для FilesClient
def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    """
    функция создает экземпляр FilesClient с уже настроенным HTTP-клиентом

    :param user: словарь с данными пользователя для аутентификации
    :return: готовый к использованию FilesClient
    """
    return FilesClient(client=get_private_http_client(user))