from httpx import Client


def get_public_http_client() -> Client:
    """
    функция создает экземпляр httpx.Client с базовыми настройками
    :return: готовый к использованию объект httpx.Client
    """
    return Client(timeout=100, base_url="http://localhost:8000")