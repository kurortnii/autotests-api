import allure
from httpx import Request, Response

from tools.http.curl import make_curl_from_request
from tools.logger import get_logger

logger = get_logger("HTTP_CLIENT")


def curl_event_hook(request: Request):
    """
    event hook для автоматического прикрепления cURL команды к Allure отчету

    :param request: HTTP-запрос, переданный в `httpx` клиент
    """
    # генерируем команду cURL из объекта запроса
    curl_command = make_curl_from_request(request)

    # прикрепляем сгенерированную cURL команду к отчету Allure
    allure.attach(curl_command, 'cURL command', allure.attachment_type.TEXT)


def log_request_event_hook(request: Request):
    """
    логирует информацию об отправленном HTTP-запросе

    :param request: объект запроса HTTPX
    """
    # пишем в лог информационное сообщение о запросе
    logger.info(f"Make {request.method} request to {request.url}")


def log_response_event_hook(response: Response):
    """
    логирует информацию о полученном HTTP-ответе

    :param response: объект ответа HTTPX
    """
    # пишем в лог информационное сообщение о полученном ответе
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )
