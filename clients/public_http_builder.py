from httpx import Client
from config import settings

from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook


def get_public_http_client() -> Client:
    """
    функция создает экземпляр httpx.Client с базовыми настройками
    :return: готовый к использованию объект httpx.Client
    """
    return Client(timeout=settings.http_client.timeout,
                  base_url=settings.http_client.client_url,
                  event_hooks={
                      "request": [curl_event_hook, log_request_event_hook],
                      "response": [log_response_event_hook]})