from pydantic import BaseModel, HttpUrl


class FileSchema(BaseModel):
    """
    описание структуры файла
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    описание структуры запроса на создание файла
    """
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    описание структуры ответа создания файла
    """
    file: FileSchema
