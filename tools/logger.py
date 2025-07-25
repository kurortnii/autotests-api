import logging


def get_logger(name: str) -> logging.Logger:
    # инициализация логгера с указанным именем
    logger = logging.getLogger(name)
    # устанавливаем уровень логирования DEBUG для логгера
    # чтобы он обрабатывал все сообщения от DEBUG и выше
    logger.setLevel(logging.DEBUG)

    # создаем обработчик, который будет выводить логи в консоль
    handler = logging.StreamHandler()
    # устанавливаем уровень логирования DEBUG для обработчика
    # чтобы он обрабатывал все сообщения от DEBUG и выше
    handler.setLevel(logging.DEBUG)

    # задаем форматирование лог-сообщений: включаем время, имя логгера, уровень и сообщение
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    # добавляем обработчик к логгеру
    logger.addHandler(handler)

    # возвращаем настроенный логгер
    return logger

