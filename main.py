from jsonschema import validate, ValidationError

# пример схемы
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}

# пример данных
data = {
    "name": "john doe",
    "age": "30"
}

try:
    validate(instance=data, schema=schema)
    print("данные соответствуют схеме")
except ValidationError as error:
    print('ошибка валидации:', error.message)