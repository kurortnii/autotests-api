from typing import Any

from pydantic import BaseModel, Field, ConfigDict


class ValidationErrorSchema(BaseModel):
    """
    модель, описывающая структуру ошибки валидации API
    """
    model_config = ConfigDict(populate_by_name=True)

    type: str
    input: Any
    context: dict[str, Any] = Field(alias="ctx")
    message: str = Field(alias="msg")
    location: list[str] = Field(alias="loc")


class ValidationErrorResponseSchema(BaseModel):
    """
    модель, описывающая структуру ответа API с ошибкой валидации
    """
    model_config = ConfigDict(populate_by_name=True)

    details: list[ValidationErrorSchema] = Field(alias="detail")


class InternalErrorResponseSchema(BaseModel):
    """
    модель для описания внутренней ошибки
    """
    model_config = ConfigDict(populate_by_name=True)

    details: str = Field(alias="detail")

