from config import settings

import platform

import sys


def create_allure_environment():
    sys_items = [f'os_info={platform.system()}, {platform.release()}',
                 f'python_version={sys.version}']

    # создаем список из элементов в формате {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    items += sys_items
    # собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # открываем файл ./allure-result/environment.properties на чтение
    with open(settings.allure_result_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)