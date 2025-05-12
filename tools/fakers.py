from faker import Faker


class Fake:
    """
    класс для генерации случайных тестовых данных с использованием библиотеки Faker
    """

    def __init__(self, faker: Faker):
        """
        :param faker: инстанс класса Faker, который будет использоваться для генерации данных
        """
        self.faker = faker

    def text(self) -> str:
        """
        генерирует случайный текст
        :return: cлучайный текст
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        генерирует случайный UUID4
        :return: случайный uuid4
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        генерирует случайный email
        :return: случайный email
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        генерирует случайное предложение
        :return: случайное предложение
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        генерирует случайный пароль
        :return: случайный пароль
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        генерирует случайную фамилию
        :return: случайная фамилия
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        генерирует случайно имя
        :return: случайное имя
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        генерирует случайное среднее имя
        :return: случайное среднее имя
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        генерирует строку с предполагаемым временем (например, "2 weeks")
        :return: строка с предполагаемым временем
        """
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        генерируется случайное число в заданном диапозоне
        :param start: начало диапозона (включительно)
        :param end: конец диапозона (включительно)
        :return: случайное целое число
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        генерирует случайный максимальный балл в диапозоне от 50 до 100
        :return: случайный балл
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        генерирует случайный минимальный балл в диапозоне от 1 до 30
        :return: случайный балл
        """
        return self.integer(1, 30)


fake = Fake(faker=Faker())