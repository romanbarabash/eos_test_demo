import time
from dataclasses import dataclass

from faker import Faker

from src.models.base_model import BaseModel

fake = Faker(['en-US'])


@dataclass
class UserModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

    @classmethod
    def create(cls, *args, **kwargs):
        return cls(first_name=fake.first_name(),
                   last_name=fake.last_name(),
                   email='test.qa98989' + '+' + str(time.time())[:10] + '@gmail.com',
                   password=fake.first_name() + str(time.time())[:10])
