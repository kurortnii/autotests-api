from pydantic import BaseModel, HttpUrl, Field
from tools.fakers import fake


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
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default='tests')
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
    описание структуры ответа создания файла
    """
    file: FileSchema


class GetFileResponseSchema(BaseModel):
    """
    описание структуры запроса получения файла
    """
    file: FileSchema
