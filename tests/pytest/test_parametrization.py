import pytest
from _pytest.fixtures import SubRequest


@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
# фикстура будет возвращать три разных хоста
# соответственно все автотесты использующие данную фикстуру будут запускаться три раза
def host(request: SubRequest) -> str:
    return request.param


# в самом тесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_host(host: str):
    # используем фикстуру в автотесте, она вернет нам хост в виде строки
    print(f"Running test on host: {host}")


@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


# параметризуем по операционной системе
@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
# параметризуем по хосту
@pytest.mark.parametrize("host", [
    "https://dev.company.com",
    "https://stable.company.com",
    "https://prod.company.com"
])
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # параметр user передается в качестве аргумента в каждый тестовый метод класса
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")



users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize("phone_number",
                         users.keys(),
                         ids=lambda phone_number: f"{phone_number}: {users[phone_number]}")
def test_identifiers(phone_number: str):
    pass


@pytest.mark.parametrize(
    "value",
    [1, pytest.param(2, marks=pytest.mark.skip(reason="Not supported")), 3]
)
def test_example(value):
    pass


@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(1, marks=pytest.mark.xfail(reason="Known issue with 1")),
        2,
        pytest.param(3, marks=pytest.mark.skip(reason="Feature not implemented for 3")),
    ]
)
def test_function(input_value):
    assert input_value != 1