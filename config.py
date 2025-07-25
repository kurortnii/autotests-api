from typing import Self

from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientConfig(BaseModel):
    url: HttpUrl
    timeout: float

    @property
    def client_url(self) -> str:
        return str(self.url)


class TestDataConfig(BaseModel):
    image_jpg_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="."
    )
    test_data: TestDataConfig
    http_client: HTTPClientConfig
    allure_result_dir: DirectoryPath

    @classmethod
    def initialize(cls) -> Self:
        allure_result_dir = DirectoryPath("./allure-results")
        allure_result_dir.mkdir(exist_ok=True)

        return Settings(allure_result_dir=allure_result_dir)


settings = Settings.initialize()
