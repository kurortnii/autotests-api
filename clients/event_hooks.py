import allure
from httpx import Request

from tools.http.curl import make_curl_from_request


def curl_event_hook(request: Request):
    """
    event hook для автоматического прикрепления cURL команды к Allure отчету

    :param request: HTTP-запрос, переданный в `httpx` клиент
    """
    # генерируем команду cURL из объекта запроса
    curl_command = make_curl_from_request(request)

    # прикрепляем сгенерированную cURL команду к отчету Allure
    allure.attach(curl_command, 'cURL command', allure.attachment_type.TEXT)

