from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

from tools.logger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")


@allure.step("Validate JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    проверяет, соответствует ли JSON-объект (instance) заданной JSON-схеме

    :param instance: json-данные, которые нужно вернуть
    :param schema: ожидаемая json-схема
    :raises json.exceptions.ValidationError: если instance не соответствует schema
    """
    logger.info("Validating JSON schema")

    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )