from pydantic import BaseModel
from pprint import pprint


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    address: Address


user = User(
    id="123",
    name='Alice',
    email='alice@example.com',
    address={"city": "New York", "zip_code": "10001"}
)
pprint(user.address.city)


# print('Hello PyCharm!')