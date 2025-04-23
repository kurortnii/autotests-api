from typing import Any

from jsonschema import validate
from jsonschema.validators import Draft202012Validator


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме

    :param instance: json-данные, которые нужно вернуть
    :param schema: ожидаемая json-схема
    :raises json.exceptions.ValidationError: если instance не соответствует schema
    """
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )