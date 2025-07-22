from httpx import Request, RequestNotRead


def make_curl_from_request(request: Request) -> str:
    """
    генерирует команду cURL из HTTP-запроса httpx

    :param request: HTTP-запрос, из которого будет сформирована команда cURL
    :return: строка с командой cURL, содержащая метод запроса, URL, заголовки и тело (если есть)
    """
    # создаем список с основной командой cURL, включая метод и URL
    result: list[str] = [f"curl -X '{request.method}'", f"'{request.url}'"]

    # добавлям заголовки в формате -H "Header: Value"
    for header, value in request.headers.items():
        result.append(f"-H '{header}: {value}'")

    # добавляем тело запроса, если оно есть (например, для POST, PUT)
    try:
        if body := request.content:
            result.append(f"-d '{body.decode('utf-8')}'")
    except RequestNotRead:
        pass

    return "\\\n  ".join(result)